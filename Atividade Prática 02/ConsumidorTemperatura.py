import pika

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Declaração do tópico para receber a temperatura
channel.exchange_declare(exchange='temperatura', exchange_type='fanout')

# Cria uma fila exclusiva e obtém o nome da fila
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# Faz o binding da fila com o tópico
channel.queue_bind(exchange='temperatura', queue=queue_name)

print('Aguardando temperatura da CPU...')


def callback(ch, method, properties, body):
    temperature = float(body)
    print(f"Recebida temperatura da CPU: {temperature}°C")
    
    # Verifica se há detecção de incêndio
    if temperature > 70:
        print("Temperatura acima do limite! Detectado incêndio!")
        # Publica mensagem de detecção de incêndio
        channel.basic_publish(exchange='', routing_key='incendio', body='Incêndio detectado!')


# Registra o consumidor para a fila
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

# Inicia o loop de espera por mensagens
channel.start_consuming()
