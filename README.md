Signal Science site requests analyzer.

Export request data as json from Salt https://salt.beefalo.sigsci.net/corps/<<corp>>/sites/<<site>>/requests. 

<< Insert getdata.png>>

This project has utilities to parse and analyze the Salt output. 

1. count: Number of requests
2. ids: Unique request ids
3. allHeaders: All header values from 'headersIn' for the requests
3. headers(id): All header values from 'headersIn' for a specific id
4. headerSummary: All headers listed one time, with a count of each header