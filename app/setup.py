from cx_Freeze import setup, Executable

build_exe_options = { 
   
    'packages': ['uvicorn', 'logging', 'anyio'], # 默认可不填，程序会自动寻找依赖，如果运行时，提示有缺少的包，可以在这里添加
    'excludes': [],
    "include_files": ["static", "templates", "resource", 'agentapp_decrypt.db', "sqlcipher-shell64.exe"]  # 可以添加程序用到的其他文件
}

setup(
    name="blockatm_guard",
    version="1.0",
    description="BlockATM-Guard",
    author="Combofish",
    options={ "build_exe":build_exe_options},
    executables=[Executable(script="main.py",base="win32gui",target_name='blockatm_guard',icon="resource/favicon.ico")])