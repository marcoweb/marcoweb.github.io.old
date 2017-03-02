#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marco Carvalho'
SITENAME = u'MarcoWeb'
SITEURL = ''

MENUITEMS = (
    ('Home', '/'),
    #('Sobre', 'pages/about.html'),
    #('Area Para Alunos', '/pages/students.html'),
)

DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt-br'
LOCALE = ('pt_BR')

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-themes/marcoweb-pelican-theme'

DISQUS_SITENAME = "marcoweb"

# Theme Properties
HEADER_IMAGE = '/images/logo-header.png'
WIDGETS = {
    'social',
    'podcasts'
}
SOCIAL = {
    'facebook': 'https://www.facebook.com/marcocarvalho.web',
    'twitter': 'https://twitter.com/mcarvalhoweb',
    'google-plus': 'https://plus.google.com/u/0/+MarcoCarvalhoweb',
    'github': 'https://github.com/marcoweb'
}
PODCASTS = {
    'DatabaseCast': 'https://imasters.com.br/perfil/databasecast/',
    'DevNaEstrada': 'http://devnaestrada.com.br/',
    'Hipsters Ponto Tech': 'http://hipsters.tech/',
    'Lambda3': 'https://blog.lambda3.com.br/tag/podcast/',
    'NerdCast': 'https://jovemnerd.com.br/nerdcast/',
    'Xadrez Verbal': 'https://xadrezverbal.com/'
}
