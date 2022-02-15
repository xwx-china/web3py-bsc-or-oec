import requests,json

from bsc.xwf_nft import Role,Element

from public.web3_utils import Web3Utils

from bsc.bsc_key import AdminKey

url = "https://app.xwg.games/marketplace/nftProduct/list"

web3Utils = Web3Utils("https://bsc-dataseed.binance.org/", 5, 56)

w3 = web3Utils.w3

headers = {
    'accept':'application/json, text/plain, */*',
    'content-type':'application/json',
    'cookie':'intercom-id-y6yb2mhq=db45629e-375e-41d4-a52c-a74b9e8dd71e; intercom-session-y6yb2mhq=; _ga=GA1.1.2115522397.1643828412; amp_fef1e8=c3260d2e-e857-4479-b872-cb300fe4703aR...1fqtstbqu.1fqtsulsd.3.2.5; _ga_0JZ9C3M56S=GS1.1.1643828411.1.1.1643828562.0',
}

# grades = ['1']
# for grade in grades:
fiveElements = ['3']
for fiveElement in fiveElements:
    names = ['Naomi', 'Luna', 'Ivy', 'Gigi', 'Blanc', 'Abigail', 'Quinn', 'Amoura', 'Lamia']
    # print("品质等于:" + grade)
    cntPrice = 0
    for name in names:
        nftName = Role[name].value
        data_json = json.dumps({
            "pageSize": 1,
            "currentPage": 1,
            "condition": {
                "contractAddr": "0x1ee6539c12361b6bc1fb930435c70d557dee392f",
                "orderType": "Fixed",
                "status": "Normal",
                "coinType": "XWG",
                # "grade": grade,
                "nftName": nftName,
                "sortAttr": "nftPrice",
                "sortMethod": "ASC",
                "fiveElement":fiveElement
            }
        })
        res = requests.post(url, data_json, headers=headers)
        data = json.loads(res.text)
        nfts = data['_data']['pageItems']
        if len(nfts) > 0:
            nft = nfts[0]
            price = w3.fromWei(int(nft['nftPrice']), "ether")
            cntPrice = cntPrice + price
            print('nftId:'+ str(nft['nftId'])+" 名称:"+name+" 价格:"+ str(price)+ " 元素:"+ str(nft['fiveElement']))
        else:
            print("名称:" + name + " 无价格")
    print("总金额:"+str(cntPrice))

key = AdminKey.KEY.value

account = web3Utils.get_account(key)

# 主钱包交易数量
nonce = web3Utils.get_nonce(account.address)

data = '0xd6febde8'+web3Utils.hex64('434602') + web3Utils.hex64(25)
tx = web3Utils.mandatory_sign_send(key, nonce, 110000, web3Utils.w3.toChecksumAddress('0x1ee6539c12361b6bc1fb930435c70d557dee392f'), data)
print(tx)
nonce = nonce + 1



