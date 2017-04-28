from app import db


# 用户
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64))
    phone = db.Column(db.String(128))
    category = db.Column(db.String(64))
    photo = db.Column(db.String(128))
    pin = db.Column(db.Integer, nullable=False)


    # 是否被认证
    def is_authenticated(self):
        return True

    # 是否有效,除非用户被禁止
    def is_active(self):
        return True

    # 是否匿名
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, category, pin=0, photo='', phone=0, address='', name='wtf'):
        self.username = username
        self.category = category
        self.password = password
        self.pin = pin
        self.phone = phone
        self.photo = photo
        self.address = address
        self.name = name


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    introduction = db.Column(db.String(1000))
    photo = db.Column(db.String(140))
    price = db.Column(db.Integer)
    businesses_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))

    def __init__(self, name, introduction, price, photo, businesses_id):
        self.name = name
        self.introduction = introduction
        self.price = price
        self.photo = photo
        self.businesses_id = businesses_id

        # 头像
        # def avatar(self):
        #     fruit = .query.filter_by(id=self.id).first()
        #     img = fruit.photo
        #     return img


# 商家
class Businesses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    address = db.Column(db.String(64))
    activities = db.Column(db.String(128))
    phone = db.Column(db.String(128))
    category = db.Column(db.String(64))
    deliver_fee = db.Column(db.Integer, default=0)
    sales = db.Column(db.Integer, default=0)
    photo = db.Column(db.String(128))
    assess = db.relationship('Assess', backref='businesses', lazy='dynamic')
    food = db.relationship('Food', backref='businesses', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, address, activities, photo, phone, category, deliver_fee, sales, user_id):
        self.name = name
        self.address = address
        self.activities = activities
        self.photo = photo
        self.category = category
        self.deliver_fee = deliver_fee
        self.sales = sales
        self.user_id = user_id
        self.phone = phone



class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_name = db.Column(db.String(30))
    user_phone = db.Column(db.String(30))
    businesses_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
    user_address = db.Column(db.String(30))
    status = db.Column(db.String(5))  # 订单属性:购物车,未支付,完成
    items = db.relationship('OrderItem', backref='order', lazy='dynamic')

    def __init__(self, user_id):
        # 初始化用户的购物车(首先检查用户是否有购物车, 没有就添加)
        self.user_id = user_id
        self.status = "购物车"
        self.user_address = ''
        self.cost = 0

    # 更新价格
    def updatecost(self):
        cost = 0
        for a in self.items:
            cost += a.cost
        self.cost = cost


# 订单的单个商品
class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer)
    food_name = db.Column(db.String(64))
    price = db.Column(db.Integer)
    num = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    Order_id = db.Column(db.Integer, db.ForeignKey('order.id'), )

    # 添加商品到购物车
    def add(self, food_id, num, order_id):
        self.food_id = food_id
        self.food_name = Food.query.filter_by(id=food_id).first().name
        self.price = Food.query.filter_by(id=food_id).first().price
        self.num = num
        self.cost = self.price * self.num
        self.Order_id = order_id

    # 改变商品数量
    def changenum(self, num):
        self.num += num
        self.cost = self.price * self.num


# 评价
class Assess(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(64))
    score = db.Column(db.Integer)
    time = db.Column(db.DateTime)
    businesses_id = db.Column(db.Integer, db.ForeignKey('businesses.id'))
