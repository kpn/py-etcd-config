========
Usage
========

To use etcd_config in a project::

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
