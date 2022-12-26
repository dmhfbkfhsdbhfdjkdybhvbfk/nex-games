from flask import Flask, render_template,request
import taker

app = Flask(__name__,template_folder="Template")

@app.route("/")
def hello_world():
    client_ip = request.remote_addr
    taker.take_user_ip("102.89.40.108")
    return render_template("index.html")

@app.route("/<string:page_name>")
def Free_fire(page_name):
    return render_template(page_name)





