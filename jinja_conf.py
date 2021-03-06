import jinja2
import os

template_dir = os.path.join(os.path.dirname('__file__'), 'templates')
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(template_dir),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)