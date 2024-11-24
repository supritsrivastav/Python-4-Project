import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv("dataset2.csv")

# Display initial information about the dataset
print("\n=== Initial Data Analysis ===")
print("\nFirst few rows:")
print(df.head())

print("\nMissing values count:")
print(df.isnull().sum())

print("\nDataset Info:")
print(df.info())

# === Handling Missing Values Using Different Methods ===

# 1. Create a copy of original data to preserve it
df_cleaned = df.copy()

# 2. Fill missing values based on data type and business logic
# For numeric columns - fill with mean
df_cleaned["Age"] = df_cleaned["Age"].fillna(df_cleaned["Age"].mean().round())
df_cleaned["Purchase_Amount"] = df_cleaned["Purchase_Amount"].fillna(
    df_cleaned["Purchase_Amount"].mean().round(2)
)
df_cleaned["Satisfaction_Score"] = df_cleaned["Satisfaction_Score"].fillna(
    df_cleaned["Satisfaction_Score"].mean().round(1)
)

# For categorical columns - fill with mode
df_cleaned["Category"] = df_cleaned["Category"].fillna(df_cleaned["Category"].mode()[0])
df_cleaned["Payment_Method"] = df_cleaned["Payment_Method"].fillna(
    df_cleaned["Payment_Method"].mode()[0]
)
df_cleaned["Name"] = df_cleaned["Name"].fillna("Unknown Customer")

print("\n=== After Filling Missing Values ===")
print("\nMissing values count after cleaning:")
print(df_cleaned.isnull().sum())

# 3. Demonstrate different dropna methods
# Create copies for different dropping strategies
df_drop_all = df.dropna()  # Drop rows with any missing values
df_drop_specific = df.dropna(
    subset=["Purchase_Amount", "Satisfaction_Score"]
)  # Drop rows with missing values in specific columns

print("\n=== Results After Different Dropping Strategies ===")
print(f"\nOriginal dataset shape: {df.shape}")
print(f"Shape after dropping all missing values: {df_drop_all.shape}")
print(f"Shape after dropping specific columns missing values: {df_drop_specific.shape}")

# 4. Analysis of cleaned data
print("\n=== Analysis of Cleaned Data ===")
print("\nSummary Statistics:")
print(df_cleaned.describe())

# 5. Save cleaned dataset
df_cleaned.to_csv("customer_sales_data_cleaned.csv", index=False)

# 6. Visualization of missing values before cleaning
plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap (Before Cleaning)")
plt.savefig("missing_values_heatmap.png")
plt.close()

# 7. Calculate and display some useful statistics
print("\n=== Additional Statistics ===")
print(f"\nAverage Purchase Amount: ${df_cleaned['Purchase_Amount'].mean():.2f}")
print(f"Average Satisfaction Score: {df_cleaned['Satisfaction_Score'].mean():.2f}")
print(f"Most Common Payment Method: {df_cleaned['Payment_Method'].mode()[0]}")
print(f"Most Common Category: {df_cleaned['Category'].mode()[0]}")

# 8. Group analysis
print("\n=== Category-wise Analysis ===")
category_analysis = df_cleaned.groupby("Category")["Purchase_Amount"].agg(
    ["mean", "count"]
)
print("\nCategory-wise Purchase Analysis:")
print(category_analysis)


# Function to demonstrate different filling strategies
def demonstrate_filling_strategies(data, column):
    """
    Demonstrate different strategies for filling missing values
    """
    strategies = {
        "Mean": data[column].fillna(data[column].mean()),
        "Median": data[column].fillna(data[column].median()),
        "Forward Fill": data[column].fillna(method="ffill"),
        "Backward Fill": data[column].fillna(method="bfill"),
    }

    return pd.DataFrame(strategies)


# Demonstrate different filling strategies for Purchase_Amount
print("\n=== Different Filling Strategies for Purchase Amount ===")
filling_demo = demonstrate_filling_strategies(df, "Purchase_Amount")
print(filling_demo.head())