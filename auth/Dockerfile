FROM python

WORKDIR /root/app

COPY protobufs/ /root/protobufs/
COPY auth/ /root/app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --pyi_out=. --grpc_python_out=. ../protobufs/auth.proto

EXPOSE 50051
ENTRYPOINT [ "python", "main.py" ]