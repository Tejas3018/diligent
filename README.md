This project fulfills the assessment requirements using Cursor-style workflows 

1. Synthetic Data Generation
Run:

python generate_data.py
Creates:

users.csv

products.csv

orders.csv

order_items.csv

reviews.csv

All data is generated using Faker with realistic relationships.

2. Ingest Into SQLite
Run:

python ingest_to_sqlite.py
This creates:

ecom.db

With tables:

users

products

orders

order_items

reviews

Indexes are added to speed joins.

3. SQL Join Queries
Run:

sqlite3 ecom.db < queries.sql
Produces:

✔ Top Customers by Spend
(user_id, name, email, orders_count, total_spend)

✔ Revenue by Product Category
(category, revenue, orders_count, avg_rating)

## Output Preview

Here is the SQL join result:

![Output Screenshot](output.png)

4. Tech Stack
Python (pandas, faker, sqlite3)

SQLite

SQL joins

GitHub

5. How to Reproduce
pip install pandas faker
python generate_data.py
python ingest_to_sqlite.py
sqlite3 ecom.db < queries.sql
