from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='i+&@647%ko1b#wto+#ov#m!5c1m(m_%u0lu7^2@)2!lkel#h*q')
DEBUG = env.bool('DJANGO_DEBUG', default=True)


