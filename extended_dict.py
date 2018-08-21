class ExtendedDict(dict):
    def __setitem__(self, key, value):
        if (type(key) != str):
            raise ValueError
        else:
            super().__setitem__(key, value)

    def get(self, key):
        if (type(key) != str):
            raise ValueError
        else:
            return super().__getitem__(key)

    def __getitem__(self, key):
        if(type(key) == slice):
            my_list = list()
            for i in sorted(list(self.keys())):
                my_list.append((i, super().__getitem__(i)))
            return my_list[key]
        elif (type(key) != str):
            raise ValueError

        else:
            return super().__getitem__(str(key))

    def __setattr__(self, key, value):
        self.__setitem__(str(key), value)

    def __getattr__(self, key):
        if (type(key) != str):
            raise ValueError
        return self.__getitem__(str(key))

    def __delitem__(self, key):
        if(type(key) != str):
            raise ValueError
        else:
            super().__delitem__(key)

    def __delattr__(self, key):
        super(ExtendedDict, self).__delitem__(str(key))
