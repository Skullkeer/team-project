from flask import Flask, render_template, request
from helpful_bot import Helpful_bot
from sarcastic_bot import Sarcastic_bot
from random_bot import Random_bot

app = Flask(__name__)

h_bot = Helpful_bot()
s_bot = Sarcastic_bot()
r_bot = Random_bot()

@app.route("/", methods=["GET", "POST"])
def home_page():
    result_h = None
    result_s = None
    result_r = None

    if request.method == "POST":
        value = request.form["user_input"]
        result_h = h_bot.respond(value)
        result_s = s_bot.respond(value)
        result_r = r_bot.respond(value)



    return render_template("template.html", result_h=result_h, result_s=result_s, result_r=result_r)

if __name__ == "__main__":
    app.run(debug=True)
