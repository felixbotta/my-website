import environ
from .base import *

env = environ.Env()

DEBUG = env.bool("DEBUG", False)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {
    "default": env.db(),
}

AWS_ACCESS_KEY_ID = 'AKIAYWNVDEXIRGWGNL6K'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'developer-site-fcb'

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
