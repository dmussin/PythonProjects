from flask import Flask
import random
app = Flask(__name__)

@app.route('/')
def display():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


random_number = random.randrange(1,10)


@app.route('/<int:guess>')
def guess_number(guess):
    if guess > random_number:
        return '<h1 style="color:red;">Too High, try again!</h1>' \
               '<img src = "https://thumbs.gfycat.com/ZanyRegularGermanspaniel-max-1mb.gif" width=200>'
    elif guess < random_number:
        return '<h1 style="color:purple;">Too Low, try again!</h1>' \
               '<img src = "https://thumbs.gfycat.com/CavernousWhimsicalHound-max-1mb.gif" width=200>'
    else:
        return '<h1 style="color:blue;">Correct!</h1>' \
               '<img src = "https://thumbs.gfycat.com/BetterImpartialAsiaticlesserfreshwaterclam.webp" width=200>'


if __name__ == "__main__":
    app.run(debug=True)