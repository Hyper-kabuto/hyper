'''
猜数字
在注释里增加：
1、猜的数字是系统产生，不是自己定义
            使用random随机数技术来获取随机数
 范围：0~150
    猜10次！
    如果输入大了：温馨提示：大了
    如果输入小了：温馨提示：小了
    正好猜中，恭喜您，猜中，本次猜的数字为xxxx。
操作完成之后才增加：
    起始：5000金币，每猜错一次，减去500金币，一直扣完为止。15次没猜中，系统锁定。猜中加3000
'''
import random
Ran = random.randint(0,150)
print(Ran)
j=5000
i=0
while i<15 :
    num=input("猜吧")
    num=int(num)
    i=i+1
    if num == Ran:
        print("恭喜您，猜对，本次猜的数字为",Ran)
        j=j+3000
        print("金币",j)
    elif num<Ran:
        print("小了")
        j=j-500
        print("金币",j)
    elif num>Ran:
        print("大了")
        j=j-500
        print("金币",j)










