##Flask-WTF
使用最新版0.9.3  具体见 https://flask-wtf.readthedocs.org/en/latest/

我已经改过来了，以后写其他代码的时候记得用最新的

##import问题
不要使用from daigou.biz.user import * 这种形式，应该具体到确定的类或者函数。

如：from daigou.biz.user import UserBiz

##Flask-Mail
MAIL_SERVER用127.0.0.1, 就是用本机来做发件服务器，不要用gmail

MAIL_ADDR_MY 用 u'代购 <noreply@daigou.com>'

##UI
这个还是得自己写。。。看下Bootstrap 3

## __init__.py
404, 500等错误页面没有定义

##gitignore
提交代码的时候用git status 看下会提交哪些文件, 临时文件不要提交

##参考
需要参考代码的时候，尽量看smallstudent的代码，感觉那个写得好一些。

##安装新的框架
记得在docs/install.md里标注下，方便其他人看到

##tower.im
已完成的任务记得勾选已完成

##css和js
css：用less编写，具体看下官网，尽量避免在具体网页使用style="..."语法

js:

一些公用的, 工具式的js代码写在common.js中,

对于特定流程中会用到的,功能性的js代码,可放置在site/js/中新建的相关文件夹里,

对于特定网页会用到的少量代码直接写在该html文件中.

##html
一般网页都应该继承自"layout.html"

安装juggernaut和redis,redis-server
pip install redis juggernaut
sudo apt-get install redis-server
服务器要先启动redis和juggernaut
#start redis
redis-server
#start juggernaut
juggernaut