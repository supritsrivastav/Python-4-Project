# 590016738 SUPRIT SRIVASTAVA MCA

# Data Cleaning and Analysis with Pandas
# SCREENSHOT
![image](https://github.com/user-attachments/assets/eab83c05-b403-4bd2-aaf8-4f39a26caed6)
![image](https://github.com/user-attachments/assets/9df32692-adae-4955-9f31-3384fc3d34bc)
![image](https://github.com/user-attachments/assets/1e41d3e8-5ce0-49e2-9e3c-cdf33a69911a)



## Project Description

This project demonstrates comprehensive data cleaning and analysis techniques using Python's Pandas library. It focuses on handling missing values in a customer sales dataset using various methods such as `fillna()` and `dropna()`. The project includes visualization of missing data patterns and provides multiple strategies for data cleaning.

##  Features

- Missing value detection and visualization
- Multiple data cleaning strategies
- Statistical analysis of cleaned data
- Category-wise analysis
- Various filling strategies demonstration
- Data visualization using seaborn and matplotlib
- Comprehensive documentation of cleaning processes

##  Requirements

- Python 3.x
- Required Libraries:
  ```
  pandas
  matplotlib
  seaborn
  ```

a_cleaning.py


##  Key Functions Explained

### 1. Data Loading and Initial Analysis
```python
df = pd.read_csv('customer_sales_data.csv')
df.isnull().sum()
```
- Loads the dataset
- Provides initial missing value count

### 2. Missing Value Handling
```python
# Fill numeric columns with mean
df_cleaned['Age'] = df_cleaned['Age'].fillna(df_cleaned['Age'].mean().round())

# Fill categorical columns with mode
df_cleaned['Category'] = df_cleaned['Category'].fillna(df_cleaned['Category'].mode()[0])
```
- Uses appropriate filling strategies based on data type
- Rounds numeric values for practical use

### 3. Different Dropping Strategies
```python
df_drop_all = df.dropna()  # Complete case analysis
df_drop_specific = df.dropna(subset=['Purchase_Amount', 'Satisfaction_Score'])
```
- Demonstrates various ways to handle missing data through removal

### 4. Custom Filling Strategy Function
```python
def demonstrate_filling_strategies(data, column):
    strategies = {
        'Mean': data[column].fillna(data[column].mean()),
        'Median': data[column].fillna(data[column].median()),
        'Forward Fill': data[column].fillna(method='ffill'),
        'Backward Fill': data[column].fillna(method='bfill')
    }
    return pd.DataFrame(strategies)
```
- Shows different approaches to filling missing values
- Helps in comparing various filling strategies
