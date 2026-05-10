import yaml
from pprint import pprint

with open('config.yaml', 'r') as f:
    config: dict = yaml.safe_load(f)
    
pprint(config, sort_dicts=False)
print(config['multiline_string'])
print(config['multiline_string2'])
print(config['multiline_string3'])
