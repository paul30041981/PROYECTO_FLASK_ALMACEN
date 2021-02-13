from app import db
from datetime import datetime
from decimal import Decimal
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255),  nullable=False)
    price = db.Column(db.Float)

 
    def __init__(self, name=None, price=None):
        self.name = name
        self.price = price

    def __repr__(self):
        return '<Product %r>' % (self.name)

class ProductForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired('Este campo nombre es requerido')])
    price = DecimalField('Precio', validators=[
        DataRequired('Este campo precio es requerido'),
        NumberRange(min=Decimal('0.0'), max=None, message='Precio debe de ser Mayor a 0')
        ])
    # submit = SubmitField('Conectarse')
