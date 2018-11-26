# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:52:34 2018

@author: EbubekirDogan
"""

#variable (degisken)

#variable
#function
#object

var1 = 10          # integer = int
var2 = 15 
gun = "pazartesi"  # string
var3 = 10.0        # double (float)
var5 = 10
# 5var = 10  # hata verir.Degiskenler sayi ile baslayamaz.
var6 = 11
Var7 = 12  # standart convention of python'a gore buyuk harfle baslamasi uygun degil

# %%
# string 
s = "merhaba"

variable_type = type(s) # type methodu ile s degiskeninin turunu ogreniyoruz. str = string

print(s)

s1 = "Samsun"
s2 ="İstanbul"
result = s1 + s2
uzunluk = len(result) 

# %% numbers

#integer tür
sayi = -111

# double = float = ondalikli sayi
float_deneme = -30.7

# %% built in functions
str1= "deneme"
float1 = 10.6 
# float(10)
# int(float1)
# round(float1)
str2 = "1005"

# %% user defined functions

var1 = 20
var2 = 50

output = (((var1+var2)*50)/100.0)*var1/var2

# fonksiyon parametresi = input
def benim_ilk_func(a,b):
    
    """
    bu benim ilk denemem
    
    parametre: 
        
    return: 
    """
    output = (((a+b)*50)/100.0)*a/b
    
    return output
    
sonuc = benim_ilk_func(var1,var2)

def deneme1():
    print("bu benim ikinci denemem")

# %% default ve flexible functionları

# default f: cemberin cevre uzunlugu = 2*pi*r
    
def cember_cevresi_hesapla(r,pi=3.14):
    
    """
    cember cevresi hesapla
    input(parametre): r,pi
    output = cemberin cevresi
    """
    
    output = 2*pi*r
    return output

# flexible
    
def hesapla(boy,kilo,*args):
    print(args)
    output = (boy+kilo)*args[0]
    return output

#def hesapla(boy,kilo,yas):
#    output = (boy+kilo)*yas
#    return output
    

# %% QUIZ
    
# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float()) 
# *args soyisim
# default parametre ayakkabi numarasi
    
yas = 10
name = "ali"
soyisim = "veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi=35):
    print("Cocugun ismi: ",name, " yasi: ",yas," ayak numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    
    return output

sonuc = function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)


# %% 
# lambda function

def hesapla(x):
    return x*x
sonuc = hesapla(3)


sonuc2 = lambda x: x*x
print(sonuc2(3))
