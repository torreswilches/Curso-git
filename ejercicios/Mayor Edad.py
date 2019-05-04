# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:01:11 2019

@author: android
"""

print("Digite Edad")
edad = input()
edad = int(edad)
if edad >= 18:
    print('Es Mayor de Edad')
else:
    print('Es Menor de Edad')

# si de linea con sino
print('Es Mayor de Edad') if edad >= 18 else print('Es Menor de Edad')
