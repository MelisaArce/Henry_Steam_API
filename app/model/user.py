from pydantic import BaseModel
from typing import List

class YearlyPlay(BaseModel):
    year : int = None
    hours : float = None

    def new(year:int,hours:float):
        new_y = YearlyPlay()
        new_y.year = year
        new_y.hours = hours

        return new_y

class UserAddiction(BaseModel):
    user_id : str = None
    genre : str = None
    yearly_played_hours : List[YearlyPlay] = []

class User(BaseModel):
    user_id : str = None
    review_percentage : float = 0
    money_spent : float = 0
    item_count : int = 0