import grpc
import click
import my_service_pb2
import my_service_pb2_grpc


@click.command()
@click.argument("command")
@click.option("--host", default="localhost", help="Host do servidor")
@click.option("--port", default=50051, help="Porta do servidor")
def run(command, host, port):
    with grpc.insecure_channel(f"{host}:{port}") as channel:
        stub = my_service_pb2_grpc.MyServiceStub(channel)
        request = my_service_pb2.CommandRequest(command=command)
        response = stub.ExecuteCommand(request)

    print(response.output)


if __name__ == "__main__":
    run()
