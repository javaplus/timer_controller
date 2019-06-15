from flask import Flask, request, json
import logging
import sys
import paho.mqtt.client as mqtt
import time
from flask_cors import CORS

client = mqtt.Client()

#from timer import stopCountDown

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
CORS(app)

@app.route('/')
def api_pitimer():
    return 'Hello World'

@app.route('/stop')
def api_stop():
    
    return 'stopping'

@app.route('/timer', methods = ['POST'])
def api_timer():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Data=' + request.data)
    logging.info(request.json["minutes"])
    minutes = int(request.json["minutes"])
    # convert minutes to the time in the future when the 
    # timer should end. This way it can calculate num of minutes
    sec = minutes * 60 #number of seconds
    futureTimeInSecs = time.time() + sec

    requestData = {}
    requestData["timeToEnd"] = str(futureTimeInSecs)
    #pass speaktime and interval time 
    requestData["speaktime"] = request.json["speaktime"]
    requestData["speakinterval"] = request.json["speakinterval"]
    
    mqttc = mqtt.Client("timer_pub")
    mqttc.connect("localhost", 1883)
    # retain messages so on restart clients get last message
    mqttc.publish("timer/timer", json.dumps(requestData),qos=0,retain=True) 
    mqttc.loop(2) #timeout = 2s

    #timer.countDown(int(request.json["minutes"])) 


    return 'Processing Timer'

@app.route('/say', methods = ['POST'])
def say():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Data=' + request.data)

    mqttc = mqtt.Client("speech_pub")
    mqttc.connect("localhost", 1883)
    # retain messages so on restart clients get last message
    mqttc.publish("speech/talk", request.data,qos=0,retain=False)
    mqttc.loop(2) #timeout = 2s

    return 'Processing Phrase'




if __name__ == '__main__':
    pitimer = logging.getLogger("flask.app")
    pitimer.setLevel(logging.WARN)
    adaLogger = logging.getLogger("Adafruit_I2C")
    adaLogger.setLevel(logging.WARN)


    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    pitimer.addHandler(ch)
    #logging.basicConfig(stream=sys.stdout)
    app.run(host='0.0.0.0')
