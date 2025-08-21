FROM python:slim

RUN apt update -y && \
    apt upgrade -y && apt install socat -y

RUN useradd -m jailuser && \
    mkdir /app && \
    chown jailuser:jailuser /app

WORKDIR /app
COPY jail.py /app/
COPY secret /app/secret

RUN chmod +x /app/jail.py

USER jailuser

ENTRYPOINT ["socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:/usr/local/bin/python /app/jail.py"]
