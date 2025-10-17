import time
import random
import sys
import os
from colorama import init, Fore, Back, Style

init()

def print_with_delay(text, delay=0.03, color=Fore.WHITE):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def print_command(command, color=Fore.GREEN):
    print(f"{Fore.CYAN}analyst@workstation:~$ {color}{command}{Style.RESET_ALL}")
    time.sleep(0.5)

def print_error(text, delay=0.02):
    for char in text:
        print(f"{Fore.RED}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def print_warning(text, delay=0.02):
    for char in text:
        print(f"{Fore.YELLOW}{char}", end='', flush=True)
        time.sleep(delay)
    print(f"{Style.RESET_ALL}")

def simulate_data_loading():
    print_command("python -c \"import pandas as pd; print('Loading data...')\"")
    print_with_delay("Loading data...", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); print(f'Shape: {df.shape}')\"")
    print_with_delay("Shape: (10000, 15)", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); print(df.info())\"")
    print_with_delay("<class 'pandas.core.frame.DataFrame'>", 0.02)
    print_with_delay("RangeIndex: 10000 entries, 0 to 9999", 0.02)
    print_with_delay("Data columns (total 15 columns):", 0.02)
    print_with_delay(" #   Column         Non-Null Count  Dtype", 0.02)
    print_with_delay("---  ------         --------------  -----", 0.02)
    print_with_delay(" 0   date           10000 non-null  object", 0.02)
    print_with_delay(" 1   product_id     10000 non-null  int64", 0.02)
    print_with_delay(" 2   product_name   10000 non-null  object", 0.02)
    print_with_delay(" 3   category       10000 non-null  object", 0.02)
    print_with_delay(" 4   price          10000 non-null  float64", 0.02)
    print_with_delay(" 5   quantity       10000 non-null  int64", 0.02)
    print_with_delay(" 6   revenue        10000 non-null  float64", 0.02)
    print_with_delay(" 7   customer_id    10000 non-null  int64", 0.02)
    print_with_delay(" 8   region         10000 non-null  object", 0.02)
    print_with_delay(" 9   sales_channel  10000 non-null  object", 0.02)
    print_with_delay(" 10  discount       10000 non-null  float64", 0.02)
    print_with_delay(" 11  profit         10000 non-null  float64", 0.02)
    print_with_delay(" 12  cost           10000 non-null  float64", 0.02)
    print_with_delay(" 13  rating         9876 non-null   float64", 0.02)
    print_with_delay(" 14  review_count   9876 non-null   int64", 0.02)
    print_with_delay("dtypes: float64(5), int64(4), object(6)", 0.02)
    print_with_delay("memory usage: 1.1+ MB", 0.02)
    time.sleep(2)

def simulate_data_cleaning():
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); print('Missing values:'); print(df.isnull().sum())\"")
    print_with_delay("Missing values:", 0.02)
    print_with_delay("date              0", 0.02)
    print_with_delay("product_id        0", 0.02)
    print_with_delay("product_name      0", 0.02)
    print_with_delay("category          0", 0.02)
    print_with_delay("price             0", 0.02)
    print_with_delay("quantity          0", 0.02)
    print_with_delay("revenue           0", 0.02)
    print_with_delay("customer_id       0", 0.02)
    print_with_delay("region            0", 0.02)
    print_with_delay("sales_channel     0", 0.02)
    print_with_delay("discount          0", 0.02)
    print_with_delay("profit            0", 0.02)
    print_with_delay("cost              0", 0.02)
    print_with_delay("rating          124", 0.02)
    print_with_delay("review_count    124", 0.02)
    print_with_delay("dtype: int64", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); df['rating'].fillna(df['rating'].mean(), inplace=True); print('Rating missing values filled')\"")
    print_with_delay("Rating missing values filled", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); df['review_count'].fillna(0, inplace=True); print('Review count missing values filled')\"")
    print_with_delay("Review count missing values filled", 0.02)
    time.sleep(1)

def simulate_exploratory_analysis():
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); print('Summary statistics:'); print(df.describe())\"")
    print_with_delay("Summary statistics:", 0.02)
    print_with_delay("         product_id      price    quantity     revenue  customer_id     discount      profit       cost  rating  review_count", 0.02)
    print_with_delay("count  10000.000000  10000.000  10000.000  10000.000  10000.000000  10000.000000  10000.000000  10000.000000  10000.000000  10000.000000", 0.02)
    print_with_delay("mean    5000.500000     45.678     12.345    567.890   5000.500000      0.123456     89.012345    478.877655     4.234567     15.678901", 0.02)
    print_with_delay("std     2886.895679     23.456      8.901    234.567   2886.895679      0.234567     67.890123    234.567890     0.789012     12.345678", 0.02)
    print_with_delay("min        1.000000     10.000      1.000    100.000      1.000000      0.000000     10.000000    100.000000     1.000000      0.000000", 0.02)
    print_with_delay("25%     2500.750000     25.000      6.000    400.000   2500.750000      0.000000     45.000000    300.000000     3.500000      5.000000", 0.02)
    print_with_delay("50%     5000.500000     45.000     12.000    550.000   5000.500000      0.100000     75.000000    450.000000     4.200000     12.000000", 0.02)
    print_with_delay("75%     7500.250000     65.000     18.000    700.000   7500.250000      0.200000    120.000000    600.000000     5.000000     20.000000", 0.02)
    print_with_delay("max    10000.000000    100.000     50.000   1500.000  10000.000000      0.500000    200.000000   1200.000000     5.000000     50.000000", 0.02)
    time.sleep(2)
    
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); print('Category distribution:'); print(df['category'].value_counts())\"")
    print_with_delay("Category distribution:", 0.02)
    print_with_delay("Electronics    2500", 0.02)
    print_with_delay("Clothing       2000", 0.02)
    print_with_delay("Home           1800", 0.02)
    print_with_delay("Sports         1500", 0.02)
    print_with_delay("Books          1200", 0.02)
    print_with_delay("Beauty         1000", 0.02)
    print_with_delay("Name: category, dtype: int64", 0.02)
    time.sleep(1)

def simulate_data_visualization():
    print_command("python -c \"import matplotlib.pyplot as plt; import pandas as pd; df = pd.read_csv('sales_data.csv'); plt.figure(figsize=(10,6)); df['category'].value_counts().plot(kind='bar'); plt.title('Sales by Category'); plt.savefig('category_sales.png'); print('Chart saved as category_sales.png')\"")
    print_with_delay("Chart saved as category_sales.png", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import matplotlib.pyplot as plt; import pandas as pd; df = pd.read_csv('sales_data.csv'); plt.figure(figsize=(12,8)); df.groupby('region')['revenue'].sum().plot(kind='pie', autopct='%1.1f%%'); plt.title('Revenue by Region'); plt.savefig('revenue_by_region.png'); print('Chart saved as revenue_by_region.png')\"")
    print_with_delay("Chart saved as revenue_by_region.png", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import seaborn as sns; import matplotlib.pyplot as plt; import pandas as pd; df = pd.read_csv('sales_data.csv'); plt.figure(figsize=(10,6)); sns.scatterplot(data=df, x='price', y='quantity'); plt.title('Price vs Quantity'); plt.savefig('price_vs_quantity.png'); print('Chart saved as price_vs_quantity.png')\"")
    print_with_delay("Chart saved as price_vs_quantity.png", 0.02)
    time.sleep(1)

def simulate_statistical_analysis():
    print_command("python -c \"import pandas as pd; from scipy import stats; df = pd.read_csv('sales_data.csv'); correlation = df['price'].corr(df['quantity']); print(f'Price-Quantity correlation: {correlation:.3f}')\"")
    print_with_delay("Price-Quantity correlation: -0.234", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import pandas as pd; from scipy import stats; df = pd.read_csv('sales_data.csv'); electronics = df[df['category']=='Electronics']['revenue']; clothing = df[df['category']=='Clothing']['revenue']; t_stat, p_value = stats.ttest_ind(electronics, clothing); print(f'T-test p-value: {p_value:.6f}')\"")
    print_with_delay("T-test p-value: 0.000123", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); monthly_sales = df.groupby(df['date'].str[:7])['revenue'].sum(); print('Monthly sales trend:'); print(monthly_sales)\"")
    print_with_delay("Monthly sales trend:", 0.02)
    print_with_delay("2024-01    123456.78", 0.02)
    print_with_delay("2024-02    134567.89", 0.02)
    print_with_delay("2024-03    145678.90", 0.02)
    print_with_delay("2024-04    156789.01", 0.02)
    print_with_delay("2024-05    167890.12", 0.02)
    print_with_delay("2024-06    178901.23", 0.02)
    print_with_delay("Name: revenue, dtype: float64", 0.02)
    time.sleep(2)

def simulate_machine_learning():
    print_command("python -c \"from sklearn.model_selection import train_test_split; from sklearn.linear_model import LinearRegression; import pandas as pd; df = pd.read_csv('sales_data.csv'); X = df[['price', 'discount', 'rating']]; y = df['quantity']; X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42); model = LinearRegression(); model.fit(X_train, y_train); print('Model trained successfully')\"")
    print_with_delay("Model trained successfully", 0.02)
    time.sleep(1)
    
    print_command("python -c \"from sklearn.metrics import r2_score, mean_squared_error; from sklearn.linear_model import LinearRegression; import pandas as pd; df = pd.read_csv('sales_data.csv'); X = df[['price', 'discount', 'rating']]; y = df['quantity']; X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42); model = LinearRegression(); model.fit(X_train, y_train); y_pred = model.predict(X_test); r2 = r2_score(y_test, y_pred); mse = mean_squared_error(y_test, y_pred); print(f'R² Score: {r2:.3f}'); print(f'MSE: {mse:.3f}')\"")
    print_with_delay("R² Score: 0.678", 0.02)
    print_with_delay("MSE: 45.234", 0.02)
    time.sleep(1)
    
    print_command("python -c \"import joblib; from sklearn.linear_model import LinearRegression; model = LinearRegression(); joblib.dump(model, 'sales_prediction_model.pkl'); print('Model saved as sales_prediction_model.pkl')\"")
    print_with_delay("Model saved as sales_prediction_model.pkl", 0.02)
    time.sleep(1)

def simulate_report_generation():
    print_command("python -c \"import pandas as pd; df = pd.read_csv('sales_data.csv'); report = open('sales_report.txt', 'w'); report.write('SALES ANALYSIS REPORT\\n'); report.write('='*50 + '\\n'); report.write(f'Total Sales: ${df[\"revenue\"].sum():,.2f}\\n'); report.write(f'Total Orders: {len(df)}\\n'); report.write(f'Average Order Value: ${df[\"revenue\"].mean():.2f}\\n'); report.write(f'Top Category: {df[\"category\"].value_counts().index[0]}\\n'); report.close(); print('Report generated: sales_report.txt')\"")
    print_with_delay("Report generated: sales_report.txt", 0.02)
    time.sleep(1)
    
    print_command("cat sales_report.txt")
    print_with_delay("SALES ANALYSIS REPORT", 0.02)
    print_with_delay("==================================================", 0.02)
    print_with_delay("Total Sales: $5,678,901.23", 0.02)
    print_with_delay("Total Orders: 10000", 0.02)
    print_with_delay("Average Order Value: $567.89", 0.02)
    print_with_delay("Top Category: Electronics", 0.02)
    time.sleep(1)

def main():
    print(f"{Fore.CYAN}=== 데이터 분석 ==={Style.RESET_ALL}")
    print()
    
    simulate_data_loading()
    print()
    
    simulate_data_cleaning()
    print()
    
    simulate_exploratory_analysis()
    print()
    
    simulate_data_visualization()
    print()
    
    simulate_statistical_analysis()
    print()
    
    simulate_machine_learning()
    print()
    
    simulate_report_generation()
    print()

if __name__ == "__main__":
    main() 