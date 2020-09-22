{{  cookiecutter.project_name }}
========

{% if cookiecutter.build_system == "drone" %}
[![Build Status]({{ cookiecutter.build_system_url }}/api/badges/{{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }}/status.svg?branch=master)]({{ cookiecutter.build_system_url }}/{{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }})
{% endif %}

{{ cookiecutter.project_short_description }}

# Installation

## Pre-Requisites

Following pre-requisites are needed before installation:

{% if cookiecutter.framework == "flask" %}
- python 2.7
{% elif cookiecutter.framework == "nodejs" %}
- node 8
{% else %}
{% endif %}
- git
- docker
- nginx
- certbot
- mongodb 3.6

## Run Code

After the pre-requisites are installed, clone this repository using git and move into the repository by running: 

```bash
cd {{ cookiecutter.repo_name }}
```

Then to run the code run following commands:

```bash
sudo docker build  -t {{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }}:{{ cookiecutter.version }} .
sudo docker run --rm -p {{ cookiecutter.port }}:{{ cookiecutter.port }}/tcp {{ cookiecutter.git_organization }}/{{ cookiecutter.repo_name }}:{{ cookiecutter.version }}
```
