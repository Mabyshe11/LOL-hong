import pyautogui
import random
import time
import keyboard

# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

# 计算屏幕中心坐标
center_x = screen_width / 2
center_y = screen_height / 2


# 定义一个函数来执行按键和鼠标移动序列
def perform_action():
    # 键盘Q键按下
    keyboard.press('q')
    # 随机延迟10-110毫秒
    time.sleep(random.uniform(0.01, 0.1))

    # 键盘Q键抬起
    keyboard.release('q')
    # 随机延迟10-40毫秒
    time.sleep(random.uniform(0.01, 0.1))

    # 键盘space键按下
    keyboard.press('space')
    # 随机延迟10-40毫秒
    time.sleep(random.uniform(0.01, 0.1))

    # 鼠标移动到屏幕中心点
    pyautogui.moveTo(center_x, center_y)

    # 键盘E键按下
    keyboard.press('e')
    # 随机延迟10-40毫秒
    time.sleep(random.uniform(0.01, 0.1))
    # 键盘E键抬起
    keyboard.release('e')
    # 随机延迟10-40毫秒
    time.sleep(random.uniform(0.01, 0.1))

    # 键盘space键抬起
    keyboard.release('space')
    # 随机延迟10-110毫秒
    time.sleep(random.uniform(0.01, 0.1))


keyboard.add_hotkey('T', perform_action)

# 保持程序运行，以便监听键盘事件
try:
    keyboard.wait()
except KeyboardInterrupt:
    print("程序已停止")