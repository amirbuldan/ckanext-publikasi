from flask import (Blueprint, render_template, jsonify, request, url_for)
import ckan.plugins.toolkit as tk

bp = Blueprint(
    "produk_hukum",
    __name__,
    url_prefix="/produk-hukum"
)

def index():
    return render_template('produk_hukum/index.html')


bp.add_url_rule(
    '/', endpoint='index', view_func=index
)



def get_blueprints():
    return [bp]