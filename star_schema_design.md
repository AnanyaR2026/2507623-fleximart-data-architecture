# FlexiMart Star Schema Design Documentation

## Section 1: Schema Overview

### FACT TABLE: fact_sales
- Grain: One row per product per order line item  
- Business Process: Sales transactions  

**Measures (Numeric Facts):**
- quantity_sold: Number of units sold  
- unit_price: Price per unit at the time of sale  
- discount_amount: Discount applied to the item  
- total_amount: Final amount (quantity × unit_price - discount)  

**Foreign Keys:**  
- date_key → dim_date  
- product_key → dim_product  
- customer_key → dim_customer  

---

### DIMENSION TABLE: dim_date
- Purpose: Date dimension for time-based analysis  
- Type: Conformed dimension  

**Attributes:**  
- date_key (PK): Surrogate key, integer, format YYYYMMDD  
- full_date: Actual date (YYYY-MM-DD)  
- day_of_week: Monday, Tuesday, etc.  
- day_of_month: 1-31  
- month: 1-12  
- month_name: January, February, etc.  
- quarter: Q1, Q2, Q3, Q4  
- year: 2023, 2024, etc.  
- is_weekend: Boolean (TRUE/FALSE)  

---

### DIMENSION TABLE: dim_product
- Purpose: Product dimension for product-level analysis  
- Type: Conformed dimension  

**Attributes:**  
- product_key (PK): Surrogate key  
- product_id: Original product identifier  
- product_name: Name of the product  
- category: Product category (Electronics, Fashion, Groceries, etc.)  
- subcategory: More specific grouping (Mobile, Footwear, Food, etc.)  
- unit_price: Price per unit  

---

### DIMENSION TABLE: dim_customer
- Purpose: Customer dimension for customer-level analysis  
- Type: Conformed dimension  

**Attributes:**  
- customer_key (PK): Surrogate key  
- customer_id: Original customer identifier  
- customer_name: Full name of the customer  
- city: City of residence  
- state: State of residence  
- customer_segment: Customer segment (Regular, Premium, etc.)  

---

## Section 2: Design Decisions

1. Granularity Choice: 
   We chose transaction line-item level granularity to capture every product sold per order. This allows detailed analysis such as revenue per product, quantity trends, and discounts applied on each item. It ensures accurate aggregation at multiple levels (daily, monthly, category-level, etc.).  

2. Use of Surrogate Keys:
   Surrogate keys (integers) are used instead of natural keys to improve join performance, reduce storage size, and avoid issues with changing natural identifiers (e.g., product IDs or customer emails). Surrogate keys are stable, ensuring data integrity over time.  

3. Support for Drill-down and Roll-up:
   This star schema allows easy OLAP operations:  
   - Drill-down: Aggregate sales by month → day → individual transactions  
   - Roll-up: Aggregate sales by product category → all products  
   - Time-series analysis: Monthly, quarterly, yearly revenue trends  
   - Customer insights: Purchase patterns by city or segment  

Overall, this design balances query efficiency, scalability, and analytical flexibility.

---

## Section 3: Sample Data Flow

Source Transaction: 
- Order #101, Customer "John Doe", Product "Laptop", Quantity: 2, Unit Price: 50,000  

Transformed into Star Schema:

fact_sales:
```json
{
  "date_key": 20240115,
  "product_key": 5,
  "customer_key": 12,
  "quantity_sold": 2,
  "unit_price": 50000,
  "discount_amount": 0,
  "total_amount": 100000
}
