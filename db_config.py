from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Lumia2020*'
app.config['MYSQL_DATABASE_DB'] = 'nemesis'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['UPLOAD_FOLDER'] = './uploads'
app.config['UPLOAD_EXCEL'] = './excel'

mysql.init_app(app)

#class Config(object):
#    MAIL_SERVER = 'smtp.gmail.com'
#    MAIL_PORT = 587
#    MAIL_USE_SSL = False
#    MAIL_USE_TLS = True,
#    MAIL_USERNAME = 'sistemanemesis18@gmail.com'
#    MAIL_PASSWORD = 'Nemesis2021!'
    #MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')
