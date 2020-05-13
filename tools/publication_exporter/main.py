import bibtexparser
import yaml

PATH_TO_BIBTEX_FILE = "./references.bib"

def authorMap(author):
    authorLower = author.lower()
    if "zrebiec" in authorLower:
        return "Źrebiec, J."
    elif "pilat" in authorLower:
        return "Piłat, A."
    elif "sikora" in authorLower:
        return "Sikora, B."
    elif "baranowski" in authorLower:
        return "Baranowski, J."
    elif "cieslik" in authorLower:
        return "Cieślik, J."
    elif "gliwa" in authorLower:
        return "Gliwa, J."
    elif "klocek" in authorLower:
        return "Klocek, J."
    elif "piatek" in authorLower:
        return "Piątek, P."
    elif "rosol" in authorLower:
        return "Rosół, M."
    elif "rozewicz" in authorLower:
        return "Różewicz, M."
    elif "turnau" in authorLower:
        return "Turnau, A."
    else:
        return author

def getAuthors(authorsStr):
    return [authorMap(author.strip().rstrip(",")) for author in authorsStr.split("and")]

with open(PATH_TO_BIBTEX_FILE) as publications_file:
    publications = bibtexparser.load(publications_file)

dataToExport = []

for pub in publications.entries:
    print(pub)
    toExport = dict(publication=dict(title=pub["title"], year=int(pub["year"]), doi=pub.get("doi"), url=pub.get("url"), authors=getAuthors(pub["author"]), type=pub["ENTRYTYPE"], id=pub["ID"], publisher=pub.get("publisher"), booktitle=pub.get("booktitle")))
    dataToExport.append(toExport)

allowedAuthors = ["Piłat, A.", "Sikora, B.", "Źrebiec, J.", "Gliwa, J."]

dataToExport = dict(publications=dataToExport, allowedAuthors=allowedAuthors)

stream = open("publications.yml", "w")
yaml.dump(dataToExport, stream)