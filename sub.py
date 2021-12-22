import paho.mqtt.client as paho

broker = "broker.hivemq.com"

def on_message(client, userdata, msg):
    print("channel: "+msg.topic+", Msg: "+str(msg.payload))    

client = paho.Client()
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("mohammad-180162/#")

client.loop_forever()