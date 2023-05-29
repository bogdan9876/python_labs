from models.printer import Printer


class MatrixPrinter(Printer):
    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 needles_works=0, sensors=0):
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.needles_works = needles_works
        self.sensors = sensors

    def print(self, pages):
        pass

    def load_paper(self, count):
        pass

    def get_remaining_pages_count(self):
        return self.pages_capability

    def __repr__(self):
        return (
            super().__str__() +
            f", needles works = {self.needles_works}, sensors = {self.sensors}"
        )
