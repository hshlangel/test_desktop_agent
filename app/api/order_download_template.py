# -*- coding:utf-8 -*-
import traceback
from typing import List
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse
from fastapi import UploadFile
from utils.logger import Logger
from utils.tool import get_run_dir
from core.exceptions import Exceptions
from utils.cache import AppCache

# 下載訂單模板
class APIOrderDownloadTemplate():
    
    @staticmethod
    def handle_request():
        try:

            login_chainid:str = AppCache().get_login_chain()
            login_network:str = AppCache().get_chain_network(login_chainid)
            
            file_path = f'{get_run_dir()}/templates/BlockTemplate_{login_network.replace(' ', '')}.xlsx'
            filename = f'BlockTemplate_{login_network.replace(' ', '')}.xlsx'

            Logger().logger.info(f'file_path = {file_path}, filename = {filename}')

            Logger().logger.info("download order template")
            return FileResponse(path=file_path, filename=filename)
        
        except Exception as err:
            Logger().logger.error('{} :{}'.format(err, str(traceback.format_exc())))
