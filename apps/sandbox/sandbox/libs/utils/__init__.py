import json
from typing import Dict, List
from pyspark.sql import DataFrame


def df2list(df:DataFrame) -> List[Dict]:
 
    json_list = df.toJSON().collect()
    
    ans :List[Dict]= [json.loads(j) for j in json_list]

    return ans