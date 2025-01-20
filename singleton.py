class Singleton:
    """
    Singleton design pattern.

    This class ensures that only one instance of the Singleton class exists
    throughout the lifetime of the application.

    Usage:
    >>> s1 = Singleton()
    >>> s2 = Singleton()
    >>> s1 is s2  # Both references point to the same instance
    True
    """
    _instance = None

    def __new__(cls):
        """
        Creating new instance of the singleton class if one does not exist

        returns:
            new instances of the class
        """

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

def main():
    
    s1 = Singleton()
    s2 = Singleton()

    print("Both the classes are of once instance",s1 is s2)

if __name__ == "__main__":
    main()