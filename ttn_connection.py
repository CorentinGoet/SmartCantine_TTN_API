"""
@author Corentin Goetghebeur

This script collects data from our application in The Things Network to put it in our own database.
This script is based on the api written by Terry Moore. https://github.com/terrillmoore/ttn_storage_api
"""

import ttn_storage_api


if __name__ == '__main__':

    # Define parameters for our application
    app_name = "smart-cantine-app"
    key = "NNSXS.VRIDNAJR4HU6CTMXV5RK7GZ36RIQHPILZPFUBNA.KG57DQVTXBZXCPYJGXESQJW5X72C2EON4N25ZAT3P2ULJXXLWQDQ"

    # fetch and display data
    r = ttn_storage_api.sensor_pull_storage(app_name, key, "1h")
    print(r)
