from public.web3_utils import Web3Utils
from oec.oec_key import AdminKey


web3Utils = Web3Utils("https://exchainrpc.okex.org/", 0.1, 66)

key = AdminKey.KEY.value

account = web3Utils.get_account(key)

nonce = web3Utils.get_nonce(account.address)

# tx = web3Utils.mandatory_sign_send(key, nonce, 5210203, '0xa802b35a7f265ea79a2cb3ebe8629098ec4bcefb', '0xeca3bfe70000000000000000000000004A3654EE1E8F21D4F57f7eB68CA56C2c82909198')
# print(tx)
