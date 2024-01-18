from app import app
from flask import render_template, request, session
# import sqlite3
from utils import get_db_connection
from models.edit_dish_model import get_dish, get_dish_product

@app.route('/edit_dish', methods=['get', 'post'])
def edit_dish():
    conn = get_db_connection()
    if request.values.get('dish'):
        dish_id = int(request.values.get('dish'))

    df_dish = get_dish(conn, dish_id)
    df_product = get_dish_product(conn,dish_id)
    html = render_template(
        'edit_dish.html',
        product = df_product,
        dish=df_dish,
        dish_id = dish_id,
        len=len,
    )
    return html
