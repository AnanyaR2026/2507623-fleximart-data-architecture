-- ===============================
-- DIM_DATE: January – February 2024
-- 30 dates including weekdays and weekends
-- ===============================
INSERT INTO dim_date (date_key, full_date, day_of_week, day_of_month, month, month_name, quarter, year, is_weekend) VALUES
(20240101, '2024-01-01', 'Monday', 1, 1, 'January', 'Q1', 2024, TRUE),
(20240102, '2024-01-02', 'Tuesday', 2, 1, 'January', 'Q1', 2024, FALSE),
(20240103, '2024-01-03', 'Wednesday', 3, 1, 'January', 'Q1', 2024, FALSE),
(20240104, '2024-01-04', 'Thursday', 4, 1, 'January', 'Q1', 2024, FALSE),
(20240105, '2024-01-05', 'Friday', 5, 1, 'January', 'Q1', 2024, FALSE),
(20240106, '2024-01-06', 'Saturday', 6, 1, 'January', 'Q1', 2024, TRUE),
(20240107, '2024-01-07', 'Sunday', 7, 1, 'January', 'Q1', 2024, TRUE),
(20240108, '2024-01-08', 'Monday', 8, 1, 'January', 'Q1', 2024, FALSE),
(20240109, '2024-01-09', 'Tuesday', 9, 1, 'January', 'Q1', 2024, FALSE),
(20240110, '2024-01-10', 'Wednesday', 10, 1, 'January', 'Q1', 2024, FALSE),
(20240111, '2024-01-11', 'Thursday', 11, 1, 'January', 'Q1', 2024, FALSE),
(20240112, '2024-01-12', 'Friday', 12, 1, 'January', 'Q1', 2024, FALSE),
(20240113, '2024-01-13', 'Saturday', 13, 1, 'January', 'Q1', 2024, TRUE),
(20240114, '2024-01-14', 'Sunday', 14, 1, 'January', 'Q1', 2024, TRUE),
(20240115, '2024-01-15', 'Monday', 15, 1, 'January', 'Q1', 2024, FALSE),
(20240116, '2024-01-16', 'Tuesday', 16, 1, 'January', 'Q1', 2024, FALSE),
(20240117, '2024-01-17', 'Wednesday', 17, 1, 'January', 'Q1', 2024, FALSE),
(20240118, '2024-01-18', 'Thursday', 18, 1, 'January', 'Q1', 2024, FALSE),
(20240119, '2024-01-19', 'Friday', 19, 1, 'January', 'Q1', 2024, FALSE),
(20240120, '2024-01-20', 'Saturday', 20, 1, 'January', 'Q1', 2024, TRUE),
(20240121, '2024-01-21', 'Sunday', 21, 1, 'January', 'Q1', 2024, TRUE),
(20240201, '2024-02-01', 'Thursday', 1, 2, 'February', 'Q1', 2024, FALSE),
(20240202, '2024-02-02', 'Friday', 2, 2, 'February', 'Q1', 2024, FALSE),
(20240203, '2024-02-03', 'Saturday', 3, 2, 'February', 'Q1', 2024, TRUE),
(20240204, '2024-02-04', 'Sunday', 4, 2, 'February', 'Q1', 2024, TRUE),
(20240205, '2024-02-05', 'Monday', 5, 2, 'February', 'Q1', 2024, FALSE),
(20240206, '2024-02-06', 'Tuesday', 6, 2, 'February', 'Q1', 2024, FALSE),
(20240207, '2024-02-07', 'Wednesday', 7, 2, 'February', 'Q1', 2024, FALSE),
(20240208, '2024-02-08', 'Thursday', 8, 2, 'February', 'Q1', 2024, FALSE),
(20240209, '2024-02-09', 'Friday', 9, 2, 'February', 'Q1', 2024, FALSE),
(20240210, '2024-02-10', 'Saturday', 10, 2, 'February', 'Q1', 2024, TRUE);

-- ===============================
-- DIM_PRODUCT: 15 products across 3 categories
-- ===============================
INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Samsung Galaxy S21','Electronics','Mobile',45000),
('P002','iPhone 13','Electronics','Mobile',70000),
('P003','HP Laptop','Electronics','Laptop',55000),
('P004','Nike Shoes','Fashion','Footwear',3500),
('P005','Adidas T-Shirt','Fashion','Clothing',1200),
('P006','Levi Jeans','Fashion','Clothing',2800),
('P007','Sony Headphones','Electronics','Accessory',2000),
('P008','Dell Monitor 24"','Electronics','Accessory',12000),
('P009','Organic Almonds','Groceries','Food',900),
('P010','Basmati Rice 5kg','Groceries','Food',650),
('P011','Organic Honey 500g','Groceries','Food',450),
('P012','Boat Earbuds','Electronics','Accessory',1500),
('P013','Puma Sneakers','Fashion','Footwear',4500),
('P014','Reebok Trackpants','Fashion','Clothing',1900),
('P015','OnePlus Nord','Electronics','Mobile',30000);

-- ===============================
-- DIM_CUSTOMER: 12 customers across 4 cities
-- ===============================
INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Bangalore','Karnataka','Regular'),
('C002','Priya Patel','Mumbai','Maharashtra','Premium'),
('C003','Amit Kumar','Delhi','Delhi','Regular'),
('C004','Sneha Reddy','Hyderabad','Telangana','Regular'),
('C005','Vikram Singh','Chennai','Tamil Nadu','Premium'),
('C006','Anjali Mehta','Bangalore','Karnataka','Regular'),
('C007','Ravi Verma','Pune','Maharashtra','Regular'),
('C008','Pooja Iyer','Bangalore','Karnataka','Premium'),
('C009','Karthik Nair','Kochi','Kerala','Regular'),
('C010','Deepa Gupta','Delhi','Delhi','Premium'),
('C011','Arjun Rao','Hyderabad','Telangana','Regular'),
('C012','Lakshmi Krishnan','Chennai','Tamil Nadu','Regular');

-- ===============================
-- FACT_SALES: 40 transactions linking above
-- ===============================
INSERT INTO fact_sales (date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount) VALUES
(20240101,1,1,1,45000,0,45000),
(20240102,2,2,2,70000,0,140000),
(20240103,3,3,1,55000,5000,50000),
(20240104,4,4,3,3500,0,10500),
(20240105,5,5,2,1200,0,2400),
(20240106,6,6,1,2800,0,2800),
(20240107,7,7,2,2000,0,4000),
(20240108,8,8,3,12000,1000,11000),
(20240109,9,9,1,900,0,900),
(20240110,10,10,2,650,0,1300),
(20240111,11,11,3,450,0,1350),
(20240112,12,12,1,1500,0,1500),
(20240113,13,1,2,4500,500,8500),
(20240114,14,2,1,1900,0,1900),
(20240115,15,3,1,30000,2000,28000),
(20240116,1,4,2,45000,0,90000),
(20240117,2,5,1,70000,0,70000),
(20240118,3,6,1,55000,0,55000),
(20240119,4,7,3,3500,0,10500),
(20240120,5,8,2,1200,0,2400),
(20240121,6,9,1,2800,0,2800),
(20240201,7,10,1,2000,0,2000),
(20240202,8,11,2,12000,0,24000),
(20240203,9,12,3,900,0,2700),
(20240204,10,1,2,650,0,1300),
(20240205,11,2,1,450,0,450),
(20240206,12,3,1,1500,0,1500),
(20240207,13,4,2,4500,0,9000),
(20240208,14,5,1,1900,0,1900),
(20240209,15,6,1,30000,0,30000),
(20240210,1,7,3,45000,0,135000),
(20240210,2,8,2,70000,0,140000),
(20240210,3,9,1,55000,0,55000),
(20240210,4,10,1,3500,0,3500),
(20240210,5,11,2,1200,0,2400),
(20240210,6,12,1,2800,0,2800),
(20240210,7,1,1,2000,0,2000),
(20240210,8,2,2,12000,0,24000),
(20240210,9,3,1,900,0,900),
(20240210,10,4,1,650,0,650);
