from setuptools import setup, find_packages

setup(
    name='apikit',
    version='0.4',
    url='http://github.com/pudo/apikit',
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
        'Flask', 'six'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
