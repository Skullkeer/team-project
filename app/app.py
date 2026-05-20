from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home_page():
    result = None

    if request.method == "POST":
        value = request.form["user_input"]
        result = f"you typed: {value}"

    return render_template("template.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
#
