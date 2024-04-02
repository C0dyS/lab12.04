class Calculator:
    @classmethod
    def add(cls,x,y):
        return x + y
    @classmethod
    def subtract(cls,x,y):
        return x - y
    @classmethod
    def multiply(cls,x,y):
        return x * y
    @classmethod
    def divide(cls,x,y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        else:
            return x / y
    @classmethod
    def __call__(cls,operation_type,a,b):
        if operation_type == 'add':
            return cls.add(a,b)
        elif operation_type == 'subtract':
            return cls.subtract(a,b)
        elif operation_type == 'multiply':
            return cls.multiply(a,b)
        elif operation_type == 'divide':
            return cls.divide(a,b)
        else:
            raise ValueError('Wrong operation type')

test_1 = Calculator()
print(test_1('add',1,3))
print(test_1('divide',1,3))