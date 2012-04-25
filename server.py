#!/usr/bin/env python

import json
from snake import *
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.websocket import WebSocketHandler

class Handler(WebSocketHandler):
        def open(self):
                print("New connection opened.")

        def on_message(self, message):
                message = json.loads(message)
                response = m(message)
                self.write_message(response)

        def on_close(self):
                print("Connection closed.")

print("Server started.")
HTTPServer(Application([("/", Handler)], debug=True)).listen(8888)
IOLoop.instance().start()
