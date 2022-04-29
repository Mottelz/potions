'''
This page contains example code that is not used in the project, but used during the lessons
'''

# Examples of three ways to get a variable from the user
@app.route('/potions/<id>')
def potionByRoute(id):
    result = getPotionById(int(id))
    if result:
        return result
    else:
        return {"error": "No potion with that ID found"}

@app.route('/potions')
def potionByParam():
    id = request.args['id']
    result = getPotionById(int(id))
    if result:
        return result
    else:
        return {"error": "No potion with that ID found"}

@app.route('/potions', methods=['POST'])
def potionByPost():
    id = request.json['id']
    result = getPotionById(int(id))
    if result:
        return result
    else:
        return {"error": "No potion with that ID found"}