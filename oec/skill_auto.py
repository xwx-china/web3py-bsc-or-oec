from oec.skill_utils import Skill
from oec.oec_key import AdminKey

skill = Skill()

key = AdminKey.KEY.value

account = skill.web3Utils.get_account(key)

nonce = skill.web3Utils.get_nonce(account.address)

cnt = '3'

tx = skill.play_game(key, nonce, '30472', '79452', '2', cnt)
nonce = nonce + 1

tx = skill.play_game(key, nonce, '30477', '78471', '2', cnt)
nonce = nonce + 1

tx = skill.play_game(key, nonce, '5475', '79452', '2', cnt)
nonce = nonce + 1

tx = skill.play_game(key, nonce, '5467', '79452', '3', cnt)
nonce = nonce + 1

