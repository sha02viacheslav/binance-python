

class AveragePrice:

    def __init__(self):
        self.mins = 0
        self.price = 0
    
    @staticmethod
    def json_parse(json_data):
        data_obj = AveragePrice()
        data_obj.mins = json_data.get_int("mins")
        data_obj.price = json_data.get_float("price")

        return data_obj
