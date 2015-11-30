# LazyConfig [![Build Status](https://travis-ci.org/alexandrevicenzi/lazyconfig.svg?branch=master)](https://travis-ci.org/alexandrevicenzi/lazyconfig)

Yaml configuration made lazy

## Setup

TODO

## Requirements

Python 2.6+ or 3.2+ or PyPy.

## How to use?

Create a configuration file (YAML):

```yaml
redis:
  db: 0
  pwd: 'test'
  host: 'localhost'
  port: 6379
```

Import `lazyconfig` to your project:

```python
import redis

from lazyconfig import lazyconfig

lazyconfig.set_config_file('my_config_file.yaml')

redis.Redis(host=lazyconfig.config.redis.host,
            port=lazyconfig.config.redis.port,
            db=lazyconfig.config.redis.db,
            password=lazyconfig.config.redis.pwd)
```

> **Notes:**
> - By default you don't need to call `set_config_file` if your configuration file is `config.yaml` and located in the App root directory.
> - This lib is not lazy load at all. The configuration file is loaded if you call `lazyconfig.config` or `lazyconfig.load()`.
> - Loaded once, you don't need to load again. If so, call `lazyconfig.reload()`.

## Why is it good for?

Well, if you're a Django user, you know that [Django settings](https://docs.djangoproject.com/en/1.8/topics/settings/) is a really good stuff.
But how about your small project? This is a lib that helps you to configure your App is a similar way.

## Tests

`python tests/test.py`

## License

MIT
