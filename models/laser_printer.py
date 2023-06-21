import logging

from models.printer import Printer
from decorators.logger import logged
from exceptions.capacity_error import CapacityError

class LaserPrinter(Printer):
    REQUIRED_COLOUR_PER_PAGE = 10

    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 pages_done=0):
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.pages_done = pages_done
        self.favorite_tasks = {"ACA, CAC"}

    @logged(CapacityError, "file")
    def print(self, pages):
        if pages > self.pages_capability:
            raise CapacityError("Insufficient pages capability.")
        self.paper_count -= pages
        logging.info(f"Printed {pages} pages. Paper count: {self.paper_count}")

    def load_paper(self, count):
        pass

    @logged(CapacityError, "file")
    def get_remaining_pages_count(self):
        return self.pages_capability - self.pages_done

    def __repr__(self):
        return super().__str__() + f", pages_done = {self.pages_done}"

    def __len__(self):
        return len(self.favorite_tasks)
