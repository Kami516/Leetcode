import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    sorted_world = world[(world['population'] >= 25000000) | (world['area'] >= 3000000)]
    return sorted_world[['name','population','area']]