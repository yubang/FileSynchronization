#coding:UTF-8

"""
清除pyc文件
"""

import os,re

def index(path):
    if(os.path.exists(path) and os.path.isdir(path)):
        fps=os.listdir(path)
        for fp in fps:
            filePath=path+'/'+fp
            if(os.path.isfile(filePath)):
                if(re.search(r'.pyc$',filePath)):
                    os.remove(filePath)
                    print 'delete:'+filePath
            else:
                index(filePath)
                
if __name__ == '__main__':
    index('.')