from abc import ABC
from enum import nonmember


#creat BaseClass
class BaseClass(ABC):
    _id = 0
    objects_list = None

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id


    @classmethod
    def store(cls, obj):
        if cls.objects_list is None:
            cls.objects_list = list()
        cls.objects_list.append(obj)
    
