from bsc.bsw_utils import Bsw
from bsc.bsc_key import AdminKey,BswKey
import time

'''
自动进行游戏脚本
'''
bsw = Bsw()
key = AdminKey.KEY.value

gameKey = BswKey.KEY26.value

account = bsw.web3Utils.get_account(key)

gameAccount = bsw.web3Utils.get_account(gameKey)

# 主钱包交易数量
nonce = bsw.web3Utils.get_nonce(account.address)

# 游戏钱包交易数量
gameNonce = bsw.web3Utils.get_nonce(gameAccount.address)

'''
第一组游戏
'''
nftIds = [87945,45166,87712,46945,87853,48283]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1

bsw.playGame(gameKey, gameNonce, 3, [87945,45166])
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 3, [87712,46945])
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 3, [87853,48283])
gameNonce = gameNonce + 1

nftIds = [87945,45166,87712,46945,87853,48283]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1
'''
第二组游戏
'''
nftIds = [128641,59132,104131,61600,48783,49286]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1

bsw.playGame(gameKey, gameNonce, 3, [128641,59132,104131])
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 3, [61600,48783,49286])
gameNonce = gameNonce + 1

nftIds = [128641,59132,104131,61600,48783,49286]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1
'''
第三组游戏
'''
nftIds = [48333,49394,43679,62326,62226,61708]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1

bsw.playGame(gameKey, gameNonce, 3, [48333,49394,43679])
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 3, [62326,62226,61708])
gameNonce = gameNonce + 1

nftIds = [48333,49394,43679,62326,62226,61708]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1
'''
获取收益
'''
bsw.harvest(gameKey, gameNonce)
gameNonce = gameNonce + 1
'''
最后一组游戏 养钱包
'''
nftIds = [61070,62136,61454,128521,167919,113288]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(key, nonce, bsw.bspContract, gameAccount.address, nftId)
    nonce = nonce + 1

bsw.playGame(gameKey, gameNonce, 3, [61070,62136,61454])
gameNonce = gameNonce + 1
bsw.playGame(gameKey, gameNonce, 2, [128521,167919,113288])
gameNonce = gameNonce + 1

nftIds = [61070,62136,61454,128521,167919,113288]
for nftId in nftIds:
    bsw.web3Utils.transfer_erc721(gameKey, gameNonce, bsw.bspContract, account.address, nftId)
    gameNonce = gameNonce + 1

