import sys
import os

# 取得專案根目錄的絕對路徑
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

# 加入 `utils/` 和 `backend/` 到 sys.path
sys.path.append(os.path.join(ROOT_DIR, "utils"))
sys.path.append(os.path.join(ROOT_DIR, "backend"))

print("bootstrap.py: sys.path 設定完成")