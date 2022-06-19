#Use the following python code to access the Ethereum node and output the version information and account information of the Ethereum node.
#https://www.programmersought.com/article/302715830/

import requests, time, json
from pprint import pprint

def rpc(method,params=[]):
  print('{0} => '.format(method))
  data = json.dumps({
    'jsonrpc':'2.0',
    'method': method,
    'params': params,
    'id': int(time.time() * 1000)
  })
  rsp = requests.post('http://localhost:7545',data=data)
  pprint(rsp.json())

rpc('web3_clientVersion')
rpc('eth_accounts')