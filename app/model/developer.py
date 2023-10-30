from pydantic import BaseModel
from typing import List

class Developer(BaseModel):
    name : str = None

    def new(name:str):
        new_d=Developer()
        new_d.name = name

        return new_d

class DeveloperSentiments(BaseModel):
    name : str = None
    positive_quantity : int = None
    negative_quantity : int = None

class DeveloperYearlyHistory(BaseModel):
    items_quantity : int = None
    year : int = None
    free_items_quantity : int = None

    def new(items_quantity:int,year:int,free_items_quantity:int):
        new_d = DeveloperYearlyHistory()
        new_d.items_quantity = items_quantity
        new_d.year = year
        new_d.free_items_quantity = free_items_quantity
        
        return new_d

class DeveloperHistory(BaseModel):
    name : str = None
    historical: List[DeveloperYearlyHistory] = []