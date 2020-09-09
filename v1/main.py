from http.server import BaseHTTPRequestHandler
from datetime import datetime
import urllib.request
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
            self.send_response(200)
            self.end_headers()
            with urllib.request.urlopen('https://pritishaw.github.io/ReadMe-Charts/') as response:
                self.wfile.write(response.read())
        else:
            try:
                df = pd.read_csv(params["src"][0])                

                if "dark" in params:
                    plt.style.use('dark_background')
                else:
                    plt.style.use('default')
                plt.figure()

                x_min= x_max= y_min= y_max = None

                if "xmin" in params:
                    x_min = int(params["xmin"][0])
                if "xmax" in params:
                    x_max = int(params["xmax"][0])
                if "ymin" in params:
                    y_min = int(params["ymin"][0])
                if "ymax" in params:
                    y_max = int(params["ymax"][0])

                if "legend" not in params:
                    df.plot(ylim=[y_min, y_max], xlim=[x_min, x_max], legend=None)
                else:
                    df.plot(ylim=[y_min, y_max], xlim=[x_min, x_max])
                    plt.legend(loc='best')
                
                if "title" in params:
                    plt.title(params["title"][0])
                if "x" in params:
                    plt.xlabel(params["x"][0])
                if "y" in params:
                    plt.ylabel(params["y"][0])

                fig = plt.gcf()
                buf = io.BytesIO()
                type = "svg"
                if "type" in params:
                    type = params["type"][0]
                fig.savefig(buf, format=type)
                buf.seek(0)

                self.send_response(200)
                self.send_header('Content-type', 'image/svg+xml' if type=="svg" else f"image/{type}")
                self.end_headers()
                self.wfile.write(buf.read())
            except Exception as err:
                self.send_response(403)
                self.end_headers()
                self.wfile.write(f"Failed to render: {err}".encode())
        return
