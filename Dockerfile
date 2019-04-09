FROM ubuntu

LABEL maintainer="Musker.Chao <aery_mzc9123@163.com>"

RUN apt-get update && \
    apt-get -y install python3 python3-pip python3-dev git && \
    apt-get clean 

WORKDIR /opt

ENV WHOIS_CONTAINER https://gitee.com/spdir/whois-query.git

RUN git clone $WHOIS_CONTAINER && \
    cd whois-query && \
    python3 -m pip install -r requirements.txt && \
    chmod +x start.sh

EXPOSE 8080

CMD ["/opt/whois-query/start.sh"]
