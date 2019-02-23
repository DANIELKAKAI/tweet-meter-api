# tweet meter Api
A simple api built using flask that does sentimental analysis for tweeter
<br/>
endpoint: https://4l5m7snv0h.execute-api.us-east-1.amazonaws.com/dev/search/

### GET request example
```python
import requests

query = '#ucl'

payload = {'query':query}

res = requests.get('https://4l5m7snv0h.execute-api.us-east-1.amazonaws.com/dev/search/',params=payload)

data = res.json()

print(data)
#prints {'negative': 14, 'neutral': 40, 'positive': 44}

```
### POST request example
```python
import requests

query = '#ucl'

payload = {'query':query}

res = requests.post('https://4l5m7snv0h.execute-api.us-east-1.amazonaws.com/dev/search/',json=payload)

data = res.json()

print(data)

```

