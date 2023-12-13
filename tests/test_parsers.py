import pytest
import file_converter.parsers as parsers


def test_json_parser_by_json_file(json_file):
    data = parsers.parsers_manager.get_parser('json').parse(json_file)
    assert data == {'id': 1, 'title': 'test', 'text': 'lorem ipsum dolor', 'author': 'unknown', 'date': '2023-12-10'}


def test_xml_parser_by_rss_file(rss_file):
    data = parsers.parsers_manager.get_parser('rss').parse(rss_file)
    assert data == {'channel':
                        {'title': 'W3Schools Home Page',
                         'link': 'https://www.w3schools.com',
                         'description': 'Free web building tutorials',
                         'item': [
                                    {'title': 'RSS Tutorial',
                                     'link': 'https://www.w3schools.com/xml/xml_rss.asp',
                                     'description': 'New RSS tutorial on W3Schools'},
                                    {'title': 'XML Tutorial',
                                     'link': 'https://www.w3schools.com/xml',
                                     'description': 'New XML tutorial on W3Schools'}
                                 ]}}
    

def test_xml_parser_by_atom_file(atom_file):
    data = parsers.parsers_manager.get_parser('atom').parse(atom_file)
    assert data == {'title': 'dive into mark',
                    'subtitle': 'A <em>lot</em> of effort went into making this effortless',
                    'updated': '2005-07-31T12:29:29Z',
                    'id': 'tag:example.org,2003:3',
                    'link': [{'rel': 'alternate',
                              'type': 'text/html',
                              'hreflang': 'en',
                              'href': 'http://example.org/'},
                            {'rel': 'self', 'type': 'application/atom+xml',
                             'href': 'http://example.org/feed.atom'}],
                    'rights': 'Copyright (c) 2003, Mark Pilgrim',
                    'generator': 'Example Toolkit',
                    'entry': {'title': 'Atom draft-07 snapshot',
                              'link': [{'rel': 'alternate',
                                        'type': 'text/html',
                                        'href': 'http://example.org/2005/04/02/atom'},
                                        {'rel': 'enclosure', 'type': 'audio/mpeg',
                                         'length': '1337',
                                         'href': 'http://example.org/audio/ph34r_my_podcast.mp3'}],
                    'id': 'tag:example.org,2003:3.2397', 'updated': '2005-07-31T12:29:29Z',
                    'published': '2003-12-13T08:29:29-04:00',
                    'author': {'name': 'Mark Pilgrim',
                               'uri': 'http://example.org/',
                               'email': 'f8dy@example.com'},
                    'contributor': {'name': 'Sam Ruby'}}}
