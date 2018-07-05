FROM ubuntu
RUN apt update
RUN apt-get -y install git wget supervisor
WORKDIR /opt
RUN git clone https://gitee.com/spdir/whois-query.git && cd whois-query && \
python3.6 -m pip install -r requirements.txt && python -m pip install supervisor
RUN wget https://gitee.com/spdir/whois-query/raw/master/docker/tornado.conf -O /etc/supervisor/conf.d/tornado.conf
EXPOSE 8080
ENTRYPOINT ["/usr/bin/supervisord" , "-c" , "/etc/supervisord.conf"]
CMD []
