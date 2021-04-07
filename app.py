from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

anagramm = {}

class Anagram(Resource):
    def get(self):
        word = request.args.get("word")
        answer = []
        for i in anagramm["load"]:
            b = ' '.join(i).split()
            b.sort()
            c = ' '.join(word).split()
            c.sort()
            if c == b: answer.append(i)
        if len(answer) == 0: return None
        else: return answer

    def put(self):
        anagramm["load"] = request.get_json()
        return anagramm["load"]

api.add_resource(Anagram, '/load', "/get")

if __name__ == '__main__':
    app.run(debug=True)
