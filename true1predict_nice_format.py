import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pathlib import Path

# --- 1. CSVファイルの読み込み ---
# ユーザーがアップロードしたファイル名に修正
file_path = 'epoch50-05093temp.csv'
try:
    data = pd.read_csv(file_path)
    # 4番目の不要な列を削除（もし存在するなら）
    if len(data.columns) > 3:
        data = data.iloc[:, :3]
    # 列名が正しいか確認し、もしなければ設定
    if 'True_Label' not in data.columns or 'Predicted_Value' not in data.columns:
        # 適切な列名を設定します。CSVの構造に基づいて調整が必要な場合があります。
        # ここでは、最初の2列をそれぞれ 'True_Label', 'Predicted_Value' と仮定します。
        data.columns = ['True_Label', 'Predicted_Value', 'Image_Path']

    # --- 2. グラフの作成 (Matplotlib) ---
    print("Matplotlibを使用してグラフを作成します。")
    plt.figure(figsize=(8, 8))

    # フォントサイズを現在のサイズの3倍に設定
    base_fontsize = plt.rcParams.get('font.size', 10)
    fs = base_fontsize * 3

    # 散布図をプロット (x軸: True_Label, y軸: Predicted_Value)
    plt.scatter(data['True_Label'], data['Predicted_Value'], alpha=0.5, label='predicted values')

    # 理想的な予測を示す y=x の線をプロット
    # グラフの最小値と最大値を取得して線の範囲を決定
    min_val = min(data['True_Label'].min(), data['Predicted_Value'].min())
    max_val = max(data['True_Label'].max(), data['Predicted_Value'].max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--', linewidth=2, label='ideal')

    # --- 3. グラフの装飾 ---
    plt.title('Experiment Value vs. Predicted Value')
    plt.xlabel('Experiment Friction Force [mN]', fontsize=fs)
    plt.ylabel('Predicted Friction Force [mN]', fontsize=fs)
    plt.legend(fontsize= fs)       # 凡例はデフォルトサイズのまま
    plt.grid(False)     # グリッド線を表示
    plt.axis('equal')  # X軸とY軸のスケールを等しくする
    plt.tight_layout() # レイアウトを調整
    plt.tick_params(
    direction='in',  # 内向き
    length=10,       # 長さ10
    width=2,         # 太さ2
    labelsize=15,    # 数字の大きさ15
    top=True,        # 上にも目盛り線を追加
    right=True       # 右にも目盛り線を追加
)
    # --- 4. グラフを画像として保存 ---
    output_filename = 'true_vs_predicted_graph.png'
    plt.savefig(output_filename)
    print(f"グラフを '{output_filename}'として保存しました。")

except FileNotFoundError:
    print(f"エラー: ファイル '{file_path}' が見つかりません。")
except Exception as e:
    print(f"グラフの作成中にエラーが発生しました: {e}")
    # データフレームの最初の数行を表示して、問題の診断に役立てる
    print("\nデータの最初の5行:")
    print(data.head())