#!/usr/bin/python

import urllib2, base64, re, struct, time, socket, sys, datetime, os.path, requests

try:
    import json
except:
    import simplejson as json

# import pyglet
#
# window = pyglet.window.Window()
#
# label = pyglet.text.Label('Hello, world',
# 			font_name='Times New Roman',
# 			font_size=12,
# 			x=window.width//2, y=window.height//2,
# 			anchor_x='center', anchor_y='center')
#
# @window.event
# def on_draw():
#     window.clear()
#     label.draw()

# {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1,
#     "auth": null
# }

def zbxLogin(url, login, passwd):
    if login and passwd:
        logindata = {}
        logindata["user"] = login
        logindata["password"] = passwd
        data = {}
        data["jsonrpc"] = "2.0"
        data["method"] = "user.login"
        data["params"] = logindata
        data["id"] = 1
        json_data = json.dumps(data)

    r = urllib2.Request(url, json_data, {'Content-Type': 'application/json-rpc'})
    d = urllib2.urlopen(r).read()
    parsed_json = json.loads(d)
    return parsed_json["result"]

authId = zbxLogin("http://zabbix-prod.psrv4.citronium.com/zabbix/api_jsonrpc.php", "mmamaev", "j3qq4h7h2v")

print authId

# pyglet.app.run()