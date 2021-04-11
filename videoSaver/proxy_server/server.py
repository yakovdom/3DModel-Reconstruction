import json
from tornado import httpserver
from tornado import gen
from tornado.ioloop import IOLoop
import tornado.web
import uuid

from sys import stdout as st

def report(msg):
    st.write('\n\nREPORT: {}\n\n'.format(msg))
    st.flush()


SERVICE_PORT = 1234

class Handler(tornado.web.RequestHandler):
    def post(self):
        report(self.request.body)
        filename = uuid.uuid4()
        uploaded_file = self.request.body
        object_storage.object_storage().save(filename, uploaded_file)
        '''
        body = json.loads(self.request.body)
        name = body['name']
        id = body['id']
        category = body['category']
        process_db_answer(self, *items.add(id, name, category))
        '''

    def get(self):
        '''
        global items, authorizer
        if not check_authorization_and_fields(self, 'get_item', ['id']):
            return

        body = json.loads(self.request.body)
        id = body.pop('id')
        process_db_answer(self, *items.get_by_id(id))
        '''

    '''
    def put(self):
        global items
        if not check_authorization_and_fields(self, 'change_item', ['id']):
            return

        body = json.loads(self.request.body)
        id = body.pop('id')

        process_db_answer(self, *items.update(id, body['name'], body['category']))

    def delete(self):
        global items
        if not check_authorization_and_fields(self, 'delete_item', ['id']):
            return

        body = json.loads(self.request.body)
        id = body.pop('id')

        process_db_answer(self, *items.delete(id))
    '''

'''
class ItemsHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            offset = int(self.get_query_argument('offset'))
        except:
            offset = 0

        try:
            limit = int(self.get_query_argument('limit'))
        except:
            limit = 10000
        st.write('\n\n{} {} \n\n'.format(limit, offset))
        st.flush()
        process_db_answer(self, *items.get_all(offset, limit))
'''


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
