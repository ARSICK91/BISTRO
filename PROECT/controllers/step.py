from app import app
from flask import render_template, request, session
from utils import get_db_connection
from models.step_model import insert, select_all, update_buy
import threading
import schedule
import time


def job():
    conn = get_db_connection()
    update_buy(conn)


def run_schedule():
    schedule.every(1).to(5).seconds.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)


t = threading.Thread(target=run_schedule)
t.start()

@app.route('/step', methods=['get', 'post'])
def step():
    conn = get_db_connection()
    new_order = False
    if request.values.get('add_step'):
        insert(conn, int(request.values.get('add_step')))
        new_order = True

    df_buy_step = select_all(conn)
    html = render_template(
        'step.html',
        new_order=new_order,
        df_buy_step=df_buy_step,
        len=len,
    )
    return html
