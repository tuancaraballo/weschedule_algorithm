from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Tuan'


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Hello !!' + request.form['name']
    else:
        return 'nothing to return'

if __name__ == "__main__":
    app.run()
