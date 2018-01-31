from flask_restful import Resource, abort

from app.api import api_rest

class BaseResource(Resource):
    def get(self, *args, **kwargs):
        abort(405)

    def post(self, *args, **kwargs):
        abort(405)

def rest_resource(resource_cls):
    api_rest.add_resource(resource_cls, *resource_cls.endpoints)
