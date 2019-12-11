import os
from setuptools import setup
from seohelper import get_version


requires = []
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.md")).read()

setup(
    name="django-seohelper",
    version=get_version(),
    license="GNU Lesser General Public License (LGPL), Version 3",
    description="Manager the meta information of your pages in Django",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="web django apps seo seohelper",
    author="Klaus Laube",
    author_email="kplaube@gmail.com",
    url="https://github.com/kplaube/django-seohelper/",
    packages=["seohelper"],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    classifiers=[
        "Environment :: Plugins",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
