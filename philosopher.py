# """
# 哲学家就餐问题 - 基础版本（会产生死锁）
# ======================================

# 这是经典的会产生死锁的实现。每个哲学家先拿左边的叉子，再拿右边的叉子。
# 当所有哲学家同时拿起左边的叉子时，就会发生死锁。

# 运行此脚本，大概率会在几秒后卡住（死锁）。
# 按 Ctrl+C 可以中断。
# """

# import threading
# import time
# import random

# # 哲学家人数
# NUM_PHILOSOPHERS = 5

# # 为每个哲学家创建一个锁（代表叉子）
# # forks[i] 位于哲学家 i 和 (i+1) % NUM_PHILOSOPHERS 之间
# forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]


# def philosopher(index: int):
#     """
#     哲学家线程的执行逻辑
#     index: 哲学家的编号 0 ~ NUM_PHILOSOPHERS-1
#     """
#     left_fork = index
#     right_fork = (index + 1) % NUM_PHILOSOPHERS

#     while True:
#         # 1. 思考
#         print(f"[哲学家 {index}] 正在思考... 💭")
#         time.sleep(random.uniform(0.5, 1.5))

#         # 2. 尝试拿起左边的叉子
#         print(f"[哲学家 {index}] 饿了，尝试拿起左边叉子 {left_fork} 🍴")
#         forks[left_fork].acquire()
#         print(f"[哲学家 {index}] 拿起了左边叉子 {left_fork} ✅")

#         # 3. 尝试拿起右边的叉子
#         print(f"[哲学家 {index}] 尝试拿起右边叉子 {right_fork} 🍴")
#         forks[right_fork].acquire()
#         print(f"[哲学家 {index}] 拿起了右边叉子 {right_fork} ✅")

#         # 4. 就餐
#         print(f"[哲学家 {index}] 两只叉子都有了，开始就餐！🍝")
#         time.sleep(random.uniform(0.5, 1.0))

#         # 5. 放下叉子
#         forks[right_fork].release()
#         forks[left_fork].release()
#         print(f"[哲学家 {index}] 就餐完毕，放下叉子，继续思考。😌")


# def main():
#     print("=" * 60)
#     print("哲学家就餐问题 - 基础死锁版本")
#     print("=" * 60)
#     print(f"哲学家数量: {NUM_PHILOSOPHERS}")
#     print("策略: 先左后右（可能死锁）")
#     print("观察: 运行几秒后大概率会全部卡住...")
#     print("=" * 60)

#     threads = []
#     for i in range(NUM_PHILOSOPHERS):
#         t = threading.Thread(target=philosopher, args=(i,), daemon=True)
#         threads.append(t)
#         t.start()

#     # 主线程等待观察（按Ctrl+C退出）
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("\n[!] 用户中断。观察到死锁了吗？")


# if __name__ == "__main__":
#     main()


import threading
import time
import random

# 哲学家人数
NUM_PHILOSOPHERS = 5

# 创建 5 把叉子（锁）
forks = [threading.Lock() for _ in range(NUM_PHILOSOPHERS)]

def philosopher(index: int):
    """
    哲学家线程逻辑
    """
    # 确定左右叉子的编号
    left_fork_id = index
    right_fork_id = (index + 1) % NUM_PHILOSOPHERS

    # --- 核心改进：资源排序策略 ---
    # 总是先尝试获取编号较小的锁，再获取编号较大的锁
    first_fork = min(left_fork_id, right_fork_id)
    second_fork = max(left_fork_id, right_fork_id)

    while True:
        # 1. 思考
        print(f"  [哲学家 {index}] 正在思考... 💭")
        time.sleep(random.uniform(1, 2))

        # 2. 尝试就餐
        print(f"🥢 [哲学家 {index}] 饿了，尝试拿起叉子 {first_fork} 和 {second_fork}")
        
        # 按照固定顺序锁定，防止环路等待
        with forks[first_fork]:
            print(f"✅ [哲学家 {index}] 拿到了第一把叉子 {first_fork}")
            with forks[second_fork]:
                print(f"🍝 [哲学家 {index}] 拿齐了！开始吃意大利面...")
                time.sleep(random.uniform(0.5, 1.5))
        
        # 'with' 语句结束会自动释放锁
        print(f"😌 [哲学家 {index}] 吃饱了，放下叉子，回到了思考状态。")

def main():
    print("=" * 50)
    print("  哲学家就餐问题 - 死锁修复版 (资源排序法)")
    print("=" * 50)
    
    threads = []
    for i in range(NUM_PHILOSOPHERS):
        # 创建并启动哲学家线程
        t = threading.Thread(target=philosopher, args=(i,), daemon=True)
        threads.append(t)
        t.start()

    # 保持主线程运行
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序由用户停止。")

if __name__ == "__main__":
    main()