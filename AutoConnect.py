import sys
import time
import pyautogui
from selenium import webdriver

# 指定webdriver路径
webdriver_path = "C:\\Users\\lenovo\\.cache\\selenium\\msedgedriver\\win64\\122.0.2365.80\\msedgedriver.exe"


# 使用一个方法，用来判断浏览器是否连接到网络，如果连接上了，就不必再执行下面的代码了
def check_network_connection():
    try:
        # 使用 Edge 浏览器驱动打开百度网站
        driver = webdriver.Edge()
        driver.get("https://www.baidu.com")
        driver.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


if check_network_connection():
    print("程序无法在连接到网络时运行")
    sys.exit(1)
else:
    print("网络未连接，程序可以继续运行")

# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())
# Move the mouse to the desired position...
# Point(x=1736, y=1061)(屏幕右下角的网络按钮坐标）
pyautogui.click(1736, 1061, clicks=1, button='left')  # 在坐标 (1736,1061) 处左键单击，打开设置框
time.sleep(1)  # 等待一秒钟
# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())
# Move the mouse to the desired position...
# Point(x=1572, y=564)（下次需要点击的坐标，即打开WIFI连接的按钮）
pyautogui.click(1572, 564, clicks=1, button='left')  # 打开网络连接界面
time.sleep(1)  # 等待一秒钟
# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())
# Move the mouse to the desired position...
# Point(x=1612, y=653)
pyautogui.click(1612, 653, clicks=1, button='left')  # 点击进入“打开浏览器并连接”按钮
time.sleep(8)  # 等待8秒钟，防止浏览器加载过慢
# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())  # 找到运营商位置
pyautogui.click(1177, 226, clicks=1, button='left')  # 点击选择运营商
time.sleep(1)
# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())  # 找到账号输入框位置
pyautogui.click(1086, 330, clicks=1, button='left')  # 点击账号输入框
time.sleep(3)
# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())  # 找到记录的账号密码
pyautogui.click(1086, 408, clicks=1, button='left')  # 选择相应的账号和密码
time.sleep(3)
# print("Move the mouse to the desired position...")
# time.sleep(3)  # 延迟3秒，确保有足够的时间移动鼠标
# print(pyautogui.position())  # 找到登录按钮的坐标
pyautogui.click(1064, 448, clicks=1, button='left')  # 点击登录
