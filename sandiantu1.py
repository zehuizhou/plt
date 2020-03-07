# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=14)

# 指定图像的宽和高，单位为英寸，dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
fig = plt.figure(figsize=(20, 8), dpi=80)

# 用两组数据构成多个坐标点，考察坐标点的分布，判断两变量之间是否存在某种关联或总结坐标点的分布模式。
with open('year.txt', 'r') as f:
    content = f.read().splitlines()
    year_list = content

with open('rank.txt', 'r') as f:
    content = f.read().splitlines()
    rank_list = content

x = year_list
y = rank_list

plt.title(u'年份和评分的关系', FontProperties=font)
plt.scatter(x, y)
plt.show()