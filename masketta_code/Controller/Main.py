import flask
import os
import sys
import math
import jinja2


def serve_page( request_object ) :
	
	determine_action(request_object)

	
	
	
	
	
	#jinja2.render_template("zenbu/header")
	
	
def determine_action( request_object ) :
	print("hooray for dixie")
	


def fail():
	url = request_object.url
	base_url = request_object.base_url
	url_root = request_object.url_root
	full_path = request_object.full_path
	args = str(request_object.args)
	pathme = path_test	
	
	return (f" url: {url}"
			f" base_url: {base_url}"
			f" url_root: {url_root}"
			f" full_path: {full_path}"
			f" args: {args}"
			f" pathme = {pathme}")

	
	
	
	
	
	
	
	
	
	


















