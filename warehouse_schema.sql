-- ===============================
-- DIMENSION TABLE: dim_date
-- ===============================
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    day_of_week VARCHAR(10),
    month INT,
    month_name VARCHAR(15),
    quarter VARCHAR(2),
    year INT,
    is_weekend BOOLEAN
);

-- ===============================
-- DIMENSION TABLE: dim_product
-- ===============================
CREATE TABLE dim_product (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    product_id VARCHAR(20),
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price_range VARCHAR(20)
);

-- ===============================
-- DIMENSION TABLE: dim_customer
-- ===============================
CREATE TABLE dim_customer (
    customer_key INT AUTO_INCREMENT PRIMARY KEY,
    customer_id VARCHAR(20),
    customer_name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50),
    registration_date DATE
);

-- ===============================
-- FACT TABLE: fact_sales
-- ===============================
CREATE TABLE fact_sales (
    sales_id INT AUTO_INCREMENT PRIMARY KEY,
    date_key INT,
    product_key INT,
    customer_key INT,
    quantity_sold INT,
    unit_price DECIMAL(10,2),
    discount_amount DECIMAL(10,2),
    total_amount DECIMAL(10,2),

    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key)
);
