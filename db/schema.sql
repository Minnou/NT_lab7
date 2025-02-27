CREATE SCHEMA bike_store_schema;

CREATE TABLE bike_store_schema.brands (
    brand_id SERIAL PRIMARY KEY,
    brand_name TEXT NOT NULL
);

CREATE TABLE bike_store_schema.categories (
    category_id SERIAL PRIMARY KEY,
    category_name TEXT NOT NULL
);

CREATE TABLE bike_store_schema.customers (
    customer_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL
);

CREATE TABLE bike_store_schema.stores (
    store_id SERIAL PRIMARY KEY,
    store_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL,
    street TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL
);

CREATE TABLE bike_store_schema.products (
    product_id SERIAL PRIMARY KEY,
    product_name TEXT NOT NULL,
    brand_id INT NOT NULL,
    category_id INT NOT NULL,
    model_year TEXT NOT NULL,
    list_price REAL NOT NULL,
    FOREIGN KEY (brand_id) REFERENCES bike_store_schema.brands(brand_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES bike_store_schema.categories(category_id) ON DELETE CASCADE
);

CREATE TABLE bike_store_schema.staffs (
    staff_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    active BOOLEAN NOT NULL,
    store_id INT NOT NULL,
    manager_id INT NULL,
    FOREIGN KEY (store_id) REFERENCES bike_store_schema.stores(store_id) ON DELETE CASCADE
);

CREATE TABLE bike_store_schema.orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_status INT NOT NULL,
    order_date DATE NOT NULL,
    required_date DATE NOT NULL,
    shipped_date DATE NULL,
    store_id INT NOT NULL,
    staff_id INT NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES bike_store_schema.customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (store_id) REFERENCES bike_store_schema.stores(store_id) ON DELETE CASCADE,
    FOREIGN KEY (staff_id) REFERENCES bike_store_schema.staffs(staff_id) ON DELETE CASCADE
);

CREATE TABLE bike_store_schema.order_items (
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    list_price REAL NOT NULL,
    discount REAL NOT NULL,
    PRIMARY KEY (order_id, item_id),
    FOREIGN KEY (order_id) REFERENCES bike_store_schema.orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES bike_store_schema.products(product_id) ON DELETE CASCADE
);

CREATE TABLE bike_store_schema.stocks (
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (store_id, product_id),
    FOREIGN KEY (store_id) REFERENCES bike_store_schema.stores(store_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES bike_store_schema.products(product_id) ON DELETE CASCADE
);

COPY bike_store_schema.brands (brand_id, brand_name)
FROM 'E:\PyPy\NT_lab7\db\brands.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.categories (category_id, category_name)
FROM 'E:\PyPy\NT_lab7\db\categories.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.customers (customer_id, first_name, last_name, phone, email, street, city, state, zip_code)
FROM 'E:\PyPy\NT_lab7\db\customers.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.stores (store_id, store_name, phone, email, street, city, state, zip_code)
FROM 'E:\PyPy\NT_lab7\db\stores.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.products (product_id, product_name, brand_id, category_id, model_year, list_price)
FROM 'E:\PyPy\NT_lab7\db\products.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.staffs (staff_id, first_name, last_name, email, phone, active, store_id, manager_id)
FROM 'E:\PyPy\NT_lab7\db\staffs.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.orders (order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id)
FROM 'E:\PyPy\NT_lab7\db\orders.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.order_items (order_id, item_id, product_id, quantity, list_price, discount)
FROM 'E:\PyPy\NT_lab7\db\order_items.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;

COPY bike_store_schema.stocks (store_id, product_id, quantity)
FROM 'E:\PyPy\NT_lab7\db\stocks.csv' 
DELIMITER ',' 
null as 'NULL' 
CSV HEADER;
