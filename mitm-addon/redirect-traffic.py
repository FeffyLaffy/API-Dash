from mitmproxy import ctx
import mitmproxy.http


class LocalRedirect:

    def __init__(self):
        print('Loaded redirect addon')

    def request(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("pretty host is: %s" % flow.request.pretty_host)
        if flow.request.pretty_host in [
            "prpr-muse-dash.peropero.net",
            "us-musedash.peropero.net",
            "user-us.peropero.net",
        ]:
            ctx.log.info("pretty host is: %s" % flow.request.pretty_host)
            flow.request.host = "127.0.0.1"
            flow.request.port = 4433
            flow.request.scheme = 'http'


addons = [
    LocalRedirect()
]
