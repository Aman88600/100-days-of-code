from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Getting the posts
    response = requests.get("https://api.npoint.io/e36f46fcb59d92450c79")
    posts = eval(response.text)
    return render_template("index.html", posts=posts)

#Post route
@app.route('/post/<int:id>')
def get_blog(id):
    # Getting All Posts
    posts = requests.get("https://api.npoint.io/e36f46fcb59d92450c79")
    posts = eval(posts.text)

    # Getting a specific show_post using the id attribute and breaking the loop for optimization
    for post in posts:
        if post['id'] == id:
            show_post = post
            break
    return render_template("post.html", post=show_post)
# Making an about route
@app.route('/about')
def about():
    return render_template('about.html')

# Making a contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)