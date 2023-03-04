# VsftpdScan
Vsftpd批量扫描笑脸漏洞工具

<h1>该工具用以扫描Vsftpd 2.3.4版本是否存在未修复的笑脸漏洞,使用python3编写<h1></br>

使用以下命令来启动它
```
python vsftpdtool.py *.txt
```
或者是</br>
```
python3 vsftpdtool.py *.txt
```
>注：*.txt应该是存有待扫描主机ip的txt文件或其他文本文件
>文本文件的内容应该是像下面这样每行一条ip
```
1.1.1.1
2.2.2.2
```
