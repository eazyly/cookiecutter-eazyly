#!/bin/sh

{% if cookiecutter.framework == "flask" %}
pip install -e .
{% elif cookiecutter.framework == "nodejs" %}
npm install
{% else %}
#  Install depedencies etc over here. 
{% endif %}