from flask import Flask, request

from staticModel import getAllPotions, getPotionById


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'You are now home'

@app.route('/inventory')
def inventory():
    stock = {
        'potions': getAllPotions()
    }
    return stock

@app.route('/inventory/<category>/<id>')
def lookupItemByRoute(category, id):
    if category.lower() == 'potions':
        result = getPotionById(int(id))
        if result:
            return result
        else:
            return {"error": f"{id} is not a valid {category} id"}
    else:
        return {"error": f"{category} is not a valid category"}



# @app.route('/potions/<id>')
# def potionByRoute(id):
#     result = getPotionById(int(id))
#     if result:
#         return result
#     else:
#         return {"error": "No potion with that ID found"}

# @app.route('/potions')
# def potionByParam():
#     id = request.args['id']
#     result = getPotionById(int(id))
#     if result:
#         return result
#     else:
#         return {"error": "No potion with that ID found"}

# @app.route('/potions', methods=['POST'])
# def potionByPost():
#     id = request.json['id']
#     result = getPotionById(int(id))
#     if result:
#         return result
#     else:
#         return {"error": "No potion with that ID found"}