import pandas

def get_order_dishes(conn, id_buy):
    return pandas.read_sql("""
        SELECT buy_dish.id_dish, amount, buy_dish.price AS buy_dish_price, name_dish, name_product,image,id_buy_dish
        FROM buy_dish
        JOIN dish USING(id_dish)
        JOIN buy_dish_product USING(id_buy_dish)
        JOIN dish_product USING(id_dish_product)
        JOIN product USING(id_product)
        WHERE id_buy = :id_buy
""", conn, params={"id_buy": id_buy})


def get_order_price(conn, id_buy):
    return pandas.read_sql("""
        SELECT SUM(price) AS total_price
        FROM buy_dish
        WHERE id_buy = :id_buy
""", conn, params={"id_buy": id_buy})


def get_order_distinct(conn, id_buy):
    return pandas.read_sql("""
        SELECT DISTINCT name_dish, image,id_buy_dish,price,amount
        FROM buy_dish
        JOIN dish USING(id_dish)
        JOIN buy_dish_product USING(id_buy_dish)
        WHERE id_buy = :id_buy
""", conn, params={"id_buy": id_buy})

def delete_dish(conn,id_buy_dish):
    cur = conn.cursor() 

    cur.execute('''
    DELETE FROM buy_dish_product WHERE id_buy_dish = ?;
    ''', (id_buy_dish,))
    conn.commit()
    
    cur.execute('''
        DELETE FROM buy_dish WHERE id_buy_dish = ?;
    ''', (id_buy_dish,))
    conn.commit()
