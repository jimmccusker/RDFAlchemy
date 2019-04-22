# encoding: utf-8
from __future__ import print_function
import rdfalchemy
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy.descriptors import rdfLocale
from rdfalchemy.samples.doap import DOAP, Project
import platform

if platform.system() == 'Java':
    from nose import SkipTest
    raise SkipTest("Skipping, Java - Python unicode conflict")

rdfSubject.db.parse('rdfalchemy/samples/schema/doap.rdf')
p = Project(DOAP.SVNRepository)

Project.ls = rdfalchemy.rdfSingle(
    rdfalchemy.RDFS.label, cacheName='ls')
Project.lm = rdfalchemy.rdfMultiple(
    rdfalchemy.RDFS.label, cacheName='lm')
Project.len = rdfLocale(
    rdfalchemy.RDFS.label, 'en')
Project.les = rdfLocale(
    rdfalchemy.RDFS.label, 'es')
Project.lfr = rdfLocale(
    rdfalchemy.RDFS.label, 'fr')


def en_es_test():
    assert p.len == u'Subversion Repository', p.len
    assert p.les == u'Repositorio Subversion'
    assert p.lfr == u'D\xe9p\xf4t Subversion'

# unkown resp
print(repr(p.ls))
print(repr(p.lm))
print(repr(p.len))
print(repr(p.les))
print(repr(p.lfr))
