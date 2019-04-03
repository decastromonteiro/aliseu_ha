import paho.mqtt.client as mqtt
import rpi_rf
import argparse
import logging
import time

# DEFAULT PARAMETERS
broker_address = "192.168.1.184"
broker_port = 60
topic = "house/fan/#"
username = 'admin'
password = 'admin'
log = False

# FANS Codes

fans_codes = {
    'uuid4': {
        'light': [1, 2, 3, 4],
        'fan': [13, 14, 15, 16],
        'speed': [5, 6, 7, 8],
        'direction': [9, 10, 11, 12],
        'timer': [17, 18, 19, 20]

    }
}


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe(topic)


# Callback responável por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
    print(msg.topic + " -  " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
# Seta um usuário e senha para o Broker, se não tem, não use esta linha
client.username_pw_set("USUARIO", password="SENHA")
# Conecta no MQTT Broker, no meu caso, o Mosquitto
client.connect("IP_OU_URL_BROKER", PORTA, 60)
# Inicia o loop
client.loop_forever()
