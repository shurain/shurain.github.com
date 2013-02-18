"""Settings for pelican."""
AUTHOR = 'Sungjoo Ha'
SITENAME = 'sh.'
SITEURL = 'http://blog.shurain.net'
SITE_URL = SITEURL
TIMEZONE = 'UTC'

# This can also be the absolute path to a theme that you downloaded
# i.e. './themes/anothertheme/'
THEME = 'notmyidea'

# The folder ``images`` should be copied into the folder ``static`` when
# generating the output.
STATIC_PATHS = ['images', ]

# See http://pelican.notmyidea.org/en/latest/settings.html#timezone

# Pelican will take the ``Date`` metadata and put the articles into folders
# like ``/posts/2012/02/`` when generating the output.
PERMALINK_STRUCTURE = '{date:%Y}/{date:%m}/'
ARTICLE_URL = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_URL = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_URL = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_URL = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE
ARTICLE_SAVE_AS = '%s{slug}.html' % PERMALINK_STRUCTURE
ARTICLE_LANG_SAVE_AS = '%s{slug}-{lang}.html' % PERMALINK_STRUCTURE
PAGE_SAVE_AS = '%spages/{slug}.html' % PERMALINK_STRUCTURE
PAGE_LANG_SAVE_AS = '%spages/{slug}-{lang}.html' % PERMALINK_STRUCTURE

# I like to put everything into the category ``Blog``, which also appears on
# the main menu. Tags will not appear on the menu.
DEFAULT_CATEGORY = 'Blog'

# I like to have ``Archives`` in the main menu.
MENUITEMS = (
    ('Archives', '/archives.html'),
)

SOCIAL = (
    ('shurain_', 'http://twitter.com/shurain_'),
)

#FEED_ATOM = 'shurain'
FEED_DOMAIN = 'http://feeds/feedburner.com'
FEED_ALL_ATOM = 'shurain'


WITH_PAGINATION = True
DEFAULT_PAGINATION = 10
REVERSE_ARCHIVE_ORDER = True

# Uncomment what ever you want to use
GOOGLE_ANALYTICS = 'UA-20801130-1'
DISQUS_SITENAME = 'shurain'
GITHUB_URL = 'http://github.com/shurain/shurain.github.com'
TWITTER_USERNAME = 'shurain_'
