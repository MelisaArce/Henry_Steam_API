from app.model.user import User,UserAddiction,YearlyPlay
import app.services.pandas_service as pandas_service
import numpy as np


def get_user(user_id:str)->User:
    user = User()
    user.user_id = user_id

    user_data_df = pandas_service.get_user_data_df()
    user_data_df = user_data_df[user_data_df["id_usuario"]==user_id]

    user.money_spent = float(user_data_df.iloc[0]["dinero_gastado"])
    user.item_count = int(user_data_df.iloc[0]["cantidad_items"])

    user.review_percentage = float(user_data_df.iloc[0]["porcentaje_recomendado"])

    return user

def most_addictive(genre:str)->UserAddiction:
    addiction = UserAddiction()
    addiction.genre = genre

    genre_top_players_df = pandas_service.get_genre_top_players_df()
    genre_top_players_df = genre_top_players_df[genre_top_players_df["genero"]==genre]

    addiction.user_id = genre_top_players_df.iloc[0]["id_usuario"]

    addiction.yearly_played_hours = genre_top_players_df.apply(lambda r: YearlyPlay.new(int(r["anio_juego"]),float(r["tiempo_jugado_genero_anio"])),axis=1).tolist()

    return addiction



    



