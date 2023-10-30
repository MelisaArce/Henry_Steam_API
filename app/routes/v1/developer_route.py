from fastapi import APIRouter
from app.utils.rest_util import get_valid_rest_object
import app.services.developer_service as developer_service

import app.config.configuration as conf
from app.config.vars import Vars
from app.model.developer import Developer,DeveloperSentiments,DeveloperHistory
from typing import List

URI = "/developers"
VERSION = "/v1"


blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI,tags=["developers"])

@blue_print.get('/top3/{year}', response_model=List[Developer])
def get_top3(year:int):
    top_3 = developer_service.get_top_3(year)
    return get_valid_rest_object(top_3)

@blue_print.get('/{developer}/sentiment', response_model=DeveloperSentiments)
def get_developer_sentiments(developer):
    sentiments = developer_service.get_sentiments(developer)
    return get_valid_rest_object(sentiments)

@blue_print.get('/{developer}/history', response_model=DeveloperHistory)
def get_developer_history(developer):
    sentiments = developer_service.get_history(developer)
    return get_valid_rest_object(sentiments)