# -*- coding: utf-8 -*-
"""Copia de Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sV3zbtAGxJ2SYJrRYOpePIxdWEm_eHwv

**Task 07: Querying RDF(s)**
"""

# !pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")
print("\n")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# SPARQL
from rdflib.plugins.sparql import prepareQuery

print("SPARQL")
q1 = prepareQuery('''
  SELECT DISTINCT ?Subject WHERE { 
    ?Subject rdfs:subClassOf <http://somewhere#Person>.
  }
  ''',
  initNs = { "rdfs": RDFS, "rdf": RDF}
)

for r in g.query(q1):
  print(r.Subject)
print("\n")

#RDFLIB
print("RDFLIB")
NS = Namespace("http://somewhere#")
for s,p,o in g.triples((None, RDFS.subClassOf, NS.Person)):
  print(s)
print("\n")

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
print("SPARQL")
q2 = prepareQuery('''
  SELECT DISTINCT ?Subject WHERE { 
    ?Subject rdf:type <http://somewhere#Person>. 
  }
  ''',
  initNs = { "rdf": RDF}
)
q2_2 = prepareQuery('''
  SELECT DISTINCT ?Subject WHERE { 
    ?Subject rdf:type ?Person. 
    ?Person rdfs:subClassOf <http://somewhere#Person>
  }
  ''',
  initNs = { "rdf": RDF, "rdfs": RDFS}
)
print("Instancias clase Person")
for r in g.query(q2):
  print(r.Subject)
print("Instancias subclases de Person")
for s in g.query(q2_2):
  print(s.Subject)
print("\n")

# RDFLIB
print("RDFLIB")
NS = Namespace("http://somewhere#")
print("Instancias clase Person")
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  print(s)
print("Instancias subclases de Person")
for s,p,o in g.triples((None, RDFS.subClassOf, NS.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    print(s1)
print("\n")

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# SPARQL
print("SPARQL")
q3 = prepareQuery('''
  SELECT DISTINCT ?Subject ?Property WHERE { 
    ?Subject rdf:type <http://somewhere#Person>. 
    ?Subject ?Property ?Object.
  }
  ''',
  initNs = { "rdf":RDF}
)
q3_2 = prepareQuery('''
  SELECT DISTINCT ?Subject ?Person ?Property WHERE { 
    ?Subject rdf:type ?Person. 
    ?Person rdfs:subClassOf <http://somewhere#Person>.
    ?Subject ?Property ?Object.
  }
  ''',
  initNs = { "rdf":RDF, "rdfs":RDFS}
)

print("Instancias clase Person")
for r in g.query(q3):
  print(r.Subject, r.Property)
print("Instancias subclases de Person")
for s in g.query(q3_2):
  print(s.Subject, s.Person, s.Property)
print("\n")

# RDFLIB
print("RDFLIB")
NS = Namespace("http://somewhere#")
print("Instancias clase Person")
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  for s1,p1,o1 in g.triples((s,None,None)):
    print(s1,p1,o1)
print("Instancias subclases de Person")
for s,p,o in g.triples((None, RDF.type, None)):
  for s1,p1,o1 in g.triples((o, RDFS.subClassOf, NS.Person)):
    for s2,p2,o2 in g.triples((s, None, None)):
        print(s2,p2,o2)
