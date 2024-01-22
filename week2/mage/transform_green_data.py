import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def camel_to_snake(column_name):
    result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', column_name)
    result = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', result)  # Handle consecutive uppercase letters
    return result.lower()


@transformer
def transform(data, *args, **kwargs):
    print(f"Preprocessing: rows with zero passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing: rows with zero trip_distance: {data['trip_distance'].isin([0]).sum()}")

    data = data[(data["passenger_count"] > 0) & (data["trip_distance"] > 0)]
    data["lpep_pickup_date"] = data["lpep_pickup_datetime"].dt.date
    data.columns = [camel_to_snake(col) for col in data.columns]

    return data


@test
def test_output(output, *args) -> None:
    assert output['vendor_id'].isin([1,2,3]).all(), 'vendor_id is of list 1,2 or 3'
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with 0 passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with 0 distance'
