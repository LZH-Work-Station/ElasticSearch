import yaml


class YamlConfig:
    yaml_path = "../conf/application.yml"

    # 读取yaml配置文件
    def __init__(self):
        file = open(YamlConfig.yaml_path)
        config = yaml.load(file.read(), Loader=yaml.FullLoader)
        file.close()
        self.config = config
