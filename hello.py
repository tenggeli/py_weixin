#!/usr/bin/env python
# -*- coding: utf-8 -*-
import web
urls = (
        '/t', 'test', #测试
        '/', 'home'
)
app = web.application(urls, globals())
#返回wsgi接口
# 需要在main外面，uwsgi调用不会执行main
application = app.wsgifunc()
class test:
    '测试'
    def GET(self):
        # 开发测试用
        referer = web.ctx.env.get('HTTP_REFERER', 'http://google.com')
        client_ip = web.ctx.env.get('REMOTE_ADDR')
        host = web.ctx.env.get('host')
        fullpath = web.ctx.fullpath
        user_agent = web.ctx.env.get('HTTP_USER_AGENT')
        data = ""
        data += 'Client: %s<br/>\n' % client_ip
        data += 'User-agent: %s<br/>\n' % user_agent
        data += 'FullPath: %s<br/>\n' % fullpath
        data += 'Referer: %s<br/>\n' % referer
        return data
    def POST(self):
        pass
class home:
    '根目录请求的处理'
    def GET(self):
        return "Hello Web.py"
    def POST(self):
        return self.GET()
if __name__ == "__main__":
    app.run()