import sys
sys.path.append("..")

import json

from public.web3_utils import Web3Utils

class Isl:
    '''ISL聚合器工具类

    本类提供ISL游戏通用方法
    本类提供ISL聚合器交易质押等方法

    Attributes:
        web3Utils(Web3Utils): Web3Utils对象

    '''
    pass

    web3Utils = Web3Utils("https://exchainrpc.okex.org/", 0.1, 66)

    # ISL游戏收获合约未开源
    gameHarvestAddress = web3Utils.w3.toChecksumAddress("0x10dbbc7e42ac461fbe8f228cf00f4bc432b4d9c3")

    # ISL游戏掠夺合约未开源
    gamePlunderAddress = web3Utils.w3.toChecksumAddress("0xa802b35a7f265ea79a2cb3ebe8629098ec4bcefb")

    gameHarvestAbi = json.loadsabi = ('[{"inputs":[{"internalType":"address","name":"_islandMaster","type":"address"},{"internalType":"address","name":"_islandMasterFactory","type":"address"},{"internalType":"address","name":"_islandFarm","type":"address"},{"internalType":"address","name":"_island","type":"address"},{"internalType":"address","name":"_islandProps","type":"address"},{"internalType":"address","name":"_islandStatue","type":"address"},{"internalType":"address","name":"_islandOther","type":"address"},{"internalType":"address","name":"_destroyAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[{"internalType":"address","name":"_addMinter","type":"address"}],"name":"addMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"baseRewardTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_delMinter","type":"address"}],"name":"delMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"gemLastTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_typeOf","type":"uint256"},{"internalType":"address","name":"_user","type":"address"}],"name":"getAllReward","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getGemProdBonus","outputs":[{"internalType":"uint256[22]","name":"","type":"uint256[22]"},{"internalType":"uint256[3]","name":"","type":"uint256[3]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getMinter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMinterLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getStoreProdBonus","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getTreeProdBonus","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserLastTime","outputs":[{"internalType":"uint256[4]","name":"","type":"uint256[4]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"initUserTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"innerDepositResource","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_attack","type":"address"},{"internalType":"address","name":"_defender","type":"address"},{"internalType":"uint256","name":"_rate","type":"uint256"}],"name":"innerWithdrawResource","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"islLastTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"lastDefTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"minDepositTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_islandMaster","type":"address"},{"internalType":"address","name":"_islandFarm","type":"address"},{"internalType":"address","name":"_island","type":"address"},{"internalType":"address","name":"_islandProps","type":"address"},{"internalType":"address","name":"_islandStatue","type":"address"},{"internalType":"address","name":"_islandOther","type":"address"},{"internalType":"address","name":"_destroyAddress","type":"address"}],"name":"setAddr","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"stoneLastTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"timberLastTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_typeOf","type":"uint256"}],"name":"withdrawResource","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

    gamePlunderAbi = json.loadsabi = ('[{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"addBlackList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_addMinter","type":"address"}],"name":"addMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_time","type":"uint256"}],"name":"addUserDefTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"attackUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_islandShip","type":"address"},{"internalType":"address","name":"_islandMaster","type":"address"},{"internalType":"address","name":"_islanMasterdFactory","type":"address"},{"internalType":"address","name":"_islandComputerOther","type":"address"},{"internalType":"address","name":"_islandMasterReward","type":"address"},{"internalType":"address","name":"_islandProps","type":"address"},{"internalType":"address","name":"_islandFarm","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"islAmount","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"exp","type":"uint256"},{"indexed":true,"internalType":"address","name":"defender","type":"address"},{"indexed":false,"internalType":"address","name":"attacker","type":"address"},{"indexed":false,"internalType":"uint256","name":"cap","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"def","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"wood","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"stone","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"gemId","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"gemCount","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"propId1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"propCount1","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"propId2","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"propCount2","type":"uint256"}],"name":"AttackUser","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"_propId","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"_propNum","type":"uint256"}],"name":"AttackUserBonus","type":"event"},{"inputs":[{"internalType":"address","name":"_delMinter","type":"address"}],"name":"delMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_exp","type":"uint256"},{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_cap","type":"uint256"},{"internalType":"uint256","name":"_def","type":"uint256"},{"internalType":"uint256[5]","name":"_propIds","type":"uint256[5]"},{"internalType":"uint256[5]","name":"_counts","type":"uint256[5]"}],"name":"emitAttackUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"removeBlackList","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_islandShip","type":"address"},{"internalType":"address","name":"_islandMaster","type":"address"},{"internalType":"address","name":"_islanMasterdFactory","type":"address"},{"internalType":"address","name":"_islandComputerOther","type":"address"},{"internalType":"address","name":"_islandMasterReward","type":"address"},{"internalType":"address","name":"_islandProps","type":"address"},{"internalType":"address","name":"_islandFarm","type":"address"}],"name":"setAddr","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_baseProp","type":"uint256"},{"internalType":"uint256","name":"_baseConsu","type":"uint256"},{"internalType":"uint256","name":"_startTime","type":"uint256"}],"name":"setBaseParam","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_fightTime","type":"uint256"},{"internalType":"uint256","name":"_baseDefTime","type":"uint256"},{"internalType":"uint256","name":"_maxCool","type":"uint256"},{"internalType":"uint256","name":"_maxBonus","type":"uint256"},{"internalType":"uint256","name":"_maxGap","type":"uint256"}],"name":"setBaseSetting","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"_levels","type":"uint256[]"},{"internalType":"uint256[]","name":"_exps","type":"uint256[]"}],"name":"setLevelToFightExp","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"setPause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"setPaused","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"_time","type":"uint256"}],"name":"subUserFightTime","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"baseConsu","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseDefTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseFightTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"},{"internalType":"uint256","name":"cap","type":"uint256"},{"internalType":"uint256","name":"def","type":"uint256"}],"name":"canAttackUser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"defLastTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"fightLastTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_index","type":"uint256"}],"name":"getMinter","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getMinterLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getNow","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserBaseTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"getUserEnergy","outputs":[{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_user","type":"address"}],"name":"isBlack","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"isMinter","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"levelToFightExp","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxBonus","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxCool","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxGap","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"paused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"startTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"userMedal","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')

    gameHarvestContract = web3Utils.w3.eth.contract(address=web3Utils.w3.toChecksumAddress(gameHarvestAddress), abi=gameHarvestAbi)

    gamePlunderContract = web3Utils.w3.eth.contract(address=web3Utils.w3.toChecksumAddress(gamePlunderAddress), abi=gamePlunderAbi)

    def play_game_harvest(self, key, nonce):
        '''进行游戏方法 收获

        收获冷却时间3小时,所以每3小时执行一次

        Args:
            key (str): 钱包密钥
            nonce (int): 交易数量
        Returns:
            tx (str): 链上txhash
        '''
        pass

        # 游戏方法名
        playGameMethod = "0x8a47be05"
        # 游戏所需gas上限
        gas = 1500000
        # 拼接data参数
        data = playGameMethod + "0000000000000000000000000000000000000000000000000000000000000000"
        tx = self.web3Utils.mandatory_sign_send(key, nonce, gas, self.gameHarvestAddress, data)
        return tx

    def withdrawResource(self, key, nonce):
        '''进行游戏方法

        收获冷却时间3小时,所以每3小时执行一次

        Args:
            key (str): 钱包密钥
            nonce (int): 交易数量
        Returns:
            tx (str): 链上txhash
        '''
        pass

        account = self.web3Utils.get_account(key)
        func = self.gameHarvestContract.functions.withdrawResource(0)
        params = {
            "from": account.address,
            "value": self.web3Utils.w3.toWei(0, 'ether'),
            'gasPrice': self.web3Utils.gwei,
            "gas": 1500000,
            "nonce": nonce,
        }
        return self.web3Utils.sign_send(func, params, key, "进行游戏")

    def play_game_plunder(self, key, nonce, toAddress):
        '''进行游戏方法 掠夺

        掠夺冷却时间3小时,所以每3小时执行一次
        掠夺会消耗1点飞船耐久

        Args:
            key (str): 钱包密钥
            nonce (int): 交易数量
            toAddress (str): 掠夺地址
        Returns:
            tx (str): 链上txhash
        '''
        pass

        # 游戏方法名
        playGameMethod = "0xeca3bfe7"
        # 游戏所需gas上限
        gas = 5500000
        # 转换掠夺地址
        address64 = self.web3Utils.hex64_adreess(toAddress)
        # 拼接data参数
        data = playGameMethod + address64
        tx = self.web3Utils.mandatory_sign_send(key, nonce, gas, self.gameHarvestAddress, data)
        return tx




