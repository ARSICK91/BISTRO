from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.order_model import get_order_dishes, get_order_price, get_order_distinct, delete_dish


@app.route('/order', methods=['get', 'post'])
def order():
    conn = get_db_connection()
    if request.values.get('delete'):
        delete_dish(conn, int(request.values.get('delete')))

    df_order_dishes = get_order_dishes(conn, session['id_buy'])
    df_price = get_order_price(conn, session['id_buy'])
    df_dish_dis = get_order_distinct(conn, session['id_buy'])

    html = render_template(
        'order.html',
        buy_id=session['id_buy'],
        df_order_dishes=df_order_dishes,
        df_price=df_price,
        df_dish_dis=df_dish_dis,
        len=len,
    )
    return html


if __name__ == '__main__':
    app.run(debug=True)
