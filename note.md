#配置python flask

##环境配置
采用Python3.6+flask+flask_SQLAlchemy进行配置，开发环境使用pyCharm。

**可以在系统python下安装相应的库**（不推荐）

方法如下：

* 如果安装了py可执行程序，在cmd输入

`py -3 -m pip install flask,flask-sqlalchemy,werkzeug,Jinja2`

* 如果没安装的话就把`\..(对应目录)..\Python36\Scripts`加入系统环境变量,然后cmd输入

`pip install flask,flask-sqlalchemy,werkzeug,Jinja2`

* 然后在pyCharm新建工程的时候导入系统python库即可：
在新建Flask工程时注意勾选`Inherit global site-packages`

不推荐的原因是，这种方法没有与系统python环境相隔离，还有可能引入一堆无关的库

**直接在pyCharm配置虚拟环境**（推荐）

在新建Flask工程时使用了virtualenv，生成了与系统环境隔离的虚拟环境

在菜单`file > setting > project > project interpreter`可以看到当前环境下的依赖库，也可以点击旁边"+"号添加库

但我遇到的问题是很多第三方库不知道哪个是对的，于是我采用cmd方式添加库：

* 打开cmd，cd进入工程下的`venv\Scripts\`目录，执行`activate`即可进入虚拟环境

* 同上步骤使用`pip install flask-sqlalchemy,werkzeug,Jinja2`（不需要安装flask，pyCharm已集成 ）

* 重启pyCharm



## 数据库连接
采用的是mysql8.0.11解压版进行安装

在mysql5.7环境里,虽然可以设置default_authentication_plugin来改变认证加密方式,但是一般人不会去设置.在mysql8.0下,默认变成了default_authentication_plugin=caching_sha2_password,包括你刚初始化的root用户也是这个认证加密方式,这样的结果是让你除非用新的协议驱动,例如必须用8.0自带的mysql客户端才行,不然就连接不上数据库.这样就必然造成不兼容的情况,幸好,是可以改回旧的方式的.

## 