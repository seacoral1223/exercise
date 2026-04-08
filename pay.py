import threading
import time

MAX_MAILBOX = 3

class Mailbox:
    def __init__(self):
        self.data = []
        self.lock = threading.Lock()

box = Mailbox()
running = True

# 发送策略
WAIT_FOREVER = 0
WAIT_TIMEOUT = 1
NO_WAIT = 2
BUFFER_MSG = 3

# 获取当前时间（毫秒）
def current_ms():
    return int(time.time() * 1000)

# 发送函数
def mach_msg_sim(msg, option, timeout_ms=0):
    start = current_ms()

    while True:
        with box.lock:  # 加锁（互斥）
            if len(box.data) < MAX_MAILBOX:
                box.data.append(msg)
                print(f"[发送{msg}] 成功")
                return 0

        # 邮箱满后的处理
        if option == NO_WAIT:
            print(f"[发送{msg}] 邮箱满 -> 立即失败")
            return -1

        if option == BUFFER_MSG:
            print(f"[发送{msg}] 邮箱满 -> 缓存消息")
            return 1

        if option == WAIT_TIMEOUT:
            if current_ms() - start >= timeout_ms:
                print(f"[发送{msg}] 超时失败")
                return -1
            print(f"[发送{msg}] 等待中...")
            time.sleep(0.2)

        if option == WAIT_FOREVER:
            print(f"[发送{msg}] 阻塞等待...")
            time.sleep(0.2)

# 接收线程
def receiver():
    global running
    while running:
        with box.lock:
            if len(box.data) > 0:
                msg = box.data.pop(0)
                print(f">>> 接收消息: {msg}")

        time.sleep(0.5)

    print("receiver 退出")

# 发送线程
def sender():
    global running
    time.sleep(1)

    mach_msg_sim(1, WAIT_FOREVER)
    mach_msg_sim(2, WAIT_FOREVER)
    mach_msg_sim(3, WAIT_FOREVER)

    mach_msg_sim(4, NO_WAIT)
    mach_msg_sim(5, WAIT_TIMEOUT, 1000)
    mach_msg_sim(6, BUFFER_MSG)

    mach_msg_sim(7, WAIT_FOREVER)

    time.sleep(3)
    running = False  # 通知退出

# 主函数
def main():
    t1 = threading.Thread(target=receiver)
    t2 = threading.Thread(target=sender)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("程序结束")

if __name__ == "__main__":
    main()