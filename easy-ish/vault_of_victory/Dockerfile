FROM ubuntu:latest

RUN apt-get update && apt-get install -y socat

# create ctf-user
RUN groupadd -r ctf && useradd -r -g ctf ctf

#add chall items
WORKDIR /home/ctf
COPY vault /home/ctf/vault
RUN chmod +x /home/ctf/vault
EXPOSE 1234

RUN mkdir /home/ctf/win
COPY blanka.txt /home/ctf/win/blanka.txt
COPY chunli.txt /home/ctf/win/chunli.txt
COPY guile.txt /home/ctf/win/guile.txt
COPY ryu.txt /home/ctf/win/ryu.txt

# set some proper permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/vault
RUN chmod 440 /home/ctf/win/blanka.txt
RUN chmod 440 /home/ctf/win/chunli.txt
RUN chmod 440 /home/ctf/win/guile.txt
RUN chmod 440 /home/ctf/win/ryu.txt

USER ctf
CMD ["socat", "TCP-LISTEN:1234,reuseaddr,fork", "EXEC:/home/ctf/vault"]