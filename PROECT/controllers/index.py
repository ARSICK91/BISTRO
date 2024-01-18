from app import app
import random
from flask import render_template, request, session
from utils import get_db_connection
from models.index_model import get_all_dish, add_new_buy, count_dish_by_buy, add_buy, add_buy_dish_product


@app.route('/', methods=['get', 'post'])
def index():
    conn = get_db_connection()
    
    if request.form.getlist('product') and request.form.get('amount_dish') and request.form.get('id_dish') and request.form.get('price'):
        selected_products = request.form.getlist('product')
        amount_dish_by_buy = request.form.get('amount_dish')
        id_dish = request.form.get('id_dish')
        price = request.form.get('price')
        id_buy_dish = add_buy(conn, id_dish, session['id_buy'], amount_dish_by_buy, price)
        add_buy_dish_product(conn, id_buy_dish, id_dish, selected_products)

    elif request.values.get('back_to_index'):
        pass

    else:
        session['number_table'] = int(random.randrange(10))
        id_buy = add_new_buy(conn, session['number_table'])
        session['id_buy'] = id_buy

    df_all_dish = get_all_dish(conn)
    count_dish = count_dish_by_buy(conn, session['id_buy'])

    html = render_template(
        'index.html',
        all_dish=df_all_dish,
        count_dish=count_dish,
        len=len,
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)
