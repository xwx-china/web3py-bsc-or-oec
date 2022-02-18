from isl_utils import Isl
from oec_key import AdminKey
from public.log_utils import Logger

import threading

isl = Isl()

logger = Logger('isl.log').get_log()

def start():
    '''
    开始游戏
    '''
    logger.info('脚本开始')
    try:
        # 获取key
        key = AdminKey.KEY.value
        # 获取账号
        account = isl.web3Utils.get_account(key)
        # 获取上一次进行游戏时间
        nonce = isl.web3Utils.get_nonce(account.address)
        # 发送交易
        tx = isl.play_game_harvest(key, nonce)
        logger.info('收获tx:' + str(tx))
        logger.info('脚本结束1小时后继续执行')
        threading.Timer(3600, start).start()
    except Exception as e:
        logger.error("脚本异常")
        logger.warning("5分钟后重新调用脚本")
        threading.Timer(300, start).start()

timer = threading.Timer(3600, start).start()