#!/usr/bin/env python
# -*- coding: utf-8 -*-

alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
smeshenie = int(input('Шаг шифровки: '))
message =  "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.".upper()
itog = ''
for i in message: # проход по алфавиту
    mesto = alfavit.find(i) #находим буквы в алфавите и добавляем их в переменную место
    new_mesto = mesto + smeshenie #берем букву и смещаемся от нее в право  на указанное кол-во
    #new_mesto теперь  A + 2 = C   т.е сместили все буквы  A =C, B= D, C = E ...
    if i in alfavit:#если i в алфавите то
        itog += alfavit[new_mesto]  # распологаем текст с новыми значениями со смещением
        #текст принимает иной расшифрованный вид
    else:
        itog += i #если i небыло в тексте ее не оставляем без изменения и никуда не добавляем.
print(itog)