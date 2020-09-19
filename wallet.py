# from constants import *

import subprocess
import json

# The php command that will get our derived addresses
# --coin ETH will derive ethereum addresses
# --format=json changes the terminal output to json format
command = 'php derive -g --mnemonic="INSERT" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

keys = json.loads(output)
# print all the addresses
print(keys)

# print out the first address
print(keys[0]['address'])