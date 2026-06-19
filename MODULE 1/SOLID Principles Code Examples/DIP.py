class MySQLDatabase:

    def connect(self):
        print("Connected to MySQL")


class Application:

    def __init__(self):
        self.db = MySQLDatabase()

    def start(self):
        self.db.connect()


app = Application()
app.start()