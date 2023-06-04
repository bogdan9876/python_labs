import logging

# pylint: disable=import-error
from decorators.logger import logged
from exceptions.capacity_error import CapacityError
from models.printer import Printer


class InkjetPrinter(Printer):
    """
    A class representing an inkjet printer.
    """

    REQUIRED_COLOUR_PER_PAGE = 10

    # pylint: disable=too-many-arguments
    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0,
                 color_type=None, color_level=None, cyan=None, magenta=None, yellow=None,
                 black=None):
        """
        Initialize an InkjetPrinter object.
        """
        super().__init__(model, printer_type, is_color, is_duplex,
                         paper_tray_capacity, paper_count, pages_capability)
        self.color_type = color_type
        self.color_level = color_level
        self.cyan = cyan
        self.magenta = magenta
        self.yellow = yellow
        self.black = black
        self.favorite_tasks = {"ABA, BAB"}

    @logged(CapacityError, "file")
    def print(self, pages):
        """
        Print the specified number of pages.
        """
        if pages > self.pages_capability:
            raise CapacityError("Insufficient pages capability.")
        self.paper_count -= pages
        logging.info(f"Printed {pages} pages. Paper count: {self.paper_count}")

    def load_paper(self, count):
        """
        Load the specified number of paper sheets.
        """
        # Implement the logic to load paper
        pass

    def get_remaining_pages_count(self):
        """
        Get the remaining number of pages that can be printed.
        """
        # pylint: disable=line-too-long
        return (self.black + self.yellow + self.cyan + self.magenta) / InkjetPrinter.REQUIRED_COLOUR_PER_PAGE

    def __repr__(self):
        """
        Return a string representation of the InkjetPrinter object.
        """
        return (
            super().__str__() +
            f", color type = {self.color_type}, color level = {self.color_level}, "
            f"cyan = {self.cyan}, magenta = {self.magenta}, yellow = {self.yellow},"
            f" black = {self.black},"
        )

    def __len__(self):
        """
        Return the number of favorite tasks.
        """
        return len(self.favorite_tasks)
