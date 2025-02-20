from flask import (Blueprint, render_template, jsonify, request, url_for)
import ckan.plugins.toolkit as tk

bp = Blueprint(
    "produk_hukum",
    __name__,
    url_prefix="/produk-hukum"
)

def index():
    data_publikasi = tk.get_action('produk_hukum_get_all')(context={}, data_dict={})
    print(data_publikasi)
    return render_template('produk_hukum/index.html', response={'data': data_publikasi['data']})

def create():
    PUBLIKASI_TYPE = 'produk_hukum'
    return render_template('produk_hukum/produk_hukum_form.html')

def store():
    data_form = request.form
    print(data_form)

    data_publikasi = {
        'title': data_form.get('title'),
        'description': data_form.get('description'),
        'author': data_form.get('author'),
        'type' : data_form.get('type'),
        # 'cover_image': data_form.get('cover_image'),
        'cover_image': request.files['cover_image'],
        'publication_file': request.files['publication_file'],
        'catalog_number': data_form.get('catalog_number'),
        'publication_number': data_form.get('publication_number'),
        'isbn_issn': data_form.get('isbn_issn'),
        'release_frequency': data_form.get('release_frequency'),
        'release_date': data_form.get('release_date'),
        'language': data_form.get('language'),
    }

    publikasi_instance = tk.get_action('publikasi_create')(context={}, data_dict=data_publikasi)
    print('publikasi instance : {}'.format(publikasi_instance))

    # return jsonify({'data': data_publikasi})

    return tk.redirect_to('produk_hukum.index')

def get(id):
    
    publikasi = tk.get_action('publikasi_get')(context={}, data_dict={'id': id})

    return render_template('produk_hukum/produk_hukum_read.html', response={'data': publikasi})

def edit(id):
    publikasi = tk.get_action('publikasi_get')(context={}, data_dict={'id': id})

    return render_template('produk_hukum/produk_hukum_form.html', mode='edit', response={'data': publikasi})

def update(id):
    data_form = request.form
    print(data_form)

    data_publikasi = {
        'id': id,
        'title': data_form.get('title'),
        'description': data_form.get('description'),
        'author': data_form.get('author'),
        'type' : data_form.get('type'),
        # 'cover_image': data_form.get('cover_image'),
        'cover_image': request.files['cover_image'],
        'publication_file': request.files['publication_file'],
        'catalog_number': data_form.get('catalog_number'),
        'publication_number': data_form.get('publication_number'),
        'isbn_issn': data_form.get('isbn_issn'),
        'release_frequency': data_form.get('release_frequency'),
        'release_date': data_form.get('release_date'),
        'language': data_form.get('language'),
    }

    publikasi_instance = tk.get_action('publikasi_update')(context={}, data_dict=data_publikasi)
    print('publikasi instance : {}'.format(publikasi_instance))

    # return jsonify({'data': publikasi_instance['publikasi']})

    return tk.redirect_to('produk_hukum.get', id=id)


def delete(id):

    tk.get_action('publikasi_delete')(context={}, data_dict={'id': id})

    return tk.redirect_to('produk_hukum.index')


bp.add_url_rule(
    '/', endpoint='index', view_func=index
)
bp.add_url_rule(
    '/add', endpoint='create', view_func=create, methods=['GET']
)
bp.add_url_rule(
    '/add', endpoint='store', view_func=store, methods=['POST']
)
bp.add_url_rule(
    '/<int:id>', endpoint='get', view_func=get
)
bp.add_url_rule(
    '/edit/<int:id>', endpoint='edit', view_func=edit
)
bp.add_url_rule(
    '/update/<int:id>', endpoint='update', view_func=update, methods=['POST']
)
bp.add_url_rule(
    '/delete/<int:id>', endpoint='delete', view_func=delete, methods=['POST']
)




def get_blueprints():
    return [bp]