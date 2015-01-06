#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'pingus'
SITENAME = u'OSAlt Site'
SITEURL = "http://OSAlt.github.io"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# working
# Blogroll
LINKS = (('NixiePixel', 'http://www.nixiepixel.com'),
                 #('Python.org', 'http://python.org/'),
                 #         ('Jinja2', 'http://jinja.pocoo.org/')
                          )

SOCIAL = (('twitter', 'http://twitter.com/NixiePixel'),
                  ('github', 'https://github.com/OSAlt'),
                           )

STATIC_PATHS = ['images']


DEFAULT_PAGINATION = 10

THEME = "pelican-themes/water-iris"


