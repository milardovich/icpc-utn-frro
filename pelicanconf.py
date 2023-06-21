AUTHOR = 'Sergio Milardovich'
SITENAME = 'UTN Programación Competitiva - ACM-ICPC'
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
         ('Biblioteca', '/biblioteca.html'),
         ('Eventos', '/category/eventos.html'),
         ('Novedades', '/category/novedades.html'),
         )

DEFAULT_PAGINATION = 500

THEME = 'themes/Peli-Kiera'

EVENTS_COUNT = 5
NEWS_COUNT = 5
STATIC_PATHS = ["images"]
NEWS_CATEGORY = 'Novedades'
EVENTS_CATEGORY = 'Eventos'
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True