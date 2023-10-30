from fastapi import APIRouter
from app.utils.rest_util import get_valid_rest_object
import app.services.user_service as user_service

import app.config.configuration as conf
from app.config.vars import Vars
from app.model.user import UserAddiction
from typing import List

URI = "/genres"
VERSION = "/v1"

blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI,tags=["genres"])

@blue_print.get('/{genre}/users/top', response_model=UserAddiction)
def get_top_user(genre):
    user_addiction = user_service.most_addictive(genre)
    return get_valid_rest_object(user_addiction)