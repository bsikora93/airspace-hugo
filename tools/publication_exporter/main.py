import bibtexparser
import yaml

PATH_TO_BIBTEX_FILE = "C:/Users/Kuba/Downloads/references.bib"

def getAuthors(authorsStr):
    return [author.strip().rstrip(",") for author in authorsStr.split("and")]

with open(PATH_TO_BIBTEX_FILE) as publications_file:
    publications = bibtexparser.load(publications_file)

dataToExport = []

for pub in publications.entries:
    toExport = dict(publication=dict(title=pub["title"], year=int(pub["year"]), doi=pub.get("doi"), url=pub.get("url"), authors=getAuthors(pub["author"]), type=pub["ENTRYTYPE"], id=pub["ID"]))
    dataToExport.append(toExport)

dataToExport = dict(publications=dataToExport)

stream = open("publications.yml", "w")
yaml.dump(dataToExport, stream)