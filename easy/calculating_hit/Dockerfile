FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat

# create ctf-user
RUN groupadd -r ctf && useradd -r -g ctf ctf

#add chall items
WORKDIR /home/ctf
RUN chown -R root:ctf /home/ctf
COPY calc /home/ctf/calc
RUN chmod +x /home/ctf/calc
EXPOSE 1235

COPY flag.txt /home/ctf/flag.txt
COPY art.txt /home/ctf/art.txt

USER ctf
CMD ["socat", "TCP-LISTEN:1235,reuseaddr,fork", "EXEC:/home/ctf/calc"]