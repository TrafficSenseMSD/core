# ./edges_xml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2018-02-11 21:00:54.173400 by PyXB version 1.2.6 using Python 3.6.3.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:8e81e4d8-0f98-11e8-8c08-186590d9922f')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: positiveFloatType
class positiveFloatType (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveFloatType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 10, 4)
    _Documentation = None
positiveFloatType._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.float, value=pyxb.binding.datatypes._fp(0.0))
positiveFloatType._InitializeFacetMap(positiveFloatType._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'positiveFloatType', positiveFloatType)
_module_typeBindings.positiveFloatType = positiveFloatType

# Atomic simple type: nonNegativeFloatType
class nonNegativeFloatType (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeFloatType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 16, 4)
    _Documentation = None
nonNegativeFloatType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeFloatType, value=pyxb.binding.datatypes.float(0.0))
nonNegativeFloatType._InitializeFacetMap(nonNegativeFloatType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'nonNegativeFloatType', nonNegativeFloatType)
_module_typeBindings.nonNegativeFloatType = nonNegativeFloatType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 24, 12)
    _Documentation = None
STD_ANON._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.float(-1.0))
STD_ANON._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON, value=pyxb.binding.datatypes.float(-1.0))
STD_ANON._InitializeFacetMap(STD_ANON._CF_minInclusive,
   STD_ANON._CF_maxInclusive)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 35, 12)
    _Documentation = None
STD_ANON_._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_._CF_pattern.addPattern(pattern='(norm|normc)\\((\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+)))?)?\\)')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_pattern)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: positiveIntType
class positiveIntType (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'positiveIntType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 43, 4)
    _Documentation = None
positiveIntType._CF_minExclusive = pyxb.binding.facets.CF_minExclusive(value_datatype=pyxb.binding.datatypes.int, value=pyxb.binding.datatypes.long(0))
positiveIntType._InitializeFacetMap(positiveIntType._CF_minExclusive)
Namespace.addCategoryObject('typeBinding', 'positiveIntType', positiveIntType)
_module_typeBindings.positiveIntType = positiveIntType

# Atomic simple type: nonNegativeIntType
class nonNegativeIntType (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeIntType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 49, 4)
    _Documentation = None
nonNegativeIntType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeIntType, value=pyxb.binding.datatypes.int(0))
nonNegativeIntType._InitializeFacetMap(nonNegativeIntType._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'nonNegativeIntType', nonNegativeIntType)
_module_typeBindings.nonNegativeIntType = nonNegativeIntType

# Atomic simple type: boolType
class boolType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boolType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 55, 4)
    _Documentation = None
boolType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=boolType, enum_prefix=None)
boolType.true = boolType._CF_enumeration.addEnumeration(unicode_value='true', tag='true')
boolType.false = boolType._CF_enumeration.addEnumeration(unicode_value='false', tag='false')
boolType.True_ = boolType._CF_enumeration.addEnumeration(unicode_value='True', tag='True_')
boolType.False_ = boolType._CF_enumeration.addEnumeration(unicode_value='False', tag='False_')
boolType.yes = boolType._CF_enumeration.addEnumeration(unicode_value='yes', tag='yes')
boolType.no = boolType._CF_enumeration.addEnumeration(unicode_value='no', tag='no')
boolType.on = boolType._CF_enumeration.addEnumeration(unicode_value='on', tag='on')
boolType.off = boolType._CF_enumeration.addEnumeration(unicode_value='off', tag='off')
boolType.n1 = boolType._CF_enumeration.addEnumeration(unicode_value='1', tag='n1')
boolType.n0 = boolType._CF_enumeration.addEnumeration(unicode_value='0', tag='n0')
boolType.x = boolType._CF_enumeration.addEnumeration(unicode_value='x', tag='x')
boolType.emptyString = boolType._CF_enumeration.addEnumeration(unicode_value='-', tag='emptyString')
boolType._InitializeFacetMap(boolType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'boolType', boolType)
_module_typeBindings.boolType = boolType

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 74, 12)
    _Documentation = None
STD_ANON_2._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_2._CF_pattern.addPattern(pattern='(0|(0?.(\\d+))|(1|1.0*)),(0|(0?.(\\d+))|(1|1.0*)),(0|(0?.(\\d+))|(1|1.0*))(,(0|(0?.(\\d+))|(1|1.0*)))?')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_pattern)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 79, 12)
    _Documentation = None
STD_ANON_3._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_3._CF_pattern.addPattern(pattern='(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5]),(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5]),(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])(,(\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5]))?')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_pattern)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 84, 12)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.red = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='red', tag='red')
STD_ANON_4.green = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='green', tag='green')
STD_ANON_4.blue = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='blue', tag='blue')
STD_ANON_4.yellow = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='yellow', tag='yellow')
STD_ANON_4.cyan = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='cyan', tag='cyan')
STD_ANON_4.magenta = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='magenta', tag='magenta')
STD_ANON_4.orange = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='orange', tag='orange')
STD_ANON_4.white = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='white', tag='white')
STD_ANON_4.black = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='black', tag='black')
STD_ANON_4.grey = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='grey', tag='grey')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: shapeType
class shapeType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shapeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 101, 4)
    _Documentation = None
shapeType._CF_pattern = pyxb.binding.facets.CF_pattern()
shapeType._CF_pattern.addPattern(pattern='((\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+)))?(\\s(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+)))?)*)?')
shapeType._InitializeFacetMap(shapeType._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'shapeType', shapeType)
_module_typeBindings.shapeType = shapeType

# Atomic simple type: shapeTypeTwo
class shapeTypeTwo (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'shapeTypeTwo')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 109, 4)
    _Documentation = None
shapeTypeTwo._CF_pattern = pyxb.binding.facets.CF_pattern()
shapeTypeTwo._CF_pattern.addPattern(pattern='(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+)))?\\s(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+)))?(\\s(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))(,(\\-)?(\\d+.?|(\\d*.\\d+)))?)*')
shapeTypeTwo._InitializeFacetMap(shapeTypeTwo._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'shapeTypeTwo', shapeTypeTwo)
_module_typeBindings.shapeTypeTwo = shapeTypeTwo

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 119, 12)
    _Documentation = None
STD_ANON_5._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_5._CF_pattern.addPattern(pattern='(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_pattern)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 126, 12)
    _Documentation = None
STD_ANON_6._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_6._CF_pattern.addPattern(pattern='(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_pattern)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 133, 12)
    _Documentation = None
STD_ANON_7._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_7._CF_pattern.addPattern(pattern='(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+)),(\\-)?(\\d+.?|(\\d*.\\d+))')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_pattern)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 186, 12)
    _Documentation = None
STD_ANON_8._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_8._CF_pattern.addPattern(pattern='(\\-)?(\\d+)(,(\\-)?(\\d+))*')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_pattern)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: tlTypeType
class tlTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tlTypeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 208, 4)
    _Documentation = None
tlTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tlTypeType, enum_prefix=None)
tlTypeType.actuated = tlTypeType._CF_enumeration.addEnumeration(unicode_value='actuated', tag='actuated')
tlTypeType.delay_based = tlTypeType._CF_enumeration.addEnumeration(unicode_value='delay_based', tag='delay_based')
tlTypeType.static = tlTypeType._CF_enumeration.addEnumeration(unicode_value='static', tag='static')
tlTypeType._InitializeFacetMap(tlTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tlTypeType', tlTypeType)
_module_typeBindings.tlTypeType = tlTypeType

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 222, 12)
    _Documentation = None
STD_ANON_9._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_9._CF_pattern.addPattern(pattern='[ruyYgGoOs]+')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_pattern)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: nodeTypeType
class nodeTypeType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nodeTypeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 257, 4)
    _Documentation = None
nodeTypeType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nodeTypeType, enum_prefix=None)
nodeTypeType.traffic_light = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='traffic_light', tag='traffic_light')
nodeTypeType.right_before_left = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='right_before_left', tag='right_before_left')
nodeTypeType.priority = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='priority', tag='priority')
nodeTypeType.dead_end = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='dead_end', tag='dead_end')
nodeTypeType.unregulated = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='unregulated', tag='unregulated')
nodeTypeType.traffic_light_unregulated = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='traffic_light_unregulated', tag='traffic_light_unregulated')
nodeTypeType.rail_signal = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='rail_signal', tag='rail_signal')
nodeTypeType.allway_stop = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='allway_stop', tag='allway_stop')
nodeTypeType.priority_stop = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='priority_stop', tag='priority_stop')
nodeTypeType.zipper = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='zipper', tag='zipper')
nodeTypeType.rail_crossing = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='rail_crossing', tag='rail_crossing')
nodeTypeType.traffic_light_right_on_red = nodeTypeType._CF_enumeration.addEnumeration(unicode_value='traffic_light_right_on_red', tag='traffic_light_right_on_red')
nodeTypeType._InitializeFacetMap(nodeTypeType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nodeTypeType', nodeTypeType)
_module_typeBindings.nodeTypeType = nodeTypeType

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 276, 12)
    _Documentation = None
STD_ANON_10._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_10._CF_pattern.addPattern(pattern='\\d+(([,;]|\\s)\\d+)*')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_pattern)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 20, 12)
    _Documentation = None
STD_ANON_11._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_11._CF_pattern.addPattern(pattern='\\d+.\\d+')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_pattern)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 52, 12)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.center = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_12.right = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Union simple type: nonNegativeFloatTypeWithErrorValue
# superclasses pyxb.binding.datatypes.anySimpleType
class nonNegativeFloatTypeWithErrorValue (pyxb.binding.basis.STD_union):

    """Simple type that is a union of nonNegativeFloatType, STD_ANON."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeFloatTypeWithErrorValue')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 22, 4)
    _Documentation = None

    _MemberTypes = ( nonNegativeFloatType, STD_ANON, )
nonNegativeFloatTypeWithErrorValue._CF_pattern = pyxb.binding.facets.CF_pattern()
nonNegativeFloatTypeWithErrorValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nonNegativeFloatTypeWithErrorValue)
nonNegativeFloatTypeWithErrorValue._InitializeFacetMap(nonNegativeFloatTypeWithErrorValue._CF_pattern,
   nonNegativeFloatTypeWithErrorValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nonNegativeFloatTypeWithErrorValue', nonNegativeFloatTypeWithErrorValue)
_module_typeBindings.nonNegativeFloatTypeWithErrorValue = nonNegativeFloatTypeWithErrorValue

# Union simple type: nonNegativeDistributionType
# superclasses pyxb.binding.datatypes.anySimpleType
class nonNegativeDistributionType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of nonNegativeFloatType, STD_ANON_."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'nonNegativeDistributionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 33, 4)
    _Documentation = None

    _MemberTypes = ( nonNegativeFloatType, STD_ANON_, )
nonNegativeDistributionType._CF_pattern = pyxb.binding.facets.CF_pattern()
nonNegativeDistributionType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=nonNegativeDistributionType)
nonNegativeDistributionType._InitializeFacetMap(nonNegativeDistributionType._CF_pattern,
   nonNegativeDistributionType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'nonNegativeDistributionType', nonNegativeDistributionType)
_module_typeBindings.nonNegativeDistributionType = nonNegativeDistributionType

# Union simple type: colorType
# superclasses pyxb.binding.datatypes.anySimpleType
class colorType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of STD_ANON_2, STD_ANON_3, STD_ANON_4."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'colorType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 72, 4)
    _Documentation = None

    _MemberTypes = ( STD_ANON_2, STD_ANON_3, STD_ANON_4, )
colorType._CF_pattern = pyxb.binding.facets.CF_pattern()
colorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=colorType)
colorType.red = 'red'                             # originally STD_ANON_4.red
colorType.green = 'green'                         # originally STD_ANON_4.green
colorType.blue = 'blue'                           # originally STD_ANON_4.blue
colorType.yellow = 'yellow'                       # originally STD_ANON_4.yellow
colorType.cyan = 'cyan'                           # originally STD_ANON_4.cyan
colorType.magenta = 'magenta'                     # originally STD_ANON_4.magenta
colorType.orange = 'orange'                       # originally STD_ANON_4.orange
colorType.white = 'white'                         # originally STD_ANON_4.white
colorType.black = 'black'                         # originally STD_ANON_4.black
colorType.grey = 'grey'                           # originally STD_ANON_4.grey
colorType._InitializeFacetMap(colorType._CF_pattern,
   colorType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'colorType', colorType)
_module_typeBindings.colorType = colorType

# Complex type intOptionType with content type EMPTY
class intOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type intOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'intOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 149, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_intOptionType_value', pyxb.binding.datatypes.int, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 150, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 150, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_intOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 151, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 151, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_intOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 152, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 152, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_intOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 153, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 153, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.intOptionType = intOptionType
Namespace.addCategoryObject('typeBinding', 'intOptionType', intOptionType)


# Complex type floatOptionType with content type EMPTY
class floatOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type floatOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'floatOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 156, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_floatOptionType_value', pyxb.binding.datatypes.float, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 157, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 157, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_floatOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 158, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 158, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_floatOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 159, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 159, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_floatOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 160, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 160, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.floatOptionType = floatOptionType
Namespace.addCategoryObject('typeBinding', 'floatOptionType', floatOptionType)


# Complex type timeOptionType with content type EMPTY
class timeOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type timeOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 163, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_timeOptionType_value', pyxb.binding.datatypes.float, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 164, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 164, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_timeOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 165, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 165, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_timeOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 166, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 166, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_timeOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 167, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 167, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.timeOptionType = timeOptionType
Namespace.addCategoryObject('typeBinding', 'timeOptionType', timeOptionType)


# Complex type strOptionType with content type EMPTY
class strOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type strOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'strOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 170, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_strOptionType_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 171, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 171, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_strOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 172, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 172, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_strOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 173, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 173, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_strOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 174, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 174, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.strOptionType = strOptionType
Namespace.addCategoryObject('typeBinding', 'strOptionType', strOptionType)


# Complex type fileOptionType with content type EMPTY
class fileOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type fileOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'fileOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_fileOptionType_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 178, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 178, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_fileOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 179, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 179, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_fileOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 180, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 180, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_fileOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 181, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 181, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.fileOptionType = fileOptionType
Namespace.addCategoryObject('typeBinding', 'fileOptionType', fileOptionType)


# Complex type paramType with content type EMPTY
class paramType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type paramType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'paramType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 230, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute key uses Python identifier key
    __key = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'key'), 'key', '__AbsentNamespace0_paramType_key', pyxb.binding.datatypes.string, required=True)
    __key._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 231, 8)
    __key._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 231, 8)
    
    key = property(__key.value, __key.set, None, None)

    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_paramType_value', pyxb.binding.datatypes.string, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 232, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 232, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __key.name() : __key,
        __value.name() : __value
    })
_module_typeBindings.paramType = paramType
Namespace.addCategoryObject('typeBinding', 'paramType', paramType)


# Complex type restrictionType with content type EMPTY
class restrictionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type restrictionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'restrictionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 252, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute vClass uses Python identifier vClass
    __vClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vClass'), 'vClass', '__AbsentNamespace0_restrictionType_vClass', pyxb.binding.datatypes.string, required=True)
    __vClass._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 253, 8)
    __vClass._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 253, 8)
    
    vClass = property(__vClass.value, __vClass.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_restrictionType_speed', pyxb.binding.datatypes.float, required=True)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 254, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 254, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __vClass.name() : __vClass,
        __speed.name() : __speed
    })
_module_typeBindings.restrictionType = restrictionType
Namespace.addCategoryObject('typeBinding', 'restrictionType', restrictionType)


# Complex type deleteType with content type EMPTY
class deleteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type deleteType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'deleteType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 77, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_deleteType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 78, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 78, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_deleteType_index', pyxb.binding.datatypes.nonNegativeInteger)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 79, 8)
    __index._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 79, 8)
    
    index = property(__index.value, __index.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __index.name() : __index
    })
_module_typeBindings.deleteType = deleteType
Namespace.addCategoryObject('typeBinding', 'deleteType', deleteType)


# Complex type roundaboutType with content type EMPTY
class roundaboutType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type roundaboutType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'roundaboutType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 82, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute nodes uses Python identifier nodes
    __nodes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nodes'), 'nodes', '__AbsentNamespace0_roundaboutType_nodes', pyxb.binding.datatypes.string)
    __nodes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 83, 8)
    __nodes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 83, 8)
    
    nodes = property(__nodes.value, __nodes.set, None, None)

    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_roundaboutType_edges', pyxb.binding.datatypes.string, required=True)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 84, 8)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 84, 8)
    
    edges = property(__edges.value, __edges.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __nodes.name() : __nodes,
        __edges.name() : __edges
    })
_module_typeBindings.roundaboutType = roundaboutType
Namespace.addCategoryObject('typeBinding', 'roundaboutType', roundaboutType)


# Complex type neighType with content type EMPTY
class neighType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type neighType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'neighType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 87, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lane uses Python identifier lane
    __lane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lane'), 'lane', '__AbsentNamespace0_neighType_lane', pyxb.binding.datatypes.string, required=True)
    __lane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 88, 8)
    __lane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 88, 8)
    
    lane = property(__lane.value, __lane.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lane.name() : __lane
    })
_module_typeBindings.neighType = neighType
Namespace.addCategoryObject('typeBinding', 'neighType', neighType)


# Complex type locationType with content type EMPTY
class locationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type locationType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'locationType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 117, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute netOffset uses Python identifier netOffset
    __netOffset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'netOffset'), 'netOffset', '__AbsentNamespace0_locationType_netOffset', _module_typeBindings.STD_ANON_5)
    __netOffset._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 118, 8)
    __netOffset._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 118, 8)
    
    netOffset = property(__netOffset.value, __netOffset.set, None, None)

    
    # Attribute convBoundary uses Python identifier convBoundary
    __convBoundary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'convBoundary'), 'convBoundary', '__AbsentNamespace0_locationType_convBoundary', _module_typeBindings.STD_ANON_6)
    __convBoundary._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 125, 8)
    __convBoundary._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 125, 8)
    
    convBoundary = property(__convBoundary.value, __convBoundary.set, None, None)

    
    # Attribute origBoundary uses Python identifier origBoundary
    __origBoundary = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'origBoundary'), 'origBoundary', '__AbsentNamespace0_locationType_origBoundary', _module_typeBindings.STD_ANON_7)
    __origBoundary._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 132, 8)
    __origBoundary._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 132, 8)
    
    origBoundary = property(__origBoundary.value, __origBoundary.set, None, None)

    
    # Attribute projParameter uses Python identifier projParameter
    __projParameter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'projParameter'), 'projParameter', '__AbsentNamespace0_locationType_projParameter', pyxb.binding.datatypes.string, required=True)
    __projParameter._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 139, 8)
    __projParameter._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 139, 8)
    
    projParameter = property(__projParameter.value, __projParameter.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __netOffset.name() : __netOffset,
        __convBoundary.name() : __convBoundary,
        __origBoundary.name() : __origBoundary,
        __projParameter.name() : __projParameter
    })
_module_typeBindings.locationType = locationType
Namespace.addCategoryObject('typeBinding', 'locationType', locationType)


# Complex type boolOptionType with content type EMPTY
class boolOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type boolOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'boolOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 142, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_boolOptionType_value', _module_typeBindings.boolType, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 143, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 143, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_boolOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 144, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 144, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_boolOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 145, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 145, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_boolOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 146, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 146, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.boolOptionType = boolOptionType
Namespace.addCategoryObject('typeBinding', 'boolOptionType', boolOptionType)


# Complex type intArrayOptionType with content type EMPTY
class intArrayOptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type intArrayOptionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'intArrayOptionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 184, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute value uses Python identifier value_
    __value = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'value'), 'value_', '__AbsentNamespace0_intArrayOptionType_value', _module_typeBindings.STD_ANON_8, required=True)
    __value._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 185, 8)
    __value._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 185, 8)
    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute synonymes uses Python identifier synonymes
    __synonymes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'synonymes'), 'synonymes', '__AbsentNamespace0_intArrayOptionType_synonymes', pyxb.binding.datatypes.string)
    __synonymes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 192, 8)
    __synonymes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 192, 8)
    
    synonymes = property(__synonymes.value, __synonymes.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_intArrayOptionType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 193, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 193, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute help uses Python identifier help
    __help = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_intArrayOptionType_help', pyxb.binding.datatypes.string)
    __help._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 194, 8)
    __help._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 194, 8)
    
    help = property(__help.value, __help.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __value.name() : __value,
        __synonymes.name() : __synonymes,
        __type.name() : __type,
        __help.name() : __help
    })
_module_typeBindings.intArrayOptionType = intArrayOptionType
Namespace.addCategoryObject('typeBinding', 'intArrayOptionType', intArrayOptionType)


# Complex type tlLogicType with content type ELEMENT_ONLY
class tlLogicType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tlLogicType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tlLogicType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 197, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element phase uses Python identifier phase
    __phase = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phase'), 'phase', '__AbsentNamespace0_tlLogicType_phase', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12), )

    
    phase = property(__phase.value, __phase.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_tlLogicType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_tlLogicType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 202, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 202, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_tlLogicType_type', _module_typeBindings.tlTypeType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 203, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 203, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute programID uses Python identifier programID
    __programID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'programID'), 'programID', '__AbsentNamespace0_tlLogicType_programID', pyxb.binding.datatypes.string, required=True)
    __programID._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 204, 8)
    __programID._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 204, 8)
    
    programID = property(__programID.value, __programID.set, None, None)

    
    # Attribute offset uses Python identifier offset
    __offset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'offset'), 'offset', '__AbsentNamespace0_tlLogicType_offset', pyxb.binding.datatypes.float)
    __offset._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 205, 8)
    __offset._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 205, 8)
    
    offset = property(__offset.value, __offset.set, None, None)

    _ElementMap.update({
        __phase.name() : __phase,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __type.name() : __type,
        __programID.name() : __programID,
        __offset.name() : __offset
    })
_module_typeBindings.tlLogicType = tlLogicType
Namespace.addCategoryObject('typeBinding', 'tlLogicType', tlLogicType)


# Complex type phaseType with content type EMPTY
class phaseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type phaseType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'phaseType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 217, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__AbsentNamespace0_phaseType_duration', _module_typeBindings.nonNegativeFloatType, required=True)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 218, 8)
    __duration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 218, 8)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute minDur uses Python identifier minDur
    __minDur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minDur'), 'minDur', '__AbsentNamespace0_phaseType_minDur', _module_typeBindings.nonNegativeFloatType)
    __minDur._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 219, 8)
    __minDur._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 219, 8)
    
    minDur = property(__minDur.value, __minDur.set, None, None)

    
    # Attribute maxDur uses Python identifier maxDur
    __maxDur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxDur'), 'maxDur', '__AbsentNamespace0_phaseType_maxDur', _module_typeBindings.nonNegativeFloatType)
    __maxDur._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 220, 8)
    __maxDur._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 220, 8)
    
    maxDur = property(__maxDur.value, __maxDur.set, None, None)

    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__AbsentNamespace0_phaseType_state', _module_typeBindings.STD_ANON_9, required=True)
    __state._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 221, 8)
    __state._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 221, 8)
    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __duration.name() : __duration,
        __minDur.name() : __minDur,
        __maxDur.name() : __maxDur,
        __state.name() : __state
    })
_module_typeBindings.phaseType = phaseType
Namespace.addCategoryObject('typeBinding', 'phaseType', phaseType)


# Complex type typeType with content type ELEMENT_ONLY
class typeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type typeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'typeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 235, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element restriction uses Python identifier restriction
    __restriction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'restriction'), 'restriction', '__AbsentNamespace0_typeType_restriction', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12), )

    
    restriction = property(__restriction.value, __restriction.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_typeType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 239, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 239, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute allow uses Python identifier allow
    __allow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'allow'), 'allow', '__AbsentNamespace0_typeType_allow', pyxb.binding.datatypes.string)
    __allow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 240, 8)
    __allow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 240, 8)
    
    allow = property(__allow.value, __allow.set, None, None)

    
    # Attribute disallow uses Python identifier disallow
    __disallow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disallow'), 'disallow', '__AbsentNamespace0_typeType_disallow', pyxb.binding.datatypes.string)
    __disallow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 241, 8)
    __disallow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 241, 8)
    
    disallow = property(__disallow.value, __disallow.set, None, None)

    
    # Attribute priority uses Python identifier priority
    __priority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'priority'), 'priority', '__AbsentNamespace0_typeType_priority', pyxb.binding.datatypes.int)
    __priority._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 242, 8)
    __priority._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 242, 8)
    
    priority = property(__priority.value, __priority.set, None, None)

    
    # Attribute numLanes uses Python identifier numLanes
    __numLanes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numLanes'), 'numLanes', '__AbsentNamespace0_typeType_numLanes', pyxb.binding.datatypes.int)
    __numLanes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 243, 8)
    __numLanes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 243, 8)
    
    numLanes = property(__numLanes.value, __numLanes.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_typeType_speed', pyxb.binding.datatypes.float)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 244, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 244, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute discard uses Python identifier discard
    __discard = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'discard'), 'discard', '__AbsentNamespace0_typeType_discard', _module_typeBindings.boolType)
    __discard._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 245, 8)
    __discard._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 245, 8)
    
    discard = property(__discard.value, __discard.set, None, None)

    
    # Attribute oneway uses Python identifier oneway
    __oneway = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'oneway'), 'oneway', '__AbsentNamespace0_typeType_oneway', _module_typeBindings.boolType)
    __oneway._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 246, 8)
    __oneway._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 246, 8)
    
    oneway = property(__oneway.value, __oneway.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_typeType_width', pyxb.binding.datatypes.float)
    __width._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 247, 8)
    __width._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 247, 8)
    
    width = property(__width.value, __width.set, None, None)

    
    # Attribute sidewalkWidth uses Python identifier sidewalkWidth
    __sidewalkWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sidewalkWidth'), 'sidewalkWidth', '__AbsentNamespace0_typeType_sidewalkWidth', pyxb.binding.datatypes.float)
    __sidewalkWidth._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 248, 8)
    __sidewalkWidth._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 248, 8)
    
    sidewalkWidth = property(__sidewalkWidth.value, __sidewalkWidth.set, None, None)

    
    # Attribute bikeLaneWidth uses Python identifier bikeLaneWidth
    __bikeLaneWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'bikeLaneWidth'), 'bikeLaneWidth', '__AbsentNamespace0_typeType_bikeLaneWidth', pyxb.binding.datatypes.float)
    __bikeLaneWidth._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 249, 8)
    __bikeLaneWidth._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 249, 8)
    
    bikeLaneWidth = property(__bikeLaneWidth.value, __bikeLaneWidth.set, None, None)

    _ElementMap.update({
        __restriction.name() : __restriction
    })
    _AttributeMap.update({
        __id.name() : __id,
        __allow.name() : __allow,
        __disallow.name() : __disallow,
        __priority.name() : __priority,
        __numLanes.name() : __numLanes,
        __speed.name() : __speed,
        __discard.name() : __discard,
        __oneway.name() : __oneway,
        __width.name() : __width,
        __sidewalkWidth.name() : __sidewalkWidth,
        __bikeLaneWidth.name() : __bikeLaneWidth
    })
_module_typeBindings.typeType = typeType
Namespace.addCategoryObject('typeBinding', 'typeType', typeType)


# Complex type splitType with content type EMPTY
class splitType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type splitType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'splitType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 274, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lanes uses Python identifier lanes
    __lanes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lanes'), 'lanes', '__AbsentNamespace0_splitType_lanes', _module_typeBindings.STD_ANON_10)
    __lanes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 275, 8)
    __lanes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 275, 8)
    
    lanes = property(__lanes.value, __lanes.set, None, None)

    
    # Attribute pos uses Python identifier pos
    __pos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pos'), 'pos', '__AbsentNamespace0_splitType_pos', pyxb.binding.datatypes.float, required=True)
    __pos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 282, 8)
    __pos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 282, 8)
    
    pos = property(__pos.value, __pos.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_splitType_speed', _module_typeBindings.positiveFloatType)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 283, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 283, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_splitType_type', _module_typeBindings.nodeTypeType)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 284, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 284, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute tl uses Python identifier tl
    __tl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tl'), 'tl', '__AbsentNamespace0_splitType_tl', pyxb.binding.datatypes.string)
    __tl._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 285, 8)
    __tl._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 285, 8)
    
    tl = property(__tl.value, __tl.set, None, None)

    
    # Attribute tlType uses Python identifier tlType
    __tlType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tlType'), 'tlType', '__AbsentNamespace0_splitType_tlType', _module_typeBindings.tlTypeType)
    __tlType._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 286, 8)
    __tlType._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 286, 8)
    
    tlType = property(__tlType.value, __tlType.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_splitType_shape', _module_typeBindings.shapeType)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 287, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 287, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute radius uses Python identifier radius
    __radius = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_splitType_radius', _module_typeBindings.nonNegativeFloatType)
    __radius._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 288, 8)
    __radius._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 288, 8)
    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Attribute keepClear uses Python identifier keepClear
    __keepClear = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'keepClear'), 'keepClear', '__AbsentNamespace0_splitType_keepClear', _module_typeBindings.boolType)
    __keepClear._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 289, 8)
    __keepClear._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 289, 8)
    
    keepClear = property(__keepClear.value, __keepClear.set, None, None)

    
    # Attribute idBefore uses Python identifier idBefore
    __idBefore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idBefore'), 'idBefore', '__AbsentNamespace0_splitType_idBefore', pyxb.binding.datatypes.string)
    __idBefore._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 290, 8)
    __idBefore._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 290, 8)
    
    idBefore = property(__idBefore.value, __idBefore.set, None, None)

    
    # Attribute idAfter uses Python identifier idAfter
    __idAfter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'idAfter'), 'idAfter', '__AbsentNamespace0_splitType_idAfter', pyxb.binding.datatypes.string)
    __idAfter._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 291, 8)
    __idAfter._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 291, 8)
    
    idAfter = property(__idAfter.value, __idAfter.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lanes.name() : __lanes,
        __pos.name() : __pos,
        __speed.name() : __speed,
        __type.name() : __type,
        __tl.name() : __tl,
        __tlType.name() : __tlType,
        __shape.name() : __shape,
        __radius.name() : __radius,
        __keepClear.name() : __keepClear,
        __idBefore.name() : __idBefore,
        __idAfter.name() : __idAfter
    })
_module_typeBindings.splitType = splitType
Namespace.addCategoryObject('typeBinding', 'splitType', splitType)


# Complex type edgesType with content type ELEMENT_ONLY
class edgesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type edgesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'edgesType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 13, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element edge uses Python identifier edge
    __edge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edge'), 'edge', '__AbsentNamespace0_edgesType_edge', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 15, 12), )

    
    edge = property(__edge.value, __edge.set, None, None)

    
    # Element roundabout uses Python identifier roundabout
    __roundabout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'roundabout'), 'roundabout', '__AbsentNamespace0_edgesType_roundabout', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 16, 12), )

    
    roundabout = property(__roundabout.value, __roundabout.set, None, None)

    
    # Element delete uses Python identifier delete
    __delete = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'delete'), 'delete', '__AbsentNamespace0_edgesType_delete', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 17, 12), )

    
    delete = property(__delete.value, __delete.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_edgesType_version', _module_typeBindings.STD_ANON_11)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 19, 8)
    __version._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 19, 8)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __edge.name() : __edge,
        __roundabout.name() : __roundabout,
        __delete.name() : __delete
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.edgesType = edgesType
Namespace.addCategoryObject('typeBinding', 'edgesType', edgesType)


# Complex type edgeType with content type ELEMENT_ONLY
class edgeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type edgeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'edgeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 28, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lane uses Python identifier lane
    __lane = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lane'), 'lane', '__AbsentNamespace0_edgeType_lane', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 30, 12), )

    
    lane = property(__lane.value, __lane.set, None, None)

    
    # Element split uses Python identifier split
    __split = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'split'), 'split', '__AbsentNamespace0_edgeType_split', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 31, 12), )

    
    split = property(__split.value, __split.set, None, None)

    
    # Element neigh uses Python identifier neigh
    __neigh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'neigh'), 'neigh', '__AbsentNamespace0_edgeType_neigh', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 32, 12), )

    
    neigh = property(__neigh.value, __neigh.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_edgeType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 33, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_edgeType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 35, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 35, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_edgeType_from', pyxb.binding.datatypes.string, required=True)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 36, 8)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 36, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_edgeType_to', pyxb.binding.datatypes.string, required=True)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 37, 8)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 37, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_edgeType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 38, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 38, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_edgeType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 39, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 39, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute allow uses Python identifier allow
    __allow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'allow'), 'allow', '__AbsentNamespace0_edgeType_allow', pyxb.binding.datatypes.string)
    __allow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 40, 8)
    __allow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 40, 8)
    
    allow = property(__allow.value, __allow.set, None, None)

    
    # Attribute disallow uses Python identifier disallow
    __disallow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disallow'), 'disallow', '__AbsentNamespace0_edgeType_disallow', pyxb.binding.datatypes.string)
    __disallow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 41, 8)
    __disallow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 41, 8)
    
    disallow = property(__disallow.value, __disallow.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_edgeType_length', _module_typeBindings.positiveFloatType)
    __length._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 42, 8)
    __length._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 42, 8)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute endOffset uses Python identifier endOffset
    __endOffset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endOffset'), 'endOffset', '__AbsentNamespace0_edgeType_endOffset', _module_typeBindings.nonNegativeFloatType)
    __endOffset._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 43, 8)
    __endOffset._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 43, 8)
    
    endOffset = property(__endOffset.value, __endOffset.set, None, None)

    
    # Attribute numLanes uses Python identifier numLanes
    __numLanes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'numLanes'), 'numLanes', '__AbsentNamespace0_edgeType_numLanes', pyxb.binding.datatypes.positiveInteger)
    __numLanes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 44, 8)
    __numLanes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 44, 8)
    
    numLanes = property(__numLanes.value, __numLanes.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_edgeType_speed', _module_typeBindings.positiveFloatType)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 45, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 45, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute priority uses Python identifier priority
    __priority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'priority'), 'priority', '__AbsentNamespace0_edgeType_priority', pyxb.binding.datatypes.int)
    __priority._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 46, 8)
    __priority._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 46, 8)
    
    priority = property(__priority.value, __priority.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_edgeType_width', _module_typeBindings.positiveFloatType)
    __width._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 47, 8)
    __width._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 47, 8)
    
    width = property(__width.value, __width.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_edgeType_shape', _module_typeBindings.shapeType)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 48, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 48, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute sidewalkWidth uses Python identifier sidewalkWidth
    __sidewalkWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sidewalkWidth'), 'sidewalkWidth', '__AbsentNamespace0_edgeType_sidewalkWidth', _module_typeBindings.nonNegativeFloatType)
    __sidewalkWidth._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 49, 8)
    __sidewalkWidth._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 49, 8)
    
    sidewalkWidth = property(__sidewalkWidth.value, __sidewalkWidth.set, None, None)

    
    # Attribute bikeLaneWidth uses Python identifier bikeLaneWidth
    __bikeLaneWidth = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'bikeLaneWidth'), 'bikeLaneWidth', '__AbsentNamespace0_edgeType_bikeLaneWidth', _module_typeBindings.nonNegativeFloatType)
    __bikeLaneWidth._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 50, 8)
    __bikeLaneWidth._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 50, 8)
    
    bikeLaneWidth = property(__bikeLaneWidth.value, __bikeLaneWidth.set, None, None)

    
    # Attribute spreadType uses Python identifier spreadType
    __spreadType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'spreadType'), 'spreadType', '__AbsentNamespace0_edgeType_spreadType', _module_typeBindings.STD_ANON_12)
    __spreadType._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 51, 8)
    __spreadType._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 51, 8)
    
    spreadType = property(__spreadType.value, __spreadType.set, None, None)

    _ElementMap.update({
        __lane.name() : __lane,
        __split.name() : __split,
        __neigh.name() : __neigh,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __from.name() : __from,
        __to.name() : __to,
        __type.name() : __type,
        __name.name() : __name,
        __allow.name() : __allow,
        __disallow.name() : __disallow,
        __length.name() : __length,
        __endOffset.name() : __endOffset,
        __numLanes.name() : __numLanes,
        __speed.name() : __speed,
        __priority.name() : __priority,
        __width.name() : __width,
        __shape.name() : __shape,
        __sidewalkWidth.name() : __sidewalkWidth,
        __bikeLaneWidth.name() : __bikeLaneWidth,
        __spreadType.name() : __spreadType
    })
_module_typeBindings.edgeType = edgeType
Namespace.addCategoryObject('typeBinding', 'edgeType', edgeType)


# Complex type laneType with content type ELEMENT_ONLY
class laneType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type laneType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'laneType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 61, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element neigh uses Python identifier neigh
    __neigh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'neigh'), 'neigh', '__AbsentNamespace0_laneType_neigh', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 63, 12), )

    
    neigh = property(__neigh.value, __neigh.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_laneType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 64, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_laneType_index', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 66, 8)
    __index._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 66, 8)
    
    index = property(__index.value, __index.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_laneType_speed', _module_typeBindings.positiveFloatType)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 67, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 67, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_laneType_width', _module_typeBindings.positiveFloatType)
    __width._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 68, 8)
    __width._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 68, 8)
    
    width = property(__width.value, __width.set, None, None)

    
    # Attribute allow uses Python identifier allow
    __allow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'allow'), 'allow', '__AbsentNamespace0_laneType_allow', pyxb.binding.datatypes.string)
    __allow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 69, 8)
    __allow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 69, 8)
    
    allow = property(__allow.value, __allow.set, None, None)

    
    # Attribute disallow uses Python identifier disallow
    __disallow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disallow'), 'disallow', '__AbsentNamespace0_laneType_disallow', pyxb.binding.datatypes.string)
    __disallow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 70, 8)
    __disallow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 70, 8)
    
    disallow = property(__disallow.value, __disallow.set, None, None)

    
    # Attribute prefer uses Python identifier prefer
    __prefer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prefer'), 'prefer', '__AbsentNamespace0_laneType_prefer', pyxb.binding.datatypes.string)
    __prefer._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 71, 8)
    __prefer._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 71, 8)
    
    prefer = property(__prefer.value, __prefer.set, None, None)

    
    # Attribute acceleration uses Python identifier acceleration
    __acceleration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'acceleration'), 'acceleration', '__AbsentNamespace0_laneType_acceleration', _module_typeBindings.boolType)
    __acceleration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 72, 8)
    __acceleration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 72, 8)
    
    acceleration = property(__acceleration.value, __acceleration.set, None, None)

    
    # Attribute endOffset uses Python identifier endOffset
    __endOffset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endOffset'), 'endOffset', '__AbsentNamespace0_laneType_endOffset', _module_typeBindings.nonNegativeFloatType)
    __endOffset._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 73, 8)
    __endOffset._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 73, 8)
    
    endOffset = property(__endOffset.value, __endOffset.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_laneType_shape', _module_typeBindings.shapeType)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 74, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 74, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    _ElementMap.update({
        __neigh.name() : __neigh,
        __param.name() : __param
    })
    _AttributeMap.update({
        __index.name() : __index,
        __speed.name() : __speed,
        __width.name() : __width,
        __allow.name() : __allow,
        __disallow.name() : __disallow,
        __prefer.name() : __prefer,
        __acceleration.name() : __acceleration,
        __endOffset.name() : __endOffset,
        __shape.name() : __shape
    })
_module_typeBindings.laneType = laneType
Namespace.addCategoryObject('typeBinding', 'laneType', laneType)


edges = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'edges'), edgesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', edges.name().localName(), edges)



tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase'), phaseType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12)))

tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 198, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tlLogicType._UseForTag(pyxb.namespace.ExpandedName(None, 'phase')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tlLogicType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tlLogicType._Automaton = _BuildAutomaton()




typeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restriction'), restrictionType, scope=typeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 236, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(typeType._UseForTag(pyxb.namespace.ExpandedName(None, 'restriction')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
typeType._Automaton = _BuildAutomaton_()




edgesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edge'), edgeType, scope=edgesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 15, 12)))

edgesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'roundabout'), roundaboutType, scope=edgesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 16, 12)))

edgesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'delete'), deleteType, scope=edgesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 17, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 14, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edgesType._UseForTag(pyxb.namespace.ExpandedName(None, 'edge')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 15, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edgesType._UseForTag(pyxb.namespace.ExpandedName(None, 'roundabout')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 16, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edgesType._UseForTag(pyxb.namespace.ExpandedName(None, 'delete')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 17, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
edgesType._Automaton = _BuildAutomaton_2()




edgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lane'), laneType, scope=edgeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 30, 12)))

edgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'split'), splitType, scope=edgeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 31, 12)))

edgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'neigh'), neighType, scope=edgeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 32, 12)))

edgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=edgeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 33, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 30, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 31, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 32, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 33, 12))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edgeType._UseForTag(pyxb.namespace.ExpandedName(None, 'lane')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 30, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(edgeType._UseForTag(pyxb.namespace.ExpandedName(None, 'split')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 31, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(edgeType._UseForTag(pyxb.namespace.ExpandedName(None, 'neigh')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 32, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(edgeType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 33, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
edgeType._Automaton = _BuildAutomaton_3()




laneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'neigh'), neighType, scope=laneType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 63, 12)))

laneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=laneType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 64, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 63, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 64, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(laneType._UseForTag(pyxb.namespace.ExpandedName(None, 'neigh')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 63, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(laneType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/edges_file.xsd', 64, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
laneType._Automaton = _BuildAutomaton_4()

