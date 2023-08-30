import tkinter as tk
from tkinter import messagebox
import requests
from newsapi import NewsApiClient
from twilio.rest import Client
import os


class StockNewsAlertApp:
    def __init__(self, root):
        self.root = root
        self.root.config(bg="#00539C")
        self.root.title("Stock News Alert")

        self.NEWS_API_KEY = os.environ["NEWS_API_KEY"]
        self.account_sid = os.environ["account_sid"]
        self.auth_token = os.environ["auth_token"]
        self.ALPHA_VANTAGE_API_KEY = os.environ["ALPHA_VANTAGE_API_KEY"]

        self.label = tk.Label(root, text="Enter the stock info:", bg="#00539C")
        self.label.grid(row=0, column=0, columnspan=2)

        self.StockCodeLabel = tk.Label(root, text="Stock Code:", bg="#00539C")
        self.StockCodeLabel.grid(row=1, column=0)
        self.StockCodeEntry = tk.Entry(root, highlightthickness=0, bg="#EEA47F", fg="#00008B")
        self.StockCodeEntry.grid(row=1, column=1)

        self.CompanyNameLabel = tk.Label(root, text="Company Name:", bg="#00539C")
        self.CompanyNameLabel.grid(row=2, column=0)
        self.CompanyNameEntry = tk.Entry(root, highlightthickness=0, bg="#EEA47F", fg="#00008B")
        self.CompanyNameEntry.grid(row=2, column=1)

        self.button = tk.Button(root, text="Start Monitoring", command=self.start_monitoring, highlightthickness=0, border=0)
        self.button.grid(row=3, column=0, columnspan=2)

    def start_monitoring(self):
        account_sid = self.account_sid
        auth_token = self.auth_token
        ALPHA_VANTAGE_API_KEY = self.ALPHA_VANTAGE_API_KEY
        news_api_key = self.NEWS_API_KEY

        STOCK = self.StockCodeEntry.get()
        COMPANY_NAME = self.CompanyNameEntry.get()
      
        parameters = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": STOCK,
            "apikey": ALPHA_VANTAGE_API_KEY
        }

        try:
            response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
            response.raise_for_status()
            print(response.json())
            data = response.json()["Time Series (Daily)"]
            data_list = [data[key] for key in data]

            yesterday_close_price = float(data_list[0]['4. close'])
            prev_day_close_price = float(data_list[1]['4. close'])
            rate_of_change = 100 * (yesterday_close_price - prev_day_close_price) / yesterday_close_price

            if rate_of_change > 2 or rate_of_change < -5:
                NEWS_API_KEY = news_api_key
                newsapi = NewsApiClient(api_key=NEWS_API_KEY)
                top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME, language='en', country='us')

                client = Client(account_sid, auth_token)

                if rate_of_change > 0:
                    message = client.messages.create(
                        from_='+13614016594',
                        body=f"{STOCK}: 🔺{round(rate_of_change, 1)}%\n\n"
                             f"Headline: {top_headlines['articles'][0]['title']}\n\n"
                             f"Brief: {top_headlines['articles'][0]['description']}",
                        to='+905539431821'
                    )
                else:
                    message = client.messages.create(
                        from_='+13614016594',
                        body=f"TSLA: 🔻{round(-rate_of_change, 1)}%\n\n"
                             f"Headline: {top_headlines['articles'][0]['title']}\n\n"
                             f"Brief: {top_headlines['articles'][0]['description']}",
                        to='+905539431821'
                    )

                messagebox.showinfo("Alert Sent", "Stock alert message has been sent!")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n\n{str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StockNewsAlertApp(root)
    root.mainloop()
