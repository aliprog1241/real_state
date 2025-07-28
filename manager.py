class Manager:

    def __init__(self, _class=None):
        self._class = _class

    def __str__(self):
        return f'manager {self._class}'

    def search(self, **kwargs):
        results = list()
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                    results.append(obj)

        return results

    def get(self, **kwargs):
        for key, value in kwargs.items():
            for obj in self._class.objects_list:
                if hasattr(obj, key) and getattr(obj, key) == value:
                   return obj

        return None

