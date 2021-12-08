import redis
import os

r = redis.StrictRedis(host=os.getenv('HOST_REDIS', 'redis'),
                      port=os.getenv('PORT_REDIS', 6379),
                      db=0
                      )

def add_to_redis(key, val):
    try:
        r.set(key, val)
        return True
    except:
        return False


def delete_value_from_redis(key):
    try:
        r.delete(key)
        return True
    except:
        return False


def get_value_from_redis(key):
    """
    returns a tuple,
    first value defines if it is in cachem the other value is what is in the cache
    """
    value = None
    try:
        value = r.get(key)
        if value:
            value = value.decode('utf-8')
            return True, value
        return False, value
    except:
        return False, value