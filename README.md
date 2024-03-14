此程序用来帮助打开电脑时自动连接校园网，用到了Python的`pyautogui`库来确定鼠标要点击位置的坐标。

**屏幕坐标：** 你可以使用 `pyautogui` 库提供的 `position()` 函数来获取当前鼠标的坐标。这样你可以先用鼠标手动点击要确定的位置，然后通过 `position()` 函数获取坐标信息。

可以通过添加适当的延迟来确保有足够的时间将鼠标移动到目标位置。可以使用 `time.sleep()` 函数来实现延迟，该函数可以在指定的秒数后暂停程序的执行。

```python
import pyautogui
import time 

print("Move the mouse to the desired position...")
time.sellp(3) # 延迟3秒，确保有足够的时间移动鼠标
print(pyautogui.position())
```

运行上述代码后，移动鼠标到目标位置并等待几秒钟，控制台会输出鼠标当前的坐标信息。

在进行自动化操作时，建议先进行多次测试和验证，以确保脚本能够准确地定位目标位置。

确定位置后就可以用库函数来实现自动点击指定坐标：

**点击鼠标：** 使用 `click(x, y, clicks, interval, button)` 函数在指定坐标

`(x, y)` 处点击鼠标，可指定点击次数、间隔和按钮。

```ptthon
pyautogui.click(100, 100, clicks=2, interval=0.5, button='left') 
# 在坐标 (100, 100) 处左键双击，间隔0.5秒
```

利用此方法，便可实现运行程序后自动连接校园网，不过鉴于不同电脑的屏幕大小不同，使用时需要改变坐标参数
