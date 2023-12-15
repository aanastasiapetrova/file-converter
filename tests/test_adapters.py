import pytest

def test_json_adapter_by_json_parsed_data(json_adapter, parsed_json_data):
    data_before_adapter = parsed_json_data.copy()

    data_after_adapter = json_adapter.adapt(parsed_json_data)

    assert 'records' in list(data_after_adapter.keys())
    assert len(data_after_adapter['records']) == len(data_before_adapter['items'])

