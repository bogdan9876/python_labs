import logging

from exceptions.capacity_error import CapacityError
from models.printer import Printer
from decorators.logger import logged


class LedPrinter(Printer):
    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 count_of_light_panels=0, zoom=0.0):
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.count_of_light_panels = count_of_light_panels
        self.zoom = zoom
        self.favorite_tasks = {"AFA, FAF"}

    @logged(CapacityError, "file")
    def print(self, pages):
        if pages > self.pages_capability:
            raise CapacityError("Insufficient pages capability.")
        self.paper_count -= pages
        logging.info(f"Printed {pages} pages. Paper count: {self.paper_count}")

    def load_paper(self, count):
        pass

    def get_remaining_pages_count(self):
        return self.pages_capability

    def __repr__(self):
        return (
            super().__str__() +
            f", count of light panels = {self.count_of_light_panels}, zoom = {self.zoom}"
        )

    def __len__(self):
        return len(self.favorite_tasks)
