from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"Hello World!"}


api.add_resource(HelloWorld, "/helloworld")

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
