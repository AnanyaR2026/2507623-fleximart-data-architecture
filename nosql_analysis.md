
# Task 2.1: NoSQL Justification Report

## Section A: Limitations of RDBMS (Relational Databases)

Structured and predictable data is ideal for relational databases like MySQL. However, managing contemporary e-commerce product data presents a number of difficulties.

Fixed Schema Limitation: All products in an RDBMS have to adhere to the same table structure. When different items need distinct qualities, this creates an issue. 
For instance, while shoes require size, color, and material, computers require fields like RAM, CPU, and storage. 
Multiple complex tables or numerous useless (NULL) columns result from storing all of them in a single table.

Frequent Schema Changes: Adding new product categories frequently necessitates using ALTER TABLE to modify already-existing tables. 
Large databases may experience outages as a result of these dangerous, time-consuming processes.

Complex Handling of Nested Data: Foreign keys must be used to link customer reviews that are kept in different tables. 
Multiple JOIN operations are needed to retrieve product details and reviews, which lowers performance and increases query complexity.

Scalability Issues: Relational databases mainly scale vertically, which becomes costly and ineffective as data volume increases.

---

## Section B: Benefits of NoSQL (MongoDB)

MongoDB uses a flexible, document-oriented methodology to overcome the drawbacks of relational databases.

Flexible Schema Design: Every document can have a unique structure thanks to MongoDB. 
It is possible to store products with diverse properties in the same collection without having to adhere to a predetermined schema. 
Because of this, adding new product kinds is simple and doesn't need changing the database structure.

Embedded Documents: As embedded arrays, customer reviews can be kept right within the product document. 
This makes it possible to retrieve product and review data more quickly and does away with the requirement for joins.

Easy Schema Evolution: New fields can be added to documents at any moment without affecting data that already exists. 
This is perfect for dynamic work settings where needs are always changing.

Horizontal Scalability: Data can be spread across several servers thanks to MongoDB's support for sharding. 
Large datasets and heavy traffic loads can be handled effectively because to this.

---

## Section C: Trade-offs of Using MongoDB

MongoDB has some drawbacks despite its scalability and flexibility.

Weaker Transaction Support: For intricate, multi-step financial procedures requiring stringent ACID compliance, MongoDB's transaction processing is less effective than MySQL's.

Data Validation and Consistency: By default, MongoDB does not impose strict schema requirements. 
This increases development responsibility and raises the possibility of incorrect data since data validation must be done at the application level.
