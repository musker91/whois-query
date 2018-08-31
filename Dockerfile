FROM ubuntu

MAINTAINER Whois-Query API - Musker.Chao '<aery_mzxc9123@163.com>'

RUN apt update > /dev/null && apt -y install python3 python3-pip python3-dev git > /dev/null

WORKDIR /opt

ENV WHOIS_CONTAINER https://gitee.com/spdir/whois-query.git

RUN git clone $WHOIS_CONTAINER && \
    cd whois-query && python3 -m pip install -r requirements.txt && \
    chmod +x start.sh

EXPOSE 8080

CMD ["/opt/whois-query/start.sh"]
