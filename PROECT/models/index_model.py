import pandas
import datetime
def get_all_dish(conn):
    return pandas.read_sql("""
        SELECT id_dish, type, name_dish, image,
        SUM(price * amount_product) AS total_price,
        SUM(calorie * amount_product) AS total_calories
        FROM dish 
        LEFT JOIN dish_product USING(id_dish)
        LEFT JOIN product USING(id_product)
        GROUP BY id_dish;
""",conn)

def add_new_buy(conn, number_table):
    cur = conn.cursor() 
    current_datetime = datetime.datetime.now()
    cur.execute('''
        INSERT INTO buy ("date_time", "name_guest") VALUES (?, ?);
    ''', (current_datetime, str(number_table)))
    conn.commit()
    return cur.lastrowid

def count_dish_by_buy(conn,id_buy):
    return pandas.read_sql( '''SELECT COUNT(id_buy_dish) AS dish_count
        FROM buy_dish
        WHERE id_buy = :id''',
        conn,
        params={"id": id_buy}
    )
def add_buy(conn,id_dish,id_buy,amount_dish,price):
    cur = conn.cursor() 
    cur.execute('''
        INSERT INTO buy_dish (id_dish, id_buy,amount,price) VALUES (?,?,?,?);
    ''', (int(id_dish), int(id_buy),int(amount_dish), int(amount_dish) * int(price)))
    conn.commit()
    return cur.lastrowid

def add_buy_dish_product(conn, id_buy_dish, id_dish, selected_products):
    cur = conn.cursor()
    query = '''
        INSERT INTO buy_dish_product (id_buy_dish, id_dish_product)
        SELECT ?, id_dish_product
            FROM dish_product
        WHERE id_dish = ? AND id_product IN ({})
    '''.format(','.join('?' for _ in selected_products))
    cur.execute(query, (int(id_buy_dish), int(id_dish), *selected_products))
    conn.commit()



    







