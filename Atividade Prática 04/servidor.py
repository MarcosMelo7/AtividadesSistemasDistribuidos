import grpc
import concurrent.futures
import subprocess
import my_service_pb2
import my_service_pb2_grpc


class MyServiceServicer(my_service_pb2_grpc.MyServiceServicer):
    def ExecuteCommand(self, request, context):
        command = request.command
        print(f"Comando recebido: {command}")

        try:
            output = subprocess.check_output(command, shell=True)
            response = my_service_pb2.CommandResponse(output=output.decode())
        except subprocess.CalledProcessError as e:
            response = my_service_pb2.CommandResponse(output=e.output.decode())

        return response


def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_MyServiceServicer_to_server(MyServiceServicer(), server)

    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
