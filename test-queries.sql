SELECT * FROM brands;

SELECT * FROM products WHERE category_id = 2;

UPDATE products SET list_price = list_price * 2 WHERE product_id = 5;

DELETE FROM orders WHERE order_id = 3;

SELECT * FROM orders WHERE order_date = '2016-01-15';

SELECT * FROM customers WHERE city = 'Sunnyside';

SELECT AVG(list_price) FROM products WHERE brand_id = 1;

SELECT * FROM staffs WHERE store_id = 2;

SELECT SUM(order_id) FROM order_items WHERE discount > 0.15;

SELECT SUM(quantity) FROM stocks WHERE store_id = 1;
