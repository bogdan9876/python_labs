from models.printer import Printer


class LaserPrinter(Printer):
    REQUIRED_COLOUR_PER_PAGE = 10

    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 pages_done=0):
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.pages_done = pages_done

    def print(self, pages):
        pass

    def load_paper(self, count):
        pass

    def get_remaining_pages_count(self, get_pages_capability=None):
        return get_pages_capability()

    def __repr__(self):
        return super().__str__() + f", pages_done = {self.pages_done}"