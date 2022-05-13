from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Potion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.id}: {self.name}\tqty: {self.quantity}\tprice: {self.price}'
