import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(dbname="bike_store_db",
                                  user="postgres",
                                  password="postgres",
                                  host="127.0.0.1",
                                  port="5432")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor= connection.cursor()

    cursor.execute("SET search_path TO bike_store_schema;")

    cursor.execute("SELECT * FROM brands;")
    print("Бренды:", cursor.fetchall())

    cursor.execute("SELECT * FROM products WHERE category_id = %s;", (2,))
    print("Товары категории 2:", cursor.fetchall())

    cursor.execute("UPDATE products SET list_price = list_price * 2 WHERE product_id = %s RETURNING *;", (5,))
    print("Обновлённый товар:", cursor.fetchone())

    cursor.execute("DELETE FROM orders WHERE order_id = %s RETURNING *;", (3,))
    print("Удалённый заказ:", cursor.fetchone())

    cursor.execute("SELECT * FROM orders WHERE order_date = %s;", ('2016-01-15',))
    print("Заказы за 2016-01-15:", cursor.fetchall())

    cursor.execute("SELECT * FROM customers WHERE city = %s;", ('Sunnyside',))
    print("Клиенты из Sunnyside:", cursor.fetchall())

    cursor.execute("SELECT AVG(list_price) FROM products WHERE brand_id = %s;", (1,))
    print("Средняя цена товаров бренда 1:", cursor.fetchone())

    cursor.execute("SELECT * FROM staffs WHERE store_id = %s;", (2,))
    print("Сотрудники магазина 2:", cursor.fetchall())

    cursor.execute("SELECT SUM(order_id) FROM order_items WHERE discount > 0.15;")
    print("Количество товаров со скидкой:", cursor.fetchall())

    cursor.execute("SELECT SUM(quantity) FROM stocks WHERE store_id = %s;", (1,))
    print("Общее количество товаров в магазине 1:", cursor.fetchone())

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSql ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSql закрыто")