# Tema `icpc-frro`

Tema propio para el sitio de Programación Competitiva de la UTN Facultad
Regional Rosario. Reemplaza a `Peli-Kiera` (que queda en el repo por si hace
falta volver atrás: alcanza con cambiar `THEME` en `pelicanconf.py`).

La referencia visual son los sitios de proyectos de software libre
(freebsd.org, xfce.org, manjaro.org): barra institucional, navegación con
color de marca, portada con hero + agenda, contenido en columna legible y pie
con enlaces agrupados.

## Estructura

```
static/css/style.css   Toda la hoja de estilos (sin frameworks, sin build).
static/js/site.js      Sólo el menú responsive.
static/images/         Logo, marca de agua del hero y favicon (SVG).
templates/             Plantillas Jinja de Pelican.
```

No usa Bootstrap. Las pocas clases de Bootstrap que quedaron escritas a mano en
los artículos viejos (`alert`, `alert-warning`, `alert-heading`, `btn`,
`mb-0`) tienen su equivalente en `style.css`, así que ese contenido sigue
viéndose bien.

## Ajustes de color

Los colores salen de las variables CSS del bloque `:root` en `style.css`:
`--brand` (azul UTN), `--accent` (ámbar de los llamados a la acción) y la
escala de neutros. Cambiando esas variables cambia todo el sitio.

## Metadatos que entiende

Además de los habituales de Pelican:

- `Event_Date: YYYY-MM-DD` (opcional, en artículos de la categoría Eventos).
  Es la fecha real del evento, distinta de la fecha de publicación. Mientras no
  haya pasado, el artículo aparece en el panel **Próximas competencias** de la
  portada y su tarjeta muestra esa fecha destacada.

Y estos valores de `pelicanconf.py`: `MENUITEMS`, `EVENTS_CATEGORY`,
`NEWS_CATEGORY`, `EVENTS_COUNT`, `NEWS_COUNT`, `SITEDESCRIPTION`, `TODAY`,
`COPYRIGHT_YEAR`.

## Desarrollo

```sh
venv/bin/pelican -s pelicanconf.py -lr -p 8000    # regenera y sirve en :8000
```
