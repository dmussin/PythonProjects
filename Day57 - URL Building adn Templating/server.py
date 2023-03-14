from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    year = datetime.date.today().year
    return render_template('index.html', num=random_number, year=year)

@app.route('/guess/<name>')
def guess(name):
    parameters = {
        "name" : f"{name}",
    }

    responce_age = requests.get(url='https://api.agify.io', params=parameters)
    responce_age.raise_for_status()

    responce_gender = requests.get(url='https://api.genderize.io', params=parameters)
    responce_gender.raise_for_status()

    gender = responce_gender.json()["gender"]
    print(gender)

    age = responce_age.json()['age']
    name = responce_age.json()['name'].title()
    print(age)

    return render_template('index.html', age=age, name=name, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = 'https://api.npoint.io/3135f94cf5986c9e2cb6'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


