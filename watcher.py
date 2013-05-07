import requests
from time import sleep
import datetime

MINUTES = 60
# TODO: Add tests for this guy.
class Watcher(object):
    def __init__(self, **kwargs):
        self._client = kwargs['client']

    def watch(self, **kwargs):
        camera_url = kwargs['camera_url']
        destination = kwargs['destination']
        client_call = getattr(self._client, 'put_file')

        while True:
            img = requests.get(camera_url).content
            now_str = datetime.datetime.now().isoformat()
            ds_path = "%s%s.jpg" % (destination, now_str)
            client_call(ds_path, img)
            sleep(15 * MINUTES)
