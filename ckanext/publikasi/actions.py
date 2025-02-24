import os, uuid, datetime
import ckan.plugins.toolkit as tk
from werkzeug.utils import secure_filename
from sqlalchemy import text
from ckan.model import Session
from ckanext.publikasi.model import Publikasi

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'public/uploads'
ALLOWED_EXTENSION = {'pdf'}

def get_publikasi(context, data_dict):
    '''Retrieve metadata by ID'''
    publikasi_item = Session.query(Publikasi).filter_by(id=data_dict['id']).first()

    print("publikasi: ", publikasi_item)

    if not publikasi_item:
        raise tk.ObjectNotFound('Metadata not found')
    
    # file_stat = _file_stat(publikasi_item.file_path)
    # print('file statistic : ', file_stat)
    # print(f"{_file_stat(publikasi_item.file_path).st_size/(1<<20):,.0f} MB")
    # print(f"ukuran file : {_get_file_size(publikasi_item.file_path)}")
    # print(f"ukuran file : { file_stat.st_size }")
    
    return {
        "id": publikasi_item.id,
        "uuid": publikasi_item.unique_id,
        "name": publikasi_item.title, # tambahan untuk kebutuhan helper breadcrumb
        "title": publikasi_item.title,
        "description": publikasi_item.description,
        "author" : publikasi_item.author,
        "type": publikasi_item.type,
        "file_path": publikasi_item.file_path,
        "user_own": publikasi_item.user_own,
        "cover_image": publikasi_item.cover_image,
        "meta_catalog_number": publikasi_item.meta_catalog_number,
        "meta_publication_number": publikasi_item.meta_publication_number,
        "meta_isbn_issn": publikasi_item.meta_isbn_issn,
        "meta_release_frequency": publikasi_item.meta_release_frequency,
        "meta_release_date": publikasi_item.meta_release_date,
        "meta_language": publikasi_item.meta_language,
        "meta_file_size": publikasi_item.meta_file_size,
        "created": publikasi_item.created
    }

def get_all_publikasi(context, data_dict):
    pass
    publikasi = Session.query(Publikasi).all()
    print(publikasi)

    # handle metadata jika data kosong
    # if not metadata:
    #     raise toolkit.ObjectNotFound('Metadata not found')

    # return {}
    publikasi_obj = []

    for publikasi_item in publikasi:
        publikasi_obj.append({
            "id": publikasi_item.id,
            "uuid": publikasi_item.unique_id,
            "name": publikasi_item.title, # tambahan untuk kebutuhan helper breadcrumb
            "title": publikasi_item.title,
            "description": publikasi_item.description,
            "author" : publikasi_item.author,
            "type": publikasi_item.type,
            "file_path": publikasi_item.file_path,
            "user_own": publikasi_item.user_own,
            "cover_image": publikasi_item.cover_image,
            "meta_catalog_number": publikasi_item.meta_catalog_number,
            "meta_publication_number": publikasi_item.meta_publication_number,
            "meta_isbn_issn": publikasi_item.meta_isbn_issn,
            "meta_release_frequency": publikasi_item.meta_release_frequency,
            "meta_release_date": publikasi_item.meta_release_date,
            "meta_language": publikasi_item.meta_language,
            "meta_file_size": publikasi_item.meta_file_size,
            "created": publikasi_item.created
        })
    
    # return {
    #     'organization_id': metadata[0].organization_id,
    #     'title': metadata[0].title,
    #     'desc': metadata[0].desc,
    #     'author': metadata[0].author
    # }

    return { "data": publikasi_obj }

def get_all_publikasi_sektoral(context={}, data_dict={}):
    ''' GET ALL PUBLIKASI SEKTORAL'''
    publikasi_sektoral = Session.query(Publikasi).filter_by(type='Publikasi Sektoral').all()

    return {'issuccess': True, "data" : _to_list_dict(publikasi_sektoral)}

def get_all_publikasi_produk_hukum(context={}, data_dict={}):
    ''' GET ALL PRODUK HUKUM '''

    produk_hukum = Session.query(Publikasi).filter_by(type='Produk Hukum').all()
    return {'issuccess': True, "data" : _to_list_dict(produk_hukum)}

def publikasi_list(context={}, data_dict={}):
    publikasi = Session.query(Publikasi).order_by(text(data_dict['sort'])).all()

    publikasi_obj = []

    for publikasi_item in publikasi:
        publikasi_obj.append({
            "id": publikasi_item.id,
            "uuid": publikasi_item.unique_id,
            "name": publikasi_item.title, # tambahan untuk kebutuhan helper breadcrumb
            "title": publikasi_item.title,
            "description": publikasi_item.description,
            "author" : publikasi_item.author,
            "type": publikasi_item.type,
            "file_path": publikasi_item.file_path,
            "user_own": publikasi_item.user_own,
            "cover_image": publikasi_item.cover_image,
            "meta_catalog_number": publikasi_item.meta_catalog_number,
            "meta_publication_number": publikasi_item.meta_publication_number,
            "meta_isbn_issn": publikasi_item.meta_isbn_issn,
            "meta_release_frequency": publikasi_item.meta_release_frequency,
            "meta_release_date": publikasi_item.meta_release_date,
            "meta_language": publikasi_item.meta_language,
            "meta_file_size": publikasi_item.meta_file_size,
            "created": publikasi_item.created
        })
    return publikasi_obj

def create_publikasi(context, data_dict):
    ''' create new publikasi entry '''


    result_upload = _upload_file(data_dict['publication_file'])

    if result_upload['issuccess'] != True:
        return {'issuccess': False, 'msg': 'Terjadi kesalahan ketika upload berkas'}
    
    cover_image_upload = _upload_file(data_dict['cover_image'])
    if cover_image_upload['issuccess'] != True:
        cover_image_upload['filename'] = ''
        # return {'issuccess': False, 'msg': 'Terjadi kesalahan ketika upload cover'}

    publikasi = Publikasi(
        unique_id=uuid.uuid4(),
        title=data_dict['title'],
        description=data_dict['description'],
        author=data_dict['author'],
        type=data_dict['type'],
        file_path=result_upload['filename'],
        # file_path='',
        user_own='',
        # cover_image=data_dict['cover_image'],
        cover_image=cover_image_upload['filename'],
        meta_catalog_number=data_dict['catalog_number'],
        meta_publication_number=data_dict['publication_number'],
        meta_isbn_issn=data_dict['isbn_issn'],
        meta_release_frequency=data_dict['release_frequency'],
        meta_release_date=data_dict['release_date'],
        meta_language=data_dict['language'],
        meta_file_size=_get_file_size(result_upload['filename'])
    )

    Session.add(publikasi)
    Session.commit()

    return {'issuccess': True, 'publikasi': publikasi}
    

def update_publikasi(context, data_dict):
    ''' Update publikasi entry by ID'''

    publikasi_id = data_dict['id']

    result_upload = _upload_file(data_dict['publication_file'])

    if result_upload['issuccess'] != True:
        return {'issuccess': False, 'msg': 'Terjadi kesalahan ketika upload berkas'}
    
    publikasi_item = Session.query(Publikasi).filter_by(id=data_dict['id']).first()
    old_filename = publikasi_item.file_path
    delete_old_file = _delete_file(old_filename)

    cover_image_upload = _upload_file(data_dict['cover_image'])
    if cover_image_upload['issuccess'] != True:
        cover_image_upload['filename'] = ''
        # return {'issuccess': False, 'msg': 'Terjadi kesalahan ketika upload cover'}
    
    publikasi_updated = {
        'title': data_dict['title'],
        'description': data_dict['description'],
        'author': data_dict['author'],
        'type': data_dict['type'],
        'file_path': result_upload['filename'],
        'user_own': '',
        # 'cover_image': data_dict['cover_image'],
        'cover_image': cover_image_upload['filename'],
        'meta_catalog_number': data_dict['catalog_number'],
        'meta_publication_number': data_dict['publication_number'],
        'meta_isbn_issn': data_dict['isbn_issn'],
        'meta_release_frequency': data_dict['release_frequency'],
        'meta_release_date': data_dict['release_date'],
        'meta_language': data_dict['language'],
        'meta_file_size': _get_file_size(result_upload['filename'])
    }

    # publikasi = Publikasi(
    #     title=data_dict['title'],
    #     description=data_dict['description'],
    #     author=data_dict['author'],
    #     type=data_dict['type'],
    #     file_path=result_upload['filename'],
    #     # file_path='',
    #     user_own='',
    #     cover_image=data_dict['cover_image'],
    #     meta_catalog_number=data_dict['catalog_number'],
    #     meta_publication_number=data_dict['publication_number'],
    #     meta_isbn_issn=data_dict['isbn_issn'],
    #     meta_release_frequency=data_dict['release_frequency'],
    #     meta_release_date=data_dict['release_date'],
    #     meta_language=data_dict['language'],
    #     meta_file_size=0
    # )

    Session.query(Publikasi).filter(Publikasi.id==publikasi_id). \
        update(publikasi_updated)
    # Session.add(publikasi)
    Session.commit()

    return {'issuccess': True, 'msg': 'Publikasi updated successfully'}

def delete_publikasi(context, data_dict):
    ''' Delete Publikasi by ID '''
    publikasi_id = data_dict['id']
    publikasi = Session.query(Publikasi).filter_by(id=publikasi_id).first()

    if not publikasi : 
        raise tk.ObjectNotFound('Publikasi Not Found')

    _delete_file(publikasi.file_path)
    if publikasi.cover_image != '':
        _delete_file(publikasi.cover_image)

    Session.delete(publikasi)
    Session.commit()

    return { 'issuccess': True, 'msg': 'Publikasi deleted successfully' }


def _upload_file(file):
    ''' 
    Proses upload dihandle oleh function ini
    
    return:
        - String 'status' ['success', 'fail']
        - Any 'data': {'file_name': <nama file>}
    
    '''

    isvalidate = _validate_file_upload(file)

    if not isvalidate:
        return {'issuccess': False, 'msg': 'Gagal melakukan validasi berkas'}
        
    # Proses upload file
    # file_timestamp = datetime.date.today().strftime('%Y-%m-%d')
    file_timestamp = str(datetime.datetime.timestamp(datetime.datetime.now()))
    filename = secure_filename(file_timestamp + '_' + file.filename)
    file.save(os.path.join(BASE_PATH, UPLOAD_FOLDER, filename))
    return {'issuccess': True, 'filename': filename}

def _validate_file_upload(file):
    # cek jika file ada (file.filename=='')
    # cek allowed file extension 

    if file.filename == '':
        return False
    else :
        return True

def _delete_file(filename):
    # proses delete file
    try:
        os.remove(os.path.join(BASE_PATH, UPLOAD_FOLDER, filename))
    except:
        print('Error : Something wrong!')
        return False
    return True

def _file_stat(filename):
    # file_path = os.stat(os.path.join(BASE_PATH, UPLOAD_FOLDER, filename))
    # file_size = f"{file_path.st_size/(1<<20):,.0f} MB"
    # return file_size
    return os.stat(os.path.join(BASE_PATH, UPLOAD_FOLDER, filename))

def _get_file_size(filename):
    ''' return file size in byte '''
    return os.stat(os.path.join(BASE_PATH, UPLOAD_FOLDER, filename)).st_size

def _to_dict(publikasi_item, filter : dict =[]) -> dict :
    return {
        "id": publikasi_item.id,
        "uuid": publikasi_item.unique_id,
        "name": publikasi_item.title, # tambahan untuk kebutuhan helper breadcrumb
        "title": publikasi_item.title,
        "description": publikasi_item.description,
        "author" : publikasi_item.author,
        "type": publikasi_item.type,
        "file_path": publikasi_item.file_path,
        "user_own": publikasi_item.user_own,
        "cover_image": publikasi_item.cover_image,
        "meta_catalog_number": publikasi_item.meta_catalog_number,
        "meta_publication_number": publikasi_item.meta_publication_number,
        "meta_isbn_issn": publikasi_item.meta_isbn_issn,
        "meta_release_frequency": publikasi_item.meta_release_frequency,
        "meta_release_date": publikasi_item.meta_release_date,
        "meta_language": publikasi_item.meta_language,
        "meta_file_size": publikasi_item.meta_file_size,
        "created": publikasi_item.created
    }

def _to_list_dict(publikasi):
    publikasi_list = []
    if publikasi is None:
        return []
    for publikasi_item in publikasi:
        publikasi_list.append({
            "id": publikasi_item.id,
            "uuid": publikasi_item.unique_id,
            "name": publikasi_item.title, # tambahan untuk kebutuhan helper breadcrumb
            "title": publikasi_item.title,
            "description": publikasi_item.description,
            "author" : publikasi_item.author,
            "type": publikasi_item.type,
            "file_path": publikasi_item.file_path,
            "user_own": publikasi_item.user_own,
            "cover_image": publikasi_item.cover_image,
            "meta_catalog_number": publikasi_item.meta_catalog_number,
            "meta_publication_number": publikasi_item.meta_publication_number,
            "meta_isbn_issn": publikasi_item.meta_isbn_issn,
            "meta_release_frequency": publikasi_item.meta_release_frequency,
            "meta_release_date": publikasi_item.meta_release_date,
            "meta_language": publikasi_item.meta_language,
            "meta_file_size": publikasi_item.meta_file_size,
            "created": publikasi_item.created
        })
    
    return publikasi_list