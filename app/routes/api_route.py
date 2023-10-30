from fastapi import APIRouter

import app.config.configuration as var
from app.utils.logger_util import get_logger
from app.model.exception import AppException

blue_print = APIRouter(prefix='',tags=["monitoring"])

logger = get_logger()


@blue_print.get('/vars')
def variables():
    return var.variables_cargadas()


@blue_print.get('/errors')
def error():
    raise AppException(409, 'No Wanda Nara!')


@blue_print.get('/ping')
def alive():
    logger.info("piiing")
    return "pong"