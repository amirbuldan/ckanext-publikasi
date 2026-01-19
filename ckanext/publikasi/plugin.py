import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.publikasi.views as views
import ckanext.publikasi.views_produk_hukum as views_produk_hukum
import ckanext.publikasi.auths as Auth

import ckanext.publikasi.actions as Actions
import ckanext.publikasi.helpers as Helpers

class PublikasiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IActions)
    plugins.implements(plugins.IAuthFunctions)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'publikasi')
    

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints() + views_produk_hukum.get_blueprints()

    # IActions
    def get_actions(self):
        return {
            'publikasi_create': Actions.create_publikasi,
            'publikasi_get_all': Actions.get_all_publikasi,
            'publikasi_list': Actions.publikasi_list,
            'publikasi_get': Actions.get_publikasi,
            'publikasi_update': Actions.update_publikasi,
            'publikasi_delete': Actions.delete_publikasi,
            'publikasi_sektoral_get_all': Actions.get_all_publikasi_sektoral,
            'publikasi_sektoral_page': Actions.page_publikasi_sektoral,
            'publikasi_produk_hukum_page': Actions.page_publikasi_produk_hukum,
            'produk_hukum_get_all': Actions.get_all_publikasi_produk_hukum
        }
    
    #IAuthFunctions
    def get_auth_functions(self):
        return {'publikasi_create': Auth.publikasi_create}
    
    #ITemplateHelpers
    def get_helpers(self):
        return {
            'string_datetime': Helpers.string_datetime,
            'to_wita_timezone': Helpers.to_wita_timezone,
            'datetime_field_format': Helpers.datetime_field_format,
            'display_size_in_mb': Helpers.display_size_in_mb,
            'get_latest_publikasi': Helpers.publikasi_list,
            'dataset_list': Helpers.dataset_list
        }
