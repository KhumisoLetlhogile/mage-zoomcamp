import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    3 urls for the last quarter of 2020
    """
    url1 ='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url2 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url3 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'

    data_types = {
         'VendorID': pd.Int64Dtype(),
         'store_and_fwd_flag ': str,
         'RatecodeID ': pd.Int64Dtype(),
         'PULocationID': pd.Int64Dtype(),
         'DOLocationID': pd.Int64Dtype(),
         'passenger_count': pd.Int64Dtype(),
         'trip_distance': float,
         'fare_amount': float,
         'extra': float,
         'mta_tax': float,
         'tip_amount': float,
         'tolls_amount': float,
         'ehail_fee': float,
         'improvement_surcharge': float,
         'total_amount': float,
         'payment_type': pd.Int64Dtype(),
         'trip_type': pd.Int64Dtype(),
         'congestion_surcharge': float
    }

    parsing_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']

    "A list of urls"
    file_path = [url1,url2,url3]

    "Empty dataframe dictionary"
    dataframes = {}
    
    for i in file_path:
        "Read the 3 csv and store them in dataframes dictionary"
        dataframes[i] = pd.read_csv(f"{i}", sep=',', compression='gzip', parse_dates = parsing_dates )

    return pd.concat(
        [dataframes[file_path[0]],
        dataframes[file_path[1]],
        dataframes[file_path[2]]],axis=0
    )
    
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
