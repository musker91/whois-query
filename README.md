# Whois-query

---

### 项目介绍

免费Whois查询接口，完全开放

1. API接口,返回JSON格式数据(支持POST,GET方式)
2. 网页查询接口(支持POST,GET方式)

#### 测试接口

1. 页面: [http://whois.tt80.xin](http://whois.tt80.xin)

2. Api: [http://whois.tt80.xin/whoisapi?domain_name=](http://whois.tt80.xin/whoisapi?domain_name=tt80.xin)

```json
{
    "code": "1",
    "data": {
        "DomainName": "TT80.XIN ",
        "RegistryDomainID": "D417300000001380250-ACRS ",
        "RegistrarWhoisServer": null,
        "RegistrarUrl": "www.net.cn ",
        "UpdatedDate": "2018-06-10T12:23:28Z ",
        "CreationDate": "2017-06-09T04:28:11Z ",
        "RegistryExpiryDate": "2019-06-09T04:28:11Z ",
        "Registrar": "Alibaba Cloud Computing Ltd. d/b/a HiChina (www.net.cn) ",
        "RegistrarIanaId": "1599 ",
        "RegistrarAbuseContactEmail": null,
        "RegistrarAbuseContactPhone": null,
        "DomainStatus": [
            "ok https://icann.org/epp#ok "
        ],
        "NameServer": [
            "DNS23.HICHINA.COM ",
            "DNS24.HICHINA.COM "
        ]
    }
}
```

  ```txt
  返回状态码:
    1)  1  域名信息获取成功
    2)  0  域名不存在
    3) -1  暂不支持此域名查询
    4) -2  域名输入有误
    5) -3  域名查询失败
    6) -4  服务器异常
  ```

#### 运行服务端

**一、直接运行主程序文件启动服务**

直接运行main.py文件，需要python 3.5+版本

1、 安装依赖包

  ```txt
    python3 -m pip install -r requirements.txt
  ```

2、运行服务端程序

  ```txt
    python3 main.py
    运行时可以指定的参数
    `port`: 指定程序运行的端口
  ```

**二、使用Docker运行服务端**

```txt
docker run -d --name=whois-query -p 8080:8080 registry.cn-beijing.aliyuncs.com/musker/whois-query
```
