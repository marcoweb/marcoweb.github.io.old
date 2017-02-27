#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marco Carvalho'
SITENAME = u'MarcoWeb'
SITEURL = ''

MENUITEMS = (
    ('Home', '/'),
    ('Sobre', 'pages/about.html'),
    #('Area Para Alunos', '/pages/students.html'),
)

DISPLAY_CATEGORIES_ON_MENU = True

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

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

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

DELETE_OUTPUT_DIRECTORY = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'pelican-themes/marcoweb-pelican-theme'

# Theme Properties
HEADER_IMAGE = '/images/logo-header.png'
WIDGETS = {
    'social',
    'podcasts'
}
SOCIAL_LINKS = {
    'facebook': 'http://facebook.com/marcocarvalho.web',
    'twitter': 'http://twitter.com/marcoweb',
    'google-plus': 'google',
    'github': 'github'
}
PODCASTS = {
    'NerdCast': 'http://nerdcast.com.br'
}
