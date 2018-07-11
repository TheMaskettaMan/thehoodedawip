
from flask import Flask, render_template, request, url_for
from redis import Redis, RedisError
import os
import socket
import controller.main as CMask

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def masketta_base():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    name = os.getenv("NAME", "world")
    hostname = socket.gethostname()

    html = (f"<h3>Hello {name}!</h3>" 
           f"<b>Hostname:</b> {hostname}<br/>" 
           f"<b>Visits:</b> {visits}")

    return html

@app.route("/wew")
def wew():
	return render_template("index.html")  

@app.route("/ruminations")
def ruminate():
	print (request.script_root)
	print (request.path)
	print (request.url_root)
	return CMask.serve(request)

@app.route("/facts")
def fact():
	return CMask.serve(request)

@app.route("/test/<path:muhpath>")
def test(muhpath):
	print( request )
	path_info = { 'base': 'index', 'path': muhpath }
	return CMask.serve(request)

@app.route("/<string:first>/<path:second>")
def path_test(first, second) :
	path_info = { 'base': first, 'path': second }
	return CMask.serve(request)

@app.route("/masketta_js")
def masketta_js():
	# TODO customise which js is served after js distinctions decided
	return CMask.serve_js()

@app.route("/request_test/<path:muhpath>")
def rtest(muhpath):
	path_info = { 'base': 'index.html' }
	return CMask.serve(request)




########### TODO:

@app.route("/clan/create")
def clan_create():
	return str(request.url)

@app.route("/boi/create")
def boi_create():
	return 

@app.route("/post")
def post_create():
	return

@app.route("/tribunal")
def clan_expel_user():
	return


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


