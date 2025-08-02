import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Create a comprehensive analysis for the project
print("Creating Economic and Demographic Analysis for Scotland")

# Load and clean the births data
births_df = pd.read_csv("bt3-2023-births-time-series.csv", encoding="latin-1", skiprows=3)
births_df = births_df.rename(columns={"Year": "Date", "Total": "Births"})
births_df = births_df[pd.to_numeric(births_df["Date"], errors='coerce').notna()]
births_df["Date"] = pd.to_datetime(births_df["Date"], format="%Y")
births_df["Births"] = pd.to_numeric(births_df["Births"].str.replace(",", ""))

# Load and clean unemployment data
unemployment_df = pd.read_csv("unemployment_rate.csv", skiprows=7)
unemployment_df.columns = ["Date", "Unemployment_Rate"]
unemployment_df = unemployment_df[unemployment_df["Date"].notna()]
unemployment_df["Date"] = pd.to_datetime(unemployment_df["Date"], errors='coerce')
unemployment_df["Unemployment_Rate"] = pd.to_numeric(unemployment_df["Unemployment_Rate"], errors="coerce")

# Filter data for common time period (1971-2023)
births_filtered = births_df[(births_df["Date"].dt.year >= 1971) & (births_df["Date"].dt.year <= 2023)]
unemployment_filtered = unemployment_df[(unemployment_df["Date"].dt.year >= 1971) & (unemployment_df["Date"].dt.year <= 2023)]

print(f"Births data: {len(births_filtered)} records from {births_filtered['Date'].min()} to {births_filtered['Date'].max()}")
print(f"Unemployment data: {len(unemployment_filtered)} records")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Economic and Demographic Analysis: Scotland 1971-2023', fontsize=16, fontweight='bold')

# 1. Births trend over time
axes[0, 0].plot(births_filtered["Date"], births_filtered["Births"], color='blue', linewidth=2)
axes[0, 0].set_title('Annual Births in Scotland (1971-2023)')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Number of Births')
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)

# 2. Unemployment rate trend
unemployment_yearly = unemployment_filtered.groupby(unemployment_filtered["Date"].dt.year)["Unemployment_Rate"].mean().reset_index()
unemployment_yearly["Date"] = pd.to_datetime(unemployment_yearly["Date"], format="%Y")

axes[0, 1].plot(unemployment_yearly["Date"], unemployment_yearly["Unemployment_Rate"], color='red', linewidth=2)
axes[0, 1].set_title('Average Annual Unemployment Rate (1971-2023)')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('Unemployment Rate (%)')
axes[0, 1].grid(True, alpha=0.3)
axes[0, 1].tick_params(axis='x', rotation=45)

# 3. Birth rate changes by decade
births_filtered['Decade'] = (births_filtered["Date"].dt.year // 10) * 10
decade_births = births_filtered.groupby('Decade')["Births"].mean()

axes[1, 0].bar(decade_births.index, decade_births.values, color='green', alpha=0.7)
axes[1, 0].set_title('Average Annual Births by Decade')
axes[1, 0].set_xlabel('Decade')
axes[1, 0].set_ylabel('Average Annual Births')
axes[1, 0].grid(True, alpha=0.3)

# 4. Correlation analysis (if data overlaps)
# Merge data for correlation analysis
merged_data = pd.merge(births_filtered, unemployment_yearly, on="Date", how="inner")
if len(merged_data) > 0:
    axes[1, 1].scatter(merged_data["Unemployment_Rate"], merged_data["Births"], alpha=0.6, color='purple')
    axes[1, 1].set_title('Births vs Unemployment Rate')
    axes[1, 1].set_xlabel('Unemployment Rate (%)')
    axes[1, 1].set_ylabel('Number of Births')
    axes[1, 1].grid(True, alpha=0.3)
    
    # Calculate correlation
    correlation = merged_data["Births"].corr(merged_data["Unemployment_Rate"])
    axes[1, 1].text(0.05, 0.95, f'Correlation: {correlation:.3f}', transform=axes[1, 1].transAxes, 
                   bbox=dict(boxstyle="round", facecolor='wheat', alpha=0.5))
else:
    axes[1, 1].text(0.5, 0.5, 'Insufficient overlapping data\nfor correlation analysis', 
                   ha='center', va='center', transform=axes[1, 1].transAxes)
    axes[1, 1].set_title('Births vs Unemployment Rate')

plt.tight_layout()
plt.savefig('economic_demographic_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

# Generate summary statistics
print("\n" + "="*50)
print("SUMMARY STATISTICS")
print("="*50)

print(f"\nBIRTHS DATA (1971-2023):")
print(f"Total births: {births_filtered['Births'].sum():,}")
print(f"Average annual births: {births_filtered['Births'].mean():.0f}")
print(f"Highest year: {births_filtered.loc[births_filtered['Births'].idxmax(), 'Date'].year} ({births_filtered['Births'].max():,} births)")
print(f"Lowest year: {births_filtered.loc[births_filtered['Births'].idxmin(), 'Date'].year} ({births_filtered['Births'].min():,} births)")

print(f"\nUNEMPLOYMENT DATA:")
print(f"Average unemployment rate: {unemployment_yearly['Unemployment_Rate'].mean():.1f}%")
print(f"Highest unemployment: {unemployment_yearly['Unemployment_Rate'].max():.1f}%")
print(f"Lowest unemployment: {unemployment_yearly['Unemployment_Rate'].min():.1f}%")

# Trend analysis
births_trend = np.polyfit(range(len(births_filtered)), births_filtered["Births"], 1)
unemployment_trend = np.polyfit(range(len(unemployment_yearly)), unemployment_yearly["Unemployment_Rate"], 1)

print(f"\nTREND ANALYSIS:")
print(f"Births trend: {'Increasing' if births_trend[0] > 0 else 'Decreasing'} by {abs(births_trend[0]):.0f} births per year")
print(f"Unemployment trend: {'Increasing' if unemployment_trend[0] > 0 else 'Decreasing'} by {abs(unemployment_trend[0]):.2f}% per year")

print("\nAnalysis complete. Chart saved as 'economic_demographic_analysis.png'")

