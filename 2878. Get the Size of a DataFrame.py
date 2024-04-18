import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    s = []
    s.append(players.shape[0])
    s.append(players.shape[1])
    return s