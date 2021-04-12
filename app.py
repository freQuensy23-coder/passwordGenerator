from flask import Flask, render_template, request, url_for
from Core import Password_generator

password_generator = Password_generator()

app = Flask(__name__)
app.debug = True


@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/nonserver', methods=["POST", "GET"])
def nonserver_page():
    global password_generator
    if request.method == "GET":
        return render_template("nonserver.html")
    elif request.method == "POST":
        url = request.form["url"]
        username = request.form["username"]
        secret_pass = request.form["password"]
        generated_pass = password_generator.generate(user_name=username, secret_pass=secret_pass, url=url, color="")
        return render_template("generated.html", password=generated_pass)  # TODO


if __name__ == '__main__':
    app.run(debug=True)
