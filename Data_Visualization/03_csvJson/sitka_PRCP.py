from pathlib import Path
import csv
import matplotlib
import matplotlib.pyplot as plt
import seaborn
from datetime import datetime
import numpy as np

# 解决图像显示中文的问题
matplotlib.rcParams['axes.unicode_minus'] = False
seaborn.set_theme(font='Kaiti', style='ticks',font_scale=1.4)

# 解析csv文件头
path = Path("Data_Visualization/03_csvJson/weather_data/sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 打印文件头及其位置
prcp_index = header_row.index('PRCP')
date_index = header_row.index('DATE')

# 提取每日降水量并绘图
dates, PRCP = [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    dates.append(current_date)
    PRCP.append(float(row[prcp_index]))
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.bar(dates, PRCP, color='blue')
ax.set_title("2021年每日降水量", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("每日降水量", fontsize=16)
ax.set_ylim(0, 3)
ax.set_yticks(np.arange(0, 3, 0.5))
#ax.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()
