from setuptools import setup, find_packages

setup(
    name='restkit',
    version='0.1',
    url='http://github.com/pudo/restkit',
    license='MIT',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    description='A set of utility functions for RESTful Flask applications.',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=[],
    include_package_data=True,
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
