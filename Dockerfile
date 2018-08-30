FROM ubuntu
MAINTAINER Whois-Query API - Musker.Chao '<aery_mzxc9123@163.com>'
RUN apt update && apt -y install python3 python3-pip python3-dev git
WORKDIR /opt
RUN git clone https://gitee.com/spdir/whois-query.git && \
    cd whois-query && python3 -m pip install -r requirements.txt && \
    chmod +x start.sh

EXPOSE 8080

CMD ["bash", "/opt/start.sh"]
