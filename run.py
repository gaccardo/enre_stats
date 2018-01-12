from terminaltables import SingleTable

from src.parser import EnreHTMLParser
from src.retriever import get_data_from_enre

enre = EnreHTMLParser()
parsed = enre.parse_table(get_data_from_enre())
# status = enre.get_neighborhood("147 - VILLA CRESPO / 14728")
status = enre.get_neighborhood()

if status is not None:
    table_data = [[
        "Barrio", "Hora estimada", "Afectados"
    ]]

    for state in status:
        table_data.append(
            [
                state['barrio'],
                state['afectados'],
                state['estimado']
            ]
        )

    table = SingleTable(table_data, "Media Tension")
    print table.table
else:
    print "this code it is not present"
