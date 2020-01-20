{% for _ in cookiecutter.project_name %}={% endfor %}
{{cookiecutter.project_name}}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{cookiecutter.project_description}}

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   changelog
   getting_started
   development
   api/modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
