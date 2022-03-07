import argparse
import pandas as pd
import os
os.makedirs('regiones', exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument("file", help="path csv file")
args = parser.parse_args()

data = pd.read_csv(args.file, encoding='latin-1')

regiones = data.REGION.unique()

for region in regiones:
    data_region = data[data['REGION'] == region]
    data_region.to_csv('regiones/' + region.lower() + '.csv', index=False)
