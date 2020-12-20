import pandas as pd
import json
import numpy as np
import os
import sys
import pickle
import math
import itertools

this_dir = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.append(this_dir)

from look_up_table import LOOK_UP_TABLE, COLUMN_INPUTS, COLUMN_OUTPUTS

def group_by_kpi(df):
    """This groups adverts first by their  first key and then the version and sums their KPI's 
    for all the adverts runned irrespective of the time and location, this is grouped by their impression
    first_dropped, and click-through-event"""
    #this was not called actually
    kpis = ['impression', 'first_dropped', 'click-through-event']
    
    first_key_version = ['first_key', 'version']

    df = df.groupby(first_key_version)[kpis].sum()
    df.reset_index(inplace=True)

    return df


def get_dct_kpis_from_row(row):
    """This returns the KPI's for previous ads that had been run by Adludio's company and returns 
    it as a dictionary"""
    return {
        'impressions': row['impression'],
        'engagements': row['first_dropped'],
        'clicks_through': row['click-through-event'],
        'engagement_rate': row['engagement_rate'],
        'click_through_rate': row['click_through_rate']
    }


def get_dct_features_for_game(first_key, version):
    """ asd"""
    features = get_features()
    for fk in features:
        for v in features[fk]:
            if fk == first_key and v == version:
                return features[fk][v]


def get_ouput(df):
    """iterates over a dataframe to get values for the first key and version for the dataframe this is then 
    used to create a game key which is then used to uniquely identify any query sent and used to
    uniquely save a query to output"""
    output = {}
    for _, row in df.iterrows():

        first_key = row['first_key']
        version = row['version']
        game_key = f"{first_key}/{version}"

        output[game_key]['kpis'] = get_dct_kpis_from_row(row)
        output[game_key]['url'] = get_preview_url(game_key)
        output[game_key] = get_dct_features_for_game(first_key,version)

    return output

def get_preview_url(game_key):
    return f"https://preview.adludio.com/{game_key}"
