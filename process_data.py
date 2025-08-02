import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
# Births data (BT3)
births_df = pd.read_csv("bt3-2023-births-time-series.csv", encoding="latin-1", skiprows=3)

# Unemployment data
unemployment_df = pd.read_csv("unemployment_rate.csv", skiprows=7)

# CPI historical data (1950-1988) - Assuming 'Table 1' contains the relevant data
cpi_historical_df = pd.read_excel("cpi_historical_data.xlsx", sheet_name="Table 1", skiprows=4)

# CPI current data (1988-present) - Assuming 'Table 1' contains the relevant data
cpi_current_df_all_sheets = pd.read_excel("cpi_current_data.xlsx", sheet_name=None)

print("Data loaded successfully.")

# Debugging: Print sheets and first few rows of each sheet for CPI current data
print("\nCPI Current Data Sheets and Heads:")
for sheet_name, df in cpi_current_df_all_sheets.items():
    print(f"\nSheet: {sheet_name}")
    print(df.head())

# Clean and preprocess Births data
births_df = births_df.rename(columns={"Year": "Date", "Total": "Births"}) # Adjust column names as needed
# Filter out non-numeric values from 'Date' column and convert to numeric, then to datetime
births_df = births_df[pd.to_numeric(births_df["Date"], errors='coerce').notna()]
births_df["Date"] = pd.to_datetime(births_df["Date"], format="%Y") # Convert 'Year' to datetime
births_df["Births"] = pd.to_numeric(births_df["Births"].str.replace(",", "")) # Remove commas and convert to numeric

# Clean and preprocess Unemployment data
unemployment_df.columns = ["Date", "Unemployment_Rate"]
unemployment_df = unemployment_df[unemployment_df["Date"].notna()]
unemployment_df["Date"] = pd.to_datetime(unemployment_df["Date"], errors='coerce') # Convert 'Month Year' or 'Year' to datetime
unemployment_df["Unemployment_Rate"] = pd.to_numeric(unemployment_df["Unemployment_Rate"], errors="coerce")

# Clean and preprocess CPI historical data
cpi_historical_df = cpi_historical_df.iloc[1:].copy() # Skip metadata row
# Use the first column as Date and the second column as CPI
cpi_historical_df = cpi_historical_df.iloc[:, :2]  # Select only first two columns
cpi_historical_df.columns = ["Date", "CPI"] # Adjust column names as needed
cpi_historical_df = cpi_historical_df[cpi_historical_df["Date"].notna()]
cpi_historical_df["Date"] = pd.to_datetime(cpi_historical_df["Date"], errors='coerce') # Convert to datetime
cpi_historical_df["CPI"] = pd.to_numeric(cpi_historical_df["CPI"], errors="coerce")

# Clean and preprocess CPI current data
# This part will be updated after inspecting the sheets
# cpi_current_df = pd.read_excel("cpi_current_data.xlsx", sheet_name="Table 1", skiprows=4)
# cpi_current_df = cpi_current_df.iloc[1:].copy() # Skip metadata row
# cpi_current_df.columns = ["Date", "CPI"] # Adjust column names as needed
# cpi_current_df = cpi_current_df[cpi_current_df["Date"].notna()]
# cpi_current_df["Date"] = pd.to_datetime(cpi_current_df["Date"], format="%Y %b") # Convert 'Month Year' to datetime
# cpi_current_df["CPI"] = pd.to_numeric(cpi_current_df["CPI"], errors="coerce")

print("Data cleaning and preprocessing complete.")

# Display first few rows and info for each cleaned DataFrame
print("\nCleaned Births Data Head:")
print(births_df.head())
print("\nCleaned Births Data Info:")
print(births_df.info())

print("\nCleaned Unemployment Data Head:")
print(unemployment_df.head())
print("\nCleaned Unemployment Data Info:")
print(unemployment_df.info())

print("\nCleaned CPI Historical Data Head:")
print(cpi_historical_df.head())
print("\nCleaned CPI Historical Data Info:")
print(cpi_historical_df.info())

# Merge CPI historical and current data (this part will be updated after current CPI data is loaded correctly)
# cpi_df = pd.concat([cpi_historical_df, cpi_current_df]).sort_values(by="Date").reset_index(drop=True)
# print("\nMerged CPI Data Head:")
# print(cpi_df.head())
# print("\nMerged CPI Data Info:")
# print(cpi_df.info())

# Further merging and analysis will be done in subsequent steps

