from bsc.bsw_utils import Bsw
from bsc.bsc_key import AdminKey,BswKey
from bsc.bsc_tokens import Token,Abi

import time

'''
自动进行游戏脚本
'''
bsw = Bsw()
# 主钱包私钥
key = AdminKey.KEY.value

# 游戏钱包私钥
gameKey = BswKey.KEY6.value

# 主钱包
account = bsw.web3Utils.get_account(key)

# 游戏钱包
gameAccount = bsw.web3Utils.get_account(gameKey)

# 主钱包交易数量
nonce = bsw.web3Utils.get_nonce(account.address)

# 游戏钱包交易数量
gameNonce = bsw.web3Utils.get_nonce(gameAccount.address)

'''
查看授权
'''
adminBol = bsw.isApprovedForAll(account.address)
if adminBol:
    bsw.setApprovalForAll(key, nonce)
    nonce = nonce + 1

gameBol = bsw.isApprovedForAll(gameAccount.address)
if gameBol:
    bsw.setApprovalForAll(gameKey, gameNonce)
    nonce = gameNonce + 1

'''
第一组游戏
'''
# 游戏数组
nftIds1 = [87712,87853,188911,179331]
nftIds2 = [87945,128641,159897,59132]
nftIdsAll = nftIds1 + nftIds2
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIdsAll)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIdsAll) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
bsw.playGame(gameKey, gameNonce, 6, nftIds1)
gameNonce = gameNonce + 1
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds2)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIdsAll)
gameNonce = gameNonce + 1

'''
第二组游戏
'''
# 游戏数组
nftIds1 = [43679,49394,48283,49286,46945,188948]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds1)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIdsAll) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds1)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds1)
gameNonce = gameNonce + 1

'''
第三组游戏
'''
# 游戏数组
nftIds1 = [62326,61708,62226,61454,104131,113288]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds1)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIdsAll) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds1)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds1)
gameNonce = gameNonce + 1

'''
第三组游戏
'''
# 游戏数组
nftIds1 = [189698,48333,48783,61600,160405,147716,167516]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds1)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIdsAll) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds1)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds1)
gameNonce = gameNonce + 1

'''
第四组游戏
'''
# 游戏数组
nftIds1 = [128521,181637,62136,61070,45166]
nftIds2 = [167919]
nftIds3 = [182379]
nftIdsAll = nftIds1 + nftIds2 + nftIds3
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIdsAll)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIdsAll) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds1)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
# 转移nft
# bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds1)
# gameNonce = gameNonce + 1

'''
获取收益 不挖提卖的注释掉这两行
'''
hvtx = bsw.harvest(gameKey, gameNonce)
gameNonce = gameNonce + 1

'''
最后一组游戏 养钱包
'''
bsw.playGame(gameKey, gameNonce, 0, nftIds2)
gameNonce = gameNonce + 1
tx = bsw.playGame(gameKey, gameNonce, 0, nftIds3)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
print(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIdsAll)
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


