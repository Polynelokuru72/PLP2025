import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    df = pd.read_csv('test.csv')  # Replace with your dataset path
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
    exit()  # Exit if the file is not found

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Explore the structure of the dataset
print("\nData Types:")
print(df.dtypes)

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean the dataset by filling missing values with the mean of each column
df.fillna(df.mean(), inplace=True)  # Fills missing values with column means
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
# Compute basic statistics of the numerical columns
print("\nBasic Statistics of Numerical Columns:")
print(df.describe())

# Group by a categorical column (e.g., 'Department') and compute the mean of 'Sales' per department
if 'Department' in df.columns:
    department_avg_sales = df.groupby('Department')['Sales'].mean()
    print("\nAverage Sales per Department:")
    print(department_avg_sales)

# Task 3: Data Visualization
# 1. Line chart: Trends over time (ensure 'Date' is in datetime format)
plt.figure(figsize=(10, 6))
df['Date'] = pd.to_datetime(df['Date'])  # Ensure 'Date' column is in datetime format
df.set_index('Date', inplace=True)
df['Sales'].plot(kind='line', title='Sales Trend Over Time', color='b')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# 2. Bar chart: Comparing average sales across departments
plt.figure(figsize=(10, 6))
avg_sales_per_dept = df.groupby('Department')['Sales'].mean().sort_values()
avg_sales_per_dept.plot(kind='bar', title='Average Sales per Department', color='g')
plt.xlabel('Department')
plt.ylabel('Average Sales')
plt.show()

# 3. Histogram: Distribution of sales
plt.figure(figsize=(10, 6))
df['Sales'].hist(bins=20, color='orange', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: Relationship between Sales and Advertising Expense
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Sales', y='AdvertisingExpense', color='purple')
plt.title('Sales vs Advertising Expense')
plt.xlabel('Sales')
plt.ylabel('Advertising Expense')
plt.show()
