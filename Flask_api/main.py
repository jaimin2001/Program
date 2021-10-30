from flask import Flask 
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

videos = {}

class Video(Resource):
    def get(self, video_id):
        return Video[video_id]

api.add_resource(HelloWorld, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)    