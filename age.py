# -*- coding: utf-8 -*-
"""
4、奥运会已经进入90后的天下了？

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore') 
# 不发出警告

import os
os.chdir('./')
# 创建工作路径

df = pd.read_excel('./olympic.xlsx')
df_length = len(df)
df_columns = df.columns.tolist()
# 查看数据
# pd.read_excel → 读取excel文件，这里得到的是pandas的dataframe数据格式

'''
按照项目分类做年龄数据分布图
'''

data = df[['event','name','birthday']]
data.dropna(inplace = True)   # 去掉缺失值
# 筛选数据，按照目标字段筛选

data.index = pd.to_datetime(data['birthday'])   # 将出生年月改为时间序列
data['birthyear'] = data.index.year
data['age'] = 2016 - data['birthyear']# 计算出年龄
data['age_range'] = pd.cut(data['age'],
                          [0,26,60],            # 划分区间
                          labels=["90s", "not 90s"])   # 区间标签 

sns.set_style("ticks")  # 图表风格设置
g = sns.FacetGrid(data, col="event", hue = 'age_range',palette="Set2_r",
                  height=2.5,    # 图表大小
                  aspect=1.2,
                 col_wrap=3,sharex=False,
                xlim=[15,40], ylim=[0,14]) # 图表长宽比
# 创建绘图区域及读取数据

g.map(sns.stripplot,"age",jitter=True,
     size = 10, edgecolor = 'w',linewidth=1,marker = 'o')
g.add_legend()  # 图例
plt.savefig('age.png',dpi=400)
# 按照项目分类绘制年龄数据分布图，并图表导出
