from flask import (
    render_template,
    url_for
)
from myapp import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myapp.models import User, Base

engine = create_engine('postgresql://vagrant:vagrant@localhost/myapp_db')
Base.metadata.bind = engine
Session = sessionmaker(bind = engine)
session = Session()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
