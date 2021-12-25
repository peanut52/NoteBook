import os
import datetime

import markdown
from python_markdown_maker import *

# from markdown import *

current_day = datetime.date.today()
current_year_and_month = str(current_day.year) + str(current_day.month)


def create_director(path):
    if not os.path.exists(path):
        os.mkdir(path)


def create_everyday_md_file(path):
    today_file = os.path.join(path, str(datetime.date.today()).replace(" ", "") + '.md')
    if not os.path.exists(today_file):
        with open(today_file, 'w', encoding='utf-8') as f:
            f.write(f'# TODAY IS {datetime.date.today()}, COME ON!')
            f.write(f'\n')
            f.write(f'## 今天遇到的问题是：')

            content = f"""
```\n
\n
\n
```
"""
            f.write(content)
            f.write(f'\n')

            f.write(f'## 今天问题的解决方案是：')

            method = f"""
```\n
\n
\n
```
"""
            f.write(method)
            f.write(f'\n')
            f.write(f'感悟之灵光一现：')
            inspiration = f"""
```\n
\n
\n
```
"""
            f.write(inspiration)

if __name__ == '__main__':
    my_path = r"D:\MyNote"
    my_path = os.path.join(my_path, current_year_and_month)
    create_director(my_path)
    create_everyday_md_file(my_path)
