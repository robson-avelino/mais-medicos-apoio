import requests
from bs4 import BeautifulSoup
import json
import re

URL = "https://www12.senado.leg.br/ecidadania/visualizacaoideia?id=213702"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

texto = soup.get_text()

# procura padrão tipo "13.706 apoios"
match = re.search(r"([\d\.]+)\s+apoios", texto, re.IGNORECASE)

if match:
    apoios = match.group(1)
else:
    apoios = "0"

with open("apoios.json", "w") as f:
    json.dump({"apoios": apoios}, f, ensure_ascii=False)

print("Apoios atualizados:", apoios)
