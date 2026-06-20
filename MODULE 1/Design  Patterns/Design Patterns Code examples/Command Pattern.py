class TV:

    def turn_on(self):
        print("TV ON")


class Remote:

    def press_button(self, tv):
        tv.turn_on()


tv = TV()

remote = Remote()

remote.press_button(tv)