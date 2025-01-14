from flask import (Blueprint, render_template, jsonify, request, url_for)
import ckan.plugins.toolkit as tk

bp = Blueprint(
    "publikasi",
    __name__,
    url_prefix="/publikasi"
)

def index():
    data_publikasi = [
        {'id': 123, 'title': 'contoh publikasi', 'description': 'deskripsi publikasi 001', 'created': 'tgl 5'}, 
        {'id': 234, 'title': 'contoh publikasi 02', 'description': 'deskripsi publikasi 002', 'created': 'tgl 5'} 
    ]
    return render_template('publikasi/index.html', response={'data': data_publikasi})

def create():
    return render_template('publikasi/publikasi_form.html')

def get(id):
    pass

bp.add_url_rule(
    '/', endpoint='index', view_func=index
)
bp.add_url_rule(
    '/add', endpoint='create', view_func=create
)
bp.add_url_rule(
    '/<int:id>', endpoint='get', view_func=get
)

def get_blueprints():
    return [bp]