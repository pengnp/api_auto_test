import yaml
from utils.config import PATH
import os


class YamlUtil:

    def __init__(self, file_name):
        self.yaml_data = self.read_yaml(file_name)

    def read_yaml(self, file_name):
        path = os.path.join(PATH, f'case/{file_name}')
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)

    def get_data(self, key, flag=True):
        if flag:
            return self.yaml_data[key]['data']
        else:
            return self.yaml_data[key]


if __name__ == '__main__':
    print(YamlUtil('bili.yml').get_data('test_search'))