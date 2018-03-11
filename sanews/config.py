import os


DATABASE_URL = os.environ.get('SANEWS_DATABASE_URL', 'postgresql://sanews@localhost/sanews')
