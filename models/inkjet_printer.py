from models.printer import Printer


class InkjetPrinter(Printer):
    REQUIRED_COLOUR_PER_PAGE = 10

    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 color_type=None, color_level=None, cyan=None, magenta=None, yellow=None,
                 black=None):
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.color_type = color_type
        self.color_level = color_level
        self.cyan = cyan
        self.magenta = magenta
        self.yellow = yellow
        self.black = black
        self.favorite_tasks = {"ABA, BAB"}

    def print(self, pages):
        pass

    def load_paper(self, count):
        pass

    def get_remaining_pages_count(self):
        return (self.black + self.yellow + self.cyan + self.magenta) / InkjetPrinter.REQUIRED_COLOUR_PER_PAGE

    def __repr__(self):
        return (
            super().__str__() +
            f", color type = {self.color_type}, color level = {self.color_level}, "
            f"cyan = {self.cyan}, magenta = {self.magenta}, yellow = {self.yellow},"
            f" black = {self.black},"
        )

    def __len__(self):
        return len(self.favorite_tasks)