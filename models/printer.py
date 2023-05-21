from abc import ABC, abstractmethod

class Printer(ABC):
    __instance = None

    def __init__(self, model=None, printer_type=None, is_color=False, is_duplex=False,
                 paper_tray_capacity=0, paper_count=0, pages_capability=0):
        self.model = model
        self.type = printer_type
        self.is_color = is_color
        self.is_duplex = is_duplex
        self.paper_tray_capacity = paper_tray_capacity
        self.paper_count = paper_count
        self.pages_capability = pages_capability

    @abstractmethod
    def print(self, pages):
        pass

    @abstractmethod
    def load_paper(self, count):
        pass

    @abstractmethod
    def get_remaining_pages_count(self):
        pass 

    @staticmethod
    def get_instance():
        if Printer.__instance is None:
            Printer.__instance = Printer()
        return Printer.__instance

    def __str__(self):
        return (
            f"model = {self.model}, type = {self.type}, duplex = {self.is_duplex}, "
            f"color = {self.is_color}, paper capacity = {self.paper_tray_capacity}, "
            f"paper count = {self.paper_count}, pages capability = {self.pages_capability}"
        )
