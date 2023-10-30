from pydantic import BaseModel

class Game(BaseModel):
    item_id : str = None
    name : str = None

    def new(item_id:str,name:str):
        new_g = Game()
        new_g.item_id = item_id
        new_g.name = name

        return new_g