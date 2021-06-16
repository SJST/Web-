# -*- coding: utf-8 -*-

# @Project  : PythonSelenium
# @File     : 05_GitLab代码维护.py
# @Date     : 2021-06-16
# @Author   : Administrator
# @Info     :
# @Introduce: Git 维护代码的基本操作

# Info: git 初始化

"""
    1.要对现有的某个项目开始用 Git 管理，只需到此项目所在的目录，执行：
        git init
    2.
"""

# Info: git 添加版本控制

"""

"""

# Info: 创建并检出新的分支
"""
    执行命令: git checkout -b 'name'
    相当于执行了 git branch 
                 git checkout
            
"""
# Info:合并分支

"""
    git checkout master     切换原本分支
    git merge name  合并分支
    git branch -d name 删除分支
"""
# Info : 分支冲突

"""
有时候合并操作并不会如此顺利。如果在不同的分支中都修改了同一个文件的同一部分，Git 就无法干净地把两者合到一起

Auto-merging index.html
    CONFLICT (content): Merge conflict in index.html
    Automatic merge failed; fix conflicts and then commit the result.
    
Git 作了合并，但没有提交，它会停下来等你解决冲突。要看看哪些文件在合并时发生冲突
 git status
 例如
  <<<<<<< HEAD:index.html
    <div id="footer">contact : email.support@github.com</div>
    =======
    <div id="footer">
    please contact us at support@github.com
    </div>
    >>>>>>> iss53:index.html
    以 ===== 为界限
    上面是要合并的分支 下面是 iss53 的内容
"""


