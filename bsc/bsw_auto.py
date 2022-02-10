from bsc.bsw_utils import Bsw
import time

'''
自动进行游戏脚本
'''



bsw = Bsw()
players = bsw.array_user_players("0x1C697f76a917E8995b93B0cD5b7F7BfF35daB93B")
for player in players:
    print(player.id)
    print(player.se)
    print(player.unLockTime)

print(int(time.time()))