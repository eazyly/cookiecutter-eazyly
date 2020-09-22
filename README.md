cookiecutter-eazyly
========

[![Build Status](https://drone.ashutoshmishra.net/api/badges/eazyly/cookiecutter-eazyly/status.svg?branch=master)](https://drone.ashutoshmishra.net/eazyly/cookiecutter-eazyly)

Boilerplate for creating CI/CD enabled Server applications.

# Introduction
This project takes care of the setup and configuration so you can focus on making your service awesome. Scaffolding a project takes seconds and it gives you the essentials of devops and container orchestration, like drone, helm, kubernetes integration to get started. This project aims to get out of your way, and to allow you easily and quickly create web services while providing a solid foundation for your service to mature in the future.

## Features

- Support for RESTful & JSON-RPC services via [Python Eve](http://docs.python-eve.org/en/latest/) & [Python Flask](http://flask.pocoo.org/)
- Support for Web frameworks like [Python Flask](http://flask.pocoo.org/) & [nodejs](https://nodejs.org/en/)
- CI/CD via [Drone.io](https://drone.io)
- [Helm](https://www.helm.sh/) for deployment in [Kubernetes](https://kubernetes.io/)

## Quick Start
Install [cookiecutter](https://github.com/audreyr/cookiecutter):
```bash
pip install cookiecutter
```

Scaffold your project (from [github](https://github.com/eazyly/cookiecutter-eazyly)):
```
cookiecutter gh:eazyly/cookiecutter-eazyly
```
OR (from folder)
```
git clone https://github.com/eazyly/cookiecutter-eazyly.git
cookiecutter cookiecutter-eazyly
```

![scaffolding screencast]()

## Contributing
Want a new feature or find a bug? Submit a Pull Request!
