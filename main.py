class FileWeightDescriptor:

    def __get__(self, instance, owner):
        return instance._size

    def __set__(self,instance,value):
        if value < 0:
            raise ValueError('file size is zero')
        elif not isinstance(value,int):
                raise ValueError('wrong variable type')
        else: instance._size = value

    def format_size(self, size):
        if size < 1024:
            return f'{size} bytes'
        elif size < 1024 ** 2:
            return f'{size / 1024:.2f} KB'
        else:
            return f'{size / (1024 ** 2):.2f} MB'

class File:
    size = FileWeightDescriptor()
    def __init__(self,size):
        self._size = size

file1 = File(1024)
print(file1.size)
print(FileWeightDescriptor().format_size(file1.size))

