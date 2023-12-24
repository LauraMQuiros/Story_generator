import pandas as pd
from pathlib import Path


def explore_data(df):
    """
    Explore the data by printing the first 5 rows and the shape of the dataframe.
    :param df: dataframe to explore
    :return: None
    """
    print(df.head())
    print(df.shape)


if __name__ == '__main__':
    data_path = Path(__file__).parent.parent / 'data' / 'stories.csv'
    df = pd.read_csv(data_path)
