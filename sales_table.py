from sqlalchemy import create_engine
import pandas as pd

# Connect to MySQL
my_conn = create_engine('mysql+pymysql://root:Biroktikor211@localhost/new_app')

# Import some data from a CSV file
df = pd.read_csv(r"C:\Users\nhnah\Downloads\sales_data.csv")

# Load the imported CSV into your database
df.to_sql('sales_details', my_conn, if_exists='append', index=False)

