import matplotlib.pyplot as plt
from random_walk import Randomwalk
import plotly.express as px

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例
    rw = Randomwalk()
    rw.fill_walk()

    '''Matplotlib可视化
    # 将所有的点都绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    #ax.plot(rw.x_values, rw.y_values, linewidth=0.5)

    ax.set_aspect('equal')
    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)  # 起点
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)  # 终点
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    '''
    '''Plotly可视化
    labels = {'x': 'X 位置', 'y': 'Y 位置'}
    title = '随机漫步（{}点）'.format(rw.num_points)
    fig = px.scatter(x=rw.x_values, y=rw.y_values, title=title, labels=labels, color=range(rw.num_points), color_continuous_scale=px.colors.sequential.Blues)
    fig.update_traces(marker=dict(size=1))
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    fig.update_layout(xaxis=dict(zeroline=False), yaxis=dict(zeroline=False))
    fig.update_layout(coloraxis_showscale=False)
    #fig.write_image('rw_visual.png', scale=2)
    fig.show()
   '''

    keep_running = input("Make another walk? (y/n): ") 
    if keep_running == 'n':
        break