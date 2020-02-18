# Auto generated from mappings.yaml by pythongen.py version: 0.4.0
# Generation date: 2019-10-30 05:42
# Schema: mappings
#
# id: https://w3id.org/biolink/biolinkml/mappings
# description: Biolink model for mappings
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from biolinkml.utils.metamodelcore import URIorCURIE
from includes.types import Uriorcurie

metamodel_version = "1.4.3"


# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
META = CurieNamespace('meta', 'https://w3id.org/biolink/biolinkml/meta/')
METATYPE = CurieNamespace('metatype', 'https://w3id.org/biolink/biolinkml/type/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = META


# Types

# Class references





# Slots
class slots:
    pass

slots.mappings = Slot(uri=SKOS.mappingRelation, name="mappings", curie=SKOS.curie('mappingRelation'),
                      model_uri=META.mappings, domain=None, range=List[Union[str, URIorCURIE]])

slots.exact_mappings = Slot(uri=SKOS.exactMatch, name="exact mappings", curie=SKOS.curie('exactMatch'),
                      model_uri=META.exact_mappings, domain=None, range=List[Union[str, URIorCURIE]])

slots.close_mappings = Slot(uri=SKOS.closeMatch, name="close mappings", curie=SKOS.curie('closeMatch'),
                      model_uri=META.close_mappings, domain=None, range=List[Union[str, URIorCURIE]])

slots.related_mappings = Slot(uri=SKOS.relatedMatch, name="related mappings", curie=SKOS.curie('relatedMatch'),
                      model_uri=META.related_mappings, domain=None, range=List[Union[str, URIorCURIE]])

slots.deprecated_element_has_exact_replacement = Slot(uri=META.deprecated_element_has_exact_replacement, name="deprecated element has exact replacement", curie=META.curie('deprecated_element_has_exact_replacement'),
                      model_uri=META.deprecated_element_has_exact_replacement, domain=None, range=Optional[Union[str, URIorCURIE]], mappings = [IAO["0100001"]])

slots.deprecated_element_has_possible_replacement = Slot(uri=META.deprecated_element_has_possible_replacement, name="deprecated element has possible replacement", curie=META.curie('deprecated_element_has_possible_replacement'),
                      model_uri=META.deprecated_element_has_possible_replacement, domain=None, range=Optional[Union[str, URIorCURIE]], mappings = [OIO.consider])