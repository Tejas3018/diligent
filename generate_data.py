#cat > generate_data.py << 'PY' 
from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker()

NUM_USERS = 200
NUM_PRODUCTS = 80
NUM_ORDERS = 400
NUM_REVIEWS = 120

# Users
users = []
for i in range(1, NUM_USERS+1):
    users.append({
        "user_id": i,
        "name": fake.name(),
        "email": fake.unique.email(),
        "signup_date": fake.date_between(start_date='-2y', end_date='today').isoformat(),
        "city": fake.city()
    })
df_users = pd.DataFrame(users)
df_users.to_csv("users.csv", index=False)

# Products
categories = ["Electronics", "Home", "Clothing", "Sports", "Beauty"]
products = []
for i in range(1, NUM_PRODUCTS+1):
    products.append({
        "product_id": i,
        "name": fake.word().capitalize() + " " + fake.word().capitalize(),
        "category": random.choice(categories),
        "price": round(random.uniform(5, 500), 2),
        "sku": fake.bothify(text='???-#####')
    })
df_products = pd.DataFrame(products)
df_products.to_csv("products.csv", index=False)

# Orders and order items
orders = []
order_items = []
for oid in range(1, NUM_ORDERS+1):
    user_id = random.randint(1, NUM_USERS)
    order_date = fake.date_between(start_date='-1y', end_date='today')
    num_items = random.randint(1, 4)
    total = 0
    for _ in range(num_items):
        p = random.choice(products)
        qty = random.randint(1,3)
        line_total = round(p["price"] * qty, 2)
        total += line_total
        order_items.append({
            "order_item_id": len(order_items)+1,
            "order_id": oid,
            "product_id": p["product_id"],
            "quantity": qty,
            "unit_price": p["price"],
            "line_total": line_total
        })
    orders.append({
        "order_id": oid,
        "user_id": user_id,
        "order_date": order_date.isoformat(),
        "order_total": round(total, 2),
        "status": random.choice(["completed","shipped","returned"])
    })
df_orders = pd.DataFrame(orders)
df_order_items = pd.DataFrame(order_items)
df_orders.to_csv("orders.csv", index=False)
df_order_items.to_csv("order_items.csv", index=False)

# Reviews
reviews = []
for i in range(1, NUM_REVIEWS+1):
    pid = random.randint(1, NUM_PRODUCTS)
    uid = random.randint(1, NUM_USERS)
    reviews.append({
        "review_id": i,
        "product_id": pid,
        "user_id": uid,
        "rating": random.randint(1,5),
        "review_text": fake.sentence(nb_words=12),
        "review_date": fake.date_between(start_date='-1y', end_date='today').isoformat()
    })
df_reviews = pd.DataFrame(reviews)
df_reviews.to_csv("reviews.csv", index=False)

print("Generated: users.csv, products.csv, orders.csv, order_items.csv, reviews.csv")

