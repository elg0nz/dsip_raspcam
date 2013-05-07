import time
from yaml_loader import Loader
from ds_client import Client
from watcher import Watcher

l_conf = Loader('./dsip.yml').conf()
app_key, app_secret = l_conf.app_key, l_conf.app_secret
camera_url = l_conf.camera_url


client = Client(app_key=app_key, app_secret=app_secret)

watcher = Watcher(client=client) # TODO: Threading...
watcher.watch(camera_url=camera_url, destination='/')
