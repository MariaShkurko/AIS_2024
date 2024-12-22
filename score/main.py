from random import random
from concurrent import futures
import grpc
from score_pb2 import ScoreResponse
import score_pb2_grpc
from settings import settings


class ScoreService(
    score_pb2_grpc.ScoreServicer
):
    def Scoring(self, request, context):
        if not request.login:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Login is required")

        score = round(random(), 2)
        return ScoreResponse(score=score)


SCORE_SERVICE_URL = settings.score_service_url

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    score_pb2_grpc.add_ScoreServicer_to_server(
        ScoreService(), server
    )
    server.add_insecure_port(SCORE_SERVICE_URL)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()