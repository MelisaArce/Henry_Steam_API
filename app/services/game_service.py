from app.model.game import Game
import app.services.pandas_service as pandas_service
from typing import List


def suggest_by_game(item_id:str)->List[Game]:

    game_model_df = pandas_service.get_prediction_df()

    loaded_model = pandas_service.load_model()

    input_features = game_model_df[game_model_df['id_item'] == item_id].drop(["id_item","juego"],axis=1)  # Input features for a specific game
    similarity_scores = loaded_model.predict(input_features)

    # Assuming you have a list of all 'id_item' values
    all_id_items = game_model_df['id_item'].values

    all_game_names = game_model_df['juego'].values

    # Combine 'id_item' with similarity scores
    similarity_with_id_and_name = list(zip(all_id_items, all_game_names,similarity_scores[0]))

    # Sort by similarity scores in descending order
    similarity_with_id_and_name.sort(key=lambda x: x[2], reverse=True)

    # Get the top 5 similar items
    top_similar_items = [(item[0],item[1]) for item in similarity_with_id_and_name[1:6]]  # Exclude the input item

    return list(map(lambda i: Game.new(i[0],i[1]),top_similar_items))



