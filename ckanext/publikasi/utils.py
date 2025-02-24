from datetime import datetime

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

def format_date(dt):

    month_id = dt.strftime('%m')
    
    month_search = filter(lambda mon : mon[0] == month_id, READABLE_MONTH)

    bulan_in_indonesia = list(month_search)[0][1]

    return dt.strftime(f"%d {bulan_in_indonesia} %Y")