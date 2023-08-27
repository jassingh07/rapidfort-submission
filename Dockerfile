FROM ubuntu:jammy

RUN apt-get update && apt-get -y install pip virtualenv python3.11 libpython3.11 python3.11-distutils file

WORKDIR /app

ADD requirements.txt .
COPY file_management_app/ /app/file_management_app

RUN virtualenv --python python3.11 /app/venv
RUN /app/venv/bin/pip install -r /app/requirements.txt

EXPOSE 5001

CMD ["/app/venv/bin/python3.11", "file_management_app/main.py"]
