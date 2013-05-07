from dropbox import client, rest, session

# TODO: Add tests for this guy.
class Client(object):
    def __init__(self, **kwargs):
        app_key = kwargs['app_key']
        app_secret = kwargs['app_secret']
        ACCESS_TYPE = 'app_folder'
        CALLBACK_URL = ''

        sess = session.DropboxSession(app_key, app_secret, ACCESS_TYPE)
        request_token = sess.obtain_request_token()
        url = sess.build_authorize_url(request_token, oauth_callback=CALLBACK_URL)
        print "url:", url
        print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
        raw_input()

        access_token = sess.obtain_access_token(request_token)
        self._client = client.DropboxClient(sess)

    def put_file(self, dest_path, f):
        return self._client.put_file(dest_path, f)
