import os
import requests
import time
import json

NETWORK = 'rinkeby'
ADDRESS = 'Your Address'
API_KEY = 'Your API Key'

if NETWORK == 'mainnet':
    r = 'https://api.etherscan.io/api'
    txStatus = 'https://etherscan.io/tx/'
if NETWORK == 'rinkeby':
    r = 'https://api-rinkeby.etherscan.io/api'
    txStatus = 'https://rinkeby.etherscan.io/tx/'

def Transaction():

    def getTransaction():
        data = {'module': 'account', 'action': 'txlist', 'address': ADDRESS, 'sort': 'desc', 'apikey': API_KEY}
        response = requests.get(r, params=data).json()
        return response['result'][0]['hash']

    oldHash = str(getTransaction())

    def checkTransaction():
        time.sleep(10)
        data = {'module': 'account', 'action': 'txlist', 'address': ADDRESS, 'sort': 'desc', 'apikey': API_KEY}
        response = requests.get(r, params=data).json()
        newHash = response['result'][0]['hash']

        if oldHash == newHash:
            print("No new Transaction!")
            checkTransaction()
        else:
            print("New Transaction!")
            transactionStatus = "New Transaction! Check it - " + txStatus + newHash
            print(transactionStatus)
            Transaction()

    checkTransaction()

Transaction()