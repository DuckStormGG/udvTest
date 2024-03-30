import json

from flask import Flask, abort

app = Flask(__name__)
app.json.sort_keys = False


def get_comments(id):
    with open('static/comments.json', 'r') as comments:
        result = []
        data = json.load(comments).get("comments")
        for comment in data:
            if comment.get("news_id") == id:
                result.append(comment)
        return result, len(result)


@app.route('/', methods=['GET'])
def return_news():  # put application's code here
    with open("static/news.json", 'r') as news:
        return json.load(news)


@app.route('/news/<int:id>', methods=['GET'])
def return_news_by_id(id):
    with open("static/news.json", 'r') as news:
        data = json.load(news).get("news")
        for i in data:
            if i.get("id") == id and not i.get("deleted"):
                i["comments"], i["comments_count"] = get_comments(id)
                print(i)
                return i, 200

        return abort(404)


if __name__ == '__main__':
    app.run()
