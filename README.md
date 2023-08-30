# Stock News Alert App

The Stock News Alert App is a simple Python application that monitors the stock market and sends alerts about stock price changes along with relevant news headlines and briefs.

## Setup

1. Clone or download this repository.

2. Open a terminal or command prompt and navigate to the project directory.

3. Replace the following placeholder values in the `StockNewsAlertApp` class with your own credentials:
 - `NEWS_API_KEY`: Your NewsAPI key
 - `account_sid`: Your Twilio account SID
 - `auth_token`: Your Twilio authentication token
 - `ALPHA_VANTAGE_API_KEY`: Your Alpha Vantage API key
   
4. Run the application by executing the following command: 'python stock_news_alert.py'


## Usage

1. Launch the application by running the command provided in the setup section.

2. The application window will open. Enter the stock code and company name in the respective fields.

3. Click the "Start Monitoring" button to begin monitoring the stock.

4. If the rate of change in the stock price is greater than 2% (increase) or less than -5% (decrease), an alert will be sent via SMS using Twilio. The alert message will include the percentage change, headline, and brief from the top news related to the company.

5. An alert confirmation window will appear if the message is successfully sent.

## Notes

- This application uses the Alpha Vantage API to fetch stock price data and the NewsAPI to retrieve relevant news articles.
- Twilio is used to send SMS alerts. Ensure you have a valid Twilio account and the necessary credits for sending SMS.
- The application may need further customization based on your requirements and preferences.

## Disclaimer

This application is provided as-is and for educational purposes only. The accuracy of stock data, news articles, and alerts is not guaranteed. Use at your own risk.

