import json
from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
import uuid

from sys import stdout as st

from object_storage import storage

def report(msg):
    st.write('\n\nREPORT: {}\n\n'.format(msg))
    st.flush()


SERVICE_PORT = 1234

class Handler(tornado.web.RequestHandler):
    def post(self):
        report(self.request.body)
        filename = str(uuid.uuid4())
        uploaded_file = self.request.body
        try:
            storage().save(filename, uploaded_file)
        except Exception as e:
            self.set_status(500, 'Server error')
            self.write({'error': 'Object storage unavailable: {}'.format(e)})
            return

        self.set_status(200, 'OK')
        self.write({'filename': filename})

    def get(self):
        try:
            filename = self.get_query_argument('filename')
        except:
            self.set_status(400, 'Bad request')
            self.write({'error': 'need filename'})
            return

        try:
            file_content = storage().load(filename)
        except:
            self.set_status(500, 'Server error')
            self.write({'error': 'object storage unavalibale'})
            return

        self.set_status(200, 'OK')
        self.write(file_content)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Handler),
            # (r"/items", ItemsHandler)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(SERVICE_PORT)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
