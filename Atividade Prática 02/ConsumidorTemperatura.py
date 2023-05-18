import pika

# Função que será chamada para processar cada mensagem recebida
def callback(ch, method, properties, body):
    temperatura = float(body)
    print(f"Recebida temperatura da CPU: {temperatura}°C")
    print("Verificando se há detecção de incêndio...")
    if temperatura > 70:
        print("Temperatura acima do limite! Detectado incêndio!")
        channel.basic_publish(exchange='incendio', routing_key='', body='Incendio detectado!')
        print("Publicando mensagem de detecção de incêndio...")

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Declaração do tópico para receber a temperatura
channel.exchange_declare(exchange='temperatura', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='temperatura', queue=queue_name)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Aguardando temperatura da CPU...")
channel.start_consuming()
