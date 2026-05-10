import tomllib
from pprint import pprint

def load_toml() -> dict:
    with open("pyproject.toml", 'rb') as f:
        toml_data = tomllib.load(f)
    return toml_data

if __name__ == "__main__":
    data: dict = load_toml()
    # print(data['database'])
    pprint(data, sort_dicts=False)
