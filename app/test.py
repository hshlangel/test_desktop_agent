import webview
import time
# import os
# import sys
# import platform
#from utils.logger import Logger

# class OSName():
#     OS_WINDOWS = "Windows"
#     OS_MAC = "Darwin"
#     OS_LINUX = "Linux"
#     OS_OTHER = "Other"

# def get_run_dir():
#     os_name = platform.system()
#     if os_name == OSName.OS_WINDOWS:
#         return '.'
    
#     executable_file = sys.executable
#     if 'python' in os.path.basename(executable_file):
#         return '.'
    
#     return os.path.dirname(executable_file)

def main():
    # dir = get_run_dir()
    # local = os.path.abspath(os.path.join(os.path.dirname(sys.executable), "../../.."))
    # Logger().init('webview_test', f'{local}/logs')
    # Logger().logger.info("webview start!")
    # Logger().logger.info(f'dir = {dir}')
    # Logger().logger.info(f'argv = {os.path.dirname(sys.argv[0])}')
    # Logger().logger.info(f'local = {local}')
    # Logger().logger.info(f'executable = {sys.executable}')
    webview.create_window('BlockATM-Guard', 'http://www.baidu.com', width=1400, height=750)
    webview.start()

    #Logger().logger.info("webview end")
    time.sleep(1)

if __name__ == '__main__':
    main()