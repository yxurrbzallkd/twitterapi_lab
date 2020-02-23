#from collections import Iterable
from twitter1 import json_user_timeline
from twitter2 import json_friends
from jmespath import search


def _step(json_item, pathdict={}, pathstr='', verbose=False, indent=''):
    if isinstance(json_item, dict):
        for key, item in json_item.items():
            new_pathstr = pathstr+'.'+str(key)
            if isinstance(item, dict) or isinstance(item, list):
                # *********VISUALISATION*********
                if verbose:
                    print(indent, key, ':')
                # *******************************

                _step(item, pathdict, new_pathstr, verbose, indent+'\t')
            else:
                # *********VISUALISATION*********
                if verbose:
                    print(indent, key, ':', item)
                # *******************************


            if key in pathdict:
                pathdict[key].append(new_pathstr[1:])
            else:
                pathdict[key] = [new_pathstr[1:]]

    elif isinstance(json_item, list):
        c = 0
        for item in json_item:
            new_pathstr = pathstr+'['+str(c)+']'
            if isinstance(item, dict) or isinstance(item, list):
                _step(item, pathdict, new_pathstr, verbose, indent+'\t')
            else:
                # *********VISUALISATION*********
                if verbose:
                    print(indent, item)
                # *******************************
            c += 1
    else:
        print('Unrecognisable item type!')

    return pathdict


def make_pathdict(json_dict, verbose=False):
    '''Make a dictionary of all keys in given dictionary
       where corresponding values are lists of all "paths" (strings to use with jmespath)
       to items corresponding to the keys

    >>> make_pathdict({\
        "name": 'John',\
        "last_name": 'Doe',\
        "facts": ["Two giants live in Britain's land, John Doe and Richard Roe",\
                  'a "John Doe" injunction',\
                  {"name": "John Roe"}],\
        'starring_in': [\
            'the 2002 US television series John Doe.',\
            'the 1941 film Meet John Doe',\
            ]})
    {'name': ['name', 'facts[2].name'], 'last_name': ['last_name'], 'facts': ['facts'], 'starring_in': ['starring_in']}
    '''
    return _step(json_dict, verbose=verbose)


class JSONDict():
    def __init__(self, dictionary, verbose=False):
        self.dictionary = dictionary
        self.pathdictionary = make_pathdict(dictionary, verbose=verbose)
        self.keys = list(self.pathdictionary.keys())

    def access_display(self, key):
        if key in self.pathdictionary:
            for path in self.pathdictionary[key]:
                print('Elements at {}'.format(path))
                result = search(path, self.dictionary)
                print(result)
                print()
        else:
            print(None)

    def access(self, key):
        elements = []
        if key in self.pathdictionary:
            for path in self.pathdictionary[key]:
                elements.append(search(path, self.dictionary))

        return elements

    def accessing_interface(self):
        print('Available keys', self.keys)
        key = input('Enter key: ')
        self.access_display(key)


def accessing_DEMO(dictionary: dict):
    JSONDict(dictionary, verbose=True).accessing_interface()


def main():
    demonstration = input('Chose demonstration:\n user_timeline | friends [U/F]: ')
    if demonstration == 'F':
        accessing_DEMO(json_friends())
    elif demonstration == 'U':
        accessing_DEMO(json_user_timeline())


if __name__ == '__main__':
    main()