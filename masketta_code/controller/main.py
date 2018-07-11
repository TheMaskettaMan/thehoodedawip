import flask
import os
import sys
import math
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import controller.templater as templater
import controller.locator as locator

def serve( request ) :
	
	data = build_data(request)
	
	data['is_page'] = 1
	
	if data['is_page'] :
		page_html = templater.construct(data)
		return page_html
	else :
		return

def build_data( request ) :
	
	data = {}
	#TODO build the data elsewhere, and put it in data['template_vars']
	data['template_vars'] = {}

	data['template_data'] = locator.retrieve_templates(request)
	return data


# TODO split js dependent on prod or dev environtment
def serve_js () :
	if os.environ['masketta_env'] == 'dev' :
		filename = os.path.join(os.path.dirname(__file__), '../masketta_dist/main.bundle.js')

		with open(filename, 'r', encoding = 'utf-8') as js_file:
			js_data = js_file.read()

		return js_data

	else :
		filename = os.path.join(os.path.dirname(__file__), '../masketta_dist/main.bundle.js')

		with open(filename, 'r', encoding = 'utf-8') as js_file:
			js_data = js_file.read()

		return js_data



def fail(request_object):
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


