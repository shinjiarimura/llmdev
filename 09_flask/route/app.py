from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask!"


@app.route('/about')
def about():
    return "This is the about page."

@app.route('/hello/<username>')
def greet_user(username):
    return f"Hello, {username}"

@app.route('/user/<int:user_id>')
def show_user(user_id):
    return f"User ID is {user_id}"

@app.route('/search')
def search():
    query = request.args.get('query')
    return f"Search requests for: {query}"


if __name__ == '__main__':
    app.run(debug=True)
