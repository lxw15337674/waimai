from flask import render_template, flash, redirect, url_for, g
from flask_login import login_user, login_required, logout_user, current_user

from app import app, db, adminpassword, lm, date
from app.forms import LoginForm, RegisterForm, PayForm
from app.models import User, Order, Businesses, Food, OrderItem


@app.route('/')
def index():
    bussinesses = Businesses.query.filter_by().order_by(Businesses.sales).all()
    return render_template('index.html', bussinesses=bussinesses)


@app.route('/shop/<id>', methods=['GET', 'POST'])
@login_required
def food(id):
    bussinesses = Businesses.query.filter_by(id=id).first()
    foods = Food.query.filter_by(businesses_id=id).all()
    return render_template('food.html', shop=bussinesses, foods=foods)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash('该用户不存在')
        elif user.password != form.password.data:
            flash('密码错误')
        else:
            login_user(user, form.remember_me.data)
            # 初始化,创建购物车
            if Order.query.filter_by(user_id=g.user.id, status='购物车').first() is None:
                order = Order(g.user.id)
                db.session.add(order)
                db.session.commit()
            flash("登陆成功")
            return redirect(url_for("index"))
    return render_template('login.html', title="登录", form=form)


# 加入购物车
@app.route('/cart/<id>')
@login_required
def cart(id, num=1):
    order = Order.query.filter_by(user_id=g.user.id, status='购物车').first()  # 购物车
    food = Food.query.filter_by(id=id).first()
    if food.businesses_id != order.businesses_id:
        if order.businesses_id is None:
            order.businesses_id = food.businesses_id
        else:
            flash("请在一个商家下选择菜品")
            return redirect(url_for('food', id=food.businesses_id))
    order.businesses_id = food.businesses_id
    # 如果购物车中存在该商品则直接更新数量,如果不存在则增加该商品
    target = int(id)
    for a in order.items:
        if target == a.food_id:
            a.changenum(num)  # 更新订单商品数量
            order.updatecost()  # 更新订单价格
            db.session.commit()
            flash('已增加数量')
            return redirect(url_for('food', id=order.businesses_id))
    orderitem = OrderItem()
    orderitem.add(food_id=id, num=num, order_id=order.id)
    db.session.add(orderitem)
    order.updatecost()  # 更新订单价格
    db.session.commit()
    flash('已加入购物车')
    return redirect(url_for('food', id=order.businesses_id))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.category.data == adminpassword:
            category = "管理员"
        else:
            category = form.category.data
        user = User(name=form.name.data,
                    username=form.username.data,
                    password=form.password1.data,
                    address=form.address.data,
                    category=category,
                    phone=form.phone.data,
                    pin=form.pin.data,
                    photo=form.photo.data,
                    )
        db.session.add(user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('login'))
    return render_template('register.html', title="注册", form=form)


@app.route('/test')
def test():
    return render_template('test.html')


# 查看购物车
@app.route('/buy', methods=['GET', 'POST'])
@login_required
def buy():
    form = PayForm()
    order = Order.query.filter_by(user_id=g.user.id, status='购物车').first()  # 购物车
    if form.validate_on_submit():
        target = int(form.password.data)
        if g.user.pin == target:
            order.status = '已支付'
            order.time = date.date()
            order.address = User.query.filter_by(id=g.user.id).first().address
            # 再给用户创建购物车
            order = Order(g.user.id)
            db.session.add(order)
            db.session.commit()
            flash("支付成功")
            return redirect(url_for('index'))
        else:
            flash("支付密码错误")
    return render_template('buy.html', order=order, form=form)


@app.route('/order')
def order():
    return render_template('order.html')


@app.route('/game')
def game():
    return render_template('game.html')


# 登出
@login_required
@app.route('/logout')
def logout():
    logout_user()
    flash("登出成功")
    return redirect(url_for('login'))


# 设置请求前的全局用户
@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))
