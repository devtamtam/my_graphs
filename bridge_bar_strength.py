import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.path import Path

# データの定義
labels = ['1st', '2nd']
values = [421, 455]

# グラフの基本設定（height_ratiosを1:4に変更）
fig, ax = plt.subplots(nrows=2, figsize=(3, 4), dpi=160, sharex='col',
                       gridspec_kw={'height_ratios': (4, 1)})
fig.patch.set_facecolor('white')

# 棒グラフの描画
ax[0].bar(labels, values, color=['skyblue', 'orange'], edgecolor='black')
ax[1].bar(labels, values, color=['skyblue', 'orange'], edgecolor='black')

# サブプロット間の上下間隔をゼロに設定
fig.subplots_adjust(hspace=0.0)

# 下段のプロット領域（スケールを小さく）
ax[1].set_ylim(0, 8)
ax[1].set_yticks([5])  # 目盛りを点のみに変更

# 上段のプロット領域
ax[0].set_ylim(415, 460)
ax[0].set_yticks([420, 430, 450])  # 目盛りを3点のみに変更

# 下段のプロット領域上辺を非表示
ax[1].spines['top'].set_visible(False)

# 上段のプロット領域底辺を非表示、X軸の目盛とラベルを非表示
ax[0].spines['bottom'].set_visible(False)
ax[0].tick_params(axis='x', which='both', bottom=False, labelbottom=False)

# ニョロ線のパラメータ設定
d1 = 0.02  # X軸のはみだし量
d2 = 0.03  # ニョロ波の高さ
wn = 21    # ニョロ波の数（奇数値を指定）
pp = (0, d2, 0, -d2)

# 下段上部のニョロ線の描画
px = np.linspace(-d1, 1+d1, wn)
py = np.array([1 + pp[i % 4] for i in range(0, wn)])
p = Path(list(zip(px, py)), [Path.MOVETO] + [Path.CURVE3] * (wn-1))

# 黒線（外側）
line1 = mpatches.PathPatch(p, lw=4, edgecolor='black',
                          facecolor='None', clip_on=False,
                          transform=ax[1].transAxes, zorder=10)

# 白線（内側）
line2 = mpatches.PathPatch(p, lw=3, edgecolor='white',
                          facecolor='None', clip_on=False,
                          transform=ax[1].transAxes, zorder=10,
                          capstyle='round')

# パッチの追加
ax[1].add_patch(line1)
ax[1].add_patch(line2)

# ラベルの追加
ax[1].set_ylabel('Force (N)')
ax[0].set_title('破断予想荷重')

plt.show()
