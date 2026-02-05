import pandas as pd
import numpy as np

# Load financial data
data = pd.read_csv("data/financials.csv")

# Financial Ratios
data["EPS"] = data["Net_Income"] / data["Shares_Outstanding"]
data["PE_Ratio"] = data["Market_Price"] / data["EPS"]
data["ROE"] = data["Net_Income"] / data["Equity"]
data["Debt_to_Equity"] = data["Total_Debt"] / data["Equity"]

# Valuation (Simple Intrinsic Value using PE method)
INDUSTRY_PE = 18
data["Intrinsic_Value"] = data["EPS"] * INDUSTRY_PE

# Investment Recommendation
def recommendation(row):
    if row["Market_Price"] < row["Intrinsic_Value"]:
        return "BUY"
    elif row["Market_Price"] > row["Intrinsic_Value"]:
        return "SELL"
    else:
        return "HOLD"

data["Recommendation"] = data.apply(recommendation, axis=1)

# Display results
print("\nEquity Research Analysis Result:\n")
print(data[[
    "Company", "Market_Price", "Intrinsic_Value",
    "PE_Ratio", "ROE", "Debt_to_Equity", "Recommendation"
]])
