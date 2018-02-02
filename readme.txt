创建博客项目
20180126 https://www.zmrenwu.com/post/6/  创建文章数据，
python manage.py createsuperuser
用户名：x318
邮箱：x318@qq.com
密码：x318qaz12
jiali
xiugaijiali
0131    https://www.zmrenwu.com/post/8/
演示  http://demo.zmrenwu.com/
201802010945

搭建虚拟环境，开发博客项目
1、安装虚拟环境
pip3 install virtualenv
python3 -m pip install virtualenv
rtualenv
virtualenv-15.1.0-py2.py3-none-any.whl (1.8MB)
███████████████████████████████| 1.8MB 29kB/s
llected packages: virtualenv
installed virtualenv-15.1.0
2、创建虚拟环境
C:\Users\x318\blogproject_env
virtualenv H:\python\django\blogproject_env
virtualenv C:\Python35\blogproject_env
3、激活虚拟环境
H:\python\django\blogproject_env\Scripts\activate
C:\Users\x318\blogproject_env\Scripts\activate
C:\Python35\blogproject_env\Scripts\activate
注意 Linux 下没有 Scripts\ 这个目录，取而代之的是 bin/ 目录。且激活命令为：
$ source blogproject_env/bin/activate
4、安装django
pip3 --default-timeout=100 install django==1.10.6

安装插件
pip install markdown
pip install Pygments