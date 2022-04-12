Signal Science site requests analyzer.

Export request data as json from Salt https://salt.beefalo.sigsci.net/corps/<insert_corp>/sites/<insert_site>/requests. 

<img width="1218" alt="getdata" src="https://user-images.githubusercontent.com/820914/162868154-0d7b0db2-b8fc-4f12-a277-893593a10d96.png">

This project has utilities to parse and analyze the Salt output. 

1. `count`: Number of requests
2. `ids`: Unique request ids
3. `allHeaders`: All header values from 'headersIn' for the requests
3. `headers(id)`: All header values from 'headersIn' for a specific id
4. `headerSummary`: All headers listed one time, with a count of each header
