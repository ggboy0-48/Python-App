from pathlib import Path

# 项目路径
project_path = Path(__file__).resolve().parent.parent
# -----------------------日志路径-----------------------------
log_path = f'{project_path}/logs/log_recode.log'

# ----------------------试题题库-----------------------------
question_path = f'{project_path}/data'

# -----------------------人员名单 -----------------------------
# staff = ['周沐辰', '韩文浩', '彭梓洋', '张牧', '周妍潞', '郭悠然', '陈妍如']
staff = ['小A', '小B', '小C', '小明', '大D', '对A', '一饼']
# ----------------------result ----------------------------------
result_path = f'{project_path}/data/result.json'

# ------------------------mapping ---------------------------------
level_mapping = {'一级': 1, '二级': 2, '三级': 3, '四级': 4, '五级': 5, '六级': 6}



