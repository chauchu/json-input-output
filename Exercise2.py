import json
import pandas as pd


# load the json file
def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


# create a dataframe from the json file
def genDF(path):
    data = getJSON(path)
    df = pd.DataFrame.from_dict(data, orient='index').reset_index()
    df = df.rename(columns={'index': 'Fullname'})
    return df


# get the statistic information from the file
def getFreq(dataframe):
    nga = {}  # create an empty dictionary
    name = dataframe.groupby('last_name')['last_name'].count().to_dict()
    people = df1.last_name.unique()

    """
    Here I create a loop to count the frequency the lastname, age, address and occupation.
    After that the categories and numbers are put in the dictionary
    """

    for p in people:
        occ = dataframe[dataframe['last_name'] == p].groupby('occupation').count()['last_name'].to_dict()
        add = df1[df1['last_name'] == p].groupby('address').count()['last_name'].to_dict()
        age = df1[df1['last_name'] == p].groupby('age').count()['last_name'].to_dict()
        age = {k: v for k, v in age.items() if v != 0}
        nga[p] = ({'count': name[p]}, {'age': age}, {'address': add}, {'occupation': occ})
    return nga


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="file json input")
    parser.add_argument('path', help="The path to the input file.")

    args = parser.parse_args()
    path = args.path

    df = genDF(path)

    df.to_csv('data-exercise2.csv', index=False)

    df['last_name'] = df['Fullname'].apply(lambda x: x.split()[1])
    df1 = df.drop('Fullname', axis=1)

    nga = getFreq(df1)

    # export to json file
    json_object = json.dumps(nga, indent=4)
    with open("statistic.json", "w") as outfile:
        outfile.write(json_object)