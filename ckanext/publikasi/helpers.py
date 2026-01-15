from datetime import datetime, timezone, timedelta
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

# timezone WITA
WITA_TZ = timezone(timedelta(hours=8))


def to_wita_timezone(dt):
    # Langkah A: Beritahu Python bahwa data dari DB adalah UTC
    # .replace(tzinfo=timezone.utc) menjadikan waktu 'aware'
    utc_time = dt.replace(tzinfo=timezone.utc)
    # Langkah B: Konversi ke offset GMT+8 (WITA)
    wita_time = utc_time.astimezone(WITA_TZ)

    return wita_time

def string_datetime(dt):

    month_id = dt.strftime('%m')
    
    month_search = filter(lambda mon : mon[0] == month_id, READABLE_MONTH)

    bulan_in_indonesia = list(month_search)[0][1]

    return dt.strftime(f"%d {bulan_in_indonesia} %Y")

def datetime_field_format(dt):
    return dt.strftime("%Y-%m-%d")

def display_size_in_mb(byte_size):
    return f"{byte_size/(1<<20):,.0f} MB"

def publikasi_list(limit=None):
    ''' Return newest publication '''

    publikasi = toolkit.get_action('publikasi_list')(data_dict={'sort': 'created desc', 'limit': limit})

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
