import unittest
import pandas as pd
from io import StringIO
from data_processing import process_data

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        # Create a sample CSV string to use for creating DataFrame
        self.sample_data = StringIO("""
order_id,customer_id,product_id,order_date,product_name,product_price,quantity
1,CUST100,ABC23,01/12/2023,Product A,100.23,2
2,CUST099,ABC24,13/01/2023,Product B,,3
3,CUST065,ABC25,14/02/2023,,150.29,1
4,CUST078,ABC26,15/03/2023,Product D,200.10,
5,CUST055,ABC27,,Product E,250.35,5
6,CUST008,,16/04/2023,Product F,300.00,4
,CUST032,,17/05/2023,Product G,350.20,3
7,CUST012,ABC29,18/06/2023,Product H,-50.12,2
8,CUST023,ABC30,19/07/2023,Product I,400.23,-1
""")
        self.df = pd.read_csv(self.sample_data)

    def test_process_data(self):
        print("Original DataFrame:")
        print(self.df)

        processed_df = process_data(self.df.copy())

        print("Processed DataFrame:")
        print(processed_df)

        # Check that rows with missing order_id, customer_id, or product_id are dropped
        self.assertFalse(processed_df[['order_id', 'customer_id', 'product_id']].isnull().any().any())

        # Check that order_date is converted to datetime and missing values are filled
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(processed_df['order_date']))
        self.assertFalse(processed_df['order_date'].isnull().any())

        # Check that product_name missing values are filled with 'Unknown'
        self.assertFalse(processed_df['product_name'].isnull().any())
        self.assertIn('Unknown', processed_df['product_name'].values)


        # Check that product_price and quantity are converted to float and int respectively
        self.assertTrue(pd.api.types.is_float_dtype(processed_df['product_price']))
        self.assertTrue(pd.api.types.is_integer_dtype(processed_df['quantity']))

        # Check for negative values in product_price and quantity
        self.assertFalse((processed_df['product_price'] < 0).any())
        self.assertFalse((processed_df['quantity'] < 0).any())

        # Check that year_month column is added correctly
        self.assertIn('year_month', processed_df.columns)
        self.assertTrue(pd.api.types.is_period_dtype(processed_df['year_month']))

if __name__ == '__main__':
    unittest.main()

