from random import random
from concurrent import futures
import grpc
from pb.score_pb2 import ScoreResponse
from pb import score_pb2_grpc
from settings import Settings


class ScoreService(
    score_pb2_grpc.ScoreServicer
):
    def Scoring(self, request, context):
        if not request.login:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Login is required")

        score = round(random(), 2)
        return ScoreResponse(score=score)


settings = Settings()

SCORE_SERVICE_HOST = settings.score_service_host
SCORE_SERVICE_PORT = settings.score_service_port

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    score_pb2_grpc.add_ScoreServicer_to_server(
        ScoreService(), server
    )
    server.add_insecure_port(f"{SCORE_SERVICE_HOST}:{SCORE_SERVICE_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()