from myapp import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, Virtual World!"
