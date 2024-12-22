FROM python:3.13

WORKDIR /root/app

COPY protobufs/ /root/protobufs/
COPY composition/ /root/app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --pyi_out=. --grpc_python_out=. ../protobufs/auth.proto
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --pyi_out=. --grpc_python_out=. ../protobufs/score.proto

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]