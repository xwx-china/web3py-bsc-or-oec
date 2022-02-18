from skill_utils import Skill
from oec_key import AdminKey,SkillKey
from public.log_utils import Logger

import threading

import math

skill = Skill()

logger = Logger('skill.log').get_log()

def get_cbcs(address):
    '''
    获取角色
    '''
    cbcs = skill.cbcContract.functions.getCharactersOwnedBy(address).call()
    return cbcs

def get_cbw(address):
    '''
    获取武器
    '''
    cbw = skill.cbwContract.functions.tokenOfOwnerByIndex(address, 0).call()
    return cbw

def get_game_keys():
    '''
    获取游戏钱包
    '''
    keys = []
    for keyE in AdminKey:
        keys.append(keyE.value)
    for keyE in SkillKey:
        keys.append(keyE.value)
    return keys

def start():
    '''
    开始游戏
    '''
    logger.info('脚本开始')
    keys = get_game_keys()
    txs = []
    for key in keys:
        account = skill.web3Utils.get_account(key)
        logger.info('钱包地址:'+account.address)
        cbcs = get_cbcs(account.address)
        cbw = get_cbw(account.address)
        nonce = skill.web3Utils.get_nonce(account.address)
        for cbc in cbcs:
            point = skill.cbcContract.functions.getStaminaPoints(cbc).call()
            logger.info('角色:' + str(cbc) + ' 体力' + str(point))
            # 判断角色体力
            if point > 120:
                # 进攻次数
                cnt = str(math.floor(point/40))
                # 获取对战怪物
                targets = skill.gameContract.functions.getTargets(cbc, cbw).call()
                monsterPowers = []
                givetokens = []
                # 遍历怪物
                for target in targets:
                    # 获取怪物战斗力
                    monsterPower = skill.gameContract.functions.getMonsterPower(target).call()
                    # 获取怪物奖励
                    givetoken = skill.gameContract.functions.getTokenGainForFight(monsterPower, bool(1)).call()
                    monsterPowers.append(monsterPower)
                    givetokens.append(givetoken)
                # 获取最高战斗力怪物
                maxMonsterPower = max(monsterPowers)
                maxMonsterPowerIndex = monsterPowers.index(maxMonsterPower)
                # 获取最高奖励怪物
                givetoken = max(givetokens)
                maxGivetokenIndex = givetokens.index(givetoken)
                # 进攻角色
                cbcStr = str(cbc)
                # 进攻武器
                cbwStr = str(cbw)
                # 判断最高奖励怪物是不是最高战斗力怪物
                if maxGivetokenIndex == maxMonsterPowerIndex:
                    # 是的话直接攻击
                    tx = skill.play_game(key, nonce, cbcStr, cbwStr, str(maxGivetokenIndex), cnt)
                    txs.append(tx)
                    nonce = nonce + 1
                # 不是最高战斗力怪物攻击最高奖励
                else:
                    tx = skill.play_game(key, nonce, cbcStr, cbwStr, str(maxGivetokenIndex), cnt)
                    nonce = nonce + 1
                    txs.append(tx)
    for tx in txs:
        logger.info('进攻tx:' + str(tx))
    logger.info('脚本结束')
    threading.Timer(3600, start).start()


timer = threading.Timer(1, start).start()

