'''
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
'''



my_dict = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

def flat_dict(my_dict, base_key=''):
    print(my_dict)
    print(base_key)
    print('===========')
    global new_dict

    for k, v in my_dict.items():
        if not isinstance(v,dict):
            new_dict[base_key+k] = v

        if isinstance(v,dict):
            flat_dict(v, base_key = base_key + k + ".")


new_dict = {}


flat_dict(my_dict)
print(new_dict)
