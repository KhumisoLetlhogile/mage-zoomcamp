if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.
    """
    # Specify your transformation logic here
    data = data[data['passenger_count']>0]
    data = data[data['trip_distance']>0]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.columns = (data.columns
                    .str.replace(' ','_')
                    .str.lower()
    )
    print(data['vendorid'].unique()) #distict value of vendor ID
    return data

@test
def test_output(output, *args) -> None:
    column_name = 'vendorid'
    assert column_name in output.columns, f"Column '{column_name}' is not present in the DataFrame."

@test
def test_output(output, *args) -> None:
    assert (output['passenger_count']>0).all(), 'Passenger_count is NOT greater than 0'

@test
def test_output(output, *args) -> None:    
    assert (output['trip_distance']>0).all(), 'Passenger_count is NOT greater than 0'