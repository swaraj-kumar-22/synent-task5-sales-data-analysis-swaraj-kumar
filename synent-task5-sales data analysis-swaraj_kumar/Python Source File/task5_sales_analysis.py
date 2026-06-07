import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Superstore.csv")

print("Dataset Preview")
print(df.head())

# Data Cleaning
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month_Year'] = df['Order Date'].dt.to_period('M')

# Monthly Revenue Trends
monthly_sales = df.groupby('Month_Year')['Sales'].sum()

plt.figure(figsize=(12,6))
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month-Year")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_revenue_trend.png")
plt.show()

# Top Selling Products
top_products = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
top_products.plot(kind='bar')
plt.title("Top Selling Products")
plt.tight_layout()
plt.savefig("visuals/top_selling_products.png")
plt.show()

# Profit by Category
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind='bar')
plt.title("Profit by Category")
plt.tight_layout()
plt.savefig("visuals/profit_by_category.png")
plt.show()

# Profit by Region
region_profit = df.groupby('Region')['Profit'].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind='bar')
plt.title("Profit by Region")
plt.tight_layout()
plt.savefig("visuals/profit_by_region.png")
plt.show()

print("\\nBusiness Insights:")
print("1. Technology category performs strongly.")
print("2. Some regions generate higher profits.")
print("3. Monthly trends help identify peak sales periods.")
