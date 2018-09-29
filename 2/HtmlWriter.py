class HtmlWriter:
    def __init__(self,filename,width):
        self.filename=filename + self.writeHtmlExp()
        self.width=width
        self.text=''

    def add_simple_line(self,content):
        if(self.text==''):
            self.text='<table border="1">'
        self.text += self.writeLine('<td colspan='+str(self.width)+'>'+content+'</td>')

    def add_file_from_arr(self,content):
        for wew in content:
            self.text+=self.writeColumnInLine(str(wew))
        self.text = self.writeLine(self.text)

    def writeColumnInLine(self,content):
        return '<td>' + content + '</td>'

    def writeLine(self, content):
        return '<tr>' + content + '</tr>'

    def writeHtmlExp(self):
        return ".html"

    def write(self):
        file_handler = open(self.filename, 'w')
        file_handler.write(self.text)
        file_handler.close()

    def close(self):
        file_handler = open(self.filename, 'a')
        file_handler.write('</table>')
        file_handler.close()
