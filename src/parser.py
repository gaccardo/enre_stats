from bs4 import BeautifulSoup


class EnreHTMLParser(object):

    def __init__(self):
        self.datasets = None

    def parse_table(self, html):
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table", attrs={"id": "InterrupcionesServicio"})
        headings = [th.get_text() for th in table.find("tr").find_all("th")]
        datasets = []
        for row in table.find_all("tr")[1:]:
            dataset = zip(headings,
                          (td.get_text() for td in row.find_all("td")))
            datasets.append(dataset)

        self.datasets = datasets

    def get_neighborhood(self, code=None):
        if self.datasets is None:
            print "first you should load the dataset"
            return

        result = list()
        if code is None:
            for group in self.datasets:
                barrio = group[2]
                estimado = group[3]
                afectados = group[4]
                result.append({
                    "barrio": barrio[1],
                    "estimado": estimado[1],
                    "afectados": afectados[1]
                })
            return result
        else:
            for group in self.datasets:
                barrio = group[2]
                estimado = group[3]
                afectados = group[4]
                if barrio[1] == code:
                    return [{
                        "barrio": barrio[1],
                        "afectados": estimado[1],
                        "estimado": afectados[1]
                    }]
