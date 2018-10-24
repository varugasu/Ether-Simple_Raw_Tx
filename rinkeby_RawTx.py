from web3 import Web3, HTTPProvider

infuraApi = 'API'
account = 'SRC ACCOUNT'
key = 'PRIVATE KEY'
destinationAccount = 'DST ACCOUNT'


w3 = Web3(HTTPProvider(f"https://rinkeby.infura.io/v3/{infuraApi}"))

tx = {
    'to': destinationAccount,
    'value': Web3.toWei('1', 'ether'),
    'gas': 210000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': w3.eth.getTransactionCount(account),
    'chainId': 4
}

signed = w3.eth.account.signTransaction(tx, key)
w3.eth.sendRawTransaction(signed.rawTransaction)
