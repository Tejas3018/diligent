#cat > ingest_to_sqlite.py << 'PY'
import pandas as pd
import sqlite3

conn = sqlite3.connect("ecom.db")

df_users = pd.read_csv("users.csv")
df_products = pd.read_csv("products.csv")
df_orders = pd.read_csv("orders.csv")
df_order_items = pd.read_csv("order_items.csv")
df_reviews = pd.read_csv("reviews.csv")

df_users.to_sql("users", conn, if_exists="replace", index=False)
df_products.to_sql("products", conn, if_exists="replace", index=False)
df_orders.to_sql("orders", conn, if_exists="replace", index=False)
df_order_items.to_sql("order_items", conn, if_exists="replace", index=False)
df_reviews.to_sql("reviews", conn, if_exists="replace", index=False)

cur = conn.cursor()
cur.execute("CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);")
cur.execute("CREATE INDEX IF NOT EXISTS idx_order_items_order_id ON order_items(order_id);")
cur.execute("CREATE INDEX IF NOT EXISTS idx_order_items_product_id ON order_items(product_id);")
cur.execute("CREATE INDEX IF NOT EXISTS idx_reviews_product_id ON reviews(product_id);")
conn.commit()
conn.close()
print('Ingested CSVs into ecom.db')
#PY
