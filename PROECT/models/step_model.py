import pandas


def update_buy(conn):
    cur = conn.cursor()
    cur.execute('''
        UPDATE step_buy
        SET id_step = 
            CASE
                WHEN id_step = 1 THEN 2
                WHEN id_step = 2 THEN 3
                ELSE id_step
            END;
''')
    conn.commit()


def insert(conn, buy_id):
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO step_buy (id_step, id_buy)
        VALUES (1, :id_buy);
    ''', {'id_buy': buy_id})
    conn.commit()


def select_all(conn):
    return pandas.read_sql('''
        SELECT id_buy, step_image
        FROM step_buy
        JOIN step USING(id_step)
        ORDER BY id_buy DESC;
''',conn)
