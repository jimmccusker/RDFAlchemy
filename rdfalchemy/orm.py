# encoding: utf-8
"""
orm.py

Created by Philip Cooper on 2007-11-23.
Copyright (c) 2007 Openvest. All rights reserved.
"""

from builtins import str
from rdfalchemy.rdfSubject import rdfSubject
from rdfalchemy.descriptors import rdfAbstract

import logging
log = logging.getLogger(__name__)


def allsub(cl, beenthere=set([])):
    "return all subclasses of the given class"
    sub = set(cl.__subclasses__()) | beenthere
    newsubs = set(cl.__subclasses__()) - beenthere
    for onesub in newsubs:
        sub |= allsub(onesub, sub)
    return sub


def mapper(*classes):
    """
    Maps the classes given to allow descriptors with ranges to the
    proper Class of that type

    The default, if no args are provided, is to map recursively all subclasses
    of :class:`~rdfalchemy.rdfSubject.rdfSubject`

    Returns a dict of {rdf_type: mapped_class} for further processing
    """
    if not classes:
        classes = allsub(rdfSubject)
    class_dict = dict([(str(cl.rdf_type), cl) for cl in classes])
    for cl in classes:  # for each class
        for v in list(cl.__dict__.values()):  # for each desciptor
            # if its a descriptor with a range
            if isinstance(v, rdfAbstract) and v.range_type:
                try:
                    v._mappedClass = class_dict[str(v.range_type)]
                except KeyError:
                    log.warn("No Class Found\nFailed to map %s range of %s" % (
                        v, v.range_type))
    return class_dict

#def mapBase(baseclass):
#    """
#    This maps all classes below baseclass as in mapper()
#    AND puts the dict of {rdf_type: mapped_class}  in
#    an baseclass._type2class attribute
#    """
#    baseclass._type2class = mapper(*allsub(baseclass))
