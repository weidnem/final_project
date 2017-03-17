from .settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['ec2-54-189-192-244.us-west-2.compute.amazonaws.com/', 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
