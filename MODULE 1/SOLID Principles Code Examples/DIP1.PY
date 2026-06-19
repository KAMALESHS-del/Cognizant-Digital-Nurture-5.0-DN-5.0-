from abc import ABC,abstractmethod
class Database(ABC):

    @abstractmethod
    def connect(self):
        pass
class MySQLDatabase(Database):

    def connect(self):
        print("Connected to MySQL")
class MongoDatabase(Database):

    def connect(self):
        print("Connected to MongoDB")
class Application:

    def __init__(self, database):
        self.database = database

    def start(self):
        self.database.connect()
mysql = MySQLDatabase()

app = Application(mysql)
app.start()

mongo=MongoDatabase()
app=Application(mongo)
app.start()