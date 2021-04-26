from flask import Flask, render_template
from threading import Thread
import pickledb as dbms
from werkzeug.exceptions import abort

db = dbms.load("playerbal.json", True)

app = Flask(__name__)

def getdbitems(db):
    dx = dict()
    x = list(db.getall())
    for i in x:
        dx[i] = db.get(str(i))
    return dx

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:player_id>')
def playerbal(player_id):
    if(str(db.get(str(player_id))) == 'False'):
        abort(404)
    else:
        return render_template('playerbal.html', balance=(db.get(str(player_id))))

@app.route('/monitoring')
def monitoring():
    return render_template('monitoring.html', balance=getdbitems(db))

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()