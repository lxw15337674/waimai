from app import db
from app.models import User, Businesses, Food

user = User(name='李希望',
            username='lxw15337674',
            password='lxw123456',
            address='河南省',
            category='用户',
            phone='15515255978',
            pin='123456',
            photo='http://img1.skqkw.cn:888/2014/11/26/08t/fj2d1xqvj1k-75634.jpg',
            )
admin = User(name='管理员',
             username='admin',
             password='admin',
             category='管理员',
             )
business = User(name='烤肉拌饭店',
                username='123456',
                password='123456',
                address='河南省',
                category='商家',
                phone='15515255978',
                pin='123456',
                photo='http://img1.skqkw.cn:888/2014/11/26/08t/fj2d1xqvj1k-75634.jpg',
                )

businesses1 = Businesses(name="烤肉店", address="东苑楼下", activities="满二送一", phone=15368588745, category="中餐", deliver_fee=2,
                         photo='https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1493286951&di=493e1b79e39826355442f3ae3e62faf7&src=http://e.hiphotos.baidu.com/bainuo/crop=2,0,636,386;w=469;q=80/sign=18d3edc5f6deb48fef26fb9ecd2d1619/a8ec8a13632762d0122ad31ba5ec08fa513dc67a.jpg',
                         sales=3, user_id=2)

businesses2 = Businesses(name="炒米", address="东苑楼下", activities="没活动", phone=15368588745, category="中餐", deliver_fee=2,
                         photo='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1493904967&di=ef7c2b260990d8a647fb275f864c0635&imgtype=jpg&er=1&src=http%3A%2F%2Fimg.zhuyun.cn%2FM00%2FE5%2FC5%2FwKgJNFdZNJ6Ab-hWAADcQaYKcVs213.jpg',
                         sales=3, user_id=2)

businesses3 = Businesses(name="青春汉堡", address="东苑楼下", activities="没活动", phone=15368588745, category="西餐", deliver_fee=1,
                         photo='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1493310607697&di=e47eac84e7bfa31039c8a0d23ce40234&imgtype=0&src=http%3A%2F%2Fwww.txw6.com%2Fuploads%2Fallimg%2F140814%2F63-140Q41641390-L.jpg',
                         sales=3, user_id=2)

food1 = Food(name="烤肉拌饭",
            introduction="好吃的饭",
            price=3,
            photo='https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1493286951&di=493e1b79e39826355442f3ae3e62faf7&src=http://e.hiphotos.baidu.com/bainuo/crop=2,0,636,386;w=469;q=80/sign=18d3edc5f6deb48fef26fb9ecd2d1619/a8ec8a13632762d0122ad31ba5ec08fa513dc67a.jpg',
            businesses_id=1)


food2 = Food(name="炒米",
            introduction="好吃的饭",
            price=4,
            photo='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1493904967&di=ef7c2b260990d8a647fb275f864c0635&imgtype=jpg&er=1&src=http%3A%2F%2Fimg.zhuyun.cn%2FM00%2FE5%2FC5%2FwKgJNFdZNJ6Ab-hWAADcQaYKcVs213.jpg',
            businesses_id=2)


food3 = Food(name="汉堡",
            introduction="好吃的饭",
            price=7,
            photo='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1493310607697&di=e47eac84e7bfa31039c8a0d23ce40234&imgtype=0&src=http%3A%2F%2Fwww.txw6.com%2Fuploads%2Fallimg%2F140814%2F63-140Q41641390-L.jpg',
            businesses_id=3)



db.session.add(user)
db.session.add(business)
db.session.add(businesses1)
db.session.add(businesses2)
db.session.add(businesses3)
db.session.add(food1)
db.session.add(food2)
db.session.add(food3)

db.session.add(admin)
db.session.commit()
