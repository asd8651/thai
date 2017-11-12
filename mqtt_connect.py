import paho.mqtt.client as mqtt
import requests
import time
import json
import sys
def on_connect(mqttc, obj, flags, rc):
    pass
def on_message(mqttc, obj, msg):
    print(msg.payload=="pv702\n")
    if(msg.payload!="pv702\n"):
        try:
            data = json.loads(msg.payload)
            print data
            params = {"pv_volt": data['pv_volt'], "pv_cur": data['pv_cur'], "pv_power": data['pv_power'],
                      "Rediation": data['Rediation'], "pv_Temp": data['pv_Temp'], "amb_temp": data['amb_temp'],
                      "Daily": data['Daily'], "total_L": data['total_L'], "total_H": data['total_H'],
                      "date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}
            res = requests.post('http://60.249.6.104:8787/api/store/MMeZwZMbHIDa', params=params)
            print res.text
        except:
            print "Unexpected error:", sys.exc_info()[0]
            pass
def on_publish(mqttc, obj, mid):
    pass
def on_subscribe(mqttc, obj, mid, granted_qos):
    pass
def on_log(mqttc, obj, level, string):
    pass
mqttc = mqtt.Client(client_id="ncut_user6537374555")
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
mqttc.username_pw_set(username="admin", password="admin")
mqttc.connect("apecpv.cmru.ac.th", 1883, 60)
mqttc.subscribe("pv702", 0)
mqttc.loop_forever()