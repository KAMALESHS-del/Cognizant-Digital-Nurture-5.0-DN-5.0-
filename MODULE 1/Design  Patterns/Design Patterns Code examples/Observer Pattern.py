class Subscriber:

    def notify(self, video):
        print("Notification:", video)


class Channel:

    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def upload_video(self, video):

        for sub in self.subscribers:
            sub.notify(video)


s1 = Subscriber()
s2 = Subscriber()
s3= Subscriber()


channel = Channel()

channel.add_subscriber(s1)
channel.add_subscriber(s2)
channel.add_subscriber(s3)
channel.upload_video("Python Tutorial")