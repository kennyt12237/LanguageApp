from tkinter import Label

class KLabel(Label):
    
    WIDGET_CREATED_EVENT = "<<WidgetCreatedEvent>>"
    PROPERTY_CHANGE_EVENT = "<<PropertyChange>>"
    def __init__(self, master, **kwargs) -> None:
        super().__init__(master, **kwargs)
        self.winfo_id()
        
    def configure(self, **kwargs) -> None:
        super().configure(**kwargs)
        self.event_generate(self.PROPERTY_CHANGE_EVENT)