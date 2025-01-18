import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

import ckanext.publikasi.views as views

import ckanext.publikasi.actions as Actions

class PublikasiPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IActions)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
            'publikasi')
    

    # IBlueprint
    def get_blueprint(self):
        return views.get_blueprints()

    # IActions
    def get_actions(self):
        return {
            'publikasi_create': Actions.create_publikasi,
            'publikasi_get_all': Actions.get_all_publikasi,
            'publikasi_get': Actions.get_publikasi,
            'publikasi_delete': Actions.delete_publikasi
        }
