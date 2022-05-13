from flask import Flask, redirect, render_template, request, url_for
from model import db, Potion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('page.html', title='Home', message='Welcome home!')

@app.route('/about')
def about():
    return render_template('page.html', title='About', message='This is the about page. We have nothing to talk about yet.')


@app.route('/inventory')
def inventory():
    data = Potion.query.all()
    return render_template('inventory.html', title='Inventory', potions=data)


@app.route('/potion', methods=['GET','POST'])
def create_potion():
    if request.method == 'GET':
        return render_template('potion.html', title='Add a Potion')
    else:
        f_name = request.form['name']
        f_quantity = request.form['quantity']
        f_price = request.form['price']
        to_add = Potion(name=f_name, quantity=f_quantity, price=f_price)
        db.session.add(to_add)
        db.session.commit()
        return redirect(url_for('inventory'))


@app.route('/filter-items', methods=['GET', 'POST'])
def filter_items():
    if request.method == 'GET':
        return render_template('search.html', title='Search')
    else:
        f_max = request.form['max']
        data = Potion.query.filter(Potion.price <= int(f_max)).all()
        return render_template('inventory.html', title='Search results', potions=data)
