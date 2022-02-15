from bsc.bsw_utils import Bsw
from bsc.bsc_key import AdminKey,BswKey
from bsc.bsc_tokens import Token,Abi

import time

'''
自动进行游戏脚本
'''
bsw = Bsw()
key = AdminKey.KEY.value

gameKey = BswKey.KEY6.value

account = bsw.web3Utils.get_account(key)

gameAccount = bsw.web3Utils.get_account(gameKey)

# 主钱包交易数量
nonce = bsw.web3Utils.get_nonce(account.address)

# 游戏钱包交易数量
gameNonce = bsw.web3Utils.get_nonce(gameAccount.address)

'''
第一组游戏
'''
nftIds = [128521,48333,61070,48783,62136]
# for nftId in nftIds:
#     bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
#     nonce = nonce + 1
players = bsw.array_user_players(gameAccount.address)
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
gameNonce = gameNonce + 1
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

'''
第二组游戏
'''
nftIds = [113288,48283,49286,49394,46945,104131]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1
players = bsw.array_user_players(gameAccount.address)
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
gameNonce = gameNonce + 1
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

'''
第三组游戏
'''
nftIds = [87712,43679,45166,59132,147716]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1
players = bsw.array_user_players(gameAccount.address)
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
gameNonce = gameNonce + 1
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

'''
第三组游戏
'''
nftIds = [61708,62226,61454,128641,167919]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1
players = bsw.array_user_players(gameAccount.address)
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
gameNonce = gameNonce + 1
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

'''
获取收益 不挖提卖的注释掉这两行
'''
hvtx = bsw.harvest(gameKey, gameNonce)
gameNonce = gameNonce + 1

'''
倒数第二组游戏 养钱包
'''
nftIds = [87853,62326]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1
players = bsw.array_user_players(gameAccount.address)
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
tx = bsw.playGame(gameKey, gameNonce, 3, nftIds)
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
gameNonce = gameNonce + 1
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

'''
最后一组游戏 养钱包
'''
nftIds = [87945,61600]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1
players = bsw.array_user_players(gameAccount.address)
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
tx = bsw.playGame(gameKey, gameNonce, 3, nftIds)
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
gameNonce = gameNonce + 1
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

'''
获取游戏钱包代币数量
'''
bsw.web3Utils.get_receipt_tx(hvtx)
bswContract = bsw.web3Utils.w3.eth.contract(address=bsw.web3Utils.w3.toChecksumAddress(Token.BSW.value), abi=Abi.BSW.value)
bswValue = bsw.web3Utils.get_contract_balance(gameAccount.address, bswContract)
print('bsw数量:'+str(bswValue))
wbnbContract = bsw.web3Utils.w3.eth.contract(address=bsw.web3Utils.w3.toChecksumAddress(Token.WBNB.value), abi=Abi.WBNB.value)
wbnbValue = bsw.web3Utils.get_contract_balance(gameAccount.address, wbnbContract)
print('wbnb数量:'+str(wbnbValue))
bfgContract = bsw.web3Utils.w3.eth.contract(address=bsw.web3Utils.w3.toChecksumAddress(Token.BFG.value), abi=Abi.BFG.value)
bfgValue = bsw.web3Utils.get_contract_balance(gameAccount.address, bfgContract)
print('bfg数量:'+str(bfgValue))
'''
发送代币到主钱包
'''
if bswValue > 0:
    bsw.web3Utils.transfer_erc20(gameKey, gameNonce, bswContract, account.address, bswValue)
    gameNonce = gameNonce + 1
if wbnbValue > 0:
    bsw.web3Utils.transfer_erc20(gameKey, gameNonce, wbnbContract, account.address, wbnbValue)
    gameNonce = gameNonce + 1
if bfgValue > 0:
    bsw.web3Utils.transfer_erc20(gameKey, gameNonce, bfgContract, account.address, bfgValue)
    gameNonce = gameNonce + 1


