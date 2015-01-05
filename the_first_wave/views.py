from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/start.jinja2')
def start(request):
    return {'project': 'the_first_wave'}

@view_config(route_name='pyramid', renderer='templates/pyramid.jinja2')
def pyramid(request):
    return {}

@view_config(route_name='concepts', renderer='templates/concepts.jinja2')
def concepts(request):
    return {}

@view_config(route_name='jinja2', renderer='templates/jinja2.jinja2')
def jinja2(request):
    aLittleDictionary = {'Imie' : 'Cezary',
                         "Nazwisko" : "Kaszuba",
                         "Wiek" : 24,
                         "Wzrost" : "185 cm",
                         "Stan cywilny" : "kawaler",
                         "Nr telefonu" : 881568723}

    aLittleList = ["Jest", "To", "Zawartosc", "Tablicy", "(listy)", "Ktora", "Zostala", "Wlasnie", "Wyswietlona"]

    variable = "Zmienna o nazwie \"variable\", ktorej zawartoscia jest wlasnie ten tekst."
    return{'variable': variable,
           'aLittleList': aLittleList,
           'aLittleDictionary': aLittleDictionary}

@view_config(route_name='view', renderer='templates/view.jinja2')
def view(request):
    #It is for example purposes only
    img_url = "static/view-1.png"
    return{'url': img_url}

@view_config(route_name='init', renderer='templates/init.jinja2')
def init(request):
    img_url = "static/init-1.png"
    height = "700px"
    return{'url': img_url,
           'height': height}

@view_config(route_name='startup', renderer='templates/startup.jinja2')
def startup(request):
    img_url = "static/startup-1.png"
    return{'url': img_url}