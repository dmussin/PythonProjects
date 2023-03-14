from flask import Flask, render_template
from post import Post
import requests


posts = requests.get("https://api.npoint.io/3135f94cf5986c9e2cb6").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/blog')
def home():
    return render_template("index.html", all_posts=post_objects)

@app.route('/post/<int:index>')
def get_blog(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
