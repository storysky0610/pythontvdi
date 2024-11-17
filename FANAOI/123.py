import csv
import random
from faker import Faker

# 初始化Faker对象，生成随机姓名
fake = Faker('zh_CN')

# 生成500个数据
data = []
for i in range(1, 501):
    # 生成ID，S0001到S0500
    id = f"S{i:04d}"
    
    # 生成随机三字人名
    name = fake.name()

    # 随机生成权限（1~3）
    permission = random.randint(1, 3)
    
    # 存储数据
    data.append([id, name, permission])

# 写入CSV文件
csv_file = "user_data.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', '姓名', '权限'])  # 写入表头
    writer.writerows(data)  # 写入数据

print(f"CSV文件已生成: {csv_file}")
