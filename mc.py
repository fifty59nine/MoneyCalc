from flask import Flask, render_template, request, redirect, url_for, session

from datetime import datetime

import db

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='FFFFf636278H!sf38'
)

@app.route('/', methods=['post','get'])
def reg_log():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if db.correct(login, password):
            session['login'] = login
            print(url_for('main'))
            return redirect(url_for('main', login = login))
        else:
            message = 'Неверный логин или пароль'
    return render_template('index.html')

@app.route('/main', methods=['post','get'])
def main():
    login = request.args['login']
    login = session['login']
    balance = db.get_bal(login)
    p_or_m = ''
    now = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'POST':
        if request.form.get('minus') == 'option1':
            p_or_m = '+'
        else:
            p_or_m = '-'
        summ = request.form.get('summ')
        text = request.form.get('info')
        date = request.form.get('dt')
        
        try:
            summ = int(summ)
            if p_or_m == '+':
                db.earning(login, summ, text, date)
            else:
                db.expense(login, summ, text, date)
        except:
            return render_template('main.html')

    return render_template('main.html', balance=balance, now=now)

@app.route('/history', methods=['get'])
def history():
    login = request.args['login']
    login = session['login']
    money = db.get_list(login)
    return render_template('history.html', money=money)