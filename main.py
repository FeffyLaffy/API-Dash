from flask import Flask
from API.login import login
from API.save import save
from API.config import config
from API.time import time

import ssl

app = Flask(__name__)
lib=["login", "save", "config", "time"]
for lib in lib:
    app.register_blueprint(globals()[lib])

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.load_cert_chain('konishi.crt', 'konishi.key')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=context, debug=True)