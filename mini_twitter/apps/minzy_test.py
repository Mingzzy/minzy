from flask import render_template, Flask, request
from apps import app


@app.route('/')
@app.route('/test', methods=['GET', 'POST'])
def test():
    get = None
    post = None

    if request.args:
        get = "https://www.google.co.kr/#newwindow=1&q=" + \
            request.args['text_get']

    return render_template("test.html", variable_get=get)
