from Rest import app

from Controller.ServerController import recup_server_props, run_shell
import json
from flask import Flask, request,Response, jsonify


#To join the network
@app.route('/get/cpu/and/ram',methods=['Get'])
def get_cpu_and_ram():
    data = recup_server_props()
    return jsonify(data)


@app.route('/run/shell/<name>',methods=['Get'])
def post_run_shell(name):
    res = run_shell(name)
    return jsonify(res)
