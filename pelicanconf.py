AUTHOR = 'Jeremy Monroe'
SITENAME = 'Steady Trekker'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'


"""
At first glance these settings are a little confusing.
The default response of web browsers when loading a directory is to look
for and load index.html.

The way ARTICLE_SAVE_AS and PAGE_SAVE_AS below work is to save articles
in the directory 'blog', in a sub dir with the article slug (usually its title),
with an index.html file in that sub dir.

This way, when you navigate to steadytrekker.com/blog/
the web browser attempts to load the blog directory and as long as a blog page
exists within the content folder pelican will make an index.html file in the
blog directory.

This makes for cleaner urls.
"""
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

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