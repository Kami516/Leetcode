import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    new_animals = animals[animals['weight']>100]
    sorted_animals = new_animals.sort_values(by='weight', ascending=False)
    return sorted_animals[['name']]