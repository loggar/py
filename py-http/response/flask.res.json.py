from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/sample', methods=['GET'])
def apod():
    url = 'url...'
    title = 'title...'

    return jsonify(url=url, title=title)


if __name__ == '__main__':
    app.run()
