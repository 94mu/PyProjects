from pathlib import Path
import csv
import matplotlib
import matplotlib.pyplot as plt
import seaborn
from datetime import datetime
import numpy as np
import pandas as pd

# 解决图像显示中文的问题
matplotlib.rcParams['axes.unicode_minus'] = False
seaborn.set_theme(font='Kaiti', style='ticks',font_scale=1.4)

# 解析csv文件头
#path = Path("Data_Visualization/03_csvJson/weather_data/sitka_weather_07-2021_simple.csv")
path = Path("Data_Visualization/03_csvJson/weather_data/sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# 打印文件头及其位置
max_index = header_row.index('TMAX')
min_index = header_row.index('TMIN')
date_index = header_row.index('DATE')

# 提取温度并绘图
'''
## 提取最高温度
highs = []
for row in reader:
    highs.append(int(row[max_index]))
## 根据最高温度绘图
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
ax.set_title("2021年7月每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度 (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()
'''
## 提取日期、最高温度和最低温度
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    dates.append(current_date)
    highs.append(int(row[max_index]))
    lows.append(int(row[min_index]))

plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 根据气象站的名称修改标题
df = pd.read_csv(path)
station_name = df['NAME'][0].split(",")[0]
ax.set_title(station_name + " 2021年每日最高和最低温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度 (F)", fontsize=16)
ax.set_ylim(10, 130)
ax.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()
