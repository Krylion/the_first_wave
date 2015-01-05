from pyramid.config import Configurator


def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('pyramid', '/pyramid')
    config.add_route('concepts', '/concepts')
    config.add_route('jinja2', '/jinja2')
    config.add_route('view', '/view')
    config.add_route('init', '/init')
    config.add_route('startup', '/startup')
    config.scan()
    return config.make_wsgi_app()
