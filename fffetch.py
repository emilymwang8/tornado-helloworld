#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author : doganaydin dogan1aydin@gmail.com @dogan1aydin
import os,tornado.web,tornado.httpclient,tornado.httpserver,tornado.escape,tornado.ioloop

class Application(tornado.web.Application):
    def __init__(self):
        adres = [(r"/",Anasayfa),]
        ayar = dict(
                template_path = os.path.join(os.path.dirname(__file__),"templates"),
                static_path = os.path.join(os.path.dirname(__file__),"static"),
                )
        tornado.web.Application.__init__(self,adres,**ayar)
        
        
class Anasayfa(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        #Adres JSON veya xml veya html bile olabilir.
        http.fetch("http://friendfeed-api.com/v2/feed/doganaydin",callback=self.async_callback(self.deneme))
    def deneme(self,bilgi):
        json = tornado.escape.json_decode(bilgi.body)
        self.write(str(json["entries"]))
        self.finish()
        
def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
    
if __name__ == "__main__":
    main() 
