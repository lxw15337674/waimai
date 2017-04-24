from flask import render_template
from app import app
from app.forms import LoginForm, RegisterForm


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    form = LoginForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     user = User.query.filter_by(name=name).first()
    #     if not user:
    #         flash('该用户不存在')
    #     elif user.password != form.password.data:
    #         flash('密码错误')
    #     else:
    #         login_user(user, form.remember_me.data)
    #         # 初始化,创建购物车
    #         if Order.query.filter_by(user_id=g.user.id, status='购物车').first() is None:
    #             order = Order(g.user.id)
    #             db.session.add(order)
    #             db.session.commit()
    #         flash("登陆成功")
    #         return redirect(url_for("goods"))
    return render_template('login.html', title="登录", form=form)

@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title="注册", form=form)


@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/game')
def game():
    return render_template('game.html')
