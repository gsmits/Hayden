#!/usr/bin/env python

import os.path
import httplib
import tornado.auth
import tornado.database
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
from model import users
from model import urls
from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", HomeHandler),
            (r"/auth/login", AuthLoginHandler),
            (r"/auth/logout", AuthLogoutHandler),
            (r"/ping", PingHandler),
        ]
        settings = dict(
            site_title=u"PingU",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="11oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            login_url="/auth/login",
            autoescape=None,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class PingHandler(BaseHandler):
    @tornado.web.authenticated
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch(self.get_argument("targethost", None), callback=self.async_callback(self.on_response))

    def on_response(self, response):
        self.set_header("Content-type", "application/json")
        self.write(json.dumps({ "status": response.code, "targeturl": response.effective_url }))

        urls.insert(response.effective_url, self.get_current_user())
        
        self.finish()

class HomeHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("home.html")

    def saveUser(self):
        u1 = users.get_user(self.get_current_user())

        if u1 is not None:
            self.write(u1["user_name"])
        else:
            users.insert(self.get_current_user())

            u1 = users.get_user(self.get_current_user())

        self.write(u1["user_name"])

class AuthLoginHandler(BaseHandler, tornado.auth.GoogleMixin):
    @tornado.web.asynchronous
    def get(self):
        if self.get_argument("openid.mode", None):
            self.get_authenticated_user(self.async_callback(self._on_auth))
            return
        self.authenticate_redirect()

    def _on_auth(self, user):
        if not user:
            raise tornado.web.HTTPError(500, "Google auth failed")

        self.set_secure_cookie("user", user["name"])
        self.redirect(self.get_argument("next", "/"))


class AuthLogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()