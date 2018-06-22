
from flask import Flask, render_template, request
from redis import Redis, RedisError
import os
import socket
import Controller.Main

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def joel_index():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    name = os.getenv("NAME", "world")
    hostname = socket.gethostname()

    html = (f"<h3>Hello {name}!</h3>" 
           f"<b>Hostname:</b> {hostname}<br/>" 
           f"<b>Visits:</b> {visits}")

    #content_hash = { 'go': "gooooo", }
    return html

@app.route("/wew")
def wew():
	return render_template("index.html")  

@app.route("/request_test/<path:muhpath>")
def rtest(muhpath):
	return Controller.Main.serve_page(request,muhpath)

@app.route("/r_test/<int:post_id>")
def rintt(post_id):
	return f"post_id: {post_id}"

@app.route("/request_info/<int:idid>")
def rinfo(idid):
	return str(request)

@app.route("/clan/create")
def clan_create():
	return str(request.url)

@app.route("/user/create")
def user_create():
	return str(request.path)

@app.route("/clan/post")
def post_create():
	return

@app.route("/clan/tribunal")
def clan_expel_user():
	return

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

