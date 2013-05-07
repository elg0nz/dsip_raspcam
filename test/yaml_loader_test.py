from unittest import TestCase
from yaml_loader import Loader
import nose
from mock import Mock

class YamlLoaderTest(TestCase):
    def test_parse_settings(self):
        document = """
        app_key: 1
        app_secret: 2
        access_type: 3
        call_back_url: 4
        """
        loader = Loader('/some/fake/path')
        loader.load_file = Mock(return_value=document)
        app_conf = loader.conf()
        self.assertEqual(app_conf.app_key, 1)
        self.assertEqual(app_conf.app_secret, 2)
        self.assertEqual(app_conf.access_type, 3)
        self.assertEqual(app_conf.call_back_url, 4)
