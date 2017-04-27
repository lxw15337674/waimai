from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config.from_object('config')  # 读取配置文件



# 数据库
db = SQLAlchemy(app)

# 登录
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
lm.login_message = u"请先登录"

# 管理员密码
adminpassword = '123'
from app import views, models
