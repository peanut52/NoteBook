# 本部分仅适用于Windows系统，暂不支持Linux

# 关于定时任务：

## 这部分代码需要满足的条件是无时无刻都能运行，因此每天生成笔记本的一定内容，可以通过定时任务来完成

## 因此，写clock.py的目的是在开机后需要主动运行，且比较频繁的任务！

## 需手动将timing_task.bat中加入windows定时任务，每天执行一次，自动生成md文件的笔记本文件，也可根据自身需求进行修改！