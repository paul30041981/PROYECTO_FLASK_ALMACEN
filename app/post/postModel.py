from app import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100),  nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String(500),  nullable=False)

    def __repr__(self):
        return f'Menu: {self.titulo}'
