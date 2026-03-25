DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT,
    price INTEGER,
    stock INTEGER
);

INSERT INTO products VALUES ('P001', 'Earphones', 'Electronics', 499, 50);
INSERT INTO products VALUES ('P002', 'Bluetooth Speaker', 'Audio', 699, 40);
INSERT INTO products VALUES ('P003', 'Smart Watch', 'Wearable', 1299, 25);
INSERT INTO products VALUES ('P004', 'Keyboard', 'Computer', 899, 60);
INSERT INTO products VALUES ('P005', 'Headphones', 'Audio', 1999, 30);
INSERT INTO products VALUES ('P006', 'Power Bank', 'Mobile Accessories', 2599, 20);
INSERT INTO products VALUES ('P007', 'Laptop Stand', 'Computer', 1499, 35);
INSERT INTO products VALUES ('P008', 'Gaming Mouse', 'Computer', 999, 45);
INSERT INTO products VALUES ('P009', 'USB Cable', 'Accessories', 199, 100);
INSERT INTO products VALUES ('P010', 'Wireless Charger', 'Mobile Accessories', 1299, 50);
INSERT INTO products VALUES ('P011', 'Tablet', 'Electronics', 15999, 15);
INSERT INTO products VALUES ('P012', 'Smartphone', 'Electronics', 24999, 20);
INSERT INTO products VALUES ('P013', 'Monitor', 'Computer', 8999, 25);
INSERT INTO products VALUES ('P014', 'Printer', 'Computer', 6999, 10);
INSERT INTO products VALUES ('P015', 'Router', 'Networking', 1999, 30);
INSERT INTO products VALUES ('P016', 'SSD 512GB', 'Storage', 3999, 40);
INSERT INTO products VALUES ('P017', 'Hard Drive 1TB', 'Storage', 4999, 35);
INSERT INTO products VALUES ('P018', 'Fitness Band', 'Wearable', 2499, 50);
INSERT INTO products VALUES ('P019', 'Webcam', 'Computer', 1499, 25);
INSERT INTO products VALUES ('P020', 'Microphone', 'Audio', 2999, 20);


INSERT INTO products VALUES ('P021', 'Faulty Item', NULL, -500, NULL);
INSERT INTO products VALUES ('P022', 'Luxury TV', 'Electronics', 999999, 2);
