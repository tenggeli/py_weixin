# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
)

app = web.application(urls, globals())
#返回wsgi接口
# 需要在main外面，uwsgi调用不会执行main
application = app.wsgifunc()

if __name__ == '__main__':
    # app = web.application(urls, globals())
    # application = app.wsgifunc()
    app.run()

