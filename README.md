# Project Description
Give user access to parts of json file obtained with Twitter API

# Files
### project.py
##### Function make_pathdict()
```python
def make_pathdict(json_dict: dict, verbose=False) -> dict:
    '''Make a dictionary of all keys in given dictionary
       where corresponding values are lists of all "paths" (strings to use with jmespath)
       to items corresponding to the keys
    ''' 
```
##### Class JSONDict()
Stores original dictionary, pathdict (obtained via make_pathdict()) and keys (list of keys of pathdict) and lets the user access different parts of dictionary

##### Functions main() and accessing_DEMO()
Demonstration of project's capabilities

### Files from https://www.py4e.com/code3/
--- twitter1.py
(edited to return dictionary with data on user's timeline)
--- twitter2.py
(edited to return dictionary with data on user's "friends" (people the user follows))
--- twurl.py
--- oauth.py
