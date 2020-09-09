from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib.parse import parse_qs, quote
import base64
import io

import pandas as pd
import matplotlib.pyplot as plt


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        params = parse_qs(path[2:])
        if "src" not in params:
            self.send_response(404)
        else:
            try:
                df = pd.read_csv(params["src"][0])
                plt.figure()
                df.plot()
                plt.legend(loc='best')
                if "title" in params:
                    plt.title(params["title"][0])
                if "x" in params:
                    plt.xlabel(params["x"][0])
                if "y" in params:
                    plt.ylabel(params["y"][0])

                fig = plt.gcf()
                buf = io.BytesIO()
                fig.savefig(buf, format='svg')
                buf.seek(0)

                self.send_response(200)
                self.send_header('Content-type', 'image/svg+xml')
                self.end_headers()
                self.wfile.write(buf.read())
            except Exception as err:
                self.send_response(502)
                self.end_headers()
                self.wfile.write(f"Failed to render: {err}".encode())
        return
