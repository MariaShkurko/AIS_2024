from concurrent import futures
import grpc
from pb.auth_pb2 import AuthResponse
from pb import auth_pb2_grpc
from settings import Settings

USER_DB = {
    "user1": "Qweasd123",
    "user2": "Rtyfgh456",
    "user3": "Uiojkl789",
}

class AuthService(
    auth_pb2_grpc.AuthServicer
):
    def Authentication(self, request, context):
        if not request.login or not request.password:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Login and password are required")

        if request.login in USER_DB and USER_DB[request.login] == request.password:
            return AuthResponse(can_login=True)

        return AuthResponse(can_login=False)

settings = Settings()

AUTH_SERVICE_HOST = settings.auth_service_host
AUTH_SERVICE_PORT = settings.auth_service_port

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServicer_to_server(
        AuthService(), server
    )
    server.add_insecure_port(f"{AUTH_SERVICE_HOST}:{AUTH_SERVICE_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()