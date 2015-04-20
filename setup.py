from setuptools import setup, find_packages

from cmsplugin_raw_html import __version__

setup(
    name='cmsplugin-raw-html',
    version=__version__,
    description='A Django CMS 3.1 plugin to add raw HTML code into page and text.',
    long_description=open('README.md').read(),
    maintainer='Mykhailo Makukha',
    maintainer_email='m.makukha@gmail.com',
    url='https://github.com/makukha/cmsplugin-raw-html',
    license='MIT',
    packages=['cmsplugin_raw_html'],
    package_dir={'cmsplugin_raw_html': 'cmsplugin_raw_html'},
    package_data={'cmsplugin_raw_html': ['templates/cmsplugin_raw_html/*.html']},
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
