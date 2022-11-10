
# ===============================
#       危険 WARNING 
# 実行する場合は、気を付けてください
# ================================

# ずっとiに二乗が代入されるので、数が大きくなっていく
# 数が大きくなりすぎると、パソコンのメモリが多くなっていくのでパソコンが重くなります。

# iに2を代入
i = 2

# 無限ループ
while(True):
    i **= 2 # iにiの二乗を代入
    print(i) # 表示

"""

# 毎秒処理を行うプログラム
import time

i = 0
while(True):
    print(i)
    i += 1
    time.sleep(1) # 1秒待つ処理

"""