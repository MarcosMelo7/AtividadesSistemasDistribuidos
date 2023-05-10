import pika

# Conexão com o servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

# Declaração do tópico para receber a detecção de incêndio
channel.queue_declare(queue='incendio')

print('Aguardando detecção de incêndio...')


def callback(ch, method, properties, body):
    print(f"Detecção de incêndio: {body}")
    # Ativa o alarme sonoro ou realiza outra ação
    
    # Exemplo: Exibir uma mensagem no terminal
    print("Incêndio detectado! Ativando alarme sonoro...")


# Registra o consumidor para a fila
channel.basic_consume(queue='incendio', on_message_callback=callback, auto_ack=True)

# Inicia o loop de espera por mensagens
channel.start_consuming()
