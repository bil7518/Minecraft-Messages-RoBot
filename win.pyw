#版本:1.0 Bata
import easygui as t
import os,sys
soe=True
list = ['停止程序','打开作者哔哩哔哩','关闭此窗口']
t.msgbox("这是MC聊天机器人的控制菜单，目前只有几个功能")
while soe:
    a=t.choicebox('请选择你要使用的功能','MC聊天机器人-功能选择',list)
    if a=="停止程序":
        t.msgbox("程序已停止...")
        os.system("taskkill /f /im MC服务器聊天Robot.exe")
    elif a=="打开作者哔哩哔哩":
        os.system("start https://space.bilibili.com/493847518")
    elif a=="关闭此窗口":
        break