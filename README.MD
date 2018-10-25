# Simple Raw Transaction in Web3.py

## Sending ether in Rinkeby Test Network through Infura API

### Requirements:

- web3.py 4.7.2
- API Key from [infura.io](https://infura.io)
- Source account and its private key
- Destination account

```
infuraApi = 'API'
account = 'SRC ACCOUNT'
key = 'PRIVATE KEY'
destinationAccount = 'DST ACCOUNT'
```

#### Transaction:

```python
tx = {
    'to': destinationAccount,
    'value': Web3.toWei('1', 'ether'),
    'gas': 210000,
    'gasPrice': w3.eth.gasPrice,
    'nonce': w3.eth.getTransactionCount(account),
    'chainId': 4 # Rinkeby Test Network
}
```

#### Signing the transaction with source account's private key:

```python
signed = w3.eth.account.signTransaction(tx, key)
```
