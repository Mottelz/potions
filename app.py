from flask import Flask, redirect, render_template, request, url_for
from model import db, Potion

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.jinja')

@app.route('/about')
def about():
    return render_template('about.jinja')


@app.route('/inventory')
def inventory():
    data = Potion.query.all()
    return render_template('inventory.jinja', potion=data)


@app.route('/potions', methods=['POST'])
def create_potion():
    f_name = request.form['name']
    f_quantity = request.form['quantity']
    f_price = request.form['price']
    to_add = Potion(name=f_name, quantity=f_quantity, price=f_price)
    db.session.add(to_add)
    db.session.commit()
    return redirect(url_for('inventory'))


# @app.route('/inventory/<category>/<id>')
# def lookupItemByRoute(category, id):
#     if category.lower() == 'potions':
#         result = getPotionById(int(id))
#         if result:
#             return result
#         else:
#             return {"error": f"{id} is not a valid {category} id"}
#     else:
#         return {"error": f"{category} is not a valid category"}
