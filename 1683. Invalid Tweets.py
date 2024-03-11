import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    t = tweets[tweets['content'].str.len() > 15]
    r = t[['tweet_id']]
    return r