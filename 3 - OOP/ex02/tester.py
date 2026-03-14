#!/usr/bin/env python3
from DiamondTrap import King


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)

# # Using @property
# print("Using @property:")
# Joffrey1 = King("Joffrey")
# print(Joffrey1.__dict__)
# print(Joffrey1.eyes)
# print(Joffrey1.hairs)
# Joffrey1.eyes = "blue"
# Joffrey1.hairs = "light"
# print(Joffrey1.eyes)
# print(Joffrey1.hairs)
# print(Joffrey1.__dict__)
