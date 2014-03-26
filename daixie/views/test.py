# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

#configs
app.config.from_object('config')


try:
    app.config.from_pyfile(app.config['DIR_CONFS'] + '/website_config.py', silent=False)
    print '[SUCCESS] load config file: ' + app.config['DIR_CONFS'] + '/website_config.py'
except Exception, e:
    pass

#
# DB
#
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

#
# Mail
#
from flask_mail import Mail
mail = Mail(app)

#
# assets
#
from flask.ext.assets import Environment, Bundle
assets = Environment(app)
less = Bundle('site/css/common.less', filters='less,cssmin', output='gen/less.css')
all_css = Bundle('bootstrap/css/bootstrap.min.css', 'datepicker/datetimepicker.min.css', less, filters='cssmin', output='gen/packed.css')
all_js = Bundle('jQuery/jquery-1.10.2.min.js','bootstrap/js/bootstrap.min.js', 'datepicker/datetimepicker.min.js', 'site/js/common.js',filters='jspacker', output='gen/packed.js')

assets.register('all_css', all_css)
assets.register('all_js', all_js)

#
# Login
#
from flask.ext.login import LoginManager
from daixie.biz.user import UserBiz

login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "general.login"
login_manager.login_message_category = "danger"
login_manager.login_message = u"这个页面需要登录后才能访问"

#
# Handler
#
@login_manager.user_loader
def load_user(user_id):
    return UserBiz.get_user_by_id(user_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(403)
def too_large(error):
    return render_template('403.html'), 403

@app.errorhandler(500)
def catch_error(error):
    return render_template('500.html'), 500

#
# Blueprints
#
from daixie.views import general
from daixie.views import user
from daixie.views import order

app.register_blueprint(general.mod)
app.register_blueprint(user.mod)
app.register_blueprint(order.mod)
