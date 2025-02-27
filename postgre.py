import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def execute_query(cursor, query, param=None):
    if param != None:
        cursor.execute(query, (param,))
    else:
        cursor.execute(query)
    return cursor.fetchall()

try:
    connection = psycopg2.connect(dbname="bike_store_db",
                                user="postgres",
                                password="postgres",
                                host="127.0.0.1",
                                port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor= connection.cursor()

    cursor.execute("SET search_path TO bike_store_schema;")
    
    print("Бренды: ", execute_query(cursor, "SELECT * FROM brands;"))

    print("Товары категории 2: ", execute_query(cursor, "SELECT * FROM products WHERE category_id = %s;", 2))

    print("Обновлённый товар: ", execute_query(cursor, "UPDATE products SET list_price = list_price * 2 WHERE product_id = %s RETURNING *;", 5))

    print("Удалённый заказ: ", execute_query(cursor, "DELETE FROM orders WHERE order_id = %s RETURNING *;", 3))
    
    print("Заказы за 2016-01-15: ", execute_query(cursor, "SELECT * FROM orders WHERE order_date = %s;", '2016-01-15'))

    print("Клиенты из Sunnyside: ", execute_query(cursor, "SELECT * FROM customers WHERE city = %s;", 'Sunnyside'))

    print("Средняя цена товаров бренда 1: ", execute_query(cursor, "SELECT AVG(list_price) FROM products WHERE brand_id = %s;", 1))

    print("Сотрудники магазина 2: ", execute_query(cursor, "SELECT * FROM staffs WHERE store_id = %s;", 2))

    print("Количество товаров со скидкой: ", execute_query(cursor, "SELECT SUM(order_id) FROM order_items WHERE discount > 0.15;"))

    print("Общее количество товаров в магазине 1: ", execute_query(cursor, "SELECT SUM(quantity) FROM stocks WHERE store_id = %s;", 1))

    print("Средняя цена товаров по брендам: ", execute_query(cursor, "SELECT b.brand_name, AVG(p.list_price) AS avg_price FROM products p \
                                                                        JOIN brands b ON p.brand_id = b.brand_id GROUP BY b.brand_name;"))
    
    print("Общая сумма продаж по каждому магазину: ", execute_query(cursor, "SELECT s.store_name, SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_sales \
                                                                            FROM order_items oi JOIN orders o ON oi.order_id = o.order_id \
                                                                            JOIN stores s ON o.store_id = s.store_id GROUP BY s.store_name;"))
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSql ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSql закрыто")