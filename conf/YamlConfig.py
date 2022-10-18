import yaml
import os
current_directory = os.path.dirname(os.path.abspath(__file__))

class YamlConfig:
    yaml_path = current_directory + "/../conf/application.yml"

    # 读取yaml配置文件
    def __init__(self):
        file = open(YamlConfig.yaml_path)
        config = yaml.load(file.read(), Loader=yaml.FullLoader)
        file.close()
        self.config = config
