import yaml

class YConfiguration(dict):
    def __getattr__(self, prop):
        if prop in self:
            return self[prop]
        else:
            raise AttributeError

class Loader(object):
    def __init__(self, file_path=None):
        self._file_path = file_path

    def load_file(self):
        try:
            return open(self._file_path).read()
        except IOError:
            print "Yaml File not found... Creating one."
            print "APP_KEY?"
            app_key = raw_input().strip()
            print "APP_SECRET?"
            app_secret = raw_input().strip()
            print "camera_url?"
            camera_url = raw_input().strip()
            yml_file = open(self._file_path, 'w')
            app_dict = {
                    'app_key' : app_key,
                    'app_secret' : app_secret,
                    'camera_url' : camera_url
            }
            dump_str = yaml.dump(app_dict, yml_file)
            yml_file.close
            return open(self._file_path).read()


    def conf(self):
        self._file = self.load_file()
        cdict = yaml.load(self._file)
        return YConfiguration(cdict)

