import math
import sys
import os
#import clannie
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
	loader = FileSystemLoader('/dev_masketta_clan/masketta_code/templates'),
	autoescape = select_autoescape(['html'],['xml'])
)

# Ensure any html added from entries in db is autoescaped elsewhere
safe_env = Environment(
	loader = FileSystemLoader('/dev_masketta_clan/masketta_code/templates'),
)

def construct (data) :

	muh_data = data
	
	muh_data = add_zenbu(muh_data)

	# TODO: determine which shell template to load as well as content(main) template

	content_template = muh_data['template_data']['content_template']
	shell_template = muh_data['template_data']['shell_template']

	# Add zenbu
	muh_data = add_zenbu(muh_data)

	# TODO: explore js loading process
	# theoretically, all of the js i need (perhaps a large json string) will be
	# already located in template vars

	template = env.get_template(shell_template)
	
	# TODO: 
	muh_data['template_vars']['content'] = env.get_template(content_template).render()

	# build our final template from the main content template
	final_template = template.render(muh_data['template_vars'])
	
	return final_template


def construct_sub_template (sub_template_data) :
	
	muh_data = sub_template_data['sub_template_name']
	return fin_sub


def add_zenbu(template_data) :
	
	header_template = env.get_template('zenbu/header.html')

	footer_template = env.get_template('zenbu/footer.html')

	template_data['template_vars']['header'] = header_template.render()

	template_data['template_vars']['footer'] = footer_template.render()
	
	
	return template_data

