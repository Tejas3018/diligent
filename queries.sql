
-- Top 10 customers by completed spend
SELECT u.user_id, u.name, u.email, COUNT(o.order_id) AS orders_count, SUM(o.order_total) AS total_spend
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE o.status = 'completed'
GROUP BY u.user_id
ORDER BY total_spend DESC
LIMIT 10;

-- Revenue by category with avg rating
SELECT p.category,
       SUM(oi.line_total) AS revenue,
       COUNT(DISTINCT oi.order_id) AS orders_count,
       ROUND(AVG(r.rating),2) AS avg_rating
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
LEFT JOIN reviews r ON p.product_id = r.product_id
GROUP BY p.category
ORDER BY revenue DESC;

