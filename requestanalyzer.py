import json
from collections import Counter
'''

'''
class RequestAnalyzer:
    
    def __init__(self, filename='test.json'):
        try:
            f = json.load(open(filename))
        except json.JSONDecodeError as jde:
            self.data = []
            print(f'Invalid JSON: {jde.msg}')
            raise
        else:
            self.data = f

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data = value

    '''
    Number of requests in request data
    '''
    def count(self):
        return len(self.data)

    '''
    Returns a list of 'id's in the request data
    '''
    def ids(self):
        result = []
        for i, v in enumerate(self.data):
            result.append(self.data[i]['id'])
        return result
    
    '''
    Returns a list of all 'headersIn' values for a specific request 'id' including duplicates
    '''
    def headers(self, id):
        result = []
        for i, idv in enumerate(self.data):
            if idv['id'] == id:
                for j, headersIn in enumerate(idv['headersIn']):
                    result.append(headersIn[0])
        return result   

    '''
    Returns a list of all 'headersIn' values including duplicates
    '''
    def allHeaders(self):
        result = []
        for i, idv in enumerate(self.data):
            for j, headersIn in enumerate(idv['headersIn']):
                result.append(headersIn[0])
        result.sort()
        return result

    '''
    Returns a Counter({'header1': 1, 'header2': 4, 'headerN': n}) of all 'headersIn' values and a the count
    '''
    def headerSummary(self):
        return Counter(self.allHeaders())
