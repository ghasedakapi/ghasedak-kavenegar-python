# ghasedak-kavenegar-python

If you need to future information about API document Please visit RESTful Document

## Installation
<p> You can install our SDK from pypi through below command </p>


```
pip install ghasedakkavenegar
```
You can download the Python SDK <a href="https://github.com/ghasedakapi/ghasedak-kavenegar-python/blob/master/kavenegar.py">Here</a> too
<p>
Then ,You need to make an account on Ghasedak from <a href="https://ghasedak.io">Here</a>
</p>
<p>
After that you just need to pick API-KEY up from your panel.

Anyway there is good tutorial about <a href="http://gun.io/blog/how-to-github-fork-branch-and-pull-request/">Pull  request</a>
</p>

## Usage

### Send
```python
from ghasedakkavenegar import *
try:
    api = KavenegarAPI('Your APIKey', timeout=20)
    params = {
        'sender': '',#optional
        'receptor': '',#multiple mobile number, split by comma
        'message': '',
    } 
    response = api.sms_send(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```

### OTP
```python
#!/usr/bin/env python
from ghasedakkavenegar import *
try:
    api = KavenegarAPI('Your APIKey', timeout=20)
    params = {
        'receptor': '',
        'template': '',
        'token': '',
        'type': 'sms',#sms vs call
    }   
  response = api.verify_lookup(params)
  print(response)
except APIException as e: 
  print(e)
except HTTPException as e: 
  print(e)
```

### Send Bulk
```python
#!/usr/bin/env python
from ghasedakkavenegar import *
try:
    api = KavenegarAPI('Your APIKey', timeout=20)
    params = {
        'sender':'["",""]',#array of string as json 
        'receptor': '["",""]',#array of string as json 
        'message': '["",""]',#array of string as json 
    } 
    response = api.sms_sendarray(params)
    print(response)
except APIException as e: 
    print(e)
except HTTPException as e: 
    print(e)
```

# Contribution
Bug fixes, docs, and enhancements welcome! Please let us know <a href="mailto:support@ghasedak.io?Subject=SDK" target="_top">support@ghasedak.io</a>

