from app.model.developer import Developer,DeveloperSentiments,DeveloperHistory,DeveloperYearlyHistory
import app.services.pandas_service as pandas_service
from typing import List


def get_top_3(year:int)->List[Developer]:
    top_3_df = pandas_service.get_top_3_df()
    top_3_df = top_3_df[top_3_df["anio"]==str(year)]

    top_3_df = top_3_df.sort_values("comentarios_positivos",ascending=False)

    return top_3_df["desarrolladora"].head(3).apply(Developer.new).tolist()


def get_sentiments(developer:str)->DeveloperSentiments:
    dev_sentiments = DeveloperSentiments()
    dev_sentiments.name = developer

    dev_sentiments_df = pandas_service.get_dev_sentiments_df()
    dev_sentiments_df = dev_sentiments_df[dev_sentiments_df["desarrolladora"]==developer]

    dev_sentiments.positive_quantity = int(dev_sentiments_df.iloc[0]["positivos"])
    dev_sentiments.negative_quantity = int(dev_sentiments_df.iloc[0]["negativos"])

    return dev_sentiments

def get_history(developer:str)->DeveloperHistory:
    history = DeveloperHistory()
    history.name = developer

    dev_history_df = pandas_service.get_dev_history_df()
    dev_history_df = dev_history_df[dev_history_df["desarrolladora"]==developer]

    history.historical = dev_history_df.apply(lambda r:DeveloperYearlyHistory.new(int(r["total_items"]),int(r["anio"]),int(r["total_free_items"])),axis=1).tolist()

    return history














