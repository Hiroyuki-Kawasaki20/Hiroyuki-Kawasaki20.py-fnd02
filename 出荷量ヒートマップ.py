import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

#日本語フォント設定
rcParams["font.family"] = "MS Gothic"

#CSVを読み込み
csv_file_path = "出荷情報_全便.csv"
df = pd.read_csv(csv_file_path, encoding="utf-8-sig")

#便番号（末尾2桁を指定）
df["bin_no"] = df["NONYUHIBIN"].astype(str).str[-2:]

#表の要素整理
results = pd.pivot_table(df,index="納入先",columns="bin_no",values="NONYUHIBIN",aggfunc="count",fill_value=0).sort_index(axis=1)

#ヒートマップ設定
plt.figure(figsize=(12, 5))
heatmap = sns.heatmap(results, cmap="YlOrRd", cbar_kws={"label": "出荷件数"},annot = True,fmt = "d",mask=(results == 0),) 
heatmap.set_facecolor("lightgray") 

#タイトル、ラベル設定
plt.title("納入先別  仕事量ヒートマップ")
plt.xlabel("便No")
plt.ylabel("納入先")

#グラフ表示
plt.tight_layout()
plt.show()
