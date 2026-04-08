import threading
import time
import random

MAX_SHELF = 5  # 货架最多放5瓶牛奶

class Shelf:
    def __init__(self):
        self.milk = 0
        self.lock = threading.Lock()

shelf = Shelf()
running = True

# 售货员（生产者）
def seller():
    global running
    while running:
        with shelf.lock:
            if shelf.milk < MAX_SHELF:
                shelf.milk += 1
                print(f"[售货员] 补充1瓶牛奶，当前库存: {shelf.milk}")
            else:
                print("[售货员] 货架满了，暂不补货")

        time.sleep(0.2)  # 模拟摆放时间


# 学生（消费者）
def student(name):
    global running
    while running:
        with shelf.lock:
            if shelf.milk > 0:
                shelf.milk -= 1
                print(f"[{name}] 买了一瓶牛奶，剩余: {shelf.milk}")
            else:
                print(f"[{name}] 没牛奶了，在等待...")

        time.sleep(random.uniform(0.5, 1.5))  # 模拟购买间隔


def main():
    global running

    t_seller = threading.Thread(target=seller)
    t_stu1 = threading.Thread(target=student, args=("学生A",))
    t_stu2 = threading.Thread(target=student, args=("学生B",))

    t_seller.start()
    t_stu1.start()
    t_stu2.start()

    time.sleep(10)  # 运行10秒
    running = False

    t_seller.join()
    t_stu1.join()
    t_stu2.join()

    print("程序结束")


if __name__ == "__main__":
    main()

# ###Condition
# import threading
# import time
# import random

# MAX_SHELF = 5

# class Shelf:
#     def __init__(self):
#         self.milk = 0
#         self.cond = threading.Condition()

# shelf = Shelf()
# running = True

# # 售货员（生产者）
# def seller():
#     global running
#     while running:
#         with shelf.cond:
#             while shelf.milk >= MAX_SHELF:
#                 print("[售货员] 货架满了，等待中...")
#                 shelf.cond.wait()

#             shelf.milk += 1
#             print(f"[售货员] 补充1瓶牛奶，当前库存: {shelf.milk}")

#             shelf.cond.notify_all()

#         time.sleep(0.2)


# # 学生（消费者）
# def student(name):
#     global running
#     while running:
#         with shelf.cond:
#             while shelf.milk <= 0:
#                 print(f"[{name}] 没牛奶了，等待中...")
#                 shelf.cond.wait()

#             shelf.milk -= 1
#             print(f"[{name}] 买了一瓶牛奶，剩余: {shelf.milk}")

#             shelf.cond.notify_all()

#         time.sleep(random.uniform(0.5, 1.5))


# def main():
#     global running

#     t1 = threading.Thread(target=seller)
#     t2 = threading.Thread(target=student, args=("学生A",))
#     t3 = threading.Thread(target=student, args=("学生B",))

#     t1.start()
#     t2.start()
#     t3.start()

#     time.sleep(10)
#     running = False

#     t1.join()
#     t2.join()
#     t3.join()

#     print("程序结束")


# if __name__ == "__main__":
#     main()

###fangfa3
# import threading
# import time
# import random
# from queue import Queue

# MAX_SHELF = 5
# shelf = Queue(maxsize=MAX_SHELF)
# running = True


# def seller():
#     global running
#     while running:
#         try:
#             shelf.put(1, timeout=1)
#             print(f"[售货员] 补充1瓶牛奶，当前库存: {shelf.qsize()}")
#         except:
#             print("[售货员] 货架满了")

#         time.sleep(0.2)


# def student(name):
#     global running
#     while running:
#         try:
#             shelf.get(timeout=1)
#             print(f"[{name}] 买了一瓶牛奶，剩余: {shelf.qsize()}")
#         except:
#             print(f"[{name}] 没牛奶了")

#         time.sleep(random.uniform(0.5, 1.5))


# def main():
#     global running

#     t1 = threading.Thread(target=seller)
#     t2 = threading.Thread(target=student, args=("学生A",))
#     t3 = threading.Thread(target=student, args=("学生B",))

#     t1.start()
#     t2.start()
#     t3.start()

#     time.sleep(10)
#     running = False

#     t1.join()
#     t2.join()
#     t3.join()

#     print("程序结束")


# if __name__ == "__main__":
#     main()