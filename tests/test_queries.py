import pytest
from file_converter.exceptions import SortDirectionIsIncorrectException, LimitValueIsIncorrect


def test_sort_method_in_straight_direction_by_json(parsed_json_data, json_query):
    """Test sort method of json query class with asc parameter."""

    sorted_items = [item['date_published'] for item in json_query.sort('asc', parsed_json_data)['items']]

    assert sorted_items[0] == min(sorted_items)
    assert sorted_items[-1] == max(sorted_items)


def test_sort_method_in_reverse_direction_by_json(parsed_json_data, json_query):
    """Test sort method of json query class with desc parameter."""

    sorted_items = [item['date_published'] for item in json_query.sort('desc', parsed_json_data)['items']]

    assert sorted_items[0] == max(sorted_items)
    assert sorted_items[-1] == min(sorted_items)


def test_sort_method_by_incorrect_sort_direction_by_json(parsed_json_data, json_query):
    """Test sort method of json query class with incorrect parameter."""

    with pytest.raises(SortDirectionIsIncorrectException):
        json_query.sort('test', parsed_json_data)


def test_filter_method_by_json(parsed_json_data, json_query):
    """Test filter method of json query class with existing name parameter."""

    filtered_items = [item['author']['name'] for item in json_query.filter('Brent Simmons', parsed_json_data)['items']]
    unique_filtered_items = set(filtered_items)

    assert len(filtered_items) == 2
    assert len(unique_filtered_items) == 1


def test_filter_method_with_unexisting_value_by_json(parsed_json_data, json_query):
    """Test filter method of json query class with unexisting name parameter."""

    filtered_items = [item['author']['name'] for item in json_query.filter('Brent', parsed_json_data)['items']]

    assert len(filtered_items) == 0


def test_limit_method_with_value_less_than_items_by_json(parsed_json_data, json_query):
    """Test limit method of json query class with parameter less than items amount."""

    items_before_limit = parsed_json_data['items']
    items_after_limit = json_query.limit('1', parsed_json_data)['items']

    assert len(items_before_limit) != len(items_after_limit)
    assert len(items_after_limit) == 1


def test_limit_method_with_value_greater_than_items_by_json(parsed_json_data, json_query):
    """Test limit method of json query class with parameter greater than items amount."""

    items_before_limit = parsed_json_data['items']
    items_after_limit = json_query.limit(f'{len(items_before_limit)+1}', parsed_json_data)['items']

    assert len(items_before_limit) == len(items_after_limit)


def test_limit_method_with_incorrect_value_by_json(parsed_json_data, json_query):
    """Test limit method of json query class with incorrect parameter."""

    with pytest.raises(LimitValueIsIncorrect):
        json_query.limit('test', parsed_json_data)


def test_sort_method_in_straight_direction_by_rss(parsed_rss_data, rss_query):
    """Test sort method of rss query class with asc parameter."""

    sorted_items = [item['pubDate'] for item in rss_query.sort('asc', parsed_rss_data)['channel']['item']]

    assert sorted_items[0] == min(sorted_items)
    assert sorted_items[-1] == max(sorted_items)


def test_sort_method_in_reverse_direction_by_rss(parsed_rss_data, rss_query):
    """Test sort method of rss query class with desc parameter."""

    sorted_items = [item['pubDate'] for item in rss_query.sort('desc', parsed_rss_data)['channel']['item']]

    assert sorted_items[0] == max(sorted_items)
    assert sorted_items[-1] == min(sorted_items)


def test_sort_method_by_incorrect_sort_direction_by_rss(parsed_rss_data, rss_query):
    """Test sort method of rss query class with incorrect parameter."""

    with pytest.raises(SortDirectionIsIncorrectException):
        rss_query.sort('test', parsed_rss_data)


def test_filter_method_by_rss(parsed_rss_data, rss_query):
    """Test filter method of rss query class with existing name parameter."""

    filtered_items = [item['author'] for item in rss_query.filter('Brent Simmons', parsed_rss_data)['channel']['item']]
    unique_filtered_items = set(filtered_items)

    assert len(filtered_items) == 2
    assert len(unique_filtered_items) == 1


def test_filter_method_with_unexisting_value(parsed_rss_data, rss_query):
    """Test filter method of rss query class with unexisting name parameter."""

    filtered_items = [item['author'] for item in rss_query.filter('Brent', parsed_rss_data)['channel']['item']]

    assert len(filtered_items) == 0


def test_limit_method_with_value_less_than_items_by_rss(parsed_rss_data, rss_query):
    """Test limit method of rss query class with parameter less than items amount."""

    items_before_limit = parsed_rss_data['channel']['item']
    items_after_limit = rss_query.limit('1', parsed_rss_data)['channel']['item']

    assert len(items_before_limit) != len(items_after_limit)
    assert len(items_after_limit) == 1


def test_limit_method_with_value_greater_than_items_by_rss(parsed_rss_data, rss_query):
    """Test limit method of rss query class with parameter greater than items amount."""

    items_before_limit = parsed_rss_data['channel']['item']
    items_after_limit = rss_query.limit(f'{len(items_before_limit)+1}', parsed_rss_data)['channel']['item']

    assert len(items_before_limit) == len(items_after_limit)


def test_limit_method_with_incorrect_value_by_rss(parsed_rss_data, rss_query):
    """Test limit method of rss query class with incorrect parameter."""

    with pytest.raises(LimitValueIsIncorrect):
        rss_query.limit('test', parsed_rss_data)


def test_sort_method_in_straight_direction_by_atom(parsed_atom_data, atom_query):
    """Test sort method of atom query class with asc parameter."""

    sorted_items = [item['published'] for item in atom_query.sort('asc', parsed_atom_data)['entry']]

    assert sorted_items[0] == min(sorted_items)
    assert sorted_items[-1] == max(sorted_items)


def test_sort_method_in_reverse_direction_by_atom(parsed_atom_data, atom_query):
    """Test sort method of atom query class with desc parameter."""

    sorted_items = [item['published'] for item in atom_query.sort('desc', parsed_atom_data)['entry']]

    assert sorted_items[0] == max(sorted_items)
    assert sorted_items[-1] == min(sorted_items)


def test_sort_method_by_incorrect_sort_direction_by_atom(parsed_atom_data, atom_query):
    """Test sort method of atom query class with incorrect parameter."""

    with pytest.raises(SortDirectionIsIncorrectException):
        atom_query.sort('test', parsed_atom_data)


def test_filter_method_by_atom(parsed_atom_data, atom_query):
    """Test filter method of atom query class with existing name parameter."""

    filtered_items = [item['author']['name'] for item in atom_query.filter('Brent Simmons', parsed_atom_data)['entry']]
    unique_filtered_items = set(filtered_items)

    assert len(filtered_items) == 2
    assert len(unique_filtered_items) == 1


def test_filter_method_with_unexisted_value(parsed_atom_data, atom_query):
    """Test filter method of atom query class with unexisting name parameter."""

    filtered_items = [item['author']['name'] for item in atom_query.filter('Brent', parsed_atom_data)['entry']]

    assert len(filtered_items) == 0


def test_limit_method_with_value_less_than_items_by_atom(parsed_atom_data, atom_query):
    """Test limit method of atom query class with parameter less than items amount."""

    items_before_limit = parsed_atom_data['entry']
    items_after_limit = atom_query.limit('1', parsed_atom_data)['entry']

    assert len(items_before_limit) != len(items_after_limit)
    assert len(items_after_limit) == 1


def test_limit_method_with_value_greater_than_items_by_atom(parsed_atom_data, atom_query):
    """Test limit method of atom query class with parameter greater than items amount."""

    items_before_limit = parsed_atom_data['entry']
    items_after_limit = atom_query.limit(f'{len(items_before_limit)+1}', parsed_atom_data)['entry']

    assert len(items_before_limit) == len(items_after_limit)


def test_limit_method_with_incorrect_value_by_atom(parsed_atom_data, atom_query):
    """Test limit method of atom query class with incorrect parameter."""

    with pytest.raises(LimitValueIsIncorrect):
        atom_query.limit('test', parsed_atom_data)