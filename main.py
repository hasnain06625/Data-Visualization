import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

print(df.head())


print("Total Sales:", df["Total_Sales"].sum())

product_sales = df.groupby("Product")["Total_Sales"].sum()

plt.figure(figsize=(7,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

region_sales = df.groupby("Region")["Total_Sales"].sum()

plt.figure(figsize=(6,6))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales by Region")
plt.ylabel("")
plt.tight_layout()
plt.show()

print("\nBest Selling Product:")
print(product_sales.idxmax())

print("\nInsights:")
print("1. Total sales calculated successfully.")
print("2. Bar chart shows product-wise sales.")
print("3. Pie chart shows sales by region.")
print("4. Best-selling product identified.")