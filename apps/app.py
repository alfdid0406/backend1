from pathlib import Path
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from apps.config import config
# ...생략...(이미 쓰여져 있으므로 굳이 표시 안하는 부분)
db = SQLAlchemy()
csrf = CSRFProtect()

login_manager = LoginManager()
login_manager.login_view = "auth signup" # 로그인 안했을 때 리다이렉트
login_manager.login_message = ""

def create_app(config_key):
    app = Flask(__name__)

    app.config.from_object(config[config_key])

    csrf.init_app(app)
    # SQLAlchemy와 앱을 연계한다
    db.init_app(app)
    # Migrate와 앱을 연계한다
    Migrate(app, db)

    login_manager.init_app(app)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    from apps.auth import views as auth_views

    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    return app



# def create_app() :
#     app = Flask(__name__)

#     app.config.from_mapping(
#         SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
#         SQLALCHEMY_DATABASE_URI=
#             f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
#         SQLALCHEMY_TRACK_MODIFICATIONS=False,
#         # SQL을 콘솔 로그에 출력하는 설정
#         SQLALCHEMY_ECHO=True,
        
#         WTF_CSRF_SECRET_KEY="dkssudgktpdy:)"
#     )
