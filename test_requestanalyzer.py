import pytest
import json
from .requestanalyzer import RequestAnalyzer

class Test:

    @pytest.fixture()
    def ra(self):
        ra = RequestAnalyzer()
        yield ra

    def test_canCallRequestAnalyzer(self, ra):
        assert type(ra) is RequestAnalyzer

    def test_canGetRecordCount(self, ra):
        assert ra.count() == 3

    def test_canGetIds(self, ra):
        assert ra.ids() == ["1a", "2b", "3c"]

    def test_canGetHeadersForId(self ,ra):
        assert ra.headers('2b') == ['Host', 'Cache-Control', 'Accept']

    def test_canGetAllHeaders(self, ra):
        knownHeaders = ["Accept", "Accept-Encoding", "Akamai-Origin-Hop", "Akamai-Origin-Hop", "Akamai-Origin-Hop", "Cache-Control", "Cache-Control", "Host", "Host", "True-Client-Ip", "X-Forwarded-Port", "X-Forwarded-Proto"]
        assert ra.allHeaders() == knownHeaders

    def test_canSummarizeAllHeaders(self, ra):
        headerSummary = {"Accept":1, "Accept-Encoding":1, "Akamai-Origin-Hop":3, "Cache-Control":2, "Host":2, "True-Client-Ip":1, "X-Forwarded-Port":1, "X-Forwarded-Proto":1}
        assert ra.headerSummary() == headerSummary

    def test_throwsJSONDecodeErrorOnInvalidJSON(self):
        with pytest.raises(json.JSONDecodeError):
            badJson = RequestAnalyzer('bad_test.json')

        