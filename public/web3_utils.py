from web3 import Web3

class Web3Utils:
    '''对业务封装web3工具类

    本类将web3通用方法封装可应用于各种公链
    本类有通用的获取用户,查询代币余额,授权代币,发送代币,交互合约等方法

    Attributes:
        w3:web3py模块对象
    '''

    def __init__(self, rpc, gwei, chainId):
        '''构造函数,传入公链的rpc创建Web3Utils对象
        Args:
            rpc (str): 公链rpc地址 例: web3Utils = Web3Utils('https://bsc-dataseed.binance.org/')
            gwei (num): gWei使用情况 (就是速度,bsc最低5gwei,oec最低0.1wei)
        Returns:
            web3Utils(Web3Utils): Web3Utils对象
        '''
        pass
        self.w3 = Web3(Web3.HTTPProvider(rpc))
        self.gwei = self.w3.toWei(gwei, 'gwei')
        self.chainId = chainId

    def get_balance(self, address):
        '''通过钱包地址获取主链代币余额 如: ETH BNB OKT AVAX HT等
        Args:
            address (str): 钱包地址 例: web3Utils.getBalance('0x1C697f76a917E8995b93B0cD5b7F7BfF35daB93B')
        Returns:
            value(int): 主链代币余额
        '''
        pass
        #通过地址获取代币数量wei为单位
        wei = self.w3.eth.getBalance(address)
        #获取代币wei和代币数量转换
        value = self.w3.fromWei(wei,'ether')
        return value

    def get_account(self, key):
        '''通过私钥获取用户使用web3获取用户
        Args:
            key (str): 钱包密钥
        Returns:
            account(account): 钱包用户
        '''
        pass
        account = self.w3.eth.account.from_key(key)
        return account

    def get_nonce(self, address):
        '''通过钱包地址获取钱包交易数量
        Args:
            address (str): 钱包地址
        Returns:
            nonce(int): 交易数量
        '''
        nonce = self.w3.eth.getTransactionCount(address)
        return nonce

    def approved_token(self, key, nonce, contract, toAddress, amount):
        '''授权代币到某地址
        Args:
            key (str): 钱包密钥
            nonce(int): 交易数量
            contract (Contract): 合约对象
            toAddress (str): 授权地址
            amount(int): 授权数量
        Returns:
            tx(str): 链上txhash
        '''
        account = self.get_account(key)
        func = contract.functions.approve(toAddress, self.w3.toWei(amount, 'ether'))
        params = {
            "from": account.address,
            "value": self.w3.toWei(0, 'ether'),
            'gasPrice': self.gwei,
            "gas": 500000,
            "nonce": nonce,
        }
        return self.sign_send(func, params, key, "授权代币到" + toAddress)

    def has_approved(self, key, contract, approvedAddress):
        '''查看代币授权
        Args:
            key (str): 钱包密钥
            approvedAddress (str): 授权地址
        Returns:
            state(boolean): true授权 false未授权
        '''
        pass
        account = self.get_account(key)
        tokenSize = contract.functions.allowance(account.address, approvedAddress).call()
        if tokenSize > 0:
            return bool(1)
        else:
            return bool(0)


    def transfer_erc20(self, key, nonce, contract, toAddress, amount):
        '''发送erc20代币到某地址
        Args:
            key (str): 钱包密钥
            nonce(int): 交易数量
            contract (Contract): 合约对象
            toAddress (str): 发送地址
            amount(int): 发送数量
        Returns:
            tx(str): 链上txhash
        '''
        pass
        account = self.get_account(key)
        func = contract.functions.transfer(toAddress, self.w3.toWei(amount, 'ether'))
        params = {
            "from": account.address,
            "value": self.w3.toWei(0, 'ether'),
            'gasPrice': self.gwei,
            "gas": 300000,
            "nonce": nonce,
        }
        return self.sign_send(func, params, key, "发送代币")

    def transfer_erc721(self, key, nonce, contract, toAddress, nftId):
        '''发送NFT
        Args:
            key (str): 钱包密钥
            nonce(int): 交易数量
            contract: NFT合约
            address (str): 发送到地址
            nftId(int): nft编号
        Returns:
            tx(str): 链上txhash
        '''
        pass
        account = self.get_account(key)
        func = contract.functions.transferFrom(account.address, toAddress, nftId)
        params = {
            "from": account.address,
            "value": self.w3.toWei(0, 'ether'),
            'gasPrice': self.gwei,
            "gas": 200000,
            "nonce": nonce,
        }
        return self.sign_send(func, params, key, "发送nft")

    def sign_send(self, func, params, key, methodName):
        '''发送合约交互
        Args:
            func: 合约方法体及参数
            params: 链上参数
            key (str): 钱包密钥
            methodName (str): 方法名称
        Returns:
            tx(str): 链上txhash
        '''
        pass
        try:
            tx = func.buildTransaction(params)
            signed_tx = self.w3.eth.account.sign_transaction(tx, private_key=key)
            tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)
            print(methodName + "交互成功")
            return tx_hash.hex()
        except Exception as e:
            print(methodName + "交互失败：", e)
        return

    def mandatory_sign_send(self, key, nonce, gas, toAddress, data):
        '''发送合约交互针对未开源合约进行交互
        Args:
            key (str): 钱包密钥
            nonce (int): 钱包交易数量
            gas (int): gas消耗上限
            toAddress (str): 合约地址
            data (str): 交互合约的uint256数据
        Returns:
            tx(str): 链上txhash
        '''
        pass
        signed_txn = self.w3.eth.account.sign_transaction(dict(
            nonce = nonce,
            gasPrice = self.gwei,
            gas = gas,
            to = self.w3.toChecksumAddress(toAddress),
            value = 0,
            data = self.w3.toHex(hexstr=data),
            chainId = self.chainId,
        ),
            key,
        )
        self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return self.w3.toHex(signed_txn.hash)

    def get_receipt_tx(self, tx):
        '''查询链上状态 是个递归
        Args:
            tx (str): hash地址
        Returns:
            receipt: 数据对象
        '''
        pass
        try:
            receipt = self.w3.eth.get_transaction_receipt(tx)
            return receipt
        except Exception as e:
            self.get_receipt_tx(tx)

    def hex64(self, num):
        '''把数字或字符串转换成64位前方用0填充
        Args:
            num (int): 数字 or num (str): 数字
        Returns:
            num64(str): 64位数字
        '''
        pass
        num16 = 0
        if type(num) == type("str"):
            num16 = hex((int(num)))
        else:
            num16 = hex(self.w3.toWei(num, 'ether'))
        num16Str = str(num16).replace('0x', '')
        num16StrLength = len(num16Str)
        zeroCount = 64 - num16StrLength
        zeroStr = ''
        i = 0
        while i < zeroCount:
            zeroStr = zeroStr + "0"
            i = i + 1
        num64 = zeroStr + str(num16Str)
        return num64

    def hex64_adreess(self, address):
        '''把地址转换成64位前方用0填充
        Args:
            address (str): 钱包地址
        Returns:
            num64(str): 64位数字
        '''
        pass
        address40 = str(address).replace('0x', '')
        address40Length = len(address40)
        zeroCount = 64 - address40Length
        zeroStr = ''
        i = 0
        while i < zeroCount:
            zeroStr = zeroStr + "0"
            i = i + 1
        address64 = zeroStr + address40
        return address64

