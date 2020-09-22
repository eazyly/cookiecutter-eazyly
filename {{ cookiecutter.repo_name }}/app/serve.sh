#!/bin/sh

{% if cookiecutter.framework == "flask" %}
gunicorn -w ${APP_THREADS} -b 0.0.0.0:${APP_PORT} ${APP_MODULE}:app
{% elif cookiecutter.framework == "nodejs" %}
node index.js
{% else %}
#  Run your server here 
{% endif %}