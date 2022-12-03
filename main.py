from sensor.configs.mongo_db_Connection import MongoDBClient
from sensor.exception import Sensor_Exception
from sensor.pipeline.training_pipeline import TrainPipeline
import sys

import warnings

if __name__ == '__main__':

    warnings.filterwarnings('ignore')
    
    ''' Testing the MongoDB Connection '''
    # mongoDb_client = MongoDBClient()
    # print(mongoDb_client.database.list_collection_names())

    ''' Testing the Exception logic of Sensor_Exception '''
    # try:
    #     x = 1/0
    # except Exception as e:
    #     raise Sensor_Exception(e, sys)
    
    ''' Testing data ingestion feature store '''
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        print(e)
    
