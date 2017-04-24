from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, RadioField, FileField
from wtforms.validators import DataRequired, EqualTo, Length, Regexp, Email, ValidationError


class LoginForm(FlaskForm):
    user = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住登录状态', default=False)
    submit = SubmitField('登录')


class RegisterForm(FlaskForm):
    user = StringField('用户名', validators=[DataRequired()])
    password1 = PasswordField('密码', validators=[
        DataRequired(), EqualTo('password2', message='密码必须相同.')])
    password2 = PasswordField('再次输入密码', validators=[DataRequired()])
    address = StringField('地址', validators=[DataRequired()])
    phone = StringField('手机号', validators=[DataRequired(), Length(11, 11, message="必须为11位数字"),
                                           Regexp('[0-9]*', message='必须为数字')])
    submit = SubmitField('注册')

    # def validate_username(self, field):
    #     if User.query.filter_by(name=field.data).first():
    #         raise ValidationError('用户名已经被使用.')


class UploadForm(FlaskForm):
    name = StringField('商品名称', validators=[DataRequired()])
    photo = StringField('商品图片', validators=[DataRequired()])
    introduction = StringField('商品介绍', validators=[DataRequired()])
    price = StringField('商品价格', validators=[DataRequired(), Regexp('[0-9]*', message='必须为数字')])
    submit = SubmitField('提交')


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired(message="搜索不能为空")])
    submit = SubmitField('搜索')
