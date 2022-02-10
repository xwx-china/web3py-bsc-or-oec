import sys
sys.path.append("..")

import json

from public.web3_utils import Web3Utils

class Skill:
    '''SKILL加密刀片游戏工具类

    本类加密刀片游戏通用方法

    Attributes:
        web3Utils(Web3Utils): Web3Utils对象
        bspAddress(str): 玩家合约地址
        bsbAddress(str): 车辆合约地址
        gameAddress(str): 游戏合约地址
        bspAbi(json): 玩家合约abi
        bsbAbi(json): 车辆合约abi
        gameAbi(json): 游戏合约abi
        bspContract(Contract): 玩家合约
        bsbContract(Contract): 车辆合约
        gameContract(Contract): 游戏合约
    '''
    pass

    web3Utils = Web3Utils("https://exchainrpc.okex.org/", 0.1, 66)

    # 加密刀片游戏合约未开源
    gameAddress = web3Utils.w3.toChecksumAddress("0x98145a2fEBac238280bbdEDc2757dC162318b16e")

    def play_game(self, key, nonce, cbcId, cbwId, enemy, cnt):
        '''进行游戏方法
        Args:
            key (str): 钱包密钥
            nonce(int): 交易数量
            cbcId (str): 角色ID
            cbwId (str): 武器ID
            enemy (str): 攻击第几个敌人从0-3
            cnt (str): 攻击几次
        Returns:
            tx(str): 链上txhash
        '''
        pass

        # 游戏方法名
        playGameMethod = "0x8ae541cb"
        # 将参数转换成64位字符串
        cbcIdStr64 = self.web3Utils.hex64(cbcId)
        cbwIdStr64 = self.web3Utils.hex64(cbwId)
        enemyStr64 = self.web3Utils.hex64(enemy)
        cntStr64 = self.web3Utils.hex64(cnt)
        # 游戏所需gas上限
        gas = 300000
        # 拼接data参数
        data = playGameMethod + cbcIdStr64 + cbwIdStr64 + enemyStr64 + cntStr64
        tx = self.web3Utils.mandatory_sign_send(key, nonce, gas, self.gameAddress, data)
        return tx


