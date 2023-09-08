#coding:utf-8
import os
import datetime
import tornado.options
import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.web import RequestHandler
from tornado.options import define,options
from tornado.websocket import WebSocketHandler

define("port",default=2222,type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.render("chat-client.html")
class ChatHandler(WebSocketHandler):
    users = set()

    def open(self):
        self.users.add(self)
        for u in self.users:
            u.write_message(
                u"[%s]-[%s]-进入聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def on_message(self, message):
        for u in self.users:
            u.write_message(u"[%s]-[%s]-说:%s" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message))

    def on_close(self):
        self.users.remove(self)
        for u in self.users:
            u.write_message(u"【%s】-【%s】-离开聊天室" % (self.request.remote_ip, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    def check_origin(self, origin: str):
        return True

if __name__=="__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/",IndexHandler),
        (r"/chat",ChatHandler)
    ],
        static_path = os.path.join(os.path.dirname(__file__),"static"),
        template_path = os.path.join(os.path.dirname(__file__),"template"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
