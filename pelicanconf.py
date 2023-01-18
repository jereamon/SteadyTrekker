AUTHOR = 'Jeremy Monroe'
SITENAME = 'Steady Trekker'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = "themes/steadytrekker_theme"
CSS_FILE = "main.css"
JS_FILE  = "main.js"

# If this is True then the categories show up on the main menu
DISPLAY_CATEGORIES_ON_MENU = False

HOME_IMAGE = "home01_radial_gradient.jpg"
HOME_IMAGE_FULL = "DSC00800-gradient.jpg"


IGNORE_FILES = [
    '*.scss',
    '*.sass',
]