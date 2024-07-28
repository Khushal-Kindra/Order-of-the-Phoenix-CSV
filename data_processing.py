import pandas as pd
import sys

def process_data(df):
    # Drop rows where 'order_id', 'customer_id', or 'product_id' are missing
    df.dropna(subset=['order_id', 'customer_id', 'product_id'], inplace=True)

    # Convert 'order_date' to datetime, coerce errors, and fill NaT with a default date
    df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
    df['order_date'].fillna(pd.to_datetime('2000-01-01'), inplace=True)

    # Fill missing 'product_name' with 'Unknown'
    df['product_name'].fillna('Unknown', inplace=True)

    # Convert 'product_price' to float and fill missing values with the mean
    df['product_price'] = df['product_price'].astype(float)
    mean_price = df['product_price'].mean()
    df['product_price'].fillna(mean_price, inplace=True)

    # Ensure no negative product prices
    df['product_price'] = df['product_price'].apply(lambda x: max(x, 0))

    # Convert 'quantity' to float to handle NaNs, fill missing values with the median, and convert back to int
    df['quantity'] = df['quantity'].astype(float)
    median_quantity = df['quantity'].median()
    df['quantity'].fillna(median_quantity, inplace=True)

    # Ensure no negative quantities and convert back to int
    df['quantity'] = df['quantity'].apply(lambda x: max(int(x), 0))

    # Create 'year_month' column
    df['year_month'] = df['order_date'].dt.to_period('M')

    return df

