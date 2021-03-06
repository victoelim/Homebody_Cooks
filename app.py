import os
import config
from flask import Flask
from models.base_model import db
from flask_login import LoginManager

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'homebody_cooks_web')

app = Flask('HOMEBODY COOKS', root_path=web_dir)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")





@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return User.get(User.id == user_id)

@app.before_request
def before_request():
    db.connect()


@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
