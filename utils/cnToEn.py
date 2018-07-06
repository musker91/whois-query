# -*- coding: utf-8 -*-

def cnToEN(data):
  """
  将中文转换为英文
  :param data: 源数据
  :return: dict
  """
  new_dict = {}
  new_dict['domain'] = data.get('域名')
  new_dict['registrar'] = data.get('注册商')
  new_dict['contacts'] = data.get('联系人')
  new_dict['contactsEmail'] = data.get('联系邮箱')
  new_dict['contactsPhone'] = data.get('联系电话')
  new_dict['creationTime'] = data.get('创建时间')
  new_dict['expiryTime'] = data.get('过期时间')
  new_dict['domainnNameServer'] = data.get('域名服务器')
  new_dict['DNS'] = data.get('DNS')
  new_dict['status'] = data.get('状态')
  new_dict['code'] = data.get('code')
  return new_dict


