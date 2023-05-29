from models.printer import Printer


class LedPrinter(Printer):
    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 count_of_light_panels=0, zoom=0.0):
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.count_of_light_panels = count_of_light_panels
        self.zoom = zoom

    def print(self, pages):
        pass

    def load_paper(self, count):
        pass

    def get_remaining_pages_count(self):
        return self.pages_capability

    def __repr__(self):
        return (
            super().__str__() +
            f", count of light panels = {self.count_of_light_panels}, zoom = {self.zoom}"
        )
