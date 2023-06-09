import yaml
import os


class YamlOperation(dict):
    def __init__(self, file_path=None, content=None):
        super().__init__()

        if file_path is not None:
            with open(file_path, "r")as file:
                content = yaml.load(file, Loader=yaml.SafeLoader)

        content = content if content is not None else {}
        # content = [content, {}][not content]
        # content = (not content and content or {})

        for key, value in content.items():
            if isinstance(value, dict):
                self[key] = YamlOperation(content=value)
            else:
                self[key] = value

    def __getattr__(self, key):
        """访问不存在的属性key时返回None"""
        return None

    def __setattr__(self, key, value):
        """设置实例属性值"""
        self[key] = value

    def __setitem__(self, key, value):
        """给self[key]赋值"""
        super().__setattr__(key, value)
        super().__setitem__(key, value)

    def __missing__(self, key):
        """访问的键key不存在时，返回None"""
        return None


yaml_data = YamlOperation(os.path.join(os.getcwd(), "features/config.yml"))

