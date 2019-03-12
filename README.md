# Config

Configurations with Singleton design pattern. Supoort loading from / saving to .json files.

Since the use of Singleton design pattern, the `Config_` can only be initialized once. The second call of `Config_(config_json)`will not load the configurations from the .json file; instead, use `Config().attr1 = value` to change value or `config.load(config_json)`. The following call of `Config_()` will return the same instance.

## Example

```python
from config import Config_

class Config(Config_):
    def __init__(self, config_json):
        super().__init__(config_json)
        self._set_default('attr1', 1)
        self._set_default('attr2', dict())

config = Config()
print(config)
config.load('input.json')
config.attr1 = 2
assert Config().attr1 == 2
config.save('output.json')
config = Config('output.json')
assert config.attr1 == 2
```
