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
            
            file_path = f'{get_run_dir()}/templates/Bulk Payout Template.xlsx'
            filename = 'Bulk Payout Template.xlsx'

            Logger().logger.info("download order template")
            return FileResponse(path=file_path, filename=filename)
        
        except Exception as err:
            Logger().logger.error('{} :{}'.format(err, str(traceback.format_exc())))
