class Printer:
    __instance = None

    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0):
        self.model = model
        self.type = printer_type
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count

    def print(self, pages):
        if self.paper_count >= pages:
            self.paper_count -= pages

    def load_paper(self, count):
        available_space = self.paper_tray_capacity - self.paper_count
        if count <= available_space:
            self.paper_count += count

    @staticmethod
    def get_instance():
        if Printer.__instance is None:
            Printer.__instance = Printer()
        return Printer.__instance

    def __str__(self):
        return (
            f"model = {self.model}, type = {self.type}, duplex = {self.is_duplex}, "
            f"color = {self.is_color}, paper capacity = {self.paper_tray_capacity}, "
            f"paper count = {self.paper_count}"
        )


if __name__ == "__main__":
    printers = [
        Printer(),
        Printer("Miwa", "LED", True, False, 50, 20),
        Printer.get_instance(),
        Printer.get_instance()
    ]

    for printer in printers:
        print(printer)
