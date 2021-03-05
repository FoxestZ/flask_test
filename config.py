#encoding: utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'zlktqa_demo'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SECRET_KEY = "jjjsks"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 邮箱配置
# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址
# MAIL_SERVER = "smtp.qq.com"
# MAIL_PORT = '587'
# MAIL_USE_TLS = True
# MAIL_USE_SSL
# MAIL_USERNAME = "1281838272@qq.com"
# MAIL_PASSWORD = "haudnncaxopaghbb" # 生成授权码，授权码是开启smtp服务后给出的
# MAIL_DEFAULT_SENDER = 1281838272@qq.com