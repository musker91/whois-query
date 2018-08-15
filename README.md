# whois-query
> Author QQ: 1152490990

#### 项目介绍
 特点: 可以通过接口直接匹配域名合法性，同时可以匹配出传入域名字串的一级域名
- API接口,返回JSON格式数据(支持POST,GET方式)

- 网关查询接口(支持POST,GET方式)



#### 测试接口
- page: `http://whois.tt80.xin/`
- api: `http://whois.tt80.xin/whoisapi?domain=`
 - 返回状态： 
     1. code：-1 没有查询到指定域名
     2. code: 1  返回指定域名信息 

#### 运行服务端
- 可以选择使用supervisor做进程管理,启动多个服务端,使用nginx做代理
- 可以直接运行main.py文件，python版本3.5+
  1) 安装依赖包
   `python3 -m pip install -r requirements.txt` 
  2) 运行服务端程序
    `python3 main.py`
