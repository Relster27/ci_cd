FROM debian:12

RUN apt-get update && \
    apt-get install -y gcc socat && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY vuln.c .

RUN gcc vuln.c -o vuln -no-pie

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:./vuln
