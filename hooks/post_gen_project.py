#!/usr/bin/env python

import os
import distutils
from distutils import dir_util
from cookiecutter.main import cookiecutter

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
APP_DIRECTORY = 'app'

if __name__ == '__main__':
    if '{{ cookiecutter.framework }}' == 'flask' and '{{ cookiecutter.project_type }}' == 'apiserver':
        cookiecutter(
            'https://github.com/eazyly/cookiecutter-{{ cookiecutter.framework }}-{{ cookiecutter.project_type }}.git', 
            no_input=True,
            extra_context={{ cookiecutter | jsonify }})
        distutils.dir_util.copy_tree('{{ cookiecutter.repo_name }}', APP_DIRECTORY)
        distutils.dir_util.remove_tree('{{ cookiecutter.repo_name }}')
