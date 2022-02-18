from oec.isl_utils import Isl
from oec.oec_key import AdminKey

from datetime import datetime,timedelta
import time

isl = Isl()
# 获取key
key = AdminKey.KEY.value
# 获取账号
account = isl.web3Utils.get_account(key)
# 获取上一次进行游戏时间
tm = isl.gameHarvestContract.functions.islLastTime(account.address).call()
# 下一次进行游戏时间
timeObj = datetime.fromtimestamp(tm) + timedelta(hours=3)
# 转换成时间戳
timeMk = int(timeObj.timestamp())
# 获取当前时间
timeMkNow = int(time.time())
print(timeMk)
print(timeMkNow)
# 判断当前时间大于游戏时间开始游戏
if timeMkNow > timeMk:
    # 获取key
    key = AdminKey.KEY.value
    # 获取账号
    account = isl.web3Utils.get_account(key)
    # 获取交易次数
    nonce = isl.web3Utils.get_nonce(account.address)
    # 发送交易
    # tx = isl.play_game_harvest(key, nonce)
    # print(tx)
