#我是a，我下面有n个账户，每个账户总资产都不一样，每个账户达到的预警线也不一样，到达预警需要一个通知，
#单票限制，因为每个账户总资产不一样，所以单票持仓一个预警可以根据资产总值来设置一个比例



import logging

import shipane_sdk

logging.basicConfig(level=logging.DEBUG)

client = shipane_sdk.Client(host='localhost', port=8888, key='')
account_info = client.get_account('account:227500000140')
cash = client.get_positions('account:227500000140')
account_cash ={}
#cash={}
account_cash['positions']='Empty DataFrame'
#account_cash['Columns']='[��ϸ, ֤ȯ����, ֤ȯ����, ��Ʊ���, �������, ��������, ӯ��, �ɱ���, ӯ����(%), �м�, ��ֵ, �г�����, �����г�, �ɶ��ʻ�, ʵ������, ��Ѷ, ���붳��, ��������]'
account_cash['Index']=''
account_cash['sub_accounts']=''
print(cash['sub_accounts'])
print(cash['sub_accounts'])