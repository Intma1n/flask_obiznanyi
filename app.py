import cursor as cursor

from config import Configuration
from posts.blueprint import posts
from flask import Flask, render_template, request, json
from flask import Blueprint
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(posts, url_prefix='/')
db = SQLAlchemy(app)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'mysql'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

#conn = mysql.connect()
#cursor = conn.cursor()
#data = cursor.fetchall()