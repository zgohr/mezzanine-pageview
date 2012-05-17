from setuptools import setup, find_packages
import sys, os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import mezzanine_pageview

setup(
    name="mezzanine-pageview",
    version=mezzanine_pageview.__version__,
    url="https://github.com/zgohr/mezzanine-pageview",
    author="Zach Gohr",
    author_email="zachary.gohr@gmail.com",
    license="MIT",
    description="Group level permission for Page viewing",
    long_description=open('README.md').read(),
    keywords="django, mezzanine, groups, permissions",
    packages=find_packages(),
    setup_requires=("setuptools"),
    install_requires=("setuptools", "mezzanine>=1.0.8",),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: "
                              "Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",],
    zip_safe=False,
    include_package_data=True,
)
