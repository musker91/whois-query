# -*- coding: utf-8 -*-
# File: whoisUtils.py
# Author: Musker
# Description: Get whois information

"""
# Status code
#  1 域名信息获取成功
#  0 域名不存在
# -1 暂不支持此域名查询
# -2 域名输入有误
# -3 域名查询失败
# -4 服务器异常
"""

import socket
import time
import re
import logging
import json
import os
from tld import get_tld

now_time = lambda: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class QueryDoaminName(object):
	"""
	获取域名详细信息，并处理域名后回去后的信息
	"""

	def __init__(self, domain_name, domain_suffix):
		self.domain_name = domain_name
		self.domain_suffix = domain_suffix
		self.domain_info = None
		self.whois_servers_list = self.__get_whois_list()

	def __get_whois_list(self):
		"""
		获取whois服务器列表
		:return list:
		"""
		json_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "whois.servers.json")
		with open(json_file_path, "r") as f:
			json_data = json.loads(f.read())
			whois_list = json_data.get(self.domain_suffix, [])
			return whois_list

	def __match_info(self):
		"""
		匹配获取到的信息是否是正确的
		:return bool, bool:
		"""
		match_status = re.search("Domain Name: " + self.domain_name.upper(), self.domain_info)
		if match_status:
			return True
		return False

	def __get_domain_info(self):
		"""
		获取域名的信息
		:return bool, str: 获取状态，状态码
		"""
		servers_list = self.whois_servers_list
		query_status = False
		code = "-3"
		for url in servers_list:
			sk = socket.socket()
			try:
				sk.connect((url, 43))	# 连接whois服务器
			except Exception as e:	# 连接whois服务器失败
				code = "-3"
				logging.error("[%s] Connect [%s] error [%s], suffix [%s]"
							  % (now_time(), url, e, self.domain_suffix))
			else:	# 连接服务器成功
				# 开始查询
				sk.send(str(self.domain_name).encode("utf-8"))
				sk.send("\r\n".encode("utf-8"))
				recv_data = ""
				while True:
					recv = sk.recv(1024)
					if len(recv) == 0:
						break
					recv_data += recv.decode("utf-8")
				self.domain_info = recv_data
				# 获取服务器返回的信息，判断是否为正确信息
				if not self.__match_info():
					code = "0"
				else:
					code, query_status = "1", True
			finally:
				sk.close()
				servers_list.remove(url)	# 删除whois服务器列表中的一个服务器地址
				if query_status:	# 如果查询到了
					return True, code
				elif len(servers_list) == 0 and self.domain_info:	# 返回信息，但域名不存在
					return False, code
				elif len(servers_list) == 0:	# 没有查询到任何信息
					return False, code

	def strToDict(self):
		"""
		将获取到的域名信息字符串转换为字典类型
		:return dict:
		"""
		def match_str(re_str):
			match_str = None
			matchObj = re.search(re_str, self.domain_info)
			if matchObj:
				match_str_all = matchObj.group(0)
				match_str = match_str_all.split(": ")[1].strip()
			return match_str

		def match_array(re_str):
			match_str = None
			matchArray = re.findall(re_str, self.domain_info)
			if matchArray:
				match_str = []
				for i in matchArray:
					match_str.append(i.split(": ")[1].strip())
			return match_str

		domain_info_dict = {
				"DomainName": match_str("Domain Name: .+"),
				"RegistryDomainID": match_str("Registry Domain ID: .+"),
				"RegistrarWhoisServer": match_str("Registrar WHOIS Server: .+"),
				"RegistrarUrl": match_str("Registrar URL: .+"),
				"UpdatedDate": match_str("Updated Date: .+"),
				"CreationDate": match_str("Creation Date: .+"),
				"RegistryExpiryDate": match_str("Registry Expiry Date: .+"),
				"Registrar": match_str("Registrar: .+"),
				"RegistrarIanaId": match_str("Registrar IANA ID: .+"),
				"RegistrarAbuseContactEmail": match_str("Registrar Abuse Contact Email: .+"),
				"RegistrarAbuseContactPhone": match_str("Registrar Abuse Contact Phone: .+"),
				"DomainStatus": match_array("Domain Status: .+"),
				"NameServer": match_array("Name Server: .+")
			}
		return domain_info_dict

	def query(self):
		"""
		域名查询主入口
		:param domain_name: 需要查询的域名
		:return (bool, str, str): (查询状态, 返回状态码, 返回获取到的域名信息字符串)
		"""
		if len(self.whois_servers_list) == 0:
			return False, "-1", None
		getInfoStatus, getInfoCode = self.__get_domain_info()
		if not getInfoStatus:
			return False, getInfoCode, None
		return True, getInfoCode, self.domain_info

def parserDomainName(domain_name):
	"""
	解析域名
	:param domain_name:
	:return (bool, str, (str, str)):  (bool, statusCode, (tld[域名后缀], fld[完整域名]))
	"""
	try:
		res = get_tld(domain_name, as_object=True,fix_protocol=True)
	except Exception as e:
		logging.error("[%s]: parser [%s] domain name has error -> [%s]" %(now_time(), domain_name, e))
		return False, "-2", (None, None)
	return True, None, (res.fld, res.tld)

def getDoaminWhois(domain_namem, tp):
	"""
	获取域名具体信息
	:param domain_namem: 域名
	:param tp: 需要返回data的类型[string->s, dict->d]
	:return bool, str, [str,dict]: 返回状态、状态码和数据
	"""
	# 解析域名
	parserStatus, code, data = parserDomainName(domain_namem)
	# 解析失败
	if not parserStatus:
		return False, code, None
	# 查询域名信息
	queryObj = QueryDoaminName(data[0], data[1])
	queryStatus, code, data = queryObj.query()
	# 如果查询失败
	if not queryStatus:
		return False, code, None
	# Api查询数据转换
	if tp == "d":
		data = queryObj.strToDict()
	return True, code, data
