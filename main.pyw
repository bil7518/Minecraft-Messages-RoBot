#版本:3.3
import pyautogui,time,easygui,random,winsound #导入需要的库
from win10toast import ToastNotifier
print("日志:")
count = 0
b=0
s=0
q=0
easygui.msgbox("使用说明:请提前将要刷的文字复制到剪贴板中。输入完次数和间隔的秒数后三秒后会开始刷屏，请提前请在三秒内进入MC中。")
a = easygui.enterbox(msg="请输入刷屏的次数:", title="MC聊天机器人", default="", strip=True, image=None, root=None)
b = easygui.enterbox(msg="请输入间隔的秒数:", title="MC聊天机器人", default="", strip=True, image=None, root=None)
q = easygui.enterbox(msg="请输入打开聊天的按键:", title="MC聊天机器人", default="", strip=True, image=None, root=None)
easygui.msgbox("将在三秒后开始刷屏。")
a=int(a) #字符串转化为数字
b=float(b)
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0")
duration = 1000  # 持续时间/ms
frequency = 500  # 频率/Hz
winsound.Beep(frequency, duration)
while (count < a): #进入循环
        time.sleep(b) #等待b秒
        pyautogui.press(q) #通过设置的聊天按键按下
        pyautogui.keyDown('Ctrl')    #通过脚本批量粘贴
        pyautogui.press('V')    
        pyautogui.keyUp('Ctrl')
        s=random.randint(100,300) #生成100~300的随机数
        s=str(s) #将随机数转换成字符串
        pyautogui.typewrite(s, 0) 
        pyautogui.press('Enter') 
        count = count + 1
        print("已完成"+str(count)+"次")
       

print("已全部完成，程序已退出.")
toaster = ToastNotifier()
toaster.show_toast("MC聊天机器人",
                   "操作已完成，程序已自动退出",
                   icon_path=None,
                   duration=5,
                   threaded=True)