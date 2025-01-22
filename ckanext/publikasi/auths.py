import ckan.plugins.toolkit as toolkit

def publikasi_create(context, data_dict=None):
    # print("dipanggil di auth cek : {}", context)

    user_name = context['user']

    users = toolkit.get_action('user_list')(data_dict={'order_by': 'sysadmin'})

    sysadmin_users = filter(lambda user: user['sysadmin'] == True, users)
    # sysadmin_users =   for user in users

    sysadmin_ids = [user['id'] for user in sysadmin_users]

    currentuser_id = toolkit.get_converter('convert_user_name_or_id_to_id')(user_name, context)

    # print('user name: {}'.format(user_name))
    # print('users: {}', users)
    # print('syadmin users: {}', list(sysadmin_users))
    # print('sysadmin ids', sysadmin_ids)
    # print('current user id : ', currentuser_id)

    if currentuser_id in sysadmin_ids:
        # print('current user adalah sysadmin ')
        return {'success': True}

    return {'success': False}


