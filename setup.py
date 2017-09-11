
from setuptools import setup
setup(**{'author': 'Andrey Makhnach',
 'author_email': 'andrey.makhnach@kpn.com',
 'classifiers': ['Development Status :: 5 - Production/Stable',
                 'Environment :: Web Environment',
                 'Intended Audience :: Developers',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Internet :: WWW/HTTP'],
 'description': 'A dynamic settings management solution using ETCD',
 'include_package_data': True,
 'install_requires': ['python-etcd>=0.4.1',
                      'python-dateutil>=2.2',
                      'six<2.0.0,>=1.10.0'],
 'long_description': "etcd_config\n===========\n\n.. image:: https://secure.travis-ci.org/kpn-digital/etcd_config.svg?branch=master\n    :target:  http://travis-ci.org/kpn-digital/etcd_config?branch=master\n\n.. image:: https://img.shields.io/codecov/c/github/kpn-digital/etcd_config/master.svg\n    :target: http://codecov.io/github/kpn-digital/etcd_config?branch=master\n\n.. image:: https://img.shields.io/pypi/v/etcd_config.svg\n    :target: https://pypi.python.org/pypi/etcd_config\n\n.. image:: https://readthedocs.org/projects/etcd_config/badge/?version=latest\n    :target: http://etcd_config.readthedocs.org/en/latest/?badge=latest\n\n\nFeatures\n--------\n\nThis library allows Python applications load configuration from ETCD:\n\n* Environment dependent values\n* Values in different config sets, identified by name\n\n\nBackends\n--------\n\n- ETCD 2.2.1\n\n\nInstallation\n------------\n\n.. code-block:: bash\n\n    $ pip install etcd-config\n\n\nUsage\n-----\n\n.. code-block:: python\n\n    import etcd_config.loader\n    config = etcd_config.loader.get_overwrites(\n        env='test',\n        dev_params='main.params',\n        etcd_details=dict(\n            protocol=getattr(params, 'ETCD_PROTOCOL', 'http'),\n            host=getattr(params, 'ETCD_HOST', 'localhost'),\n            port=getattr(params, 'ETCD_PORT', 2379),\n            username=getattr(params, 'ETCD_USERNAME', None),\n            password=getattr(params, 'ETCD_PASSWORD', None),\n            prefix='/config/your_project'\n        )\n    )\n",
 'name': 'etcd-config',
 'packages': ['etcd_config', 'tests'],
 'tests_require': ['tox'],
 'url': 'https://github.com/kpn-digital/py-etcd-config',
 'version': None,
 'zip_safe': False})