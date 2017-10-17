把要扫描的url放进domain.txt里
格式为 http://www.abc.com
然后运行 
python main.py

等程序跑完结束之后
执行python3 quchong.py

然后找到sqlmap 目录下
执行 python sqlmapapi.py -s

把spidersqli目录下的target.txt 文件复制到 autosqlmap 目录下

再执行python autoSqlmap.py 等着跑完就行了，结果如果有注入结果在result 目录下显示