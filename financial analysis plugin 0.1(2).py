from yfinance import Ticker

def fetch_financial_data(ticker_symbol):
    ticker = Ticker(ticker_symbol)
    financial_data = ticker.info
    return financial_data

def forecast_cash_flows(financial_data):
    # Code for forecasting future cash flows goes here
    # Returns a list of cash flows
    pass

def dcf_analysis(financial_data, discount_rate):
    # Forecast future cash flows
    future_cash_flows = forecast_cash_flows(financial_data)

    # Calculate the present value of the future cash flows
    present_value = 0
    for i, cash_flow in enumerate(future_cash_flows):
        present_value += cash_flow / (1 + discount_rate) ** (i + 1)

    # Calculate the intrinsic value of the company's stock
    intrinsic_value = present_value / financial_data["sharesOutstanding"]

    # Calculate the margin of safety
    margin_of_safety = (financial_data["regularMarketPrice"] - intrinsic_value) / financial_data["regularMarketPrice"]

    # Return the results as a dictionary
    return {
        "present_value": present_value,
        "intrinsic_value": intrinsic_value,
        "margin_of_safety": margin_of_safety
    }

def comparable_company_analysis(financial_data, similar_companies):
    # Fetch financial data for the similar companies
    similar_company_data = []
    for company in similar_companies:
        ticker = Ticker(company)
        data = ticker.info
        similar_company_data.append(data)

    # Calculate average values for relevant financial metrics
    average_price_to_earnings_ratio = 0
    average_price_to_book_ratio = 0
    for data in similar_company_data:
        average_price_to_earnings_ratio += data["forwardPE"]
        average_price_to_book_ratio += data["priceToBook"]
    average_price_to_earnings_ratio /= len(similar_company_data)
    average_price_to_book_ratio /= len(similar_company_data)

    # Calculate the relative performance of the given company
    relative_performance = (financial_data["forwardPE"] / average_price_to_earnings_ratio + financial_data["priceToBook"] / average_price_to_book_ratio) / 2

    # Return the results as a dictionary
    return {
        "average_price_to_earnings_ratio": average_price_to_earnings_ratio,
        "average_price_to_book_ratio": average_price_to_book_ratio,
        "relative_performance": relative_performance
    }
def comparable_company_analysis(financial_data, similar_companies):
    # Fetch financial data for the similar companies
    similar_company_data = []
    for company in similar_companies:
        ticker = Ticker(company)
        data = ticker.info
        similar_company_data.append(data)
    comparable_company_results = comparable_company_analysis(financial_data, ["AAPL", "MSFT", "GOOG"])
    average_price_to_book_ratio = comparable_company_results["average_price_to_book_ratio"]


import tkinter as tk

root = tk.Tk()
root.title("Financial Analysis Plugin")

# Create a label
label = tk.Label(root, text="Enter the ticker symbol of a company:")

# Create a text field
text_field = tk.Entry(root)

# Create a button
button = tk.Button(root, text="Analyze")

# Add the label, text field, and button to the root window
label.pack()
text_field.pack()
button.pack()

def on_button_click():
    # Get the ticker symbol from the text field
    ticker_symbol = text_field.get()

    # Fetch the financial data for the company
    financial_data = fetch_financial_data(ticker_symbol)

    # Perform the DCF analysis
    dcf_results = dcf_analysis(financial_data, 0.1)

    # Perform the comparable company analysis
    comparable_company_results = comparable_company_analysis(financial_data, ["AAPL", "MSFT", "GOOG"])

    # Clear the root window
    for widget in root.winfo_children():
        widget.destroy()

    # Clear new labels to display the results of the analysis
    intrinsic_value_label = tk.Label(root, text=f"Intrinsic value: {dcf_results['intrinsic_value']}")
    margin_of_safety_label = tk.Label(root, text=f"Margin of safety: {dcf_results['margin_of_safety']}")
    average_price_to_earnings_ratio_label = tk.Label(root, text=f"Average price-to-earnings ratio: {comparable_company_results['average_price_to_earnings_ratio']}")
    
    #Define intrinsic value
    intrinsic_value = financial_data["intrinsicValue"]
    
    # Calculate the potential upside/downside
    potential_upside = financial_data["regularMarketPrice"] - intrinsic_value
    
    # Create a new label to display the potential upside/downside
    potential_upside_label = tk.Label(root, text=f"Potential upside/downside: {potential_upside}")
    
    # Add the new label to the user interface
    potential_upside_label.pack()
    
