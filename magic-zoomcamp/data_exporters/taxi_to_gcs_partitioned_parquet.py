import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/neon-opus-412521-c07fddb18017.json'

bucket_name = 'mage-zoomcamp-khumiso-let'
project_id = 'neon-opus-412521'
table_name = 'nyc_taxi_data'

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    data['tpep_pickup_date'] = data['tpep_pickup_datetime'].dt.date

    table2 = pa.Table.from_pandas(data)
    
    gcs = pa.fs.GcsFileSystem() #File system object that will authorise using
    #using our enviroment variable automatically
    pq.write_to_dataset(
        table2,
        root_path = root_path,
        partition_cols = ['tpep_pickup_date'],
        filesystem = gcs
    )


