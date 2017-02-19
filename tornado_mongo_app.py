import tornado.ioloop
import tornado.web
import json
import pymongo

from tornado.options import define, options, parse_command_line
from bson import ObjectId
from bson.json_util import dumps

define("port", default=8000, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")


class TaskHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.connection['test']

    def get(self):
        tasks = self.db.tasks.find()
        self.write(dumps({'Tasks': tasks}))

    def post(self):
        title = self.get_argument('Title')
        if title:
            task = {
                'Title': title,
                'Done': False
            }
            self.db.tasks.insert(task)

    def put(self, task_id):
        task_id = ObjectId(task_id)
        data = json.loads(self.request.body)
        self.db.tasks.update({'_id': task_id},
                             {'$set': {'Done': data['Done']}})


routers = [
    (r'/task/', TaskHandler),
    (r'/task/(?P<task_id>.*)', TaskHandler),
    (r'/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
]

application = tornado.web.Application(routers, debug=True)

if __name__ == '__main__':
    parse_command_line()
    application.connection = pymongo.MongoClient()
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
