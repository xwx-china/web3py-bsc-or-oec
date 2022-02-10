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

    def play_game_harvest(self, key, nonce):
        '''进行游戏方法 收获

        收获冷却时间2小时,所以每2小时执行一次

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




