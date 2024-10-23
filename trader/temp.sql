USE shop;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO products (product_name, price, stock_quantity)
VALUES
('Laptop', 999.99, 10),
('Smartphone', 599.99, 25),
('Headphones', 199.99, 50),
('Keyboard', 49.99, 100),
('Mouse', 29.99, 150);