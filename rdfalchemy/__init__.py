from __future__ import absolute_import
from rdflib import URIRef, BNode, Namespace, RDF, RDFS
from rdfalchemy.Literal import Literal
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy.rdfsSubject import rdfsSubject, rdfsClass
from rdfalchemy.descriptors import (
    rdfSingle,
    rdfMultiple,
    rdfList,
    rdfContainer,
    owlTransitive
)
from .engine import (
    create_engine,
    engine_from_config
)

# if users don't use logging they could see a
# a confusing "No Handler could be found" warning
# this will mute that warning
import logging


class NullHandler(logging.Handler):
    def emit(self, record):
        pass

log = logging.getLogger(__name__)
log.addHandler(NullHandler())

__version__ = "0.3"

__exports__ = [
    BNode,
    create_engine,
    engine_from_config,
    Literal,
    Namespace,
    owlTransitive,
    RDF,
    rdfContainer,
    rdfList,
    rdfMultiple,
    RDFS,
    rdfsClass,
    rdfSingle,
    rdfsSubject,
    rdfSubject,
    URIRef
]
