#!/usr/bin/python

import urllib2, base64, re, struct, time, socket, sys, datetime, os.path, requests

try:
    import json
except:
    import simplejson as json

import config

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

def getZabbixData():
    zabbix_data = {}
    zabbix_data["jsonrpc"] = "2.0"
    zabbix_data["method"] = "user.login"
    zabbix_data["id"] = 1

    return zabbix_data

def zbxLogin(url, login, passwd):
    if login and passwd:
        zabbix_data = getZabbixData()

        logindata = {}
        logindata["user"] = login
        logindata["password"] = passwd
        zabbix_data["params"] = logindata
        zabbix_data["method"] = "user.login"
        json_data = json.dumps(zabbix_data)

    r = urllib2.Request(url, json_data, {'Content-Type': 'application/json-rpc'})
    d = urllib2.urlopen(r).read()
    parsed_json = json.loads(d)
    return parsed_json["result"]

def zbxHosts(url, authId):
    zabbix_data = getZabbixData()

    params = {}
    params["output"] = ["hostid", "host"]
    zabbix_data["params"] = params
    zabbix_data["method"] = "host.get"
    zabbix_data["auth"] = authId
    json_data = json.dumps(zabbix_data)

    r = urllib2.Request(url, json_data, {'Content-Type': 'application/json-rpc'})
    d = urllib2.urlopen(r).read()
    parsed_json = json.loads(d)
    return parsed_json["result"]

zabbix_authId = zbxLogin(config.zabbix_host, config.zabbix_username, config.zabbix_password)

zabbix_hosts = zbxHosts(config.zabbix_host, zabbix_authId)

print zabbix_hosts

# pyglet.app.run()