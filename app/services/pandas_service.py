import pandas as pd
import pickle

USER_DATA_FILE_PARQUET="files/datasets/user_data.parquet"
GENRE_TOP_PLAYER_FILE_PARQUET="files/datasets/genre_top_player.parquet"
DEVELOPER_HISTORY_FILE_PARQUET="files/datasets/dev_history.parquet"
DEVELOPER_SENTIMENT_FILE_PARQUET="files/datasets/dev_sentiments.parquet"
TOP_3_FILE_PARQUET="files/datasets/top_3.parquet"
PREDICTION_FILE_PARQUET="files/datasets/prediction_df.parquet"

MODEL_FILE = "files/cosine_similarity_model.pkl"

def _get_df(path:str):
    return pd.read_parquet(path, engine='pyarrow')

def get_user_data_df():
    return _get_df(USER_DATA_FILE_PARQUET)

def get_genre_top_players_df():
    return _get_df(GENRE_TOP_PLAYER_FILE_PARQUET)

def get_dev_history_df():
    return _get_df(DEVELOPER_HISTORY_FILE_PARQUET)

def get_dev_sentiments_df():
    return _get_df(DEVELOPER_SENTIMENT_FILE_PARQUET)

def get_top_3_df():
    return _get_df(TOP_3_FILE_PARQUET)

def get_prediction_df():
    return _get_df(PREDICTION_FILE_PARQUET)

def load_model():
    with open(MODEL_FILE, 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    return loaded_model

