activate_this = '/vagrant/myapp/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/vagrant/myapp')

from myapp import app as application
