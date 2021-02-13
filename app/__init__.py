from flask import Flask
from datetime import datetime
from pathlib import Path
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

root_dir = Path(__file__).parent.parent
template_dir = root_dir / 'resources/templates'

app = Flask(__name__, template_folder=template_dir,static_url_path='/static', static_folder='../resources/static')

app.config.from_object(Config)

db = SQLAlchemy(app) #ligar la bd a nuestra aplicacion
migrate = Migrate(app, db)

from app.post import postModel, postRouter
from app.producto import productoModel,   productoRouter


# if __name__ == '__main__':
#   app.run()
