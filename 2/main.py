from HtmlWriter import HtmlWriter
from ContentProvider import ContentProvider

def main():
    htmlWriter = HtmlWriter('1', 4)
    contentProvider = ContentProvider('spacey_db.sl3')
    contentProvider.write_html(htmlWriter)

if __name__ == "__main__":
    main()