# -*- coding:utf-8 -*-

from redis import Redis as redis
from redis import ConnectionPool as connPool

pool = connPool(host='localhost', port=6380, db=0,
                decode_responses=True, password='iot@2018')
r = redis(connection_pool=pool)
# r = Redis(host='localhost', port='6380', decode_responses=True, password='iot@2018')

key = 'c_nanme'
r.set(key, 'chengchaos')

print(r[key])
print(r.get(key))
print(type(r.get(key)))
