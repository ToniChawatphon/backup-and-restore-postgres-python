import os
import yaml


def read_yaml(path: str):
    _yaml = None
    if os.path.exists(path):
        with open(path, 'r') as f:
            _yaml = yaml.safe_load(f)
    return _yaml
