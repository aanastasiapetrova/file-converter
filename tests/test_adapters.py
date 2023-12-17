from copy import deepcopy

def test_json_adapter_by_json_parsed_data(json_adapter, parsed_json_data):
    """Test replace name of object's list from items to records in json adapter."""

    data_before_adapter = deepcopy(parsed_json_data)

    data_after_adapter = json_adapter.adapt(parsed_json_data)

    assert 'records' in list(data_after_adapter.keys())
    assert len(data_after_adapter['records']) == len(data_before_adapter['items'])


def test_json_adapter_by_items_in_json_parsed_data(json_adapter, parsed_json_data):
    """Test replace date_published key name to date and change structure of author value in json adapter."""

    items_after_adapter = json_adapter.adapt(parsed_json_data)['records']

    assert 'date_published' not in list(items_after_adapter[0].keys())
    assert 'date' in list(items_after_adapter[0].keys())
    assert isinstance(items_after_adapter[0]['author'], dict)


def test_rss_adapter_by_rss_parsed_data(rss_adapter, parsed_rss_data):
    """Test replace name of object's list from items to records in rss adapter."""

    data_before_adapter = deepcopy(parsed_rss_data)

    data_after_adapter = rss_adapter.adapt(parsed_rss_data)

    assert 'records' in list(data_after_adapter.keys())
    assert len(data_after_adapter['records']) == len(data_before_adapter['channel']['item'])


def test_rss_adapter_by_items_in_rss_parsed_data(rss_adapter, parsed_rss_data):
    """Test replace pubDate key name to date and change structure of author value in rss adapter."""

    items_after_adapter = rss_adapter.adapt(parsed_rss_data)['records']

    assert 'pubDate' not in list(items_after_adapter[0].keys())
    assert 'date' in list(items_after_adapter[0].keys())
    assert isinstance(items_after_adapter[0]['author'], dict)


def test_atom_adapter_by_atom_parsed_data(atom_adapter, parsed_atom_data):
    """Test replace name of object's list from items to records in atom adapter."""

    data_before_adapter = deepcopy(parsed_atom_data)

    data_after_adapter = atom_adapter.adapt(parsed_atom_data)

    assert 'records' in list(data_after_adapter.keys())
    assert len(data_after_adapter['records']) == len(data_before_adapter['entry'])


def test_atom_adapter_by_items_in_atom_parsed_data(atom_adapter, parsed_atom_data):
    """Test replace published key name to date and change structure of author value in atom adapter."""

    items_after_adapter = atom_adapter.adapt(parsed_atom_data)['records']

    assert 'published' not in list(items_after_adapter[0].keys())
    assert 'date' in list(items_after_adapter[0].keys())
    assert isinstance(items_after_adapter[0]['author'], dict)

