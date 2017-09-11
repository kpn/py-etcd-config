class TestSettings(object):

    ETCD_PREFIX = '/config/etcd_config'
    ETCD_ENV = 'test'
    ETCD_HOST = 'etcd'
    ETCD_PORT = 2379
    ETCD_USERNAME = 'test'
    ETCD_PASSWORD = 'test'
    ETCD_DETAILS = dict(
        host='etcd',
        port=2379,
        prefix='/config/etcd_config',
        username='test',
        password='test'
    )


settings = TestSettings()
