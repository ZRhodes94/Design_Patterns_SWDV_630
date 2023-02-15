class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Chief_Executive_Officer(metaclass=SingletonMeta):
    def CEO_information(self):
        print("""
        Chief Executive Officer Summary:
        Name- Zachary Rhodes
        Email- CEO@business.org
        Phone- 3145254440
        Permissions- Complete Access
        """)


def main():

    CEO1 = Chief_Executive_Officer()
    CEO2 = Chief_Executive_Officer()
    
    CEO1.CEO_information()
    
    print()

    if id(CEO1) == id(CEO2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
        
main()