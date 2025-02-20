from datetime import datetime
import ckan.plugins.toolkit as toolkit

READABLE_MONTH = [
    ('01', 'Januari'),
    ('02', 'Februari'),
    ('03', 'Maret'),
    ('04', 'April'),
    ('05', 'Mei'),
    ('06', 'Juni'),
    ('07', 'Juli'),
    ('08', 'Agustus'),
    ('09', 'September'),
    ('10', 'Oktober'),
    ('11', 'November'),
    ('12', 'Desember'),
]

def string_datetime(dt):

    month_id = dt.strftime('%m')
    
    month_search = filter(lambda mon : mon[0] == month_id, READABLE_MONTH)

    bulan_in_indonesia = list(month_search)[0][1]

    return dt.strftime(f"%d {bulan_in_indonesia} %Y")

def datetime_field_format(dt):
    return dt.strftime("%Y-%m-%d")

def display_size_in_mb(byte_size):
    return f"{byte_size/(1<<20):,.0f} MB"

def publikasi_list():
    ''' Return newest publication '''

    publikasi = toolkit.get_action('publikasi_list')(data_dict={'sort': 'created desc'})

    # print('publikasi list helper', publikasi)
    return publikasi

def dataset_list():
    ''' Return Dataset List '''

    dataset_list = []
    datasets = toolkit.get_action('package_list')(context={}, data_dict={'limit': 5})
    for dt in datasets:
        dataset_meta = toolkit.get_action('package_show')(context={}, data_dict={'id': dt})
        dataset_list.append(dataset_meta)

    print('get action dataset : ', datasets)
    print('get action dataset show : ', dataset_list)
    return dataset_list
