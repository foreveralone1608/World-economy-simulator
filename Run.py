from City import world
from City import city
import random
import matplotlib.pyplot as plt

Beijing = city('Beijing', 'CHINA', 'CHINA', ['Chinese', [' Taoist',50]])
Nanjing = city('Nanjing', 'CHINA', 'CHINA', ['Chinese', [' Confunist',50]])
Honkong = city('Hongkong', 'CHINA', 'CHINA', ['Chinese', [' Confunist',50]])
W = world()
W.add_city(Beijing)
W.add_city(Nanjing)
W.add_city(Honkong)
while True:
    W.migration()
    W.print()