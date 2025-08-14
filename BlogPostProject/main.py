from flask import Flask, render_template
import requests
import json
from post import Post

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
with open("posts.json", "r") as file:
    posts = json.load(file)

post_objects = [Post(p["id"], p["title"], p["subtitle"], p["body"]) for p in posts]

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
