"""
A pager class for Flask
"""
from setuptools import setup


setup(
    name='Flask-Pager',
    version='0.1',
    url='http://github.com/pudo/flask-pager',
    license='MIT',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    description='A pager class for Flask',
    long_description=__doc__,
    py_modules=['flask_pager'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
