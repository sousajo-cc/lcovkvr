import os

from flask import Flask
from flask_restful import Api, Resource, reqparse

from . import db

VALUE_ERR_RET = {'message': 'INVALID KEY!'}, 400
IO_ERR_RET = {'message': 'FILE COULD NOT BE READ'}, 422
KEY_ERR_RET = {'message': 'NOT FOUND!'}, 404


class GET(Resource):
    def get(self):
        db_ = db.get_db()
        parser = reqparse.RequestParser()
        parser.add_argument('commit_hash')
        args = parser.parse_args()
        try:
            meta = db_.get(args['commit_hash'])
            resp = {'commit_hash': args['commit_hash'],
                    'value': meta.decode("utf-8")}
            return resp, 201
        except ValueError:
            return VALUE_ERR_RET
        except IOError:
            return IO_ERR_RET
        except KeyError:
            return KEY_ERR_RET


class SET(Resource):
    def put(self, commit_hash):
        db_ = db.get_db()
        parser = reqparse.RequestParser()
        parser.add_argument('value')
        args = parser.parse_args()
        try:
            db_.put(commit_hash, bytes(args['value'], "utf-8"))
            resp = {'commit_hash': commit_hash,
                    'value': args['value']}

            return resp, 201
        except ValueError:
            return VALUE_ERR_RET
        except IOError:
            return IO_ERR_RET


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'kv.db'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    api = Api(app)
    api.add_resource(SET, '/set/<commit_hash>')
    api.add_resource(GET, '/get/')

    return app
