from flask_app import app
#remember to add controller files as you build them... ex below
from flask_app.controllers import controller_main, controller_user



if __name__=="__main__":
    app.run(debug=True)