import pytest

import file_converter.parsers as parsers


@pytest.fixture
def parsed_json_reference():
    return {
        "version": "https://jsonfeed.org/version/1",
        "title": "The Record",
        "home_page_url": "http://therecord.co/",
        "feed_url": "http://therecord.co/feed.json",
        "items": [
            {
                "id": "http://therecord.co/chris-parrish",
                "title": "Special #1 - Chris Parrish",
                "author": {"name": "Brent Simmons"},
                "date_published": "2014-05-09T14:04:00-07:00",
            },
            {
                "id": "http://therecord.co/chris-parrish",
                "title": "Special #2 - Chris Parrish",
                "author": {"name": "Mark Thompson"},
                "date_published": "2015-05-09T14:04:00-07:00",
            },
            {
                "id": "http://therecord.co/chris-parrish",
                "title": "Special #3 - Chris Parrish",
                "author": {"name": "Brent Simmons"},
                "date_published": "2013-05-09T14:04:00-07:00",
            },
        ],
    }


@pytest.fixture
def parsed_rss_reference():
    return {
        "channel": {
            "title": "W3Schools Home Page",
            "link": "https://www.w3schools.com",
            "description": "Free web building tutorials",
            "item": [
                {
                    "title": "RSS Tutorial",
                    "author": "Brent Simmons",
                    "link": "https://www.w3schools.com/xml/xml_rss.asp",
                    "description": "New RSS tutorial on W3Schools",
                    "pubDate": "Tue, 19 Oct 2004 11:09:11 -0400",
                },
                {
                    "title": "XML Tutorial",
                    "author": "Mark Thompson",
                    "link": "https://www.w3schools.com/xml",
                    "description": "New XML tutorial on W3Schools",
                    "pubDate": "Tue, 19 Oct 2004 11:09:09 -0400",
                },
                {
                    "title": "XML Tutorial II",
                    "author": "Brent Simmons",
                    "link": "https://www.w3schools.com/xml",
                    "description": "New XML tutorial on W3Schools",
                    "pubDate": "Tue, 19 Oct 2004 11:09:07 -0400",
                },
            ],
        }
    }


@pytest.fixture
def parsed_atom_reference():
    return {
        "title": "dive into mark",
        "subtitle": "effort went into making this effortless",
        "updated": "2005-07-31T12:29:29Z",
        "id": "tag:example.org,2003:3",
        "link": [
            {
                "rel": "alternate",
                "type": "text/html",
                "hreflang": "en",
                "href": "http://example.org/",
            },
            {
                "rel": "self",
                "type": "application/atom+xml",
                "href": "http://example.org/feed.atom",
            },
        ],
        "rights": "Copyright (c) 2003, Mark Pilgrim",
        "generator": "Example Toolkit",
        "entry": [
            {
                "title": "Atom draft-07 snapshot",
                "link": [
                    {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": "http://example.org/2005/04/02/atom",
                    },
                    {
                        "rel": "enclosure",
                        "type": "audio/mpeg",
                        "length": "1337",
                        "href": "http://example.org/audio/ph34r_my_podcast.mp3",
                    },
                ],
                "id": "tag:example.org,2003:3.2397",
                "updated": "2005-07-31T12:29:29Z",
                "published": "2003-12-13T08:29:29-04:00",
                "author": {
                    "name": "Brent Simmons",
                    "uri": "http://example.org/",
                    "email": "f8dy@example.com",
                },
                "contributor": {"name": "Sam Ruby"},
            },
            {
                "title": "Atom draft-12 snapshot",
                "link": [
                    {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": "http://example.org/2005/04/02/atom",
                    },
                    {
                        "rel": "enclosure",
                        "type": "audio/mpeg",
                        "length": "1337",
                        "href": "http://example.org/audio/ph34r_my_podcast.mp3",
                    },
                ],
                "id": "tag:example.org,2003:3.2397",
                "updated": "2005-07-31T12:29:29Z",
                "published": "2004-12-13T08:29:29-04:00",
                "author": {
                    "name": "Mark Thompson",
                    "uri": "http://example.org/",
                    "email": "f8dy@example.com",
                },
                "contributor": {"name": "Sam Ruby"},
            },
            {
                "title": "Atom draft-15 snapshot",
                "link": [
                    {
                        "rel": "alternate",
                        "type": "text/html",
                        "href": "http://example.org/2005/04/02/atom",
                    },
                    {
                        "rel": "enclosure",
                        "type": "audio/mpeg",
                        "length": "1337",
                        "href": "http://example.org/audio/ph34r_my_podcast.mp3",
                    },
                ],
                "id": "tag:example.org,2003:3.2397",
                "updated": "2006-07-31T12:29:29Z",
                "published": "2005-12-13T08:29:29-04:00",
                "author": {
                    "name": "Brent Simmons",
                    "uri": "http://example.org/",
                    "email": "f8dy@example.com",
                },
                "contributor": {"name": "Sam Ruby"},
            },
        ],
    }


def test_json_parser_by_json_file(json_file, parsed_json_reference):
    """Test json parser class transform json file to python object with correct structure."""

    data = parsers.parsers_manager.get_parser("json").parse(json_file)
    assert data == parsed_json_reference


def test_xml_parser_by_rss_file(rss_file, parsed_rss_reference):
    """Test xml parser class transform rss file to python object with correct structure."""

    data = parsers.parsers_manager.get_parser("rss").parse(rss_file)
    assert data == parsed_rss_reference


def test_xml_parser_by_atom_file(atom_file, parsed_atom_reference):
    """Test xml parser class transform atom file to python object with correct structure."""

    data = parsers.parsers_manager.get_parser("atom").parse(atom_file)
    assert data == parsed_atom_reference