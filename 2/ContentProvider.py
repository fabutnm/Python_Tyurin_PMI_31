import sqlite3
import json

class ContentProvider:
    def __init__(self, filename):
        self.filename = str(filename)
        self.connector = sqlite3.connect(self.filename)

    def write_html(self, htmlwriter):
        params = (2,)
        description = self.connector.execute("select description from requests where id=?", params).fetchall()
        description = json.loads(description[0][0])

        query = """
        select stars.name, stars.distance, companies.name, flights.price 
        from flights join stars on(flights.star_id=stars.id) join companies on(flights.company_id=companies.id) 
        where(stars.id=?)"""
        for star_Id in description:
            result = self.connector.execute(query, (star_Id,)).fetchall()
            if (len(result) > 0):
                htmlwriter.add_simple_line(result[0][0])
                for i in range(len(result)):
                    htmlwriter.add_file_from_arr([result[i][0], result[i][1], result[i][2], result[i][3]])

        htmlwriter.write()
        htmlwriter.close()
        self.close_connect()

    def close_connect(self):
        self.connector.close()


