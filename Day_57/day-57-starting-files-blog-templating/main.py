from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = eval(posts.text)
    return render_template("index.html", posts=posts)

@app.route('/post/<int:id>')
def get_blog(id):
    # Getting All Posts
    posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = eval(posts.text)

    # Getting a specific show_post using the id attribute and breaking the loop for optimization
    for post in posts:
        if post['id'] == id:
            show_post = post
            break
    return render_template("post.html", post=show_post)

if __name__ == "__main__":
    app.run(debug=True)
