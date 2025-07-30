from abc import ABC
from manager import Manager

class BaseClass(ABC):
    _id = 0

    def __init__(self, *args, **kwargs):
        self.id = self.generate_id()
        self.store(self)
        self.set_manager()
        super().__init__(*args, **kwargs)

    @classmethod
    def generate_id(cls):
        cls._id += 1
        return cls._id

    @classmethod
    def set_manager(cls):
        if not hasattr(cls, "manager") or cls.manager is None:
            cls.manager = Manager(cls)

    @classmethod
    def store(cls, obj):
        if not hasattr(cls, "objects_list") or cls.objects_list is None:
            cls.objects_list = []
        cls.objects_list.append(obj)
