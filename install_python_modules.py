#!/usr/bin/env python3
"""
Python初学者必备模块安装脚本
================================

安装并验证以下核心模块：
- pandas（数据处理与分析）
- numpy（数值计算）
- matplotlib（数据可视化）
- seaborn（高级数据可视化）
- scikit-learn（机器学习入门）
- requests（网络请求）
- beautifulsoup4（网页解析）
- jupyterlab（交互式编程环境）
- python-dotenv（环境变量管理）

运行方式：
    python3 install_python_modules.py
"""

import subprocess
import sys
import time


MODULES_TO_INSTALL = [
    {"pip_name": "pandas", "import_name": "pandas"},
    {"pip_name": "numpy", "import_name": "numpy"},
    {"pip_name": "matplotlib", "import_name": "matplotlib"},
    {"pip_name": "seaborn", "import_name": "seaborn"},
    {"pip_name": "scikit-learn", "import_name": "sklearn"},
    {"pip_name": "requests", "import_name": "requests"},
    {"pip_name": "beautifulsoup4", "import_name": "bs4"},
    {"pip_name": "jupyterlab", "import_name": "jupyterlab"},
    {"pip_name": "python-dotenv", "import_name": "dotenv"},
]


def run_command(cmd, description):
    """运行命令并返回结果。"""
    print(f"\n{'='*60}")
    print(f"【{description}】")
    print(f"命令: {cmd}")
    print("-"*60)
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, 
                                capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("stderr:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ 命令执行失败！")
        print(f"错误信息: {e.stderr}")
        return False


def install_modules():
    """安装所有指定模块。"""
    print(f"\n{'='*60}")
    print("开始安装 Python 模块")
    print(f"{'='*60}")
    
    for module in MODULES_TO_INSTALL:
        pip_name = module["pip_name"]
        print(f"\n📦 正在安装: {pip_name}")
        cmd = f"python3.14 -m pip install {pip_name} --upgrade"
        success = run_command(cmd, f"安装 {pip_name}")
        if not success:
            print(f"⚠️ {pip_name} 安装失败，继续安装其他模块...")
            time.sleep(2)


def verify_installation():
    """验证所有模块是否安装成功。"""
    print(f"\n{'='*60}")
    print("验证模块安装")
    print(f"{'='*60}")
    
    success_count = 0
    failed_modules = []
    
    for module in MODULES_TO_INSTALL:
        pip_name = module["pip_name"]
        import_name = module["import_name"]
        cmd = f"python3.14 -c \"import {import_name}; print('OK')\""
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {pip_name} - 导入成功")
            success_count += 1
        else:
            print(f"❌ {pip_name} - 导入失败")
            failed_modules.append(pip_name)
    
    print(f"\n{'='*60}")
    print(f"验证结果：成功 {success_count}/{len(MODULES_TO_INSTALL)}")
    if failed_modules:
        print(f"失败模块：{', '.join(failed_modules)}")
    else:
        print("🎉 所有模块安装成功！")
    
    return failed_modules


def show_module_info():
    """显示各模块的简要功能说明和基础使用示例。"""
    print(f"\n{'='*60}")
    print("各模块功能说明与基础使用示例")
    print(f"{'='*60}")
    
    module_info = [
        {
            "name": "numpy",
            "title": "数值计算",
            "description": "用于高效处理数组、矩阵和数学运算，是数据分析的基础。",
            "example": '''import numpy as np
# 创建数组
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())  # 计算平均值
print(arr.sum())   # 计算总和''',
            "version_code": "import numpy as np; print('numpy版本:', np.__version__)"
        },
        {
            "name": "pandas",
            "title": "数据处理与分析",
            "description": "用于处理表格数据，支持数据清洗、筛选、分组、聚合等操作。",
            "example": '''import pandas as pd
# 创建DataFrame
df = pd.DataFrame({
    '姓名': ['张三', '李四', '王五'],
    '年龄': [18, 20, 19],
    '成绩': [95, 88, 92]
})
print(df)           # 显示数据
print(df['成绩'].mean())  # 计算平均成绩''',
            "version_code": "import pandas as pd; print('pandas版本:', pd.__version__)"
        },
        {
            "name": "matplotlib",
            "title": "数据可视化",
            "description": "用于创建各种类型的图表，如折线图、柱状图、散点图等。",
            "example": '''import matplotlib.pyplot as plt
# 绘制折线图
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title('简单折线图')
plt.xlabel('X轴')
plt.ylabel('Y轴')
plt.show()''',
            "version_code": "import matplotlib; print('matplotlib版本:', matplotlib.__version__)"
        },
        {
            "name": "seaborn",
            "title": "高级数据可视化",
            "description": "基于matplotlib的高级可视化库，提供更美观的统计图表。",
            "example": '''import seaborn as sns
import pandas as pd
df = pd.DataFrame({
    '类别': ['A', 'A', 'B', 'B'],
    '数值': [1, 3, 2, 4]
})
sns.barplot(x='类别', y='数值', data=df)
plt.show()''',
            "version_code": "import seaborn as sns; print('seaborn版本:', sns.__version__)"
        },
        {
            "name": "scikit-learn",
            "title": "机器学习入门",
            "description": "提供各种机器学习算法，如回归、分类、聚类等。",
            "example": '''from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])
model = LinearRegression()
model.fit(X, y)
print('预测结果:', model.predict([[6]]))''',
            "version_code": "import sklearn; print('scikit-learn版本:', sklearn.__version__)"
        },
        {
            "name": "requests",
            "title": "网络请求",
            "description": "用于发送HTTP请求，获取网页内容或API数据。",
            "example": '''import requests
# 获取网页内容
response = requests.get('https://www.python.org')
print('状态码:', response.status_code)
print('网页标题:', response.text[:50])''',
            "version_code": "import requests; print('requests版本:', requests.__version__)"
        },
        {
            "name": "beautifulsoup4",
            "title": "网页解析",
            "description": "用于解析HTML和XML文档，提取网页中的数据。",
            "example": '''from bs4 import BeautifulSoup
html = '<html><body><h1>Hello World</h1></body></html>'
soup = BeautifulSoup(html, 'html.parser')
print(soup.h1.text)  # 输出: Hello World''',
            "version_code": "import bs4; print('beautifulsoup4版本:', bs4.__version__)"
        },
        {
            "name": "jupyterlab",
            "title": "交互式编程环境",
            "description": "基于Web的交互式开发环境，支持代码、Markdown、可视化等。",
            "example": '''# 在终端运行：
# jupyter lab
# 然后在浏览器中打开显示的URL即可开始使用''',
            "version_code": "import jupyterlab; print('jupyterlab版本:', jupyterlab.__version__)"
        },
        {
            "name": "python-dotenv",
            "title": "环境变量管理",
            "description": "从.env文件加载环境变量，方便管理敏感配置信息。",
            "example": '''# 创建 .env 文件：
# API_KEY=your_api_key_here
# 
# 在代码中：
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv('API_KEY')
print(api_key)''',
            "version_code": "import dotenv; print('python-dotenv版本:', dotenv.__version__)"
        },
    ]
    
    for info in module_info:
        print(f"\n📌 {info['name']} - {info['title']}")
        print(f"   说明：{info['description']}")
        print(f"\n   基础示例：")
        print(f"   {'-'*40}")
        for line in info['example'].split('\n'):
            print(f"   {line}")
        print(f"   {'-'*40}")


def show_installed_versions():
    """显示已安装模块的版本信息。"""
    print(f"\n{'='*60}")
    print("已安装模块版本信息")
    print(f"{'='*60}")
    
    version_codes = {
        "numpy": "import numpy as np; print('numpy:', np.__version__)",
        "pandas": "import pandas as pd; print('pandas:', pd.__version__)",
        "matplotlib": "import matplotlib; print('matplotlib:', matplotlib.__version__)",
        "seaborn": "import seaborn as sns; print('seaborn:', sns.__version__)",
        "scikit-learn": "import sklearn; print('scikit-learn:', sklearn.__version__)",
        "requests": "import requests; print('requests:', requests.__version__)",
        "beautifulsoup4": "import bs4; print('beautifulsoup4:', bs4.__version__)",
        "jupyterlab": "import jupyterlab; print('jupyterlab:', jupyterlab.__version__)",
        "python-dotenv": "import dotenv; print('python-dotenv:', getattr(dotenv, '__version__', 'unknown'))",
    }
    
    for module, code in version_codes.items():
        cmd = f"python3.14 -c \"{code}\""
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(result.stdout.strip())
        else:
            print(f"{module}: 未安装或导入失败")


def main():
    """主函数。"""
    print(f"\n{'='*60}")
    print("Python初学者必备模块安装脚本")
    print(f"{'='*60}")
    print(f"\n当前Python版本: {sys.version}")
    print(f"Python路径: {sys.executable}")
    
    # 安装模块
    install_modules()
    
    # 验证安装
    failed = verify_installation()
    
    # 如果有失败的，尝试重新安装
    if failed:
        print(f"\n{'='*60}")
        print("尝试重新安装失败的模块")
        print(f"{'='*60}")
        for module in failed:
            cmd = f"python3.14 -m pip install {module} --upgrade --user"
            run_command(cmd, f"重新安装 {module}（用户目录）")
        
        # 再次验证
        print(f"\n{'='*60}")
        print("重新验证安装结果")
        print(f"{'='*60}")
        verify_installation()
    
    # 显示版本信息
    show_installed_versions()
    
    # 显示功能说明
    show_module_info()
    
    print(f"\n{'='*60}")
    print("安装脚本执行完毕！")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
