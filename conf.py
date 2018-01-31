# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Docbook manpage"  # (translatable)
BLOG_TITLE = "Docbook manpage"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "https://example.com/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://example.com/"
BLOG_EMAIL = "manpage@example.com"
BLOG_DESCRIPTION = "Docbook man page example"

DEFAULT_LANG = "en"

TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = "{path}.{lang}.{ext}"


NAVIGATION_LINKS = {
    DEFAULT_LANG: (
    ),
}

# Name of the theme to use.
THEME = "bootstrap3"

# Primary color of your theme. This will be used to customize your theme and
# auto-generate related colors in POSTS_SECTION_COLORS. Must be a HEX value.
THEME_COLOR = '#65074d'

PAGES = (
    ("pages/man/*.xml", "man", "story.tmpl"),
)

COMPILERS = {
    "docbookmanpage": ('.xml',),
}

OUTPUT_FOLDER = 'output/'

