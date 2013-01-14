django-seohelper
================

![Travis CI](https://secure.travis-ci.org/kplaube/django-seohelper.png)

**Django SeoHelper** is a pluggable application that helps you to add
meta-information to your Django templates.

Soon, more information about usage.


Installation
------------

Using pip:

    pip install django-seohelper

Using the source code:

    git clone https://github.com/kplaube/django-seohelper.git
    cd django-seohelper/
    python setup.install

Configuring

* Add `seohelper` to your `INSTALLED_APPS`
* Run `syncdb` to create all necessary tables

Adding the code to your Template
--------------------------------

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

Where `seo_helper` is the templatetag, `request.path` is the complete path of the document and `meta` is the variable where SeoHelper will keep the document's metadata.

Using the admin
---------------

Let's suppose we want to add metadata to `http://myblog.com/2013/01/01/hello/`. So,
we need to access `/admin/seohelper/document/add/` and create a record with these parameters:

* **URL:** /2013/01/01/hello-world/
* **Title:** Hello World!
* **Description:** My first post.
* **Keywords:** index,follow

Now, when we access the `http://myblog.com/2013/01/01/hello/`, SeoHelper will restore those data from database and will show these in your page.
