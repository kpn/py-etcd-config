etcd_config
===========

.. image:: https://secure.travis-ci.org/kpn-digital/etcd_config.svg?branch=master
    :target:  http://travis-ci.org/kpn-digital/etcd_config?branch=master

.. image:: https://img.shields.io/codecov/c/github/kpn-digital/etcd_config/master.svg
    :target: http://codecov.io/github/kpn-digital/etcd_config?branch=master

.. image:: https://img.shields.io/pypi/v/etcd_config.svg
    :target: https://pypi.python.org/pypi/etcd_config

.. image:: https://readthedocs.org/projects/etcd_config/badge/?version=latest
    :target: http://etcd_config.readthedocs.org/en/latest/?badge=latest


Features
--------

This library allows Python applications load configuration from ETCD:

* Environment dependent values
* Values in different config sets, identified by name


Backends
--------

- ETCD 2.2.1


Installation
------------

.. code-block:: bash

    $ pip install etcd-config


Usage
-----

.. code-block:: python

    import etcd_config.loader
    config = etcd_config.loader.get_overwrites(
        env='test',
        dev_params='main.params',
        etcd_details=dict(
            protocol=getattr(params, 'ETCD_PROTOCOL', 'http'),
            host=getattr(params, 'ETCD_HOST', 'localhost'),
            port=getattr(params, 'ETCD_PORT', 2379),
            username=getattr(params, 'ETCD_USERNAME', None),
            password=getattr(params, 'ETCD_PASSWORD', None),
            prefix='/config/your_project'
        )
    )
