import webview
import time
import os
import webbrowser
import sys
import platform
import sqlite3
from utils.logger import Logger

class OSName():
    OS_WINDOWS = "Windows"
    OS_MAC = "Darwin"
    OS_LINUX = "Linux"
    OS_OTHER = "Other"

def get_run_dir():
    os_name = platform.system()
    if os_name == OSName.OS_WINDOWS:
        return '.'
    
    executable_file = sys.executable
    if 'python' in os.path.basename(executable_file):
        return '.'
    
    return os.path.abspath(os.path.dirname(__file__))
    #return os.path.dirname(executable_file)

def main():
    dir = get_run_dir()
    #local = os.path.abspath(os.path.join(os.path.dirname(sys.executable), "../../.."))
    local = os.path.abspath(os.path.dirname(sys.executable).rsplit('/', 3)[0])
    usrdir = os.path.expanduser('~')
    webbrowser.open(f'http://local/{local}')
    webbrowser.open(f'http://dir/{dir}')
    webbrowser.open(f'http://argv1/{os.path.dirname(sys.argv[0])}')
    webbrowser.open(f'http://argv2/{os.path.dirname(os.path.realpath(sys.argv[0]))}')
    webbrowser.open(f'http://executable/{sys.executable}')
    Logger().init('webview_test1', f'{usrdir}/logs')
    Logger().logger.info("webview start!")
    Logger().logger.info(f'dir = {dir}')
    Logger().logger.info(f'argv = {os.path.dirname(sys.argv[0])}')
    Logger().logger.info(f'local = {local}')
    Logger().logger.info(f'executable = {sys.executable}')
    
    sql = 'select * from agent_config order by update_time desc limit 1;'
    conn = sqlite3.connect(f'{get_run_dir()}/agentapp_decrypt.db')
    cur = conn.execute(sql)
    conn.commit()
    res = cur.fetchall()
    conn.close()
    Logger().logger.info(f'http://{res}')

    webview.create_window('BlockATM-Guard', 'http://www.baidu.com', width=1400, height=750)
    webview.start()

    Logger().logger.info("webview end")
    time.sleep(1)

if __name__ == '__main__':
    main()