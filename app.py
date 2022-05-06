from flask import Flask, redirect, render_template, request, url_for
from model import db, Potion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('page.jinja', title='Home', msg='Welcome home!')

@app.route('/about')
def about():
    return render_template('about.jinja', title='About', msg='This is the about page.')


@app.route('/inventory')
def inventory():
    data = Potion.query.all()
    potions = []
    if type(data) is not type([]):
        potions.append(data.to_dict())
    else:
        for p in data:
            potions.append(p.to_dict())

    return render_template('inventory.jinja', title='Inventory', potion=potions)


@app.route('/potions', methods=['POST'])
def create_potion():
    f_name = request.form['name']
    f_quantity = request.form['quantity']
    f_price = request.form['price']
    to_add = Potion(name=f_name, quantity=f_quantity, price=f_price)
    db.session.add(to_add)
    db.session.commit()
    return redirect(url_for('inventory'))
