# Lesson 1
## What type of visualisation is this?
## graph, i.e. a chart that plots results in two dimensions

## What is the name of the plot?
## line chart

## How many variables you need to represent visits per day in the plot?
## 2

## Values on the x axis are...
## ordinal

## Values on the y axis are...
## numeric

## What visualisation dimensions are relevant in the plot?
## orientation

## What the repeated vertical grey lines represent in the plot?
## a 7-day division, representing the end (or beginning) of the week

## Do you see any significant pattern in the plot?
## There are regular peaks at every end/beginning of the week.

## Can you explain what the pattern means in your opinion?
## peaks may represent the day in which students submit online some assignment. The last peak may represent a final examination

## Which of the Tufte's principles are respected in the plot and why?
## minimal data-ink ratio ; minimal chart-junk ; proper scale and label

# Lesson 3 - RDFlib
## Exercise in class
import pprint
import rdflib
from rdflib import URIRef, Literal, Namespace
from rdflib.namespace import XSD, RDFS, DCTERMS
# create an empty Graph
g = rdflib.ConjunctiveGraph()

# parse a local RDF file by specifying the format into the graph
result = g.parse("../resources/artchives.nq", format='nquads')

# create the empty set for topics labels
unique_topics = set()

for s,p,o in g.triples((wd.Q1089074, wdt.P921, None)):
    for s1,p1,o1 in g.triples((o, RDFS.label, None)):
        unique_topics.add(o1.strip())

for topic in unique_topics:
    print(topic)

## Homework:
## Retrieve the list of (unique) historians' countries of citizenship
## Retrieve the list of (unique) historians' countries of citizenship and the number of historians for each country.

from rdflib.namespace import RDFS
country_counter = {}
country_labels = set()

for s,p,o in g.triples((None, wdp.P27, None)):
    if o in country_counter:
        country_counter[o] += 1
    else:
        country_counter[o] = 1

    for s1,p1,o1 in g.triples((o, RDFS.label, None)):
        country_labels.add( (s1, o1.strip()))

pprint.pprint(country_counter)
pprint.pprint(country_labels)


country_counter_labels = {}
for uri,label in country_labels:
    for uri2, count in country_counter.items():
        if uri2 == uri:
            country_counter_labels[label] = count

pprint.pprint(country_counter_labels)

# Lesson 4 - SPARQL
## Write a SPARQL query to retrieve in ARTchives all the historians that were born in Berlin (wd:Q64).
g = rdflib.ConjunctiveGraph()
# parse a local RDF file by specifying the format into the graph
result = g.parse("../resources/artchives_birthplaces.nq", format='nquads')

q = g.query("""
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX wd: <http://www.wikidata.org/entity/>
    SELECT DISTINCT ?historian (SAMPLE(?l) AS ?label)
    WHERE { ?historian wdt:P19 wd:Q64 ; rdfs:label ?l .
        } GROUP BY ?historian
""")

for r in q:
    print(r[1])

## Write the SPARQL query to retrieve in Wikidata all the art historians (that are both in ARTchives and Wikidata!) that were born in Germany. Copy paste the query that returns a table: <historian URI> <historian label> <city URI> <city label>. Tip: A german city in Wikidata has the pattern wdt.P17 (country) > wd:Q183 (Germany).
historians = "the list of historians that are both in ARTchives and wikidata"

query2wd = """SELECT DISTINCT ?historian
WHERE {
    VALUES ?historian {""" + historians + """} .
    ?historian wdt:P19 ?birthplace .
    ?birthplace rdfs:label ?birthplace_label .
    ?birthplace wdt:P17 wd:Q183 .
    FILTER (langMatches(lang(?birthplace_label), ""EN""))
    } """

# Results
"""
 wd:Q60185	Aby Warburg
 wd:Q88907	Ernst Kitzinger
 wd:Q3057287	Ernst Steinmann
 wd:Q41616785	Gustav Ludwig
 wd:Q1712683	Julius S. Held
 wd:Q1629748	Kurt Badt
 wd:Q1641821	Otto Lehmann-Brockhaus
 wd:Q90407	Richard Krautheimer
 wd:Q1715096	Ulrich Middeldorf
 wd:Q1296486	Wolfgang Lotz
 wd:Q18935222	Werner Cohn
"""

# Lesson 5 - Submit your Jupyter notebook!
scatt_plot = sns.catplot(x="period_label", y="count_coll", height=2, aspect=5.5, jitter=False, data=data_by_year)
scatt_plot.set_xticklabels(rotation=90)

# Lesson 6 - Apply the apriori algorithm to calculate which people (art:hasSubjectPerson) mostly co-occur in ARTchives collections. Write here the three rules with the highest confidence in the form: (antecedents) - (consequents)
