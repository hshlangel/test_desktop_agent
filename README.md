# python依赖库安装
pip install PyQt5
pip install PyQtWebEngine


pip install fastapi uvicorn
pip install python-multipart
pip install jinja2 aiofiles
pip install pandas
pip install msoffcrypto-tool
pip install openpyxl
pip install pyotp
pip install qrcode
pip install pypi_sqlite_cipher
pip install pyyaml
pip install pyinstaller
pip install pycryptodome
pip install requests
pip install pywebview

pip install --upgrade cx_Freeze


# 压缩文件
mkdir agent_app_dir
cp .\dist\test1.exe .\agent_app_dir\

Compress-Archive -Path .\agent_app_dir\* -Destination agent_app.zip

expand -r filename.zip destination_folder

# 上传
curl https://bashupload.com/agent_app.zip --data-binary @/var/file.txt

# 安装 
choco install ninja

curl https://files.pythonhosted.org/packages/9d/eb/abc035ae8dda359dff865168dffe39d9a61f115cc6100f53276e6d4554c2/pysqlcipher3-1.2.0.tar.gz -o pysqlcipher3-1.2.0.tar.gz



# docker打包
docker pull cdrx/pyinstaller-windows

docker run -it -v .:/src/ cdrx/pyinstaller-windows /bin/bash
docker run -it -v .:/src/ cdrx/pyinstaller-windows /bin/bash


docker run -it -v .:/src/ cdrx/pyinstaller-windows 'pyinstaller -D test1.py'
docker run -it -v .:/src/ cdrx/pyinstaller-windows 'pyinstaller -F test1.py'

# 打包
## windows
pyinstaller -F -w -n desktop_angent main.py
pyinstaller -F main.py
pyinstaller -D main.py
pyinstaller -F -w -i .\resource\favicon.ico -n desktop_angent main.py
pyinstaller -D -w -i .\resource\favicon.ico -n desktop_angent main.py
pyinstaller -D -w -i .\resource\favicon.ico -n desktop_angent main.py
pyinstaller -D -w -i .\resource\favicon.ico -n desktop_angent main_win.py

pyinstaller -D -w -i .\resource\favicon.ico -n desktop_win main_win.py
pyinstaller -D -w -i .\resource\favicon.ico -n desktop_server main_server.py
pyinstaller -D -n test test.py

## windows
pyinstaller -F -w -i resource/favicon.ico -n desktop_server main_server.py
pyinstaller -F -w -i resource/favicon.ico -n desktop_win main_win.py
pyinstaller -F -w -i resource/favicon.ico -n desktop_update main_update.py

pyinstaller -D -w -i resource/favicon.ico -n blockatm-guard main.py

## mac
pyinstaller -D -w -n desktop_server main_server.py
pyinstaller -D -w -n desktop_win main_win.py
pyinstaller -D -w -n desktop_angent main.py
pyinstaller -F -w -i resource/favicon.icns -n blockatm-guard main.py



# mac
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"

# 复制
xcopy /y /c /h /r /s .\desktop_win\* .\desktop_server\


# python312

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

pip3 install --user virtualenv