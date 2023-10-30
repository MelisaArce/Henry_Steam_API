from fastapi import APIRouter
from app.utils.rest_util import get_valid_rest_object
import app.services.game_service as game_service

import app.config.configuration as conf
from app.config.vars import Vars
from app.model.game import Game
from typing import List

URI = "/games"
VERSION = "/v1"


blue_print = APIRouter(prefix=conf.get(Vars.API_BASE_PATH)+VERSION+URI,tags=["games"])

@blue_print.get('/{item_id}/suggest', response_model=List[Game])
def suggest_game(item_id):
    game = game_service.suggest_by_game(item_id)
    return get_valid_rest_object(game)