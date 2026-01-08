
-- ==========================================
-- Task 1.3: Business Query Implementation
-- Database: FlexiMart
-- ===========================================

-- -------------------------------------
-- Query 1: Customer Purchase History
-- -------------------------------------

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    c.email,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.subtotal) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.email
HAVING COUNT(DISTINCT o.order_id) >= 2
   AND SUM(oi.subtotal) > 5000
ORDER BY total_spent DESC;


-- ------------------------------------
-- Query 2: Product Sales Analysis
-- --------------------------------------

SELECT
    p.category,
    COUNT(DISTINCT p.product_id) AS num_products,
    SUM(oi.quantity) AS total_quantity_sold,
    SUM(oi.subtotal) AS total_revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
HAVING SUM(oi.subtotal) > 10000
ORDER BY total_revenue DESC;


-- --------------------------------------
-- Query 3: Monthly Sales Trend (2024)
-- --------------------------------------

SELECT
    DATE_FORMAT(o.order_date, '%M %Y') AS month_name,
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(oi.subtotal) AS monthly_revenue,
    SUM(SUM(oi.subtotal)) OVER (
        ORDER BY YEAR(o.order_date), MONTH(o.order_date)
    ) AS cumulative_revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE YEAR(o.order_date) = 2024
GROUP BY YEAR(o.order_date), MONTH(o.order_date)
ORDER BY YEAR(o.order_date), MONTH(o.order_date);
