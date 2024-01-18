import pandas

def get_dish(conn,id_dish):
    return pandas.read_sql("""
    SELECT name_dish, 
           SUM(calorie * amount_product) AS total_weight,
           SUM(price * amount_product) AS total_price, 
           image
           FROM dish 
            JOIN dish_product USING(id_dish)
            JOIN product USING(id_product)                       
            WHERE id_dish = :id
           GROUP BY id_dish;
    """, 
    conn,
    params= {'id': id_dish}
)
def get_dish_product(conn,id_dish):
    return pandas.read_sql("""
        SELECT id_product,name_product, amount_product
        FROM product
        JOIN dish_product USING(id_product)
        JOIN dish USING(id_dish)
        WHERE id_dish = :id
    """, 
    conn,
    params= {'id': id_dish}
)