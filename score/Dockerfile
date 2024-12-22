FROM python

WORKDIR /root/app

COPY protobufs/ /root/protobufs/
COPY score/ /root/app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --pyi_out=. --grpc_python_out=. ../protobufs/score.proto

EXPOSE 50052
ENTRYPOINT [ "python", "main.py" ]