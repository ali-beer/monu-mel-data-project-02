from flask_restful import Resource
from flask import request
import pandas as pd
import json

# ibra = pd.read_csv('data/ibra.csv', delimiter=',', header=0, index_col=False, low_memory=False)
# ibra_bioregions = pd.read_csv('data/ibra_bioregions.csv', delimiter=',', header=0, index_col=False, low_memory=False)
ibra_df = pd.read_csv('data/ibra_bioregions_w_total_ce.csv', delimiter=',', header=0, index_col=False, low_memory=False)

# IUCN
bioregion_by_IUCN_df = pd.read_csv('data/bioregion_by_IUCN.csv', delimiter=',', header=0, index_col=False, low_memory=False)
IUCN_category_df = pd.read_csv('data/IUCN_category.csv', delimiter=',', header=0, index_col=False, low_memory=False)

ibra_df_json = json.loads(ibra_df.to_json(orient="records"))
iucn_df_json = json.loads(bioregion_by_IUCN_df.to_json(orient="records"))

with open('data/sunburst_graph_data.json') as json_file:
    sunburst_json = json.load(json_file)


class WelcomeAPI(Resource):
    def get(self):
        ret = ({"message": "Welcome! Go to /api/ibra for IBRA data, or go to /api/iucn for IUCN data"}, 200)
        return ret[0], ret[1]


class IBRA_API(Resource):
    global ibra_df_json

    def get(self):
        ret = (ibra_df_json, 200)
        return ret[0], ret[1]

class IUCN_API(Resource):
    global iucn_df_json

    def get(self):
        ret = (iucn_df_json, 200)
        return ret[0], ret[1]

class SUNBURST_API(Resource):
    global sunburst_json

    def get(self):
        ret = (sunburst_json, 200)
        return ret[0], ret[1]

