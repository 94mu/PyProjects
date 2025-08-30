from die import Die
import plotly.express as px
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt

# 解决图像显示中文的问题
matplotlib.rcParams['axes.unicode_minus'] = False
sns.set_theme(font='Kaiti', style='ticks',font_scale=1.4)

# 创建两个骰子
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result + 1)
frequencies = [results.count(value) for value in poss_results]

# 对结果进行可视化
title = '掷1个6面骰子和1个10面骰子50,000次的结果'
labels = {'x': '结果', 'y': '频率'}
'''plotpy可视化
fig = px.bar(x=poss_results, y=frequencies, labels=labels, title=title)
fig.update_layout(xaxis=dict(dtick=1))
fig.show()
fig.write_image('die_visual.png', scale=2)
'''
'''matplotlib可视化
plt.bar(poss_results, frequencies)
plt.title(title)
plt.xlabel('结果')
plt.ylabel('频率')
plt.xticks(poss_results)
#plt.savefig('die_visual.png', bbox_inches='tight')
plt.show()
'''