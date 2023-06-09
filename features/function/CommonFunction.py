"""
这里根据具体项目，做一些适配项目常用的一些方法
"""

from features.browser import Browser






def switch_cur_handle(driver):
    handles = driver.window_handles   # 获取当前所有句柄
    print("所有handl为 {}".format(handles))
    current_handle = driver.current_window_handle  #获取当前句柄
    # 遍历获取新句柄，切换到新句柄
    for handle in handles:
        # 判断是否等于当前窗口的句柄
        if handle != current_handle:
            handles_music = handle
            # 切换窗口
            driver.switch_to.window(handles_music)
            print(handles_music)


