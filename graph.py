# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 03:19:18 2019

@author: EbubekirDgn
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('deneme.csv')
plt.plot(df["Gecen Zaman"],df["Sonuc"])
plt.xlabel("Gecen Zaman")
plt.ylabel("Değer")
plt.show()

 