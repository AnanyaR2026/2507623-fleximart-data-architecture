
"""etl_pipeline.py

Original file is located at
    https://colab.research.google.com/drive/1TlbwKq4MqUaZeLdcVr4XKTd9q8t4CYEk
"""

import pandas as pd
import sqlite3

# --------------------------
# Step 1: Load customers
# --------------------------
customers_text = """customer_id,first_name,last_name,email,phone,city,registration_date
C001,Rahul,Sharma,rahul.sharma@gmail.com,9876543210,Bangalore,2023-01-15
C002,Priya,Patel,priya.patel@yahoo.com,+91-9988776655,Mumbai,2023-02-20
C003,Amit,Kumar,,9765432109,Delhi,2023-03-10
C004,Sneha,Reddy,sneha.reddy@gmail.com,9123456789,Hyderabad,15/04/2023
C005,Vikram,Singh,vikram.singh@outlook.com,09988112233,Chennai,2023-05-22
C006,Anjali,Mehta,anjali.mehta@gmail.com,9876543210,Bangalore,2023-06-18
C007,Ravi,Verma,,+919876501234,Pune,2023-07-25
C008,Pooja,Iyer,pooja.iyer@gmail.com,9123456780,Bangalore,08-15-2023
C009,Karthik,Nair,karthik.nair@yahoo.com,9988776644,Kochi,2023-09-30
C010,Deepa,Gupta,deepa.gupta@gmail.com,09871234567,Delhi,2023-10-12
C001,Rahul,Sharma,rahul.sharma@gmail.com,9876543210,Bangalore,2023-01-15
C011,Arjun,Rao,arjun.rao@gmail.com,9876509876,Hyderabad,2023-11-05
C012,Lakshmi,Krishnan,,9988001122,Chennai,2023-12-01
C013,Suresh,Patel,suresh.patel@outlook.com,9123409876,Mumbai,2024-01-08
C014,Neha,Shah,neha.shah@gmail.com,+91-9876543221,Ahmedabad,2024-01-15
C015,Manish,Joshi,manish.joshi@yahoo.com,9988776611,Jaipur,20/01/2024
C016,Divya,Menon,divya.menon@gmail.com,9123456701,Bangalore,2024-02-05
C017,Rajesh,Kumar,rajesh.kumar@gmail.com,09876123450,Delhi,2024-02-12
C018,Kavya,Reddy,,9988112200,Hyderabad,2024-02-18
C019,Arun,Pillai,arun.pillai@outlook.com,9876543298,Kochi,02-25-2024
C020,Swati,Desai,swati.desai@gmail.com,9123456712,Pune,2024-03-01
C021,Nikhil,Bose,nikhil.bose@gmail.com,+919988776600,Kolkata,2024-03-10
C022,Priyanka,Jain,priyanka.jain@yahoo.com,9876543287,Indore,2024-03-15
C023,Rohit,Kapoor,,9988112211,Chandigarh,2024-03-20
C024,Meera,Nambiar,meera.nambiar@gmail.com,9123456723,Trivandrum,03-25-2024
C025,Sanjay,Agarwal,sanjay.agarwal@gmail.com,09876543276,Lucknow,2024-03-28
"""

with open("customers.csv", "w") as f:
    f.write(customers_text)

customers_df = pd.read_csv("customers.csv")

# Remove duplicates
customers_df = customers_df.drop_duplicates()

# Fill missing emails
customers_df['email'] = customers_df['email'].fillna('unknown@example.com')

# Standardize phone
def standardize_phone(phone):
    phone = str(phone).strip()
    if phone.startswith("0"):
        phone = "+91-" + phone[1:]
    elif phone.startswith("+91"):
        phone = phone.replace(" ","")
    else:
        phone = "+91-" + phone
    return phone

customers_df['phone'] = customers_df['phone'].apply(standardize_phone)

# Standardize registration_date
customers_df['registration_date'] = pd.to_datetime(customers_df['registration_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Drop CSV customer_id for AUTOINCREMENT
customers_to_load = customers_df.drop(columns=['customer_id'])

# ------------------------------
# Step 2: Load products
# ------------------------------
products_text = """product_id,product_name,category,price,stock_quantity
P001,Samsung Galaxy S21,Electronics,45999.00,150
P002,Nike Running Shoes,fashion,3499.00,80
P003,Apple MacBook Pro,ELECTRONICS,,45
P004,Levi's Jeans,Fashion,2999.00,120
P005,Sony Headphones,electronics,1999.00,200
P006,Organic Almonds,Groceries,899.00,
P007,HP Laptop,Electronics,52999.00,60
P008,Adidas T-Shirt,FASHION,1299.00,150
P009,Basmati Rice 5kg,groceries,650.00,300
P010,OnePlus Nord,Electronics,,95
P011,Puma Sneakers,Fashion,4599.00,70
P012,Dell Monitor 24inch,Electronics,12999.00,40
P013,Woodland Shoes,fashion,5499.00,55
P014,iPhone 13,Electronics,69999.00,80
P015,Organic Honey 500g,Groceries,450.00,200
P016,Samsung TV 43inch,ELECTRONICS,32999.00,35
P017,H&M Shirt,Fashion,,90
P018,Masoor Dal 1kg,groceries,120.00,500
P019,Boat Earbuds,Electronics,1499.00,250
P020,Reebok Trackpants,FASHION,1899.00,110
"""

with open("products.csv", "w") as f:
    f.write(products_text)

products_df = pd.read_csv("products.csv")

# Remove duplicates
products_df = products_df.drop_duplicates()

# Standardize category names
products_df['category'] = products_df['category'].str.strip().str.title()

# Convert price to numeric and fill missing with median per category
products_df['price'] = pd.to_numeric(products_df['price'], errors='coerce')
products_df['price'] = products_df.groupby('category')['price'].transform(lambda x: x.fillna(x.median()))

# Fill stock_quantity missing with 0
products_df['stock_quantity'] = pd.to_numeric(products_df['stock_quantity'], errors='coerce').fillna(0).astype(int)

# Drop CSV product_id for AUTOINCREMENT
products_to_load = products_df.drop(columns=['product_id'])

# ------------------------------
# Step 3: Load transactions
# ------------------------------
transactions_text = """transaction_id,customer_id,product_id,quantity,unit_price,transaction_date,status
T001,C001,P001,1,45999.00,2024-01-15,Completed
T002,C002,P004,2,2999.00,2024-01-16,Completed
T003,C003,P007,1,52999.00,15/01/2024,Completed
T004,,P002,1,3499.00,2024-01-18,Pending
T005,C005,P009,3,650.00,2024-01-20,Completed
T006,C006,P012,1,12999.00,01-22-2024,Completed
T007,C007,P005,2,1999.00,2024-01-23,Completed
T008,C008,,1,1299.00,2024-01-25,Completed
T009,C009,P011,1,4599.00,2024-01-28,Cancelled
T010,C010,P006,5,899.00,2024-02-01,Completed
T001,C001,P001,1,45999.00,2024-01-15,Completed
T011,C011,P014,1,69999.00,02/02/2024,Completed
T012,C012,P003,1,52999.00,2024-02-05,Completed
T013,C013,P015,3,450.00,2024-02-08,Completed
T014,C014,P019,2,1499.00,02-10-2024,Completed
T015,C015,P008,3,1299.00,2024-02-12,Completed
T016,,P013,1,5499.00,2024-02-15,Pending
T017,C017,P016,1,32999.00,2024-02-18,Completed
T018,C018,P020,2,1899.00,2024-02-20,Completed
T019,C019,P018,10,120.00,02/22/2024,Completed
T020,C020,P010,1,45999.00,2024-02-25,Completed
T021,C021,P017,2,2999.00,2024-02-28,Completed
T022,C002,P001,1,45999.00,2024-03-01,Completed
T023,C003,P019,3,1499.00,03-02-2024,Completed
T024,C004,P009,5,650.00,2024-03-05,Completed
T025,C005,,1,1999.00,2024-03-08,Completed
T026,C006,P011,1,4599.00,2024-03-10,Completed
T027,C007,P002,2,3499.00,03/12/2024,Completed
T028,C008,P015,4,450.00,2024-03-15,Completed
T029,C009,P007,1,52999.00,2024-03-18,Completed
T030,,P004,3,2999.00,2024-03-20,Pending
T031,C011,P012,1,12999.00,03-22-2024,Completed
T032,C012,P016,1,32999.00,2024-03-25,Completed
T033,C013,P005,2,1999.00,2024-03-28,Completed
T034,C014,P008,2,1299.00,2024-03-30,Completed
T035,C015,P018,8,120.00,04/01/2024,Completed
T036,C016,P014,1,69999.00,2024-04-03,Completed
T037,C017,P006,4,899.00,2024-04-05,Completed
T038,C018,P020,1,1899.00,04-08-2024,Completed
T039,C019,P019,2,1499.00,2024-04-10,Completed
T040,C020,P013,1,5499.00,2024-04-12,Completed
"""

with open("transactions.csv","w") as f:
    f.write(transactions_text)

transactions_df = pd.read_csv("transactions.csv")

# Remove duplicates
transactions_df = transactions_df.drop_duplicates()

# Standardize date
transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Ensure numeric types
transactions_df['quantity'] = pd.to_numeric(transactions_df['quantity'], errors='coerce').fillna(0).astype(int)
transactions_df['unit_price'] = pd.to_numeric(transactions_df['unit_price'], errors='coerce').fillna(0.0)
transactions_df['subtotal'] = transactions_df['quantity'] * transactions_df['unit_price']

# Connect to SQLite
conn = sqlite3.connect("fleximart.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS order_items")
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS customers")

# Create tables
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    city TEXT,
    registration_date DATE
)
""")
cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_quantity INTEGER DEFAULT 0
)
""")
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE NOT NULL,
    total_amount REAL NOT NULL,
    status TEXT DEFAULT 'Pending',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")
cursor.execute("""
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price REAL NOT NULL,
    subtotal REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")
conn.commit()

# ------------------------------
# Load customers
# ------------------------------

# Create a temporary column for unique identifier for duplicate emails
customers_to_load['temp_email_suffix'] = customers_to_load.groupby('email').cumcount()

# Update emails only for those that were duplicates and have a suffix > 0
mask_for_modification = customers_to_load['temp_email_suffix'] > 0

# Apply the modification to generate unique emails
def generate_unique_email(row):
    email_parts = row['email'].split('@')
    prefix = email_parts[0]
    domain = email_parts[1]
    return f"{prefix}_{row['temp_email_suffix']}@{domain}"

customers_to_load.loc[mask_for_modification, 'email'] = customers_to_load[mask_for_modification].apply(generate_unique_email, axis=1)

# Drop the temporary column
customers_to_load = customers_to_load.drop(columns=['temp_email_suffix'])

customers_to_load.to_sql("customers", conn, if_exists='append', index=False)

# Fetch numeric customer IDs
customer_map = pd.read_sql("SELECT customer_id, email FROM customers", conn)

# Load products
products_to_load.to_sql("products", conn, if_exists='append', index=False)

# Fetch numeric product IDs
product_map = pd.read_sql("SELECT product_id, product_name FROM products", conn)

# Map customer_id
transactions_mapped = transactions_df.merge(customer_map, left_on='customer_id', right_on='email', how='left')
transactions_mapped.rename(columns={'customer_id_y':'customer_id_numeric'}, inplace=True)

# Filter out transactions without a valid customer_id
valid_transactions_for_orders = transactions_mapped.dropna(subset=['customer_id_numeric'])


orders_data_to_insert = valid_transactions_for_orders.groupby('transaction_id').agg(
    customer_id=('customer_id_numeric','first'),
    order_date=('transaction_date','first'),
    total_amount=('subtotal','sum'),
    status=('status','first')
).reset_index() 

orders_data_to_insert['customer_id'] = orders_data_to_insert['customer_id'].astype(int)


orders_data_to_insert['total_amount'] = orders_data_to_insert['total_amount'].astype(float)

orders_for_db = orders_data_to_insert[['customer_id', 'order_date', 'total_amount', 'status']]
orders_for_db.to_sql("orders", conn, if_exists='append', index=False)


# Fetch all orders from the database
all_db_orders = pd.read_sql("SELECT order_id, customer_id, order_date, total_amount, status FROM orders", conn)


all_db_orders['total_amount'] = all_db_orders['total_amount'].astype(float)


orders_with_db_id = pd.merge(
    orders_data_to_insert, # Contains 'transaction_id' and the order details
    all_db_orders,
    on=['customer_id', 'order_date', 'total_amount', 'status'],
    how='left'
)

# Map product_id
# Filter out transaction items without a valid product_id
valid_transaction_items = transactions_mapped.dropna(subset=['product_id'])
transactions_items_prepped = valid_transaction_items.merge(product_map, left_on='product_id', right_on='product_name', how='left')
transactions_items_prepped.rename(columns={'product_id_y':'product_id_numeric'}, inplace=True) # product_id_numeric is the DB product ID

order_items_final_df = transactions_items_prepped.merge(
    orders_with_db_id[['transaction_id', 'order_id']],
    on='transaction_id',
    how='left'
)


order_items_to_load = order_items_final_df.dropna(subset=['order_id'])

order_items_to_load = order_items_to_load[[
    'order_id',
    'product_id_numeric',
    'quantity',
    'unit_price',
    'subtotal'
]].copy()
order_items_to_load.rename(columns={'product_id_numeric':'product_id'}, inplace=True)

order_items_to_load['order_id'] = order_items_to_load['order_id'].astype(int)


order_items_to_load.to_sql("order_items", conn, if_exists='append', index=False)

with open("data_quality_report.txt","w") as f:
    f.write("FLEXIMART ETL DATA QUALITY REPORT\n")
    f.write("================================\n")
    f.write(f"Customers processed: {len(customers_to_load)}\n")
    f.write(f"Products processed: {len(products_to_load)}\n")
    f.write(f"Orders processed: {len(orders_summary)}\n")
    f.write(f"Order Items processed: {len(order_items_to_load)}\n")

conn.close()
print("ETL Pipeline completed successfully!")
print("Data Quality report generated: data_quality_report.txt")
