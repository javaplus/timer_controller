from flask import Flask, request, json
import logging
import sys
import paho.mqtt.client as mqtt

client = mqtt.Client()

#from timer import stopCountDown

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

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
    mqttc = mqtt.Client("timer_pub")
    mqttc.connect("localhost", 1883)
    mqttc.publish("timer/timer", request.data,,qos=0,retain=True)
    mqttc.loop(2) #timeout = 2s

    #timer.countDown(int(request.json["minutes"])) 


    return 'Processing Timer'

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
