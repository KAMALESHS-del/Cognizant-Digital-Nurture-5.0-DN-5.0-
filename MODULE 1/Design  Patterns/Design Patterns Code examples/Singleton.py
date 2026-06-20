class Principal:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            print("Creating Principal")
            cls._instance = super().__new__(cls)

        return cls._instance



p2 = Principal()
p3=Principal()

print(p2 is p3)