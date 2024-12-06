import pandas as pd
import matplotlib.pyplot as plt

# 加载Excel文件
file_path = '~/Desktop/QM 1/rainfall_data-1.xlsx'  # 使用正确的文件路径
df = pd.read_excel(file_path, sheet_name='rainfall_data-1')

# 计算每个国家每年的降水偏差平均值
df_avg = df.groupby(['country', 'Year'])['GPCP_precip_mm_deviation_sd'].mean().reset_index()

# 创建图形，调整图形大小
plt.figure(figsize=(8, 5))  # 调整图形大小，缩小图表

# 绘制每个国家的年度降水偏差平均值
for country in df_avg['country'].unique():
    country_data = df_avg[df_avg['country'] == country]
    plt.plot(country_data['Year'], country_data['GPCP_precip_mm_deviation_sd'], label=country)

# 设置横坐标为整数年份
plt.xticks(df_avg['Year'].unique().astype(int))  # 确保横坐标是整数年份

# 添加标签和标题
plt.xlabel('Year')
plt.ylabel('Average GPCP Precipitation Deviation (Standard Deviations)')
plt.title('Average Annual Rainfall Deviations for Country-Years')

# 添加图例
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

# 调整布局，避免标签重叠
plt.tight_layout()

# 显示图表
plt.show()
