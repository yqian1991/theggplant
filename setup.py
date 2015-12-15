import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'readme.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid-jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_storage',
    'SQLAlchemy',
    'sqlalchemy_utils',
    'passlib',
    'wtforms',
    'python-slugify',
    'simplejson',
    'validictory',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'Babel',
    'lingua'
    ]

setup(name='theggplant',
      version='0.0',
      description='theggplant',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='theggplant',
      install_requires=requires,
      message_extractors = { '.': [
          ('**.py', 'python', None ),
          ('**.pt', 'lingua_xml', None ),
          ('**.jinja2', 'jinja2', None),
          ('static/**', 'ignore', None)
      ]},
      entry_points="""\
      [paste.app_factory]
      main = theggplant:main
      [console_scripts]
      initialize_theggplant_db = theggplant.scripts.initializedb:main
      """,
      )
