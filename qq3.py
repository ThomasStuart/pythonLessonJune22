# What is the code to select the max number from the list  ?
from math import inf

tips = [11, 23, 100, 21, 80]  # 100

maxt = -inf

for i in range(0, len(tips)):
    #   11, 23, 100, 21, 80
    if tips[i] > maxt:
        maxt = tips[i]

print(maxt)
