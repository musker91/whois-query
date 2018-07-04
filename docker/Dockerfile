FROM ubuntu
WORKDIR /opt
RUN apt update
RUN apt-get -y install git python3 python3-pip nginx
RUN git clone https://gitee.com/spdir/whois-query.git && cd whois-query && \
python3 -m pip install -r requirements.txt
RUN wget https://gitee.com/spdir/whois-query/raw/master/docker/tornado.conf -O /etc/supervisor/conf.d/tornado.conf
EXPOSE 8080
CMD ["/etc/init.d/supervisor","start"]
ENTRYPOINT ["/etc/init.d/supervisor","start"]
