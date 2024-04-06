# from collections import defaultdict

# TYPES = ('single', 'multi')

# class Share:

#     def __init__(self) -> None:
#         self.args = dict()
#         self.single = defaultdict(dict)
#         self.history = defaultdict(lambda: defaultdict(list))

#     def keys(self, typ, fn=None):

#         if typ.lower() not in TYPES:
#             raise KeyError(f"Given type must be one of {TYPES}, not '{typ}'.")
        
#         dic = getattr(self, typ)
        
#         if fn is None:
#             return dic.keys()
#         if fn in dic:
#             return dic[fn].keys()
#         raise KeyError(f"Given fn, '{fn}', is not in {typ} data.")

#     """
#     Single Data
#     """

#     def update_single(self, fn, key, val):
#         self.single[fn][key] = val

#     def extend_history(self, code, key, vals):
#         self.history[code][key] += vals

# if __name__ == '__main__':

#     share = Share()
#     share.update_single('함수1', 'key1', 'val1')
#     print(share.single)
#     share.update_single('함수1', 'key2', 'val2')
#     print(share.single)
#     share.update_single('함수3', 'key3', 'val3')
#     print(share.single)

#     data_dict = defaultdict(dict)
#     data_dict['a']['b'] = '1'

#     print(data_dict)

#     my_dict = {'key1' : {'key2' : { 'key3' : 'val3'}}}
#     print(my_dict)


from collections import defaultdict

TYPES = ('single', 'multi')

class Share:

    def __init__(self) -> None:
        self.multi = defaultdict(lambda: defaultdict(list))

        self.multi['fn1']['key1'] = [123,123,123,123,123,123]
        print(dict((self.multi)))


if __name__ == '__main__':
    share = Share()






