from app import db
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255),  nullable=False)
    products = db.relationship('Product', backref='category', lazy='select')

 
    def __init__(self, name=None, price=None):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)

class CategoryForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo nombre es requerido')])
