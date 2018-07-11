import flask
import os
import sys
import math

def retrieve_templates(request) :
	return {
		'shell_template' : retrieve_shell(request.script_root),
		'content_template' : retrieve_content(request.script_root),
	}

def retrieve_content(script_root) :
	print( script_root)
	script_root = 'test'
	# do i know the way?
	template_dict = {

		# admin-related
		'ruminations': 'soapbox.html',
		'facts': 'factbox.html',
		'superlative': 'superlative.html',
		

		# clan-related
		'thegoods': 'goods.html',
		'clan': 'clan.html',
		'tribunal': 'tribunal.html',



		# boi-related
		'boi': 'boi.html',
		
		# un-related
		'test': 'home.html'
	}

	return template_dict[script_root]

def retrieve_shell(script_root) :
	script_root = 'test'
	# do i know the way?
	shell_template_dict = {

		# admin-related
		'ruminations': 'index.html',
		'facts': 'index.html',
		'superlative': 'index.html',
		

		# clan-related
		'thegoods': 'index.html',
		'clan': 'index.html',
		'tribunal': 'index.html',



		# boi-related
		'boi': 'index.html',
		
		# un-related
		'test': 'index.html'
	}

	return shell_template_dict[script_root]

