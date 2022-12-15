from Rest import app

from Controller.ServerController import recup_server_props
import json
from flask import Flask, request,Response, jsonify


#To join the network
@app.route('/get/cpu/and/ram',methods=['Get'])
def get_cpu_and_ram():
    data = recup_server_props()
    return jsonify(data)

