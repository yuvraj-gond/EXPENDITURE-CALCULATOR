from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import fontstyle
text=fontstyle.apply('enter your monthy income','bold/Italic/blue/BLACK_BG')
mi=int(input(text))
print('-'*100)
text=fontstyle.apply('enter the interest rate of the bank for your saveing ','bold/Italic/blue/BLACK_BG')
interest=float(input(text))
print('enter the value that you spend in expensive')
input('press enter to continow')
print('-'*100)
eletrcity=int(input('enter your monthy eletrcity bill'))
print('-'*100)
food=int(input('enter your monthly food expensive'))
print('-'*100)
aoto=int(input('enter the aoto expensive'))
print('-'*100)
minter=int(input('enter your mobile and internet expensive'))
print('-'*100)
local=int(input('enter your local expensive'))
print('-'*100)
othe=int(input('enter your other expensive'))
print('-'*100)
allex = eletrcity + food + aoto + minter + local + othe
sav=mi-allex

text=fontstyle.apply('your expensive and saving','bold/Italic/blue/YELLOW_BG')
print(text)
print(' your total expensive is :',allex,'\n and your saving is',sav)
print('-'*100)

elist=[eletrcity,food,aoto,minter,local,othe,sav]
elist2=[eletrcity * 12,food * 12,aoto * 12,minter * 12,local * 12,othe * 12,sav*12]
item=['electricity','food','vehicles','mobile bill','local','other','saving']
dr={'expensive':item,'value':elist}
df=pd.DataFrame(dr)
print('-'*100)
input('')
df.to_csv('monthly income')
text=fontstyle.apply('your monthly income basic','bold/Italic/blue/YELLOW_BG')
print(text)
print(df.to_string())
print('-'*100)
print('-'*100),print('-'*100)
input('')
dr2={'expensive':item,'value':elist2}
df2=pd.DataFrame(dr2)
df2.to_csv('yearly income')
text=fontstyle.apply('your yearly income basic','bold/Italic/blue/YELLOW_BG')
print(text)
print(df2.to_string())
"""text = fontstyle.apply('yuvraj is the best', 'bold/Italic/green/BLACK_BG')

# display text
print(text)"""
text=fontstyle.apply('enter 1 for to know to saving at expressive year','bold/Italic/blue/YELLOW_BG')
print(text)
a=int(input('enter the no: '))
if a==1:
    a2=int(input('Of how many year you want to see your saving: '))
    g = 0
    b = sav * 12
    for i in range(0,a2):
        per = interest / 100 * b
        b = b + per
        g = g + per
    print('your total saving is',b,'of',a2,'year and your interest earn from your saving is ',g)
plt.pie(elist,labels=item)
plt.title('monthy')
plt.legend()
plt.show()
plt.bar(item,elist)
plt.show()











