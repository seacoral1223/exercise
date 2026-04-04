user=[]
while True:
    name=input('请输入姓名：')
    id=input('请输入电话号码：')
    if len(id)!=11:
        print('输入的电话号码有误')
        continue
    user.append({name:id})
    a=input('还要再输入吗？(Y/N)').upper()
    if a=='N':
        break

for item in user:
    for k, v in item.items():
        print(f'{k}:{v}')