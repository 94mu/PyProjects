from pathlib import Path
import csv
import matplotlib
import matplotlib.pyplot as plt
import seaborn
from datetime import datetime

# 解决图像显示中文的问题
matplotlib.rcParams['axes.unicode_minus'] = False
seaborn.set_theme(font='Kaiti', style='ticks',font_scale=1.4)

# 解析csv文件头
path = Path("Data_Visualization/03_csvJson/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 打印文件头及其位置
max_index = header_row.index('TMAX')
min_index = header_row.index('TMIN')
date_index = header_row.index('DATE')

# 提取温度并绘图
## 提取日期、最高温度和最低温度
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
    try:
        high = int(row[max_index])
        low = int(row[min_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(int(row[max_index]))
        lows.append(int(row[min_index]))
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.set_title("死亡谷2021年每日最高和最低温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度 (F)", fontsize=16)
ax.set_ylim(20, 140)
ax.tick_params(axis='both', which='major', labelsize=16)
fig.autofmt_xdate()
plt.show()
