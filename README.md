#### 项目介绍
特点: 可以通过接口直接匹配域名合法性，同时可以匹配出传入域名字串的一级域名
1. API接口,返回JSON格式数据(支持POST,GET方式)
2. 网关查询接口(支持POST,GET方式)
3. 使用内存缓存保存查询到的域名信息,加速查询速度,默认设置保存3天,可以在启动时指定`cache`参数来指定缓存的天数


#### 测试接口
1. page: [http://whois.tt80.xin](http://whois.tt80.xin/?domain=tt80.xin)
2. api: [http://whois.tt80.xin/whoisapi?domain=](http://whois.tt80.xin/whoisapi?domain=tt80.xin)
  ```
  返回状态码:
     1) code: -1 没有查询到指定域名
     2) code: 1  返回指定域名信息
  ```
#### 运行服务端
1. 直接运行main.py文件，python版本3.5+
2. 使用supervisor做进程管理,启动多个服务端,使用nginx做代理
```
1)安装依赖包
  python3 -m pip install -r requirements.txt
2) 运行服务端程序
    python3 main.py
    运行时可以指定的参数
      1. `cache`: 指定域名缓存的天数
      2. `port`: 指定程序运行的端口
```
3. 运行Docker容器
```
docker run -itd --name=whois-query -p 8080:8080 registry.cn-beijing.aliyuncs.com/musker/whois-query
```