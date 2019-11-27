from views import make_app
import tornado.ioloop
import tornado.web,json


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()