import pika
import random

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Declaração do tópico para publicar a temperatura
channel.exchange_declare(exchange='temperatura', exchange_type='fanout')

# Gerando uma temperatura aleatória
cpu_temperature = random.uniform(60, 80)
channel.basic_publish(exchange='temperatura', routing_key='', body=str(cpu_temperature))

print(f"Temperatura da CPU publicada: {cpu_temperature}°C")

connection.close()
    