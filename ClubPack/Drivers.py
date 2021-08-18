class Driver:
    def __init__(self, **kwargs):
        self.name = kwargs['driver_name']
        self.licence = kwargs['driver_licence']
        self.permanent = kwargs['driver_status']
        self.bus_type = kwargs['bus_type'] #bus_object
