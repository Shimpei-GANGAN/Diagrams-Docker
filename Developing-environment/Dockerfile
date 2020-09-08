FROM python:3.8.2

ENV ARCH amd64
ENV GOVERSION 1.14.2

RUN set -x \
    && cd /tmp \
    && wget https://dl.google.com/go/go$GOVERSION.linux-$ARCH.tar.gz \
    && tar -C /usr/local -xzf go$GOVERSION.linux-$ARCH.tar.gz \
    && rm /tmp/go$GOVERSION.linux-$ARCH.tar.gz

ENV PATH $PATH:/usr/local/go/bin
ENV GOPATH $HOME/work

# RUN go get github.com/mingrammer/round
