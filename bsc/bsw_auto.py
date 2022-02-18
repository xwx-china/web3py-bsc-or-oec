from bsc.bsw_utils import Bsw
from bsc.bsc_key import AdminKey,BswKey
from bsc.bsc_tokens import Token,Abi

'''
自动进行游戏脚本
'''
bsw = Bsw()
# 主钱包私钥
key = AdminKey.KEY.value

# 游戏钱包私钥
gameKey = BswKey.KEY19.value

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
print(adminBol)
if adminBol != bool(1):
    bsw.setApprovalForAll(key, nonce)
    nonce = nonce + 2

gameBol = bsw.isApprovedForAll(gameAccount.address)
print(gameBol)
if gameBol != bool(1):
    bsw.setApprovalForAll(gameKey, gameNonce)
    gameNonce = gameNonce + 2

'''
第一组游戏
'''
# 游戏数组
nftIds = [87853, 61600, 62326, 49394, 147716]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
gameNonce = gameNonce + 1

'''
第二组游戏
'''
# 游戏数组
nftIds = [128641, 128521, 46945, 49286, 104131]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
gameNonce = gameNonce + 1

'''
第三组游戏
'''
# 游戏数组
nftIds = [87712, 188911, 113288, 159897, 189698]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
gameNonce = gameNonce + 1

'''
第四组游戏
'''
# 游戏数组
nftIds = [45166, 87945, 48333, 179331, 181592]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
gameNonce = gameNonce + 1

'''
第五组游戏
'''
nftIds = [61454, 62136, 61708, 48283, 62226, 188948]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
gameNonce = gameNonce + 1

'''
第六组游戏
'''
nftIds = [167516, 43679, 181637, 59132, 61070, 181757, 160405]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 6, nftIds)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
gameNonce = gameNonce + 1

'''
第七组游戏
'''
nftIds = [197786, 48783, 200137, 167919, 200877, 182379]
# 发送nft
bsw.transferFromBsps(key, nonce, gameAccount.address, nftIds)
nonce = nonce + 1
# 获取钱包nft
players = bsw.array_user_players(gameAccount.address)
# 判断nft数量
while len(nftIds) != len(players):
    players = bsw.array_user_players(gameAccount.address)
# 开始游戏
tx = bsw.playGame(gameKey, gameNonce, 2, [197786, 48783, 200137])
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)

'''
获取收益 不挖提卖的注释掉这两行
'''
hvtx = bsw.harvest(gameKey, gameNonce)
gameNonce = gameNonce + 1

'''
最后一组游戏 养钱包
'''
bsw.playGame(gameKey, gameNonce, 0, 167919)
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 0, 200877)
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 0, 182379)
gameNonce = gameNonce + 1
bsw.web3Utils.get_receipt_tx(tx)
# 转移nft
bsw.transferFromBsps(gameKey, gameNonce, account.address, nftIds)
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


