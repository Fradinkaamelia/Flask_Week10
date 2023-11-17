from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/cv")
def tampilCV():
    return render_template("cv.html")

@app.route("/biodata")
def biodata():
    return render_template("biodata.html")

@app.route("/kontak")
def kontak():
    return render_template("kontak.html")

@app.route("/quote")
def quote():
    return render_template("quote.html")

@app.route("/fibonacci")
def deretFibonacci():
    return render_template("fibonacci.html")

@app.route("/convertjson")
def convertjson():
    return render_template("csv2json.html")

@app.route("/post", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("post.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr}. Nice to Meet You!</h1>"

if __name__ == '__main__':
    app.run(debug=True)