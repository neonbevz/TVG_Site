from flask import Flask, render_template, send_file, send_from_directory, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = bin(random.randint(0, 10000))[2:]


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if request.form['name'] == 'TVGadmin' and request.form['password'] == 'pass':
            session['logged'] = True
            return redirect('/')
        else:
            return redirect('/login')


@app.route('/')
def index():
    try:
        if session['logged']:
            return render_template('index.html')
    except KeyError:
        return redirect('/login')


@app.route('/css/<path:path>')
def style(path):
    return send_from_directory('static/css', path)


@app.route('/img/<path:path>')
def image(path):
    return send_from_directory('static/img', path)


@app.route('/js/<path:path>')
def script(path):
    return send_from_directory('static/js', path)


@app.route('/fonts/<path:path>')
def font(path):
    return send_from_directory('static/fonts', path)


@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')


@app.errorhandler(404)
def err404(e):
    return render_template('error.html', error='Error 404', message='Page not found'), 404


@app.errorhandler(403)
def err403(e):
    return render_template('error.html', error='Error 403', message='Access forbidden'), 403


@app.errorhandler(500)
def err500(e):
    return render_template('error.html', error='Error 500', message='Internal error'), 500


if __name__ == '__main__':
    app.run()
