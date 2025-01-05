'''
Python Fille:SuaiZi.py--V1.16
1-----Not Gui V1.16
2-----Gui V0.3
'''
#------------------Script Start v1.16_res----------------------------------------------------------------------------------------
from random import *
from sys import *
from turtle import *#GUI
zb = 0 #作弊开关，1为开，0为关
def nogui():
    while True:
        if zb ==1:
            print('You Win!')
            print('但是，你开启了作弊开关，所以你输了') #如果想不提示，可以注释掉这一行
            break
        i = randint(1,6)
        print(i)
        if i ==6:
            i = randint(1,6)
            print(i)
        if i ==6:
            i = randint(1,6)
            print(i)
            if i ==6:
                print(i)
                print('666')
                exit(0)
        print('End')
        break
credits = ('Lin')
print(credits)
'''PaoSuaiZi.py,Program Credits V1.02 by Lin,Python 3.x,Random,sys,v1.16'''
'''
-----无GUI最终版本:v1.16_-Finish---------------------------------------------------------------------------------------
v1.16:修复错误：作弊开关开启时，不应显示变量i的值--已修复,2024-1-5 19:15
v1.15:代码优化（未作任何功能上的改变）
v1.14:增加作弊开关
v1.13:增加如果是6时，再次投掷
          修复了一些错误(见：linzsx007001.github.io/pybug/psz.htm)--已修复,2024-1-5 19:00
'''
#Email:zsx007001@163.com
#Date:25-1-5
#End of PaoSuaiZi.py
#------------------PyID:004-paosz_nogui----------------------------------------------------------------------------------------
'''
GUI版本:
注意：需要安装Turtle库
如果没有安装，请在命令行中输入（如果有pip)：pip install Turtle或把51-95行注释掉,再添加nogui()到定义命令后(不使用GUI)
'''
def guisz():
    print('GUI版本:v0.3')
    screensize(800,600)
    #bgpic('sz.jpg')-Error-DeBFile1(2024-1-5 19:30)
    zb = 0 #作弊开关，1为开，0为关
    if zb ==1:
            print('You Win!')
            print('但是，你开启了作弊开关，所以你输了') #如果想不提示，可以注释掉这一行
            exit(0)
    i = randint(1,6)
    print(i)
    if i ==6:
        i = randint(1,6)
        print(i)
        #goto()
        if i ==6:
            i = randint(1,6)
            print(i)
            #goto()
            if i ==6:
                print(i)
                print('666')
                #goto()-command not fill- eb02
    elif i ==5:
        print(i)
        #goto()
        
    elif i ==4:
        print(i)
        #goto()
        
    elif i ==3:
        print(i)
        #goto()
        
    elif i ==2:
        print(i)
        #goto()
        
    else:
        print(i)
        #goto()
        
    credits = ('Lin')
    print(credits)
     #代码完成，图片完成
'''
-----GUI版本:v0.3 [Script Files Make],Py V2 ----------------------------------------------------------------------------------------'''
'''
V2.0:增加了GUI版本,对于作弊开关，GUI版本不支持,2024-1-5 19:32,新增选择版本功能
V2.1:GUI添加作弊开关,2024-1-5 19:35
v2.2(未发布):,,修复轨迹（Turtle)问题等（见：linzsx007001.github.io/pybug/psz.htm）,2024-1-5 19:40
'''
i = int(input('1.GUI,2.NoGUI') ) #选择版本
if i ==1:
    guisz()
elif i==2:
    nogui()
else:
    print('Error')
#------------------PyID:004-paosz_gui/howv----------------------------------------------------------------------------------------