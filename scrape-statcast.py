from typing import List, Any

from pybaseball import statcast
import pandas as pd
from datetime import datetime

#datetime.today()
dtlst22 = pd.date_range(start = "2022-04-07", end = datetime.today()).date.tolist()
dtlst21 = pd.date_range(start = "2021-04-01", end = "2021-10-03").date.tolist()
dtlst20 = pd.date_range(start = "2020-07-23", end = "2020-09-27").date.tolist()
dtlst19 = pd.date_range(start = "2019-03-20", end = "2019-09-29").date.tolist()
dtlst18 = pd.date_range(start = "2018-03-29", end = "2018-10-01").date.tolist()

error_lst = []

def main(dt):
    data = statcast(start_dt=dt, end_dt=dt)
    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":


    # 2022
    df_empy22 = pd.DataFrame()

    for i in dtlst22:
        print(i)
        df_empy22 = pd.concat([df_empy22, main(i.strftime('%Y-%m-%d'))])
    df_empy22.to_csv("statcast22.csv")

    # 2021
    df_empy21 = pd.DataFrame()

    for i in dtlst21:
        print(i)
        df_empy21 = pd.concat([df_empy21, main(i.strftime('%Y-%m-%d'))])
    df_empy21.to_csv("statcast21.csv")

    # 2020
    df_empy20 = pd.DataFrame()

    for i in dtlst20:
        print(i)
        df_empy20 = pd.concat([df_empy20, main(i.strftime('%Y-%m-%d'))])
    df_empy20.to_csv("statcast20.csv")

    # 2019
    df_empy19 = pd.DataFrame()

    for i in dtlst19:
        print(i)
        df_empy19 = pd.concat([df_empy19, main(i.strftime('%Y-%m-%d'))])
    df_empy19.to_csv("statcast19.csv")

    # 2018
    df_empy18 = pd.DataFrame()

    for i in dtlst18:
        print(i)
        df_empy19 = pd.concat([df_empy18, main(i.strftime('%Y-%m-%d'))])
    df_empy18.to_csv("statcast18.csv")
