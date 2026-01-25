import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    df = views[(views['author_id']) == (views['viewer_id'])]
    df = df[['author_id']].rename(columns={'author_id': 'id'} )
    sorted_df = df[['id']].sort_values(by=['id'])
    sorted_df = sorted_df.drop_duplicates()
    
    return sorted_df[['id']]