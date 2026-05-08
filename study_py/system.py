# 1. 实现一个管理人员的管理系统 字符版
# 2. 实现人员信息的增删查改
# 3. 实现登陆系统

# 导入os库 实现执行系统命令
import os

# 导入time库，使用time.sleep()实现延时
import time


# 定义一个User类 表示一个对象数据
class User:
    # 默认的构造函数
    def __init__(self, name="", phone="", sex="") -> None:
        self.name = name
        self.phone = phone
        self.sex = sex


# 用户数据表
users: list[User] = []

# 默认用户账号数据
default_user_info = {"username": "admin", "userpasswd": "admins"}


# 登陆函数
def login() -> bool:
    print("登 陆\n")
    acc = input("账号: ")
    passwd = input("密码: ")

    if (
        acc != default_user_info["username"]
        or passwd != default_user_info["userpasswd"]
    ):
        print("账号或密码错误")
        return False

    return True


# 显示界面函数
def display_menu():
    print("欢迎来到管理系统\n")
    print("可以输入help命令查看更多\n")


# 查找用户函数
def find(user: User) -> User | None:
    for usr in users:
        if usr.name == user.name:
            return usr

    return None


# 处理命令格式函数
def process_order_format(order: str) -> list[str]:
    return order.split(" ")


def order_help():
    print("帮 助 页")
    print("1. help 帮助命令")
    print("2. add 添加一个或多个用户")
    print("3. list 列出系统内的用户")
    print("4. del <用户Id> 删除某个用户")
    print("5. rep <用户Id> 修改用户信息")


# 增加用户函数
def order_add():
    print("增 加 用 户")
    while True:
        name = input("请输入用户的姓名: ")
        phone = input("请输入用户的手机号: ")
        sex = input("请输入用户的性别: ")

        if len(name) == 0 or len(phone) == 0 or len(sex) == 0:
            print("数据不能为空")
            return

        user = User(name=name, phone=phone, sex=sex)
        users.append(user)

        if str(input("是否退出添加用户?(Y/N): ")).lower() == "y":
            return


# 删除用户函数
def order_del(order: str):
    if len(process_order_format(order)) <= 1:
        print("命令输入错误")
        return
    name = process_order_format(order)[1]

    user = User(name=name)
    fd_user = find(user)
    if fd_user == None:
        print("没有该用户")

    else:
        i = users.index(fd_user)
        deluser = users.pop(i)
        print(f"已删除 {deluser.name}")

# 替换信息函数
def order_rep(order: str):
    if len(process_order_format(order)) <= 1:
        print("命令输入错误")
        return

    name = process_order_format(order)[1]
    user = User(name=name)
    fd_user = find(user)

    if fd_user == None:
        print("没有该用户")

    else:
        name = input("请输入新的姓名: ")
        phone = input("请输入新的手机号: ")
        sex = input("请输入新的性别: ")

        i = users.index(fd_user)

        users[i].name = name
        users[i].phone = phone
        users[i].sex = sex


# 执行命令函数
def exec_order(order: str):
    if order == "exit":
        print("再见")
        exit()
    elif order == "help":
        order_help()

    elif order == "add":
        order_add()

    elif order == "list":
        for usr in users:
            print(f"姓名: {usr.name} 性别: {usr.sex} 电话: {usr.phone}")
        return

    elif process_order_format(order)[0] == "del":
        order_del(order)

    elif process_order_format(order)[0] == "rep":
        order_rep(order)

    else:
        print("命令输入错误")


# 主页函数
def main_page():
    display_menu()

    while True:
        order = input("> ")
        exec_order(order)


# main函数
if __name__ == "__main__":
    os.system("cls")
    is_login = login()
    if not is_login:
        exit()

    time.sleep(1)
    os.system("cls")

    main_page()