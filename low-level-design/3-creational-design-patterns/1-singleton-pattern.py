import threading
# Singleton Pattern

# Early Singleton
# Class implemneting with Eager Loading
class EagerSingleton:
    # Static instance created eagerly
    __instance = None

    # Private constructor simulation
    def __init__(self):
        if EagerSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        # Declaring it private prevents creation of its object using the new keyword
        EagerSingleton.__instance = self

    # Method to get the instance of class
    @staticmethod
    def getInstance():
        return EagerSingleton.__instance  # Always returns the same instance

# Eager initialization (happens at load time)
# EagerSingleton._EagerSingleton__instance = EagerSingleton()

# Lazy Singleton
class LazySingleton:
    __instance = None

    def __init__(self):
        if LazySingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        LazySingleton.__instance = self

    @staticmethod
    def getInstance():
        if LazySingleton.__instance is None:
            LazySingleton()

        return LazySingleton.__instance 

# Lazy initialization (happens when getInstance() is called)
# LazySingleton._LazySingleton__instance = LazySingleton()

# Thread Safe Singleton
# Synchronized method to ensure thread safety

class SyncSingleton:
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if SyncSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        SyncSingleton.__instance = self

    @staticmethod
    def getInstance():
        with SyncSingleton.__lock:
            if SyncSingleton.__instance is None:
                SyncSingleton()

        return SyncSingleton.__instance 

# Double Checked Locking Singleton
# Synchronized method to ensure thread safety
class DoubleCheckedLockingSingleton:
    __instance = None
    __lock = threading.Lock()

    def __init__(self):
        if DoubleCheckedLockingSingleton.__instance is not None:
            raise Exception("This class is a singleton!")
        DoubleCheckedLockingSingleton.__instance = self

    @staticmethod
    def getInstance():
        if DoubleCheckedLockingSingleton.__instance is None:
            with DoubleCheckedLockingSingleton.__lock:
                if DoubleCheckedLockingSingleton.__instance is None:
                    DoubleCheckedLockingSingleton()

        return DoubleCheckedLockingSingleton.__instance 

# Bill Pugh Singleton
class Singleton:
    def __init__(self):
        if hasattr(Singleton, "_created"):
            raise Exception("This class is a singleton!")
        Singleton._created = True

    @staticmethod
    def getInstance():
        if not hasattr(Singleton, "_instance"):
            Singleton()

        return Singleton._instance 
