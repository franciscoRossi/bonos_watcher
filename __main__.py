from bonos_watcher.api.api import Api
from bonos_watcher.services.processor import Processor

data = Api.get_prices()["payload"]
p = Processor(data)

sorted_data = p.sort_by_price()

print("Cotizaciones dólar MEP según bonos")
print("Bono ARS  ->  Bono USD   Cotizacion")
for x in sorted_data:
    print(x["P"]["ticker"] + " -> " + x["D"]["ticker"] + " cotiza a $" + "{:.3f}".format(x["Cot"]))