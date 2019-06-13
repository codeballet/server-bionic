from flask import (
    render_template,
    url_for,
    flash,
    redirect
)
from myapp import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myapp.models import User, Base
from myapp.forms import RegisterForm

engine = create_engine('postgresql://vagrant:vagrant@localhost/myapp_db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
@app.route('/index')
def index():
    visitors = session.query(User).all()
    return render_template('index.html', visitors = visitors)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # On GET request, return false
    if form.validate_on_submit():
        flash('Registered visitor: {}'.format(form.user_name.data))
        visitor = User(user_name = form.user_name.data)
        session.add(visitor)
        session.commit()
        return redirect(url_for('index'))
    return render_template('register.html', form=form)