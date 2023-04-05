from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message='Invalid email address')])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log In')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == "12345678":
            print(login_form.email.data)
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route('/success')
def success():
   return render_template("success.html")


@app.route('/denied')
def denied():
   return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)