from flask import Flask, render_template, request
from factory import create_bot
from event_manager import EventManager

app = Flask(__name__)
eman = EventManager()

eman.attatch(create_bot("help"))
eman.attatch(create_bot("sarc"))
eman.attatch(create_bot("rand"))

@app.route("/", methods=["GET", "POST"])
def home_page():
    responses = {}

    if request.method == "POST":
        msg = request.form["user_input"]
        responses = eman.notify(msg)
    return render_template("template.html", responses = responses)



    return render_template("template.html", result_h=result_h, result_s=result_s, result_r=result_r)

if __name__ == "__main__":
    app.run(debug=True)
