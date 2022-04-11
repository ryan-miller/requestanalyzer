import json
from collections import Counter

class RequestAnalyzer:
    
    def __init__(self, filename='test.json'):
        self._data = json.load(open(filename))

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

    def count(self):
        return len(self.data)

    def ids(self):
        result = []
        for i, v in enumerate(self.data):
            result.append(self.data[i]['id'])
        return result
    
    def headers(self, id):
        result = []
        for i, idv in enumerate(self.data):
            if idv['id'] == id:
                for j, headersIn in enumerate(idv['headersIn']):
                    result.append(headersIn[0])
        return result   

    def allHeaders(self):
        result = []
        for i, idv in enumerate(self.data):
            for j, headersIn in enumerate(idv['headersIn']):
                result.append(headersIn[0])
        result.sort()
        return result

    def headerSummary(self):
        return Counter(self.allHeaders())
