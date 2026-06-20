class OldPrinte:

    def old_prin(self):
        print("Printing using old printer")


class PrinterAdapter:

    def __init__(self, printe):
        self.printe = printe

    def print(self):
        self.printe.old_prin()


printer = PrinterAdapter(OldPrinte())

printer.print()