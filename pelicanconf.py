from datetime import datetime

AUTHOR = 'Sergio Milardovich'
SITENAME = 'UTN Programación Competitiva - ACM-ICPC'
SITESUBTITLE = 'UTN · Facultad Regional Rosario'
SITEDESCRIPTION = ('Comunidad de programación competitiva de la UTN Facultad Regional Rosario: '
                   'talleres, competencias ICPC, material de estudio y prácticas.')
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('Inicio', '/'),
         ('Cómo empezar', '/como-empezar.html'),
         ('Biblioteca', '/biblioteca.html'),
         ('Prácticas', '/practicas.html'),
         ('Competencias', '/category/eventos.html'),
         ('Novedades', '/category/novedades.html'),
         )

DEFAULT_PAGINATION = 500

THEME = 'themes/icpc-frro'

EVENTS_COUNT = 6
NEWS_COUNT = 5
STATIC_PATHS = ["images", "files"]
NEWS_CATEGORY = 'Novedades'
EVENTS_CATEGORY = 'Eventos'

# Fecha de compilación: la usan las plantillas para separar los eventos
# que todavía no ocurrieron de los que ya pasaron.
TODAY = datetime.now().strftime('%Y%m%d')
COPYRIGHT_YEAR = datetime.now().strftime('%Y')

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
