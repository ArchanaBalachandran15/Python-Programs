import moduleprog as m
m.first_module("Oiii")
print(m.dict1)
print(m.dict["two"])

from module import dict1
print(dict1)

import platform
print(platform.system())