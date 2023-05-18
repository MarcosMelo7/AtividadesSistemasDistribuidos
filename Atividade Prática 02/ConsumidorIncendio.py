import pika

# Função que será chamada para processar cada mensagem recebida
def callback(ch, method, properties, body):
    print("Incêndio detectado! Ativando alarme sonoro...")

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Declaração do tópico para receber a detecção de incêndio
channel.exchange_declare(exchange='incendio', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='incendio', queue=queue_name)

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("Aguardando detecção de incêndio...")
channel.start_consuming()
        