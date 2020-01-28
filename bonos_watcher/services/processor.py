class Processor:

    def __init__(self, data):
        data = list(filter(lambda x: x["precioVenta"] != 0.0 and x["precioCompra"] != 0.0, data))
        data = list(map(lambda x: {"ticker": x["ticker"].upper(), "precioCompra": x["precioCompra"],
                                    "precioVenta": x["precioVenta"]}, data))
        self._data = data

    def _get_empty_bono(self, name):
        return {"ticker": name.upper(), "precioCompra": 0.0,
                "precioVenta": 0.0}

    def _get_linked_d_bono(self, name):
        name = name + "D"
        tmp = list(filter(lambda x: x["ticker"] == name, self._data))
        if len(tmp) > 0:
            return tmp[0]
        return self._get_empty_bono(name)

    def _get_linked_bono(self, name):
        name = name[:-1]
        tmp = list(filter(lambda x: x["ticker"] == name, self._data))
        if len(tmp) > 0:
            return tmp[0]
        return self._get_empty_bono(name)

    def get_price_rate(self, x):
        return self._get_linked_bono(x["ticker"])["precioVenta"] / x["precioCompra"]

    def sort_by_price(self):
        data = self._data
        d_list = filter(lambda x: x["ticker"][-1] == "D", data)
        d_list = map(lambda x: {"D": x, "P": self._get_linked_bono(x["ticker"]),
                                       "Cot": self.get_price_rate(x)}, d_list)
        d_list = filter(lambda x: x["Cot"] > 0, d_list)
        sorted_x = sorted(d_list, key=lambda x: x["Cot"])

        return list(sorted_x)