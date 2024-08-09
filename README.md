# django-seohelper

[![PyPI version](https://badge.fury.io/py/django-seohelper.png)](http://badge.fury.io/py/django-seohelper)

**Django SeoHelper** is a pluggable application that helps you to add
meta-information to your Django templates.

## How to use

### Installation

Using pip:

    pip install django-seohelper

Using the source code:

    git clone https://github.com/kplaube/django-seohelper.git
    cd django-seohelper/
    python setup.py install

Configuring

- Add `seohelper` to your `INSTALLED_APPS`

### Adding the code to your Template

You need to put the code below in your template file:

    {% load seo_helper %}
    {% seo_helper request.path as meta %}

    <html>
    <head>
        <title>{{ meta.title }}</title>

        <meta name="description" content="{{ meta.description }}" />
        <meta name="keywords" content="{{ meta.keywords }}" />
        <meta name="robots" content="{{ meta.robot_tags }}" />
    </head>

    ...

    </html>

Where:
- `seo_helper` is the templatetag.
- `request.path` is the complete path of the document.
- `meta` is the variable where SeoHelper will keep the document's metadata.

### Using the admin

Let's suppose we want to add metadata to `http://myblog.com/2013/01/01/hello/`. So,
we need to access `/admin/seohelper/document/add/` and create a record with these parameters:

- **URL:** /2013/01/01/hello-world/
- **Title:** Hello World!
- **Description:** My first post.
- **Keywords:** index,follow

Now, when we access the `http://myblog.com/2013/01/01/hello/`, SeoHelper will restore those data from database and will show these in your page.

## Contributing

Contributions are very welcome!

One can run the tests through `tox`. With luck, it'll
install all the dependencies and set up the virtual environments for the different
combinations of Python and Django versions. You'll still be required to have the
different Python versions in your machine, and it's recommended to use `pyenv` to
have it done.

Activate the different Python versions first:

    pyenv local 3.12.1 3.11.7 3.10.13 3.9.18

It's recommended to rely on `Pipfile` to mananage dependencies and venvs:

    pipenv install --dev

And finally, you are good to go with Tox:

    pipenv run tox