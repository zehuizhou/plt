import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

# 指定图像的宽和高，单位为英寸，dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
fig = plt.figure(figsize=(20, 8), dpi=80)

data = [('美国', 139), ('中国', 56), ('日本', 34), ('英国', 33), ('中国香港', 27), ('香港', 27), ('国大', 21), ('大陆', 21), ('法国', 20),
        ('德国', 19)]

country_list = []
number_list = []

for i in data:
    country_list.append(i[0])
    number_list.append(i[1])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.title('各个国家电影个数（前10）', FontProperties=font)
plt.bar(country_list, number_list)
plt.show()
