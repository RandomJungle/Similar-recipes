'''
Module to extract dataset, gather data into processable form
dataset used is a kaggle recipes dataset from epicurious, link : https://www.kaggle.com/hugodarwood/epirecipes

'''
import json
import re
import settings

def extract_json(datafile):
    """
    open json file and extract list of dict from it
    
    Parameters
    ----------
    datafile : string
        Name of file containing data in json format
        
    Returns
    -------
    data : list
        list of dict of all samples
    """
    with open(datafile, "r", encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    return data

def strip(data, keys):
    """
    extract subset of dataset with key elements
    
    Parameters
    ----------
    data : list
        list of dict of al samples
    keys : list
        list of keys to be kept in dicts
        
    Returns
    -------
    data : list
        list of dict of all samples, with only key elements
    """
    for sample in data :
        for key in sample.copy() :
            if key not in keys :
                sample.pop(key, None)
    return data

def execute():
    """
    execute methods extract_json and strip to produce usable dataset
    """
    result = []
    data = extract_json(settings.FILE)
    data = strip(data, settings.KEYS)
    for sample in data :
        if 'directions' in sample and 'title' in sample :
            sample['title'] = re.sub(' $', '', sample['title'])
            result.append(sample)
    return result
                      
if __name__ == '__main__':

    data = extract_json(settings.FILE)
    subdata = strip(data, settings.KEYS)
    