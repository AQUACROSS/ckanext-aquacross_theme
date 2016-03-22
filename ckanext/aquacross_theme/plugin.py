import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Aquacross_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'aquacross_theme')

    entry_points='''
        [ckan.plugins]
        aquacross_theme=ckanext.aquacross_theme.plugin:AquacrossThemePlugin''',