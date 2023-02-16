# MIT License

# Copyright (c) 2022 Feffy

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from flask import Flask
from API.config import config
from API.login import login
# from API.mongoJobs import mongoJobs
from API.save import save
from API.board import board
from API.profile import profile
from API.statistics import statistics
from API.time import time
import os
import ssl

app = Flask(__name__)

lib = os.listdir("API")
lib = list(filter(lambda x: x.endswith(".py"), lib))
lib = list(map(lambda x: x.rstrip(".py"), lib))

for lib in lib:
    if lib == 'mongoJobs':
        continue
    # if lib == 'musedash':
    #     continue
    print(f"Loading {lib}...")
    app.register_blueprint(globals()[lib])

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.load_cert_chain('konishi.crt', 'konishi.key')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=context, debug=True)
