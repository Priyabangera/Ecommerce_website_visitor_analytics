from flask import Flask
from flask_cors import CORS
from db import db
from landing import landing_blueprint
from dashboard import dashboard_blueprint

app =Flask(__name__)
CORS(app)


#SET DB config
username = 'root' 
password = ''
userpass='mysql+pymysql://'+username+':'+password+'@'

server='127.0.0.1'
dbname='/ecommerce_analytics'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

#Register Blueprint
app.register_blueprint(landing_blueprint)
app.register_blueprint(dashboard_blueprint)

@app.route('/serverstatus')
def serverstatus():

    return "Server is up and running"



if __name__=='__main__':
    app.debug =True
    app.run()

