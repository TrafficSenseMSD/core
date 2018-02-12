# ./routes.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2018-02-11 19:54:10.064760 by PyXB version 1.2.6 using Python 3.6.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3b5939a4-0f8f-11e8-b52c-186590d9922f')

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
class STD_ANON_11 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 58, 12)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.right = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
STD_ANON_11.center = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_11.arbitrary = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='arbitrary', tag='arbitrary')
STD_ANON_11.nice = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='nice', tag='nice')
STD_ANON_11.compact = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='compact', tag='compact')
STD_ANON_11.left = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='left', tag='left')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 80, 12)
    _Documentation = None
STD_ANON_12._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_12, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_12._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_12, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_minInclusive,
   STD_ANON_12._CF_maxInclusive)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 90, 20)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.off = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='off', tag='off')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 116, 12)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.RB425 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='RB425', tag='RB425')
STD_ANON_14.NGT400 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='NGT400', tag='NGT400')
STD_ANON_14.NGT400_16 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='NGT400_16', tag='NGT400_16')
STD_ANON_14.ICE1 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='ICE1', tag='ICE1')
STD_ANON_14.ICE3 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='ICE3', tag='ICE3')
STD_ANON_14.REDosto7 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='REDosto7', tag='REDosto7')
STD_ANON_14.RB628 = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='RB628', tag='RB628')
STD_ANON_14.Freight = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='Freight', tag='Freight')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 131, 12)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.default = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
STD_ANON_15.DK2008 = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='DK2008', tag='DK2008')
STD_ANON_15.LC2013 = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='LC2013', tag='LC2013')
STD_ANON_15.SL2015 = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='SL2015', tag='SL2015')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 148, 12)
    _Documentation = None
STD_ANON_16._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_16, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_16._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_16, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_minInclusive,
   STD_ANON_16._CF_maxInclusive)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 164, 12)
    _Documentation = None
STD_ANON_17._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_17, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_17._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_17, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_minInclusive,
   STD_ANON_17._CF_maxInclusive)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 181, 12)
    _Documentation = None
STD_ANON_18._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_18, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_18._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_18, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_minInclusive,
   STD_ANON_18._CF_maxInclusive)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Atomic simple type: [anonymous]
class STD_ANON_19 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 195, 12)
    _Documentation = None
STD_ANON_19._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_19._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_19, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_19._InitializeFacetMap(STD_ANON_19._CF_minInclusive,
   STD_ANON_19._CF_maxInclusive)
_module_typeBindings.STD_ANON_19 = STD_ANON_19

# Atomic simple type: [anonymous]
class STD_ANON_20 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 214, 12)
    _Documentation = None
STD_ANON_20._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_20, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_20._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_20, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_20._InitializeFacetMap(STD_ANON_20._CF_minInclusive,
   STD_ANON_20._CF_maxInclusive)
_module_typeBindings.STD_ANON_20 = STD_ANON_20

# Atomic simple type: [anonymous]
class STD_ANON_21 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 230, 12)
    _Documentation = None
STD_ANON_21._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_21, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_21._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_21, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_21._InitializeFacetMap(STD_ANON_21._CF_minInclusive,
   STD_ANON_21._CF_maxInclusive)
_module_typeBindings.STD_ANON_21 = STD_ANON_21

# Atomic simple type: [anonymous]
class STD_ANON_22 (pyxb.binding.datatypes.float):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 246, 12)
    _Documentation = None
STD_ANON_22._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=STD_ANON_22, value=pyxb.binding.datatypes.float(0.0))
STD_ANON_22._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=STD_ANON_22, value=pyxb.binding.datatypes.float(1.0))
STD_ANON_22._InitializeFacetMap(STD_ANON_22._CF_minInclusive,
   STD_ANON_22._CF_maxInclusive)
_module_typeBindings.STD_ANON_22 = STD_ANON_22

# Atomic simple type: [anonymous]
class STD_ANON_23 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 381, 12)
    _Documentation = None
STD_ANON_23._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_23, enum_prefix=None)
STD_ANON_23.triggered = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='triggered', tag='triggered')
STD_ANON_23.containerTriggered = STD_ANON_23._CF_enumeration.addEnumeration(unicode_value='containerTriggered', tag='containerTriggered')
STD_ANON_23._InitializeFacetMap(STD_ANON_23._CF_enumeration)
_module_typeBindings.STD_ANON_23 = STD_ANON_23

# Atomic simple type: [anonymous]
class STD_ANON_24 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 392, 12)
    _Documentation = None
STD_ANON_24._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_24, enum_prefix=None)
STD_ANON_24.random = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='random', tag='random')
STD_ANON_24.free = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='free', tag='free')
STD_ANON_24.allowed = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='allowed', tag='allowed')
STD_ANON_24.first = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='first', tag='first')
STD_ANON_24.best = STD_ANON_24._CF_enumeration.addEnumeration(unicode_value='best', tag='best')
STD_ANON_24._InitializeFacetMap(STD_ANON_24._CF_enumeration)
_module_typeBindings.STD_ANON_24 = STD_ANON_24

# Atomic simple type: [anonymous]
class STD_ANON_25 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 406, 12)
    _Documentation = None
STD_ANON_25._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_25, enum_prefix=None)
STD_ANON_25.random = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='random', tag='random')
STD_ANON_25.random_free = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='random_free', tag='random_free')
STD_ANON_25.free = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='free', tag='free')
STD_ANON_25.base = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='base', tag='base')
STD_ANON_25.last = STD_ANON_25._CF_enumeration.addEnumeration(unicode_value='last', tag='last')
STD_ANON_25._InitializeFacetMap(STD_ANON_25._CF_enumeration)
_module_typeBindings.STD_ANON_25 = STD_ANON_25

# Atomic simple type: [anonymous]
class STD_ANON_26 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 420, 12)
    _Documentation = None
STD_ANON_26._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_26, enum_prefix=None)
STD_ANON_26.random = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='random', tag='random')
STD_ANON_26.max = STD_ANON_26._CF_enumeration.addEnumeration(unicode_value='max', tag='max')
STD_ANON_26._InitializeFacetMap(STD_ANON_26._CF_enumeration)
_module_typeBindings.STD_ANON_26 = STD_ANON_26

# Atomic simple type: [anonymous]
class STD_ANON_27 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 431, 12)
    _Documentation = None
STD_ANON_27._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_27, enum_prefix=None)
STD_ANON_27.current = STD_ANON_27._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
STD_ANON_27._InitializeFacetMap(STD_ANON_27._CF_enumeration)
_module_typeBindings.STD_ANON_27 = STD_ANON_27

# Atomic simple type: [anonymous]
class STD_ANON_28 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 441, 12)
    _Documentation = None
STD_ANON_28._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_28, enum_prefix=None)
STD_ANON_28.random = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='random', tag='random')
STD_ANON_28.max = STD_ANON_28._CF_enumeration.addEnumeration(unicode_value='max', tag='max')
STD_ANON_28._InitializeFacetMap(STD_ANON_28._CF_enumeration)
_module_typeBindings.STD_ANON_28 = STD_ANON_28

# Atomic simple type: [anonymous]
class STD_ANON_29 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 452, 12)
    _Documentation = None
STD_ANON_29._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_29, enum_prefix=None)
STD_ANON_29.random = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='random', tag='random')
STD_ANON_29.free = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='free', tag='free')
STD_ANON_29.random_free = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='random_free', tag='random_free')
STD_ANON_29.right = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
STD_ANON_29.center = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_29.left = STD_ANON_29._CF_enumeration.addEnumeration(unicode_value='left', tag='left')
STD_ANON_29._InitializeFacetMap(STD_ANON_29._CF_enumeration)
_module_typeBindings.STD_ANON_29 = STD_ANON_29

# Atomic simple type: [anonymous]
class STD_ANON_30 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 467, 12)
    _Documentation = None
STD_ANON_30._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_30, enum_prefix=None)
STD_ANON_30.right = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
STD_ANON_30.center = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_30.left = STD_ANON_30._CF_enumeration.addEnumeration(unicode_value='left', tag='left')
STD_ANON_30._InitializeFacetMap(STD_ANON_30._CF_enumeration)
_module_typeBindings.STD_ANON_30 = STD_ANON_30

# Atomic simple type: [anonymous]
class STD_ANON_31 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 479, 12)
    _Documentation = None
STD_ANON_31._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_31, enum_prefix=None)
STD_ANON_31.current = STD_ANON_31._CF_enumeration.addEnumeration(unicode_value='current', tag='current')
STD_ANON_31._InitializeFacetMap(STD_ANON_31._CF_enumeration)
_module_typeBindings.STD_ANON_31 = STD_ANON_31

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

# Union simple type: [anonymous]
# superclasses pyxb.binding.datatypes.anySimpleType
class STD_ANON_32 (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.float, STD_ANON_13."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 88, 12)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.float, STD_ANON_13, )
STD_ANON_32._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_32._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_32)
STD_ANON_32.off = 'off'                           # originally STD_ANON_13.off
STD_ANON_32._InitializeFacetMap(STD_ANON_32._CF_pattern,
   STD_ANON_32._CF_enumeration)
_module_typeBindings.STD_ANON_32 = STD_ANON_32

# Union simple type: departType
# superclasses pyxb.binding.datatypes.anySimpleType
class departType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of nonNegativeFloatType, STD_ANON_23."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'departType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 379, 4)
    _Documentation = None

    _MemberTypes = ( nonNegativeFloatType, STD_ANON_23, )
departType._CF_pattern = pyxb.binding.facets.CF_pattern()
departType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=departType)
departType.triggered = 'triggered'                # originally STD_ANON_23.triggered
departType.containerTriggered = 'containerTriggered'# originally STD_ANON_23.containerTriggered
departType._InitializeFacetMap(departType._CF_pattern,
   departType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'departType', departType)
_module_typeBindings.departType = departType

# Union simple type: departLaneType
# superclasses pyxb.binding.datatypes.anySimpleType
class departLaneType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.nonNegativeInteger, STD_ANON_24."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'departLaneType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 390, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.nonNegativeInteger, STD_ANON_24, )
departLaneType._CF_pattern = pyxb.binding.facets.CF_pattern()
departLaneType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=departLaneType)
departLaneType.random = 'random'                  # originally STD_ANON_24.random
departLaneType.free = 'free'                      # originally STD_ANON_24.free
departLaneType.allowed = 'allowed'                # originally STD_ANON_24.allowed
departLaneType.first = 'first'                    # originally STD_ANON_24.first
departLaneType.best = 'best'                      # originally STD_ANON_24.best
departLaneType._InitializeFacetMap(departLaneType._CF_pattern,
   departLaneType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'departLaneType', departLaneType)
_module_typeBindings.departLaneType = departLaneType

# Union simple type: departPosType
# superclasses pyxb.binding.datatypes.anySimpleType
class departPosType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.float, STD_ANON_25."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'departPosType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 404, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.float, STD_ANON_25, )
departPosType._CF_pattern = pyxb.binding.facets.CF_pattern()
departPosType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=departPosType)
departPosType.random = 'random'                   # originally STD_ANON_25.random
departPosType.random_free = 'random_free'         # originally STD_ANON_25.random_free
departPosType.free = 'free'                       # originally STD_ANON_25.free
departPosType.base = 'base'                       # originally STD_ANON_25.base
departPosType.last = 'last'                       # originally STD_ANON_25.last
departPosType._InitializeFacetMap(departPosType._CF_pattern,
   departPosType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'departPosType', departPosType)
_module_typeBindings.departPosType = departPosType

# Union simple type: departSpeedType
# superclasses pyxb.binding.datatypes.anySimpleType
class departSpeedType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of nonNegativeFloatType, STD_ANON_26."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'departSpeedType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 418, 4)
    _Documentation = None

    _MemberTypes = ( nonNegativeFloatType, STD_ANON_26, )
departSpeedType._CF_pattern = pyxb.binding.facets.CF_pattern()
departSpeedType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=departSpeedType)
departSpeedType.random = 'random'                 # originally STD_ANON_26.random
departSpeedType.max = 'max'                       # originally STD_ANON_26.max
departSpeedType._InitializeFacetMap(departSpeedType._CF_pattern,
   departSpeedType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'departSpeedType', departSpeedType)
_module_typeBindings.departSpeedType = departSpeedType

# Union simple type: arrivalLaneType
# superclasses pyxb.binding.datatypes.anySimpleType
class arrivalLaneType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.nonNegativeInteger, STD_ANON_27."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'arrivalLaneType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 429, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.nonNegativeInteger, STD_ANON_27, )
arrivalLaneType._CF_pattern = pyxb.binding.facets.CF_pattern()
arrivalLaneType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=arrivalLaneType)
arrivalLaneType.current = 'current'               # originally STD_ANON_27.current
arrivalLaneType._InitializeFacetMap(arrivalLaneType._CF_pattern,
   arrivalLaneType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'arrivalLaneType', arrivalLaneType)
_module_typeBindings.arrivalLaneType = arrivalLaneType

# Union simple type: arrivalPosType
# superclasses pyxb.binding.datatypes.anySimpleType
class arrivalPosType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.float, STD_ANON_28."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'arrivalPosType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 439, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.float, STD_ANON_28, )
arrivalPosType._CF_pattern = pyxb.binding.facets.CF_pattern()
arrivalPosType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=arrivalPosType)
arrivalPosType.random = 'random'                  # originally STD_ANON_28.random
arrivalPosType.max = 'max'                        # originally STD_ANON_28.max
arrivalPosType._InitializeFacetMap(arrivalPosType._CF_pattern,
   arrivalPosType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'arrivalPosType', arrivalPosType)
_module_typeBindings.arrivalPosType = arrivalPosType

# Union simple type: departPosLatType
# superclasses pyxb.binding.datatypes.anySimpleType
class departPosLatType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.float, STD_ANON_29."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'departPosLatType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 450, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.float, STD_ANON_29, )
departPosLatType._CF_pattern = pyxb.binding.facets.CF_pattern()
departPosLatType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=departPosLatType)
departPosLatType.random = 'random'                # originally STD_ANON_29.random
departPosLatType.free = 'free'                    # originally STD_ANON_29.free
departPosLatType.random_free = 'random_free'      # originally STD_ANON_29.random_free
departPosLatType.right = 'right'                  # originally STD_ANON_29.right
departPosLatType.center = 'center'                # originally STD_ANON_29.center
departPosLatType.left = 'left'                    # originally STD_ANON_29.left
departPosLatType._InitializeFacetMap(departPosLatType._CF_pattern,
   departPosLatType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'departPosLatType', departPosLatType)
_module_typeBindings.departPosLatType = departPosLatType

# Union simple type: arrivalPosLatType
# superclasses pyxb.binding.datatypes.anySimpleType
class arrivalPosLatType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of pyxb.binding.datatypes.float, STD_ANON_30."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'arrivalPosLatType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 465, 4)
    _Documentation = None

    _MemberTypes = ( pyxb.binding.datatypes.float, STD_ANON_30, )
arrivalPosLatType._CF_pattern = pyxb.binding.facets.CF_pattern()
arrivalPosLatType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=arrivalPosLatType)
arrivalPosLatType.right = 'right'                 # originally STD_ANON_30.right
arrivalPosLatType.center = 'center'               # originally STD_ANON_30.center
arrivalPosLatType.left = 'left'                   # originally STD_ANON_30.left
arrivalPosLatType._InitializeFacetMap(arrivalPosLatType._CF_pattern,
   arrivalPosLatType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'arrivalPosLatType', arrivalPosLatType)
_module_typeBindings.arrivalPosLatType = arrivalPosLatType

# Union simple type: arrivalSpeedType
# superclasses pyxb.binding.datatypes.anySimpleType
class arrivalSpeedType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of nonNegativeFloatType, STD_ANON_31."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'arrivalSpeedType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 477, 4)
    _Documentation = None

    _MemberTypes = ( nonNegativeFloatType, STD_ANON_31, )
arrivalSpeedType._CF_pattern = pyxb.binding.facets.CF_pattern()
arrivalSpeedType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=arrivalSpeedType)
arrivalSpeedType.current = 'current'              # originally STD_ANON_31.current
arrivalSpeedType._InitializeFacetMap(arrivalSpeedType._CF_pattern,
   arrivalSpeedType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'arrivalSpeedType', arrivalSpeedType)
_module_typeBindings.arrivalSpeedType = arrivalSpeedType

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


# Complex type vTypeDistributionType with content type ELEMENT_ONLY
class vTypeDistributionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vTypeDistributionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vTypeDistributionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 531, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vType uses Python identifier vType
    __vType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vType'), 'vType', '__AbsentNamespace0_vTypeDistributionType_vType', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 533, 12), )

    
    vType = property(__vType.value, __vType.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_vTypeDistributionType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 535, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 535, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute vTypes uses Python identifier vTypes
    __vTypes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vTypes'), 'vTypes', '__AbsentNamespace0_vTypeDistributionType_vTypes', pyxb.binding.datatypes.string)
    __vTypes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 536, 8)
    __vTypes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 536, 8)
    
    vTypes = property(__vTypes.value, __vTypes.set, None, None)

    _ElementMap.update({
        __vType.name() : __vType
    })
    _AttributeMap.update({
        __id.name() : __id,
        __vTypes.name() : __vTypes
    })
_module_typeBindings.vTypeDistributionType = vTypeDistributionType
Namespace.addCategoryObject('typeBinding', 'vTypeDistributionType', vTypeDistributionType)


# Complex type routeDistributionType with content type ELEMENT_ONLY
class routeDistributionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type routeDistributionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routeDistributionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 539, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__AbsentNamespace0_routeDistributionType_route', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 541, 12), )

    
    route = property(__route.value, __route.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_routeDistributionType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 543, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 543, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute last uses Python identifier last
    __last = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'last'), 'last', '__AbsentNamespace0_routeDistributionType_last', pyxb.binding.datatypes.nonNegativeInteger)
    __last._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 544, 8)
    __last._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 544, 8)
    
    last = property(__last.value, __last.set, None, None)

    
    # Attribute routes uses Python identifier routes
    __routes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'routes'), 'routes', '__AbsentNamespace0_routeDistributionType_routes', pyxb.binding.datatypes.string)
    __routes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 545, 8)
    __routes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 545, 8)
    
    routes = property(__routes.value, __routes.set, None, None)

    
    # Attribute probabilities uses Python identifier probabilities
    __probabilities = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probabilities'), 'probabilities', '__AbsentNamespace0_routeDistributionType_probabilities', pyxb.binding.datatypes.string)
    __probabilities._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 546, 8)
    __probabilities._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 546, 8)
    
    probabilities = property(__probabilities.value, __probabilities.set, None, None)

    _ElementMap.update({
        __route.name() : __route
    })
    _AttributeMap.update({
        __id.name() : __id,
        __last.name() : __last,
        __routes.name() : __routes,
        __probabilities.name() : __probabilities
    })
_module_typeBindings.routeDistributionType = routeDistributionType
Namespace.addCategoryObject('typeBinding', 'routeDistributionType', routeDistributionType)


# Complex type vehicleRouteDistributionType with content type ELEMENT_ONLY
class vehicleRouteDistributionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vehicleRouteDistributionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vehicleRouteDistributionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 549, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__AbsentNamespace0_vehicleRouteDistributionType_route', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 551, 12), )

    
    route = property(__route.value, __route.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_vehicleRouteDistributionType_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 553, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 553, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute last uses Python identifier last
    __last = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'last'), 'last', '__AbsentNamespace0_vehicleRouteDistributionType_last', pyxb.binding.datatypes.nonNegativeInteger)
    __last._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 554, 8)
    __last._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 554, 8)
    
    last = property(__last.value, __last.set, None, None)

    _ElementMap.update({
        __route.name() : __route
    })
    _AttributeMap.update({
        __id.name() : __id,
        __last.name() : __last
    })
_module_typeBindings.vehicleRouteDistributionType = vehicleRouteDistributionType
Namespace.addCategoryObject('typeBinding', 'vehicleRouteDistributionType', vehicleRouteDistributionType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 571, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_CTD_ANON_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 572, 20)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 572, 20)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_CTD_ANON_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 573, 20)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 573, 20)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute busStop uses Python identifier busStop
    __busStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'busStop'), 'busStop', '__AbsentNamespace0_CTD_ANON_busStop', pyxb.binding.datatypes.string)
    __busStop._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 574, 20)
    __busStop._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 574, 20)
    
    busStop = property(__busStop.value, __busStop.set, None, None)

    
    # Attribute lines uses Python identifier lines
    __lines = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lines'), 'lines', '__AbsentNamespace0_CTD_ANON_lines', pyxb.binding.datatypes.string, required=True)
    __lines._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 575, 20)
    __lines._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 575, 20)
    
    lines = property(__lines.value, __lines.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_CTD_ANON_arrivalPos', pyxb.binding.datatypes.float)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 576, 20)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 576, 20)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute cost uses Python identifier cost
    __cost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cost'), 'cost', '__AbsentNamespace0_CTD_ANON_cost', pyxb.binding.datatypes.float)
    __cost._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 577, 20)
    __cost._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 577, 20)
    
    cost = property(__cost.value, __cost.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __from.name() : __from,
        __to.name() : __to,
        __busStop.name() : __busStop,
        __lines.name() : __lines,
        __arrivalPos.name() : __arrivalPos,
        __cost.name() : __cost
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 612, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_CTD_ANON__from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 613, 20)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 613, 20)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_CTD_ANON__to', pyxb.binding.datatypes.string, required=True)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 614, 20)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 614, 20)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute lines uses Python identifier lines
    __lines = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lines'), 'lines', '__AbsentNamespace0_CTD_ANON__lines', pyxb.binding.datatypes.string, required=True)
    __lines._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 615, 20)
    __lines._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 615, 20)
    
    lines = property(__lines.value, __lines.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __from.name() : __from,
        __to.name() : __to,
        __lines.name() : __lines
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type routesType with content type ELEMENT_ONLY
class routesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type routesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routesType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 9, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element vTypeDistribution uses Python identifier vTypeDistribution
    __vTypeDistribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vTypeDistribution'), 'vTypeDistribution', '__AbsentNamespace0_routesType_vTypeDistribution', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 11, 12), )

    
    vTypeDistribution = property(__vTypeDistribution.value, __vTypeDistribution.set, None, None)

    
    # Element routeDistribution uses Python identifier routeDistribution
    __routeDistribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routeDistribution'), 'routeDistribution', '__AbsentNamespace0_routesType_routeDistribution', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 12, 12), )

    
    routeDistribution = property(__routeDistribution.value, __routeDistribution.set, None, None)

    
    # Element vType uses Python identifier vType
    __vType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vType'), 'vType', '__AbsentNamespace0_routesType_vType', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 13, 12), )

    
    vType = property(__vType.value, __vType.set, None, None)

    
    # Element vehicle uses Python identifier vehicle
    __vehicle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehicle'), 'vehicle', '__AbsentNamespace0_routesType_vehicle', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 14, 12), )

    
    vehicle = property(__vehicle.value, __vehicle.set, None, None)

    
    # Element route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__AbsentNamespace0_routesType_route', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 15, 12), )

    
    route = property(__route.value, __route.set, None, None)

    
    # Element flow uses Python identifier flow
    __flow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flow'), 'flow', '__AbsentNamespace0_routesType_flow', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 16, 12), )

    
    flow = property(__flow.value, __flow.set, None, None)

    
    # Element trip uses Python identifier trip
    __trip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'trip'), 'trip', '__AbsentNamespace0_routesType_trip', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 17, 12), )

    
    trip = property(__trip.value, __trip.set, None, None)

    
    # Element person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'person'), 'person', '__AbsentNamespace0_routesType_person', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 18, 12), )

    
    person = property(__person.value, __person.set, None, None)

    
    # Element container uses Python identifier container
    __container = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'container'), 'container', '__AbsentNamespace0_routesType_container', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 19, 12), )

    
    container = property(__container.value, __container.set, None, None)

    
    # Element include uses Python identifier include
    __include = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'include'), 'include', '__AbsentNamespace0_routesType_include', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 20, 12), )

    
    include = property(__include.value, __include.set, None, None)

    _ElementMap.update({
        __vTypeDistribution.name() : __vTypeDistribution,
        __routeDistribution.name() : __routeDistribution,
        __vType.name() : __vType,
        __vehicle.name() : __vehicle,
        __route.name() : __route,
        __flow.name() : __flow,
        __trip.name() : __trip,
        __person.name() : __person,
        __container.name() : __container,
        __include.name() : __include
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.routesType = routesType
Namespace.addCategoryObject('typeBinding', 'routesType', routesType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 21, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'href'), 'href', '__AbsentNamespace0_CTD_ANON_2_href', pyxb.binding.datatypes.string)
    __href._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 22, 20)
    __href._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 22, 20)
    
    href = property(__href.value, __href.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


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


# Complex type cfIDMType with content type EMPTY
class cfIDMType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfIDMType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfIDMType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 144, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfIDMType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 145, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 145, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfIDMType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 146, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 146, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfIDMType_sigma', _module_typeBindings.STD_ANON_16)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 147, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 147, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfIDMType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 155, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 155, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute delta uses Python identifier delta
    __delta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delta'), 'delta', '__AbsentNamespace0_cfIDMType_delta', pyxb.binding.datatypes.float)
    __delta._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 156, 8)
    __delta._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 156, 8)
    
    delta = property(__delta.value, __delta.set, None, None)

    
    # Attribute stepping uses Python identifier stepping
    __stepping = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stepping'), 'stepping', '__AbsentNamespace0_cfIDMType_stepping', _module_typeBindings.positiveIntType)
    __stepping._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 157, 8)
    __stepping._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 157, 8)
    
    stepping = property(__stepping.value, __stepping.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau,
        __delta.name() : __delta,
        __stepping.name() : __stepping
    })
_module_typeBindings.cfIDMType = cfIDMType
Namespace.addCategoryObject('typeBinding', 'cfIDMType', cfIDMType)


# Complex type cfIDMMType with content type EMPTY
class cfIDMMType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfIDMMType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfIDMMType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfIDMMType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 161, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 161, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfIDMMType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 162, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 162, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfIDMMType_sigma', _module_typeBindings.STD_ANON_17)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 163, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 163, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfIDMMType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 171, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 171, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute adaptTime uses Python identifier adaptTime
    __adaptTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adaptTime'), 'adaptTime', '__AbsentNamespace0_cfIDMMType_adaptTime', pyxb.binding.datatypes.float)
    __adaptTime._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 172, 8)
    __adaptTime._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 172, 8)
    
    adaptTime = property(__adaptTime.value, __adaptTime.set, None, None)

    
    # Attribute adaptFactor uses Python identifier adaptFactor
    __adaptFactor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adaptFactor'), 'adaptFactor', '__AbsentNamespace0_cfIDMMType_adaptFactor', pyxb.binding.datatypes.float)
    __adaptFactor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 173, 8)
    __adaptFactor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 173, 8)
    
    adaptFactor = property(__adaptFactor.value, __adaptFactor.set, None, None)

    
    # Attribute stepping uses Python identifier stepping
    __stepping = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stepping'), 'stepping', '__AbsentNamespace0_cfIDMMType_stepping', _module_typeBindings.positiveIntType)
    __stepping._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 174, 8)
    __stepping._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 174, 8)
    
    stepping = property(__stepping.value, __stepping.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau,
        __adaptTime.name() : __adaptTime,
        __adaptFactor.name() : __adaptFactor,
        __stepping.name() : __stepping
    })
_module_typeBindings.cfIDMMType = cfIDMMType
Namespace.addCategoryObject('typeBinding', 'cfIDMMType', cfIDMMType)


# Complex type cfKraussType with content type EMPTY
class cfKraussType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfKraussType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfKraussType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfKraussType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 178, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 178, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfKraussType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 179, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 179, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfKraussType_sigma', _module_typeBindings.STD_ANON_18)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 180, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 180, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfKraussType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 188, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 188, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau
    })
_module_typeBindings.cfKraussType = cfKraussType
Namespace.addCategoryObject('typeBinding', 'cfKraussType', cfKraussType)


# Complex type cfSmartType with content type EMPTY
class cfSmartType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfSmartType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfSmartType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 191, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfSmartType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 192, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 192, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfSmartType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 193, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 193, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfSmartType_sigma', _module_typeBindings.STD_ANON_19)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 194, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 194, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfSmartType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 202, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 202, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute tmp1 uses Python identifier tmp1
    __tmp1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp1'), 'tmp1', '__AbsentNamespace0_cfSmartType_tmp1', pyxb.binding.datatypes.float)
    __tmp1._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 203, 8)
    __tmp1._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 203, 8)
    
    tmp1 = property(__tmp1.value, __tmp1.set, None, None)

    
    # Attribute tmp2 uses Python identifier tmp2
    __tmp2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp2'), 'tmp2', '__AbsentNamespace0_cfSmartType_tmp2', pyxb.binding.datatypes.float)
    __tmp2._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 204, 8)
    __tmp2._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 204, 8)
    
    tmp2 = property(__tmp2.value, __tmp2.set, None, None)

    
    # Attribute tmp3 uses Python identifier tmp3
    __tmp3 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp3'), 'tmp3', '__AbsentNamespace0_cfSmartType_tmp3', pyxb.binding.datatypes.float)
    __tmp3._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 205, 8)
    __tmp3._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 205, 8)
    
    tmp3 = property(__tmp3.value, __tmp3.set, None, None)

    
    # Attribute tmp4 uses Python identifier tmp4
    __tmp4 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp4'), 'tmp4', '__AbsentNamespace0_cfSmartType_tmp4', pyxb.binding.datatypes.float)
    __tmp4._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 206, 8)
    __tmp4._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 206, 8)
    
    tmp4 = property(__tmp4.value, __tmp4.set, None, None)

    
    # Attribute tmp5 uses Python identifier tmp5
    __tmp5 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp5'), 'tmp5', '__AbsentNamespace0_cfSmartType_tmp5', pyxb.binding.datatypes.float)
    __tmp5._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 207, 8)
    __tmp5._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 207, 8)
    
    tmp5 = property(__tmp5.value, __tmp5.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau,
        __tmp1.name() : __tmp1,
        __tmp2.name() : __tmp2,
        __tmp3.name() : __tmp3,
        __tmp4.name() : __tmp4,
        __tmp5.name() : __tmp5
    })
_module_typeBindings.cfSmartType = cfSmartType
Namespace.addCategoryObject('typeBinding', 'cfSmartType', cfSmartType)


# Complex type cfPWagType with content type EMPTY
class cfPWagType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfPWagType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfPWagType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 210, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfPWagType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 211, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 211, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfPWagType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 212, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 212, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfPWagType_sigma', _module_typeBindings.STD_ANON_20)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 213, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 213, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfPWagType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 221, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 221, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute tauLast uses Python identifier tauLast
    __tauLast = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tauLast'), 'tauLast', '__AbsentNamespace0_cfPWagType_tauLast', pyxb.binding.datatypes.float)
    __tauLast._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 222, 8)
    __tauLast._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 222, 8)
    
    tauLast = property(__tauLast.value, __tauLast.set, None, None)

    
    # Attribute apProb uses Python identifier apProb
    __apProb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'apProb'), 'apProb', '__AbsentNamespace0_cfPWagType_apProb', pyxb.binding.datatypes.float)
    __apProb._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 223, 8)
    __apProb._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 223, 8)
    
    apProb = property(__apProb.value, __apProb.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau,
        __tauLast.name() : __tauLast,
        __apProb.name() : __apProb
    })
_module_typeBindings.cfPWagType = cfPWagType
Namespace.addCategoryObject('typeBinding', 'cfPWagType', cfPWagType)


# Complex type cfBKernerType with content type EMPTY
class cfBKernerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfBKernerType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfBKernerType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 226, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfBKernerType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 227, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 227, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfBKernerType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 228, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 228, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfBKernerType_sigma', _module_typeBindings.STD_ANON_21)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 229, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 229, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfBKernerType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 237, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 237, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute k uses Python identifier k
    __k = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k'), 'k', '__AbsentNamespace0_cfBKernerType_k', pyxb.binding.datatypes.float)
    __k._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 238, 8)
    __k._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 238, 8)
    
    k = property(__k.value, __k.set, None, None)

    
    # Attribute phi uses Python identifier phi
    __phi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phi'), 'phi', '__AbsentNamespace0_cfBKernerType_phi', pyxb.binding.datatypes.float)
    __phi._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 239, 8)
    __phi._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 239, 8)
    
    phi = property(__phi.value, __phi.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau,
        __k.name() : __k,
        __phi.name() : __phi
    })
_module_typeBindings.cfBKernerType = cfBKernerType
Namespace.addCategoryObject('typeBinding', 'cfBKernerType', cfBKernerType)


# Complex type cfWiedemannType with content type EMPTY
class cfWiedemannType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type cfWiedemannType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'cfWiedemannType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 242, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_cfWiedemannType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 243, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 243, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_cfWiedemannType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 244, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 244, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_cfWiedemannType_sigma', _module_typeBindings.STD_ANON_22)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 245, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 245, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_cfWiedemannType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 253, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 253, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute security uses Python identifier security
    __security = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'security'), 'security', '__AbsentNamespace0_cfWiedemannType_security', pyxb.binding.datatypes.float)
    __security._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 254, 8)
    __security._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 254, 8)
    
    security = property(__security.value, __security.set, None, None)

    
    # Attribute estimation uses Python identifier estimation
    __estimation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'estimation'), 'estimation', '__AbsentNamespace0_cfWiedemannType_estimation', pyxb.binding.datatypes.float)
    __estimation._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 255, 8)
    __estimation._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 255, 8)
    
    estimation = property(__estimation.value, __estimation.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __accel.name() : __accel,
        __decel.name() : __decel,
        __sigma.name() : __sigma,
        __tau.name() : __tau,
        __security.name() : __security,
        __estimation.name() : __estimation
    })
_module_typeBindings.cfWiedemannType = cfWiedemannType
Namespace.addCategoryObject('typeBinding', 'cfWiedemannType', cfWiedemannType)


# Complex type stopType with content type EMPTY
class stopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type stopType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stopType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 512, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lane uses Python identifier lane
    __lane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lane'), 'lane', '__AbsentNamespace0_stopType_lane', pyxb.binding.datatypes.string)
    __lane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 513, 8)
    __lane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 513, 8)
    
    lane = property(__lane.value, __lane.set, None, None)

    
    # Attribute busStop uses Python identifier busStop
    __busStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'busStop'), 'busStop', '__AbsentNamespace0_stopType_busStop', pyxb.binding.datatypes.string)
    __busStop._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 514, 8)
    __busStop._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 514, 8)
    
    busStop = property(__busStop.value, __busStop.set, None, None)

    
    # Attribute containerStop uses Python identifier containerStop
    __containerStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'containerStop'), 'containerStop', '__AbsentNamespace0_stopType_containerStop', pyxb.binding.datatypes.string)
    __containerStop._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 515, 8)
    __containerStop._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 515, 8)
    
    containerStop = property(__containerStop.value, __containerStop.set, None, None)

    
    # Attribute chargingStation uses Python identifier chargingStation
    __chargingStation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'chargingStation'), 'chargingStation', '__AbsentNamespace0_stopType_chargingStation', pyxb.binding.datatypes.string)
    __chargingStation._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 516, 8)
    __chargingStation._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 516, 8)
    
    chargingStation = property(__chargingStation.value, __chargingStation.set, None, None)

    
    # Attribute parkingArea uses Python identifier parkingArea
    __parkingArea = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parkingArea'), 'parkingArea', '__AbsentNamespace0_stopType_parkingArea', pyxb.binding.datatypes.string)
    __parkingArea._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 517, 8)
    __parkingArea._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 517, 8)
    
    parkingArea = property(__parkingArea.value, __parkingArea.set, None, None)

    
    # Attribute startPos uses Python identifier startPos
    __startPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'startPos'), 'startPos', '__AbsentNamespace0_stopType_startPos', pyxb.binding.datatypes.float)
    __startPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 518, 8)
    __startPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 518, 8)
    
    startPos = property(__startPos.value, __startPos.set, None, None)

    
    # Attribute endPos uses Python identifier endPos
    __endPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endPos'), 'endPos', '__AbsentNamespace0_stopType_endPos', pyxb.binding.datatypes.float)
    __endPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 519, 8)
    __endPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 519, 8)
    
    endPos = property(__endPos.value, __endPos.set, None, None)

    
    # Attribute friendlyPos uses Python identifier friendlyPos
    __friendlyPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'friendlyPos'), 'friendlyPos', '__AbsentNamespace0_stopType_friendlyPos', _module_typeBindings.boolType)
    __friendlyPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 520, 8)
    __friendlyPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 520, 8)
    
    friendlyPos = property(__friendlyPos.value, __friendlyPos.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__AbsentNamespace0_stopType_duration', _module_typeBindings.nonNegativeFloatType)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 521, 8)
    __duration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 521, 8)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute until uses Python identifier until
    __until = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'until'), 'until', '__AbsentNamespace0_stopType_until', _module_typeBindings.nonNegativeFloatType)
    __until._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 522, 8)
    __until._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 522, 8)
    
    until = property(__until.value, __until.set, None, None)

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_stopType_index', pyxb.binding.datatypes.string)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 523, 8)
    __index._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 523, 8)
    
    index = property(__index.value, __index.set, None, None)

    
    # Attribute parking uses Python identifier parking
    __parking = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'parking'), 'parking', '__AbsentNamespace0_stopType_parking', _module_typeBindings.boolType)
    __parking._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 524, 8)
    __parking._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 524, 8)
    
    parking = property(__parking.value, __parking.set, None, None)

    
    # Attribute triggered uses Python identifier triggered
    __triggered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'triggered'), 'triggered', '__AbsentNamespace0_stopType_triggered', _module_typeBindings.boolType)
    __triggered._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 525, 8)
    __triggered._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 525, 8)
    
    triggered = property(__triggered.value, __triggered.set, None, None)

    
    # Attribute containerTriggered uses Python identifier containerTriggered
    __containerTriggered = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'containerTriggered'), 'containerTriggered', '__AbsentNamespace0_stopType_containerTriggered', _module_typeBindings.boolType)
    __containerTriggered._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 526, 8)
    __containerTriggered._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 526, 8)
    
    containerTriggered = property(__containerTriggered.value, __containerTriggered.set, None, None)

    
    # Attribute expected uses Python identifier expected
    __expected = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'expected'), 'expected', '__AbsentNamespace0_stopType_expected', pyxb.binding.datatypes.string)
    __expected._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 527, 8)
    __expected._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 527, 8)
    
    expected = property(__expected.value, __expected.set, None, None)

    
    # Attribute actType uses Python identifier actType
    __actType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'actType'), 'actType', '__AbsentNamespace0_stopType_actType', pyxb.binding.datatypes.string)
    __actType._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 528, 8)
    __actType._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 528, 8)
    
    actType = property(__actType.value, __actType.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lane.name() : __lane,
        __busStop.name() : __busStop,
        __containerStop.name() : __containerStop,
        __chargingStation.name() : __chargingStation,
        __parkingArea.name() : __parkingArea,
        __startPos.name() : __startPos,
        __endPos.name() : __endPos,
        __friendlyPos.name() : __friendlyPos,
        __duration.name() : __duration,
        __until.name() : __until,
        __index.name() : __index,
        __parking.name() : __parking,
        __triggered.name() : __triggered,
        __containerTriggered.name() : __containerTriggered,
        __expected.name() : __expected,
        __actType.name() : __actType
    })
_module_typeBindings.stopType = stopType
Namespace.addCategoryObject('typeBinding', 'stopType', stopType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 619, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_CTD_ANON_3_edges', pyxb.binding.datatypes.string)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 620, 20)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 620, 20)
    
    edges = property(__edges.value, __edges.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_CTD_ANON_3_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 621, 20)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 621, 20)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_CTD_ANON_3_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 622, 20)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 622, 20)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_CTD_ANON_3_speed', _module_typeBindings.positiveFloatType)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 623, 20)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 623, 20)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__AbsentNamespace0_CTD_ANON_3_duration', _module_typeBindings.positiveFloatType)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 624, 20)
    __duration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 624, 20)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_CTD_ANON_3_departPos', pyxb.binding.datatypes.float)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 625, 20)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 625, 20)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_CTD_ANON_3_arrivalPos', pyxb.binding.datatypes.float)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 626, 20)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 626, 20)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __edges.name() : __edges,
        __from.name() : __from,
        __to.name() : __to,
        __speed.name() : __speed,
        __duration.name() : __duration,
        __departPos.name() : __departPos,
        __arrivalPos.name() : __arrivalPos
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type vTypeType with content type ELEMENT_ONLY
class vTypeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vTypeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vTypeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 6, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_vTypeType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 8, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Element carFollowing-IDM uses Python identifier carFollowing_IDM
    __carFollowing_IDM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-IDM'), 'carFollowing_IDM', '__AbsentNamespace0_vTypeType_carFollowing_IDM', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 11, 20), )

    
    carFollowing_IDM = property(__carFollowing_IDM.value, __carFollowing_IDM.set, None, None)

    
    # Element carFollowing-IDMM uses Python identifier carFollowing_IDMM
    __carFollowing_IDMM = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-IDMM'), 'carFollowing_IDMM', '__AbsentNamespace0_vTypeType_carFollowing_IDMM', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 12, 20), )

    
    carFollowing_IDMM = property(__carFollowing_IDMM.value, __carFollowing_IDMM.set, None, None)

    
    # Element carFollowing-Krauss uses Python identifier carFollowing_Krauss
    __carFollowing_Krauss = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-Krauss'), 'carFollowing_Krauss', '__AbsentNamespace0_vTypeType_carFollowing_Krauss', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 13, 20), )

    
    carFollowing_Krauss = property(__carFollowing_Krauss.value, __carFollowing_Krauss.set, None, None)

    
    # Element carFollowing-KraussPS uses Python identifier carFollowing_KraussPS
    __carFollowing_KraussPS = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-KraussPS'), 'carFollowing_KraussPS', '__AbsentNamespace0_vTypeType_carFollowing_KraussPS', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 14, 20), )

    
    carFollowing_KraussPS = property(__carFollowing_KraussPS.value, __carFollowing_KraussPS.set, None, None)

    
    # Element carFollowing-KraussOrig1 uses Python identifier carFollowing_KraussOrig1
    __carFollowing_KraussOrig1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-KraussOrig1'), 'carFollowing_KraussOrig1', '__AbsentNamespace0_vTypeType_carFollowing_KraussOrig1', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 15, 20), )

    
    carFollowing_KraussOrig1 = property(__carFollowing_KraussOrig1.value, __carFollowing_KraussOrig1.set, None, None)

    
    # Element carFollowing-SmartSK uses Python identifier carFollowing_SmartSK
    __carFollowing_SmartSK = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-SmartSK'), 'carFollowing_SmartSK', '__AbsentNamespace0_vTypeType_carFollowing_SmartSK', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 16, 20), )

    
    carFollowing_SmartSK = property(__carFollowing_SmartSK.value, __carFollowing_SmartSK.set, None, None)

    
    # Element carFollowing-Daniel1 uses Python identifier carFollowing_Daniel1
    __carFollowing_Daniel1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-Daniel1'), 'carFollowing_Daniel1', '__AbsentNamespace0_vTypeType_carFollowing_Daniel1', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 17, 20), )

    
    carFollowing_Daniel1 = property(__carFollowing_Daniel1.value, __carFollowing_Daniel1.set, None, None)

    
    # Element carFollowing-PWagner2009 uses Python identifier carFollowing_PWagner2009
    __carFollowing_PWagner2009 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-PWagner2009'), 'carFollowing_PWagner2009', '__AbsentNamespace0_vTypeType_carFollowing_PWagner2009', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 18, 20), )

    
    carFollowing_PWagner2009 = property(__carFollowing_PWagner2009.value, __carFollowing_PWagner2009.set, None, None)

    
    # Element carFollowing-BKerner uses Python identifier carFollowing_BKerner
    __carFollowing_BKerner = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-BKerner'), 'carFollowing_BKerner', '__AbsentNamespace0_vTypeType_carFollowing_BKerner', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 19, 20), )

    
    carFollowing_BKerner = property(__carFollowing_BKerner.value, __carFollowing_BKerner.set, None, None)

    
    # Element carFollowing-Wiedemann uses Python identifier carFollowing_Wiedemann
    __carFollowing_Wiedemann = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carFollowing-Wiedemann'), 'carFollowing_Wiedemann', '__AbsentNamespace0_vTypeType_carFollowing_Wiedemann', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 20, 20), )

    
    carFollowing_Wiedemann = property(__carFollowing_Wiedemann.value, __carFollowing_Wiedemann.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_vTypeType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 25, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 25, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_vTypeType_length', _module_typeBindings.positiveFloatType)
    __length._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 26, 8)
    __length._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 26, 8)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute minGap uses Python identifier minGap
    __minGap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minGap'), 'minGap', '__AbsentNamespace0_vTypeType_minGap', _module_typeBindings.nonNegativeFloatType)
    __minGap._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 27, 8)
    __minGap._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 27, 8)
    
    minGap = property(__minGap.value, __minGap.set, None, None)

    
    # Attribute maxSpeed uses Python identifier maxSpeed
    __maxSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxSpeed'), 'maxSpeed', '__AbsentNamespace0_vTypeType_maxSpeed', _module_typeBindings.positiveFloatType)
    __maxSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 28, 8)
    __maxSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 28, 8)
    
    maxSpeed = property(__maxSpeed.value, __maxSpeed.set, None, None)

    
    # Attribute probability uses Python identifier probability
    __probability = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability'), 'probability', '__AbsentNamespace0_vTypeType_probability', _module_typeBindings.nonNegativeFloatType)
    __probability._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 29, 8)
    __probability._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 29, 8)
    
    probability = property(__probability.value, __probability.set, None, None)

    
    # Attribute speedFactor uses Python identifier speedFactor
    __speedFactor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speedFactor'), 'speedFactor', '__AbsentNamespace0_vTypeType_speedFactor', _module_typeBindings.nonNegativeDistributionType)
    __speedFactor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 30, 8)
    __speedFactor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 30, 8)
    
    speedFactor = property(__speedFactor.value, __speedFactor.set, None, None)

    
    # Attribute speedDev uses Python identifier speedDev
    __speedDev = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speedDev'), 'speedDev', '__AbsentNamespace0_vTypeType_speedDev', _module_typeBindings.nonNegativeFloatType)
    __speedDev._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 31, 8)
    __speedDev._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 31, 8)
    
    speedDev = property(__speedDev.value, __speedDev.set, None, None)

    
    # Attribute vClass uses Python identifier vClass
    __vClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vClass'), 'vClass', '__AbsentNamespace0_vTypeType_vClass', pyxb.binding.datatypes.string)
    __vClass._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 32, 8)
    __vClass._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 32, 8)
    
    vClass = property(__vClass.value, __vClass.set, None, None)

    
    # Attribute emissionClass uses Python identifier emissionClass
    __emissionClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'emissionClass'), 'emissionClass', '__AbsentNamespace0_vTypeType_emissionClass', pyxb.binding.datatypes.string)
    __emissionClass._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 33, 8)
    __emissionClass._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 33, 8)
    
    emissionClass = property(__emissionClass.value, __emissionClass.set, None, None)

    
    # Attribute guiShape uses Python identifier guiShape
    __guiShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'guiShape'), 'guiShape', '__AbsentNamespace0_vTypeType_guiShape', pyxb.binding.datatypes.string)
    __guiShape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 34, 8)
    __guiShape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 34, 8)
    
    guiShape = property(__guiShape.value, __guiShape.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_vTypeType_width', _module_typeBindings.positiveFloatType)
    __width._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 35, 8)
    __width._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 35, 8)
    
    width = property(__width.value, __width.set, None, None)

    
    # Attribute height uses Python identifier height
    __height = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'height'), 'height', '__AbsentNamespace0_vTypeType_height', _module_typeBindings.positiveFloatType)
    __height._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 36, 8)
    __height._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 36, 8)
    
    height = property(__height.value, __height.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_vTypeType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 37, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 37, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute accel uses Python identifier accel
    __accel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accel'), 'accel', '__AbsentNamespace0_vTypeType_accel', _module_typeBindings.positiveFloatType)
    __accel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 38, 8)
    __accel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 38, 8)
    
    accel = property(__accel.value, __accel.set, None, None)

    
    # Attribute decel uses Python identifier decel
    __decel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'decel'), 'decel', '__AbsentNamespace0_vTypeType_decel', _module_typeBindings.positiveFloatType)
    __decel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 39, 8)
    __decel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 39, 8)
    
    decel = property(__decel.value, __decel.set, None, None)

    
    # Attribute emergencyDecel uses Python identifier emergencyDecel
    __emergencyDecel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'emergencyDecel'), 'emergencyDecel', '__AbsentNamespace0_vTypeType_emergencyDecel', _module_typeBindings.positiveFloatType)
    __emergencyDecel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 40, 8)
    __emergencyDecel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 40, 8)
    
    emergencyDecel = property(__emergencyDecel.value, __emergencyDecel.set, None, None)

    
    # Attribute apparentDecel uses Python identifier apparentDecel
    __apparentDecel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'apparentDecel'), 'apparentDecel', '__AbsentNamespace0_vTypeType_apparentDecel', _module_typeBindings.positiveFloatType)
    __apparentDecel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 41, 8)
    __apparentDecel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 41, 8)
    
    apparentDecel = property(__apparentDecel.value, __apparentDecel.set, None, None)

    
    # Attribute personCapacity uses Python identifier personCapacity
    __personCapacity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'personCapacity'), 'personCapacity', '__AbsentNamespace0_vTypeType_personCapacity', pyxb.binding.datatypes.nonNegativeInteger)
    __personCapacity._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 42, 8)
    __personCapacity._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 42, 8)
    
    personCapacity = property(__personCapacity.value, __personCapacity.set, None, None)

    
    # Attribute containerCapacity uses Python identifier containerCapacity
    __containerCapacity = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'containerCapacity'), 'containerCapacity', '__AbsentNamespace0_vTypeType_containerCapacity', pyxb.binding.datatypes.nonNegativeInteger)
    __containerCapacity._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 43, 8)
    __containerCapacity._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 43, 8)
    
    containerCapacity = property(__containerCapacity.value, __containerCapacity.set, None, None)

    
    # Attribute boardingDuration uses Python identifier boardingDuration
    __boardingDuration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'boardingDuration'), 'boardingDuration', '__AbsentNamespace0_vTypeType_boardingDuration', _module_typeBindings.nonNegativeFloatType)
    __boardingDuration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 44, 8)
    __boardingDuration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 44, 8)
    
    boardingDuration = property(__boardingDuration.value, __boardingDuration.set, None, None)

    
    # Attribute loadingDuration uses Python identifier loadingDuration
    __loadingDuration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'loadingDuration'), 'loadingDuration', '__AbsentNamespace0_vTypeType_loadingDuration', _module_typeBindings.nonNegativeFloatType)
    __loadingDuration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 45, 8)
    __loadingDuration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 45, 8)
    
    loadingDuration = property(__loadingDuration.value, __loadingDuration.set, None, None)

    
    # Attribute lcStrategic uses Python identifier lcStrategic
    __lcStrategic = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcStrategic'), 'lcStrategic', '__AbsentNamespace0_vTypeType_lcStrategic', pyxb.binding.datatypes.float)
    __lcStrategic._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 46, 8)
    __lcStrategic._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 46, 8)
    
    lcStrategic = property(__lcStrategic.value, __lcStrategic.set, None, None)

    
    # Attribute lcCooperative uses Python identifier lcCooperative
    __lcCooperative = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcCooperative'), 'lcCooperative', '__AbsentNamespace0_vTypeType_lcCooperative', pyxb.binding.datatypes.float)
    __lcCooperative._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 47, 8)
    __lcCooperative._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 47, 8)
    
    lcCooperative = property(__lcCooperative.value, __lcCooperative.set, None, None)

    
    # Attribute lcSpeedGain uses Python identifier lcSpeedGain
    __lcSpeedGain = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcSpeedGain'), 'lcSpeedGain', '__AbsentNamespace0_vTypeType_lcSpeedGain', pyxb.binding.datatypes.float)
    __lcSpeedGain._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 48, 8)
    __lcSpeedGain._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 48, 8)
    
    lcSpeedGain = property(__lcSpeedGain.value, __lcSpeedGain.set, None, None)

    
    # Attribute lcKeepRight uses Python identifier lcKeepRight
    __lcKeepRight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcKeepRight'), 'lcKeepRight', '__AbsentNamespace0_vTypeType_lcKeepRight', pyxb.binding.datatypes.float)
    __lcKeepRight._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 49, 8)
    __lcKeepRight._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 49, 8)
    
    lcKeepRight = property(__lcKeepRight.value, __lcKeepRight.set, None, None)

    
    # Attribute lcSublane uses Python identifier lcSublane
    __lcSublane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcSublane'), 'lcSublane', '__AbsentNamespace0_vTypeType_lcSublane', pyxb.binding.datatypes.float)
    __lcSublane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 50, 8)
    __lcSublane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 50, 8)
    
    lcSublane = property(__lcSublane.value, __lcSublane.set, None, None)

    
    # Attribute lcPushy uses Python identifier lcPushy
    __lcPushy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcPushy'), 'lcPushy', '__AbsentNamespace0_vTypeType_lcPushy', pyxb.binding.datatypes.float)
    __lcPushy._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 51, 8)
    __lcPushy._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 51, 8)
    
    lcPushy = property(__lcPushy.value, __lcPushy.set, None, None)

    
    # Attribute lcPushyGap uses Python identifier lcPushyGap
    __lcPushyGap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcPushyGap'), 'lcPushyGap', '__AbsentNamespace0_vTypeType_lcPushyGap', _module_typeBindings.nonNegativeFloatType)
    __lcPushyGap._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 52, 8)
    __lcPushyGap._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 52, 8)
    
    lcPushyGap = property(__lcPushyGap.value, __lcPushyGap.set, None, None)

    
    # Attribute lcAssertive uses Python identifier lcAssertive
    __lcAssertive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcAssertive'), 'lcAssertive', '__AbsentNamespace0_vTypeType_lcAssertive', _module_typeBindings.positiveFloatType)
    __lcAssertive._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 53, 8)
    __lcAssertive._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 53, 8)
    
    lcAssertive = property(__lcAssertive.value, __lcAssertive.set, None, None)

    
    # Attribute lcLookaheadLeft uses Python identifier lcLookaheadLeft
    __lcLookaheadLeft = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcLookaheadLeft'), 'lcLookaheadLeft', '__AbsentNamespace0_vTypeType_lcLookaheadLeft', _module_typeBindings.positiveFloatType)
    __lcLookaheadLeft._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 54, 8)
    __lcLookaheadLeft._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 54, 8)
    
    lcLookaheadLeft = property(__lcLookaheadLeft.value, __lcLookaheadLeft.set, None, None)

    
    # Attribute lcSpeedGainRight uses Python identifier lcSpeedGainRight
    __lcSpeedGainRight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lcSpeedGainRight'), 'lcSpeedGainRight', '__AbsentNamespace0_vTypeType_lcSpeedGainRight', _module_typeBindings.positiveFloatType)
    __lcSpeedGainRight._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 55, 8)
    __lcSpeedGainRight._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 55, 8)
    
    lcSpeedGainRight = property(__lcSpeedGainRight.value, __lcSpeedGainRight.set, None, None)

    
    # Attribute maxSpeedLat uses Python identifier maxSpeedLat
    __maxSpeedLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxSpeedLat'), 'maxSpeedLat', '__AbsentNamespace0_vTypeType_maxSpeedLat', _module_typeBindings.positiveFloatType)
    __maxSpeedLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 56, 8)
    __maxSpeedLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 56, 8)
    
    maxSpeedLat = property(__maxSpeedLat.value, __maxSpeedLat.set, None, None)

    
    # Attribute latAlignment uses Python identifier latAlignment
    __latAlignment = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'latAlignment'), 'latAlignment', '__AbsentNamespace0_vTypeType_latAlignment', _module_typeBindings.STD_ANON_11)
    __latAlignment._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 57, 8)
    __latAlignment._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 57, 8)
    
    latAlignment = property(__latAlignment.value, __latAlignment.set, None, None)

    
    # Attribute actionStepLength uses Python identifier actionStepLength
    __actionStepLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'actionStepLength'), 'actionStepLength', '__AbsentNamespace0_vTypeType_actionStepLength', _module_typeBindings.positiveFloatType)
    __actionStepLength._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 69, 8)
    __actionStepLength._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 69, 8)
    
    actionStepLength = property(__actionStepLength.value, __actionStepLength.set, None, None)

    
    # Attribute minGapLat uses Python identifier minGapLat
    __minGapLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minGapLat'), 'minGapLat', '__AbsentNamespace0_vTypeType_minGapLat', _module_typeBindings.positiveFloatType)
    __minGapLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 70, 8)
    __minGapLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 70, 8)
    
    minGapLat = property(__minGapLat.value, __minGapLat.set, None, None)

    
    # Attribute jmCrossingGap uses Python identifier jmCrossingGap
    __jmCrossingGap = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmCrossingGap'), 'jmCrossingGap', '__AbsentNamespace0_vTypeType_jmCrossingGap', _module_typeBindings.nonNegativeFloatType)
    __jmCrossingGap._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 71, 8)
    __jmCrossingGap._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 71, 8)
    
    jmCrossingGap = property(__jmCrossingGap.value, __jmCrossingGap.set, None, None)

    
    # Attribute jmDriveAfterRedTime uses Python identifier jmDriveAfterRedTime
    __jmDriveAfterRedTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmDriveAfterRedTime'), 'jmDriveAfterRedTime', '__AbsentNamespace0_vTypeType_jmDriveAfterRedTime', _module_typeBindings.nonNegativeFloatTypeWithErrorValue)
    __jmDriveAfterRedTime._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 72, 8)
    __jmDriveAfterRedTime._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 72, 8)
    
    jmDriveAfterRedTime = property(__jmDriveAfterRedTime.value, __jmDriveAfterRedTime.set, None, None)

    
    # Attribute jmDriveRedSpeed uses Python identifier jmDriveRedSpeed
    __jmDriveRedSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmDriveRedSpeed'), 'jmDriveRedSpeed', '__AbsentNamespace0_vTypeType_jmDriveRedSpeed', _module_typeBindings.nonNegativeFloatType)
    __jmDriveRedSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 73, 8)
    __jmDriveRedSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 73, 8)
    
    jmDriveRedSpeed = property(__jmDriveRedSpeed.value, __jmDriveRedSpeed.set, None, None)

    
    # Attribute jmIgnoreKeepClearTime uses Python identifier jmIgnoreKeepClearTime
    __jmIgnoreKeepClearTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmIgnoreKeepClearTime'), 'jmIgnoreKeepClearTime', '__AbsentNamespace0_vTypeType_jmIgnoreKeepClearTime', _module_typeBindings.nonNegativeFloatTypeWithErrorValue)
    __jmIgnoreKeepClearTime._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 74, 8)
    __jmIgnoreKeepClearTime._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 74, 8)
    
    jmIgnoreKeepClearTime = property(__jmIgnoreKeepClearTime.value, __jmIgnoreKeepClearTime.set, None, None)

    
    # Attribute jmIgnoreFoeSpeed uses Python identifier jmIgnoreFoeSpeed
    __jmIgnoreFoeSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmIgnoreFoeSpeed'), 'jmIgnoreFoeSpeed', '__AbsentNamespace0_vTypeType_jmIgnoreFoeSpeed', _module_typeBindings.nonNegativeFloatType)
    __jmIgnoreFoeSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 75, 8)
    __jmIgnoreFoeSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 75, 8)
    
    jmIgnoreFoeSpeed = property(__jmIgnoreFoeSpeed.value, __jmIgnoreFoeSpeed.set, None, None)

    
    # Attribute jmIgnoreFoeProb uses Python identifier jmIgnoreFoeProb
    __jmIgnoreFoeProb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmIgnoreFoeProb'), 'jmIgnoreFoeProb', '__AbsentNamespace0_vTypeType_jmIgnoreFoeProb', _module_typeBindings.nonNegativeFloatType)
    __jmIgnoreFoeProb._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 76, 8)
    __jmIgnoreFoeProb._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 76, 8)
    
    jmIgnoreFoeProb = property(__jmIgnoreFoeProb.value, __jmIgnoreFoeProb.set, None, None)

    
    # Attribute jmSigmaMinor uses Python identifier jmSigmaMinor
    __jmSigmaMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmSigmaMinor'), 'jmSigmaMinor', '__AbsentNamespace0_vTypeType_jmSigmaMinor', _module_typeBindings.nonNegativeFloatType)
    __jmSigmaMinor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 77, 8)
    __jmSigmaMinor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 77, 8)
    
    jmSigmaMinor = property(__jmSigmaMinor.value, __jmSigmaMinor.set, None, None)

    
    # Attribute jmTimegapMinor uses Python identifier jmTimegapMinor
    __jmTimegapMinor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'jmTimegapMinor'), 'jmTimegapMinor', '__AbsentNamespace0_vTypeType_jmTimegapMinor', _module_typeBindings.nonNegativeFloatType)
    __jmTimegapMinor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 78, 8)
    __jmTimegapMinor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 78, 8)
    
    jmTimegapMinor = property(__jmTimegapMinor.value, __jmTimegapMinor.set, None, None)

    
    # Attribute sigma uses Python identifier sigma
    __sigma = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'sigma'), 'sigma', '__AbsentNamespace0_vTypeType_sigma', _module_typeBindings.STD_ANON_12)
    __sigma._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 79, 8)
    __sigma._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 79, 8)
    
    sigma = property(__sigma.value, __sigma.set, None, None)

    
    # Attribute impatience uses Python identifier impatience
    __impatience = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'impatience'), 'impatience', '__AbsentNamespace0_vTypeType_impatience', _module_typeBindings.STD_ANON_32)
    __impatience._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 87, 8)
    __impatience._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 87, 8)
    
    impatience = property(__impatience.value, __impatience.set, None, None)

    
    # Attribute tau uses Python identifier tau
    __tau = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tau'), 'tau', '__AbsentNamespace0_vTypeType_tau', _module_typeBindings.positiveFloatType)
    __tau._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 98, 8)
    __tau._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 98, 8)
    
    tau = property(__tau.value, __tau.set, None, None)

    
    # Attribute delta uses Python identifier delta
    __delta = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'delta'), 'delta', '__AbsentNamespace0_vTypeType_delta', pyxb.binding.datatypes.float)
    __delta._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 99, 8)
    __delta._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 99, 8)
    
    delta = property(__delta.value, __delta.set, None, None)

    
    # Attribute stepping uses Python identifier stepping
    __stepping = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'stepping'), 'stepping', '__AbsentNamespace0_vTypeType_stepping', _module_typeBindings.positiveIntType)
    __stepping._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 100, 8)
    __stepping._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 100, 8)
    
    stepping = property(__stepping.value, __stepping.set, None, None)

    
    # Attribute adaptTime uses Python identifier adaptTime
    __adaptTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adaptTime'), 'adaptTime', '__AbsentNamespace0_vTypeType_adaptTime', pyxb.binding.datatypes.float)
    __adaptTime._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 101, 8)
    __adaptTime._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 101, 8)
    
    adaptTime = property(__adaptTime.value, __adaptTime.set, None, None)

    
    # Attribute adaptFactor uses Python identifier adaptFactor
    __adaptFactor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'adaptFactor'), 'adaptFactor', '__AbsentNamespace0_vTypeType_adaptFactor', pyxb.binding.datatypes.float)
    __adaptFactor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 102, 8)
    __adaptFactor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 102, 8)
    
    adaptFactor = property(__adaptFactor.value, __adaptFactor.set, None, None)

    
    # Attribute tmp1 uses Python identifier tmp1
    __tmp1 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp1'), 'tmp1', '__AbsentNamespace0_vTypeType_tmp1', pyxb.binding.datatypes.float)
    __tmp1._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 103, 8)
    __tmp1._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 103, 8)
    
    tmp1 = property(__tmp1.value, __tmp1.set, None, None)

    
    # Attribute tmp2 uses Python identifier tmp2
    __tmp2 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp2'), 'tmp2', '__AbsentNamespace0_vTypeType_tmp2', pyxb.binding.datatypes.float)
    __tmp2._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 104, 8)
    __tmp2._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 104, 8)
    
    tmp2 = property(__tmp2.value, __tmp2.set, None, None)

    
    # Attribute tmp3 uses Python identifier tmp3
    __tmp3 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp3'), 'tmp3', '__AbsentNamespace0_vTypeType_tmp3', pyxb.binding.datatypes.float)
    __tmp3._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 105, 8)
    __tmp3._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 105, 8)
    
    tmp3 = property(__tmp3.value, __tmp3.set, None, None)

    
    # Attribute tmp4 uses Python identifier tmp4
    __tmp4 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp4'), 'tmp4', '__AbsentNamespace0_vTypeType_tmp4', pyxb.binding.datatypes.float)
    __tmp4._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 106, 8)
    __tmp4._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 106, 8)
    
    tmp4 = property(__tmp4.value, __tmp4.set, None, None)

    
    # Attribute tmp5 uses Python identifier tmp5
    __tmp5 = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tmp5'), 'tmp5', '__AbsentNamespace0_vTypeType_tmp5', pyxb.binding.datatypes.float)
    __tmp5._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 107, 8)
    __tmp5._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 107, 8)
    
    tmp5 = property(__tmp5.value, __tmp5.set, None, None)

    
    # Attribute tauLast uses Python identifier tauLast
    __tauLast = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tauLast'), 'tauLast', '__AbsentNamespace0_vTypeType_tauLast', pyxb.binding.datatypes.float)
    __tauLast._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 108, 8)
    __tauLast._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 108, 8)
    
    tauLast = property(__tauLast.value, __tauLast.set, None, None)

    
    # Attribute apProb uses Python identifier apProb
    __apProb = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'apProb'), 'apProb', '__AbsentNamespace0_vTypeType_apProb', pyxb.binding.datatypes.float)
    __apProb._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 109, 8)
    __apProb._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 109, 8)
    
    apProb = property(__apProb.value, __apProb.set, None, None)

    
    # Attribute k uses Python identifier k
    __k = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'k'), 'k', '__AbsentNamespace0_vTypeType_k', pyxb.binding.datatypes.float)
    __k._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 110, 8)
    __k._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 110, 8)
    
    k = property(__k.value, __k.set, None, None)

    
    # Attribute phi uses Python identifier phi
    __phi = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phi'), 'phi', '__AbsentNamespace0_vTypeType_phi', pyxb.binding.datatypes.float)
    __phi._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 111, 8)
    __phi._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 111, 8)
    
    phi = property(__phi.value, __phi.set, None, None)

    
    # Attribute security uses Python identifier security
    __security = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'security'), 'security', '__AbsentNamespace0_vTypeType_security', pyxb.binding.datatypes.float)
    __security._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 112, 8)
    __security._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 112, 8)
    
    security = property(__security.value, __security.set, None, None)

    
    # Attribute estimation uses Python identifier estimation
    __estimation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'estimation'), 'estimation', '__AbsentNamespace0_vTypeType_estimation', pyxb.binding.datatypes.float)
    __estimation._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 113, 8)
    __estimation._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 113, 8)
    
    estimation = property(__estimation.value, __estimation.set, None, None)

    
    # Attribute carFollowModel uses Python identifier carFollowModel
    __carFollowModel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'carFollowModel'), 'carFollowModel', '__AbsentNamespace0_vTypeType_carFollowModel', pyxb.binding.datatypes.string)
    __carFollowModel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 114, 8)
    __carFollowModel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 114, 8)
    
    carFollowModel = property(__carFollowModel.value, __carFollowModel.set, None, None)

    
    # Attribute trainType uses Python identifier trainType
    __trainType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'trainType'), 'trainType', '__AbsentNamespace0_vTypeType_trainType', _module_typeBindings.STD_ANON_14)
    __trainType._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 115, 8)
    __trainType._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 115, 8)
    
    trainType = property(__trainType.value, __trainType.set, None, None)

    
    # Attribute laneChangeModel uses Python identifier laneChangeModel
    __laneChangeModel = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'laneChangeModel'), 'laneChangeModel', '__AbsentNamespace0_vTypeType_laneChangeModel', _module_typeBindings.STD_ANON_15)
    __laneChangeModel._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 130, 8)
    __laneChangeModel._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 130, 8)
    
    laneChangeModel = property(__laneChangeModel.value, __laneChangeModel.set, None, None)

    
    # Attribute imgFile uses Python identifier imgFile
    __imgFile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'imgFile'), 'imgFile', '__AbsentNamespace0_vTypeType_imgFile', pyxb.binding.datatypes.string)
    __imgFile._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 140, 8)
    __imgFile._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 140, 8)
    
    imgFile = property(__imgFile.value, __imgFile.set, None, None)

    
    # Attribute osgFile uses Python identifier osgFile
    __osgFile = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'osgFile'), 'osgFile', '__AbsentNamespace0_vTypeType_osgFile', pyxb.binding.datatypes.string)
    __osgFile._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 141, 8)
    __osgFile._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 141, 8)
    
    osgFile = property(__osgFile.value, __osgFile.set, None, None)

    _ElementMap.update({
        __param.name() : __param,
        __carFollowing_IDM.name() : __carFollowing_IDM,
        __carFollowing_IDMM.name() : __carFollowing_IDMM,
        __carFollowing_Krauss.name() : __carFollowing_Krauss,
        __carFollowing_KraussPS.name() : __carFollowing_KraussPS,
        __carFollowing_KraussOrig1.name() : __carFollowing_KraussOrig1,
        __carFollowing_SmartSK.name() : __carFollowing_SmartSK,
        __carFollowing_Daniel1.name() : __carFollowing_Daniel1,
        __carFollowing_PWagner2009.name() : __carFollowing_PWagner2009,
        __carFollowing_BKerner.name() : __carFollowing_BKerner,
        __carFollowing_Wiedemann.name() : __carFollowing_Wiedemann
    })
    _AttributeMap.update({
        __id.name() : __id,
        __length.name() : __length,
        __minGap.name() : __minGap,
        __maxSpeed.name() : __maxSpeed,
        __probability.name() : __probability,
        __speedFactor.name() : __speedFactor,
        __speedDev.name() : __speedDev,
        __vClass.name() : __vClass,
        __emissionClass.name() : __emissionClass,
        __guiShape.name() : __guiShape,
        __width.name() : __width,
        __height.name() : __height,
        __color.name() : __color,
        __accel.name() : __accel,
        __decel.name() : __decel,
        __emergencyDecel.name() : __emergencyDecel,
        __apparentDecel.name() : __apparentDecel,
        __personCapacity.name() : __personCapacity,
        __containerCapacity.name() : __containerCapacity,
        __boardingDuration.name() : __boardingDuration,
        __loadingDuration.name() : __loadingDuration,
        __lcStrategic.name() : __lcStrategic,
        __lcCooperative.name() : __lcCooperative,
        __lcSpeedGain.name() : __lcSpeedGain,
        __lcKeepRight.name() : __lcKeepRight,
        __lcSublane.name() : __lcSublane,
        __lcPushy.name() : __lcPushy,
        __lcPushyGap.name() : __lcPushyGap,
        __lcAssertive.name() : __lcAssertive,
        __lcLookaheadLeft.name() : __lcLookaheadLeft,
        __lcSpeedGainRight.name() : __lcSpeedGainRight,
        __maxSpeedLat.name() : __maxSpeedLat,
        __latAlignment.name() : __latAlignment,
        __actionStepLength.name() : __actionStepLength,
        __minGapLat.name() : __minGapLat,
        __jmCrossingGap.name() : __jmCrossingGap,
        __jmDriveAfterRedTime.name() : __jmDriveAfterRedTime,
        __jmDriveRedSpeed.name() : __jmDriveRedSpeed,
        __jmIgnoreKeepClearTime.name() : __jmIgnoreKeepClearTime,
        __jmIgnoreFoeSpeed.name() : __jmIgnoreFoeSpeed,
        __jmIgnoreFoeProb.name() : __jmIgnoreFoeProb,
        __jmSigmaMinor.name() : __jmSigmaMinor,
        __jmTimegapMinor.name() : __jmTimegapMinor,
        __sigma.name() : __sigma,
        __impatience.name() : __impatience,
        __tau.name() : __tau,
        __delta.name() : __delta,
        __stepping.name() : __stepping,
        __adaptTime.name() : __adaptTime,
        __adaptFactor.name() : __adaptFactor,
        __tmp1.name() : __tmp1,
        __tmp2.name() : __tmp2,
        __tmp3.name() : __tmp3,
        __tmp4.name() : __tmp4,
        __tmp5.name() : __tmp5,
        __tauLast.name() : __tauLast,
        __apProb.name() : __apProb,
        __k.name() : __k,
        __phi.name() : __phi,
        __security.name() : __security,
        __estimation.name() : __estimation,
        __carFollowModel.name() : __carFollowModel,
        __trainType.name() : __trainType,
        __laneChangeModel.name() : __laneChangeModel,
        __imgFile.name() : __imgFile,
        __osgFile.name() : __osgFile
    })
_module_typeBindings.vTypeType = vTypeType
Namespace.addCategoryObject('typeBinding', 'vTypeType', vTypeType)


# Complex type vehicleType with content type ELEMENT_ONLY
class vehicleType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vehicleType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vehicleType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_vehicleType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 260, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Element route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__AbsentNamespace0_vehicleType_route', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 263, 20), )

    
    route = property(__route.value, __route.set, None, None)

    
    # Element routeDistribution uses Python identifier routeDistribution
    __routeDistribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routeDistribution'), 'routeDistribution', '__AbsentNamespace0_vehicleType_routeDistribution', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 264, 20), )

    
    routeDistribution = property(__routeDistribution.value, __routeDistribution.set, None, None)

    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_vehicleType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 269, 16), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_vehicleType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 273, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 273, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute route uses Python identifier route_
    __route_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'route'), 'route_', '__AbsentNamespace0_vehicleType_route_', pyxb.binding.datatypes.string)
    __route_._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 274, 8)
    __route_._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 274, 8)
    
    route_ = property(__route_.value, __route_.set, None, None)

    
    # Attribute reroute uses Python identifier reroute
    __reroute = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'reroute'), 'reroute', '__AbsentNamespace0_vehicleType_reroute', _module_typeBindings.boolType)
    __reroute._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 275, 8)
    __reroute._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 275, 8)
    
    reroute = property(__reroute.value, __reroute.set, None, None)

    
    # Attribute fromTaz uses Python identifier fromTaz
    __fromTaz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fromTaz'), 'fromTaz', '__AbsentNamespace0_vehicleType_fromTaz', pyxb.binding.datatypes.string)
    __fromTaz._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 276, 8)
    __fromTaz._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 276, 8)
    
    fromTaz = property(__fromTaz.value, __fromTaz.set, None, None)

    
    # Attribute toTaz uses Python identifier toTaz
    __toTaz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toTaz'), 'toTaz', '__AbsentNamespace0_vehicleType_toTaz', pyxb.binding.datatypes.string)
    __toTaz._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 277, 8)
    __toTaz._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 277, 8)
    
    toTaz = property(__toTaz.value, __toTaz.set, None, None)

    
    # Attribute via uses Python identifier via
    __via = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'via'), 'via', '__AbsentNamespace0_vehicleType_via', pyxb.binding.datatypes.string)
    __via._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 278, 8)
    __via._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 278, 8)
    
    via = property(__via.value, __via.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_vehicleType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 279, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 279, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute depart uses Python identifier depart
    __depart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'depart'), 'depart', '__AbsentNamespace0_vehicleType_depart', _module_typeBindings.departType, required=True)
    __depart._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 280, 8)
    __depart._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 280, 8)
    
    depart = property(__depart.value, __depart.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_vehicleType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 281, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 281, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute departLane uses Python identifier departLane
    __departLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departLane'), 'departLane', '__AbsentNamespace0_vehicleType_departLane', _module_typeBindings.departLaneType)
    __departLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 282, 8)
    __departLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 282, 8)
    
    departLane = property(__departLane.value, __departLane.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_vehicleType_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 283, 8)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 283, 8)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute departSpeed uses Python identifier departSpeed
    __departSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departSpeed'), 'departSpeed', '__AbsentNamespace0_vehicleType_departSpeed', _module_typeBindings.departSpeedType)
    __departSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 284, 8)
    __departSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 284, 8)
    
    departSpeed = property(__departSpeed.value, __departSpeed.set, None, None)

    
    # Attribute arrivalLane uses Python identifier arrivalLane
    __arrivalLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalLane'), 'arrivalLane', '__AbsentNamespace0_vehicleType_arrivalLane', _module_typeBindings.arrivalLaneType)
    __arrivalLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 285, 8)
    __arrivalLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 285, 8)
    
    arrivalLane = property(__arrivalLane.value, __arrivalLane.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_vehicleType_arrivalPos', _module_typeBindings.arrivalPosType)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 286, 8)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 286, 8)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute arrivalSpeed uses Python identifier arrivalSpeed
    __arrivalSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalSpeed'), 'arrivalSpeed', '__AbsentNamespace0_vehicleType_arrivalSpeed', _module_typeBindings.arrivalSpeedType)
    __arrivalSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 287, 8)
    __arrivalSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 287, 8)
    
    arrivalSpeed = property(__arrivalSpeed.value, __arrivalSpeed.set, None, None)

    
    # Attribute departPosLat uses Python identifier departPosLat
    __departPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPosLat'), 'departPosLat', '__AbsentNamespace0_vehicleType_departPosLat', _module_typeBindings.departPosLatType)
    __departPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 288, 8)
    __departPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 288, 8)
    
    departPosLat = property(__departPosLat.value, __departPosLat.set, None, None)

    
    # Attribute arrivalPosLat uses Python identifier arrivalPosLat
    __arrivalPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPosLat'), 'arrivalPosLat', '__AbsentNamespace0_vehicleType_arrivalPosLat', _module_typeBindings.arrivalPosLatType)
    __arrivalPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 289, 8)
    __arrivalPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 289, 8)
    
    arrivalPosLat = property(__arrivalPosLat.value, __arrivalPosLat.set, None, None)

    
    # Attribute arrival uses Python identifier arrival
    __arrival = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrival'), 'arrival', '__AbsentNamespace0_vehicleType_arrival', _module_typeBindings.nonNegativeFloatType)
    __arrival._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 290, 8)
    __arrival._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 290, 8)
    
    arrival = property(__arrival.value, __arrival.set, None, None)

    
    # Attribute routeLength uses Python identifier routeLength
    __routeLength = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'routeLength'), 'routeLength', '__AbsentNamespace0_vehicleType_routeLength', _module_typeBindings.nonNegativeFloatType)
    __routeLength._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 291, 8)
    __routeLength._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 291, 8)
    
    routeLength = property(__routeLength.value, __routeLength.set, None, None)

    
    # Attribute line uses Python identifier line
    __line = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'line'), 'line', '__AbsentNamespace0_vehicleType_line', pyxb.binding.datatypes.string)
    __line._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 292, 8)
    __line._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 292, 8)
    
    line = property(__line.value, __line.set, None, None)

    
    # Attribute personNumber uses Python identifier personNumber
    __personNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'personNumber'), 'personNumber', '__AbsentNamespace0_vehicleType_personNumber', pyxb.binding.datatypes.nonNegativeInteger)
    __personNumber._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 293, 8)
    __personNumber._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 293, 8)
    
    personNumber = property(__personNumber.value, __personNumber.set, None, None)

    _ElementMap.update({
        __param.name() : __param,
        __route.name() : __route,
        __routeDistribution.name() : __routeDistribution,
        __stop.name() : __stop
    })
    _AttributeMap.update({
        __id.name() : __id,
        __route_.name() : __route_,
        __reroute.name() : __reroute,
        __fromTaz.name() : __fromTaz,
        __toTaz.name() : __toTaz,
        __via.name() : __via,
        __type.name() : __type,
        __depart.name() : __depart,
        __color.name() : __color,
        __departLane.name() : __departLane,
        __departPos.name() : __departPos,
        __departSpeed.name() : __departSpeed,
        __arrivalLane.name() : __arrivalLane,
        __arrivalPos.name() : __arrivalPos,
        __arrivalSpeed.name() : __arrivalSpeed,
        __departPosLat.name() : __departPosLat,
        __arrivalPosLat.name() : __arrivalPosLat,
        __arrival.name() : __arrival,
        __routeLength.name() : __routeLength,
        __line.name() : __line,
        __personNumber.name() : __personNumber
    })
_module_typeBindings.vehicleType = vehicleType
Namespace.addCategoryObject('typeBinding', 'vehicleType', vehicleType)


# Complex type flowWithoutIDType with content type ELEMENT_ONLY
class flowWithoutIDType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type flowWithoutIDType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flowWithoutIDType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 296, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element route uses Python identifier route
    __route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__AbsentNamespace0_flowWithoutIDType_route', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 299, 16), )

    
    route = property(__route.value, __route.set, None, None)

    
    # Element routeDistribution uses Python identifier routeDistribution
    __routeDistribution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routeDistribution'), 'routeDistribution', '__AbsentNamespace0_flowWithoutIDType_routeDistribution', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 300, 16), )

    
    routeDistribution = property(__routeDistribution.value, __routeDistribution.set, None, None)

    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_flowWithoutIDType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_flowWithoutIDType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute route uses Python identifier route_
    __route_ = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'route'), 'route_', '__AbsentNamespace0_flowWithoutIDType_route_', pyxb.binding.datatypes.string)
    __route_._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 305, 8)
    __route_._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 305, 8)
    
    route_ = property(__route_.value, __route_.set, None, None)

    
    # Attribute fromTaz uses Python identifier fromTaz
    __fromTaz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fromTaz'), 'fromTaz', '__AbsentNamespace0_flowWithoutIDType_fromTaz', pyxb.binding.datatypes.string)
    __fromTaz._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 306, 8)
    __fromTaz._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 306, 8)
    
    fromTaz = property(__fromTaz.value, __fromTaz.set, None, None)

    
    # Attribute toTaz uses Python identifier toTaz
    __toTaz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toTaz'), 'toTaz', '__AbsentNamespace0_flowWithoutIDType_toTaz', pyxb.binding.datatypes.string)
    __toTaz._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 307, 8)
    __toTaz._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 307, 8)
    
    toTaz = property(__toTaz.value, __toTaz.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_flowWithoutIDType_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 308, 8)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 308, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_flowWithoutIDType_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 309, 8)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 309, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute via uses Python identifier via
    __via = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'via'), 'via', '__AbsentNamespace0_flowWithoutIDType_via', pyxb.binding.datatypes.string)
    __via._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 310, 8)
    __via._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 310, 8)
    
    via = property(__via.value, __via.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_flowWithoutIDType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 311, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 311, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__AbsentNamespace0_flowWithoutIDType_begin', _module_typeBindings.nonNegativeFloatType)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 312, 8)
    __begin._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 312, 8)
    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__AbsentNamespace0_flowWithoutIDType_end', _module_typeBindings.nonNegativeFloatType)
    __end._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 313, 8)
    __end._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 313, 8)
    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute period uses Python identifier period
    __period = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'period'), 'period', '__AbsentNamespace0_flowWithoutIDType_period', _module_typeBindings.positiveFloatType)
    __period._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 314, 8)
    __period._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 314, 8)
    
    period = property(__period.value, __period.set, None, None)

    
    # Attribute vehsPerHour uses Python identifier vehsPerHour
    __vehsPerHour = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vehsPerHour'), 'vehsPerHour', '__AbsentNamespace0_flowWithoutIDType_vehsPerHour', _module_typeBindings.nonNegativeFloatType)
    __vehsPerHour._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 315, 8)
    __vehsPerHour._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 315, 8)
    
    vehsPerHour = property(__vehsPerHour.value, __vehsPerHour.set, None, None)

    
    # Attribute probability uses Python identifier probability
    __probability = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability'), 'probability', '__AbsentNamespace0_flowWithoutIDType_probability', _module_typeBindings.nonNegativeFloatType)
    __probability._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 316, 8)
    __probability._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 316, 8)
    
    probability = property(__probability.value, __probability.set, None, None)

    
    # Attribute number uses Python identifier number
    __number = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'number'), 'number', '__AbsentNamespace0_flowWithoutIDType_number', pyxb.binding.datatypes.int)
    __number._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 317, 8)
    __number._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 317, 8)
    
    number = property(__number.value, __number.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_flowWithoutIDType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 318, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 318, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute departLane uses Python identifier departLane
    __departLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departLane'), 'departLane', '__AbsentNamespace0_flowWithoutIDType_departLane', _module_typeBindings.departLaneType)
    __departLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 319, 8)
    __departLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 319, 8)
    
    departLane = property(__departLane.value, __departLane.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_flowWithoutIDType_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 320, 8)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 320, 8)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute departSpeed uses Python identifier departSpeed
    __departSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departSpeed'), 'departSpeed', '__AbsentNamespace0_flowWithoutIDType_departSpeed', _module_typeBindings.departSpeedType)
    __departSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 321, 8)
    __departSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 321, 8)
    
    departSpeed = property(__departSpeed.value, __departSpeed.set, None, None)

    
    # Attribute arrivalLane uses Python identifier arrivalLane
    __arrivalLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalLane'), 'arrivalLane', '__AbsentNamespace0_flowWithoutIDType_arrivalLane', _module_typeBindings.arrivalLaneType)
    __arrivalLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 322, 8)
    __arrivalLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 322, 8)
    
    arrivalLane = property(__arrivalLane.value, __arrivalLane.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_flowWithoutIDType_arrivalPos', _module_typeBindings.arrivalPosType)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 323, 8)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 323, 8)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute arrivalSpeed uses Python identifier arrivalSpeed
    __arrivalSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalSpeed'), 'arrivalSpeed', '__AbsentNamespace0_flowWithoutIDType_arrivalSpeed', _module_typeBindings.arrivalSpeedType)
    __arrivalSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 324, 8)
    __arrivalSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 324, 8)
    
    arrivalSpeed = property(__arrivalSpeed.value, __arrivalSpeed.set, None, None)

    
    # Attribute departPosLat uses Python identifier departPosLat
    __departPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPosLat'), 'departPosLat', '__AbsentNamespace0_flowWithoutIDType_departPosLat', _module_typeBindings.departPosLatType)
    __departPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 325, 8)
    __departPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 325, 8)
    
    departPosLat = property(__departPosLat.value, __departPosLat.set, None, None)

    
    # Attribute arrivalPosLat uses Python identifier arrivalPosLat
    __arrivalPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPosLat'), 'arrivalPosLat', '__AbsentNamespace0_flowWithoutIDType_arrivalPosLat', _module_typeBindings.arrivalPosLatType)
    __arrivalPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 326, 8)
    __arrivalPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 326, 8)
    
    arrivalPosLat = property(__arrivalPosLat.value, __arrivalPosLat.set, None, None)

    
    # Attribute line uses Python identifier line
    __line = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'line'), 'line', '__AbsentNamespace0_flowWithoutIDType_line', pyxb.binding.datatypes.string)
    __line._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 327, 8)
    __line._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 327, 8)
    
    line = property(__line.value, __line.set, None, None)

    
    # Attribute personNumber uses Python identifier personNumber
    __personNumber = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'personNumber'), 'personNumber', '__AbsentNamespace0_flowWithoutIDType_personNumber', pyxb.binding.datatypes.nonNegativeInteger)
    __personNumber._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 328, 8)
    __personNumber._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 328, 8)
    
    personNumber = property(__personNumber.value, __personNumber.set, None, None)

    _ElementMap.update({
        __route.name() : __route,
        __routeDistribution.name() : __routeDistribution,
        __stop.name() : __stop,
        __param.name() : __param
    })
    _AttributeMap.update({
        __route_.name() : __route_,
        __fromTaz.name() : __fromTaz,
        __toTaz.name() : __toTaz,
        __from.name() : __from,
        __to.name() : __to,
        __via.name() : __via,
        __type.name() : __type,
        __begin.name() : __begin,
        __end.name() : __end,
        __period.name() : __period,
        __vehsPerHour.name() : __vehsPerHour,
        __probability.name() : __probability,
        __number.name() : __number,
        __color.name() : __color,
        __departLane.name() : __departLane,
        __departPos.name() : __departPos,
        __departSpeed.name() : __departSpeed,
        __arrivalLane.name() : __arrivalLane,
        __arrivalPos.name() : __arrivalPos,
        __arrivalSpeed.name() : __arrivalSpeed,
        __departPosLat.name() : __departPosLat,
        __arrivalPosLat.name() : __arrivalPosLat,
        __line.name() : __line,
        __personNumber.name() : __personNumber
    })
_module_typeBindings.flowWithoutIDType = flowWithoutIDType
Namespace.addCategoryObject('typeBinding', 'flowWithoutIDType', flowWithoutIDType)


# Complex type tripType with content type ELEMENT_ONLY
class tripType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tripType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tripType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 347, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_tripType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 349, 12), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_tripType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 350, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_tripType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 352, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 352, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute fromTaz uses Python identifier fromTaz
    __fromTaz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fromTaz'), 'fromTaz', '__AbsentNamespace0_tripType_fromTaz', pyxb.binding.datatypes.string)
    __fromTaz._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 353, 8)
    __fromTaz._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 353, 8)
    
    fromTaz = property(__fromTaz.value, __fromTaz.set, None, None)

    
    # Attribute toTaz uses Python identifier toTaz
    __toTaz = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toTaz'), 'toTaz', '__AbsentNamespace0_tripType_toTaz', pyxb.binding.datatypes.string)
    __toTaz._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 354, 8)
    __toTaz._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 354, 8)
    
    toTaz = property(__toTaz.value, __toTaz.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_tripType_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 355, 8)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 355, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_tripType_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 356, 8)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 356, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute via uses Python identifier via
    __via = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'via'), 'via', '__AbsentNamespace0_tripType_via', pyxb.binding.datatypes.string)
    __via._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 357, 8)
    __via._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 357, 8)
    
    via = property(__via.value, __via.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_tripType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 358, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 358, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute depart uses Python identifier depart
    __depart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'depart'), 'depart', '__AbsentNamespace0_tripType_depart', _module_typeBindings.departType, required=True)
    __depart._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 359, 8)
    __depart._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 359, 8)
    
    depart = property(__depart.value, __depart.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_tripType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 360, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 360, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute departLane uses Python identifier departLane
    __departLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departLane'), 'departLane', '__AbsentNamespace0_tripType_departLane', _module_typeBindings.departLaneType)
    __departLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 361, 8)
    __departLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 361, 8)
    
    departLane = property(__departLane.value, __departLane.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_tripType_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 362, 8)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 362, 8)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute departSpeed uses Python identifier departSpeed
    __departSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departSpeed'), 'departSpeed', '__AbsentNamespace0_tripType_departSpeed', _module_typeBindings.departSpeedType)
    __departSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 363, 8)
    __departSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 363, 8)
    
    departSpeed = property(__departSpeed.value, __departSpeed.set, None, None)

    
    # Attribute arrivalLane uses Python identifier arrivalLane
    __arrivalLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalLane'), 'arrivalLane', '__AbsentNamespace0_tripType_arrivalLane', _module_typeBindings.arrivalLaneType)
    __arrivalLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 364, 8)
    __arrivalLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 364, 8)
    
    arrivalLane = property(__arrivalLane.value, __arrivalLane.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_tripType_arrivalPos', _module_typeBindings.arrivalPosType)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 365, 8)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 365, 8)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute arrivalSpeed uses Python identifier arrivalSpeed
    __arrivalSpeed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalSpeed'), 'arrivalSpeed', '__AbsentNamespace0_tripType_arrivalSpeed', _module_typeBindings.arrivalSpeedType)
    __arrivalSpeed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 366, 8)
    __arrivalSpeed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 366, 8)
    
    arrivalSpeed = property(__arrivalSpeed.value, __arrivalSpeed.set, None, None)

    
    # Attribute departPosLat uses Python identifier departPosLat
    __departPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPosLat'), 'departPosLat', '__AbsentNamespace0_tripType_departPosLat', _module_typeBindings.departPosLatType)
    __departPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 367, 8)
    __departPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 367, 8)
    
    departPosLat = property(__departPosLat.value, __departPosLat.set, None, None)

    
    # Attribute arrivalPosLat uses Python identifier arrivalPosLat
    __arrivalPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPosLat'), 'arrivalPosLat', '__AbsentNamespace0_tripType_arrivalPosLat', _module_typeBindings.arrivalPosLatType)
    __arrivalPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 368, 8)
    __arrivalPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 368, 8)
    
    arrivalPosLat = property(__arrivalPosLat.value, __arrivalPosLat.set, None, None)

    _ElementMap.update({
        __stop.name() : __stop,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __fromTaz.name() : __fromTaz,
        __toTaz.name() : __toTaz,
        __from.name() : __from,
        __to.name() : __to,
        __via.name() : __via,
        __type.name() : __type,
        __depart.name() : __depart,
        __color.name() : __color,
        __departLane.name() : __departLane,
        __departPos.name() : __departPos,
        __departSpeed.name() : __departSpeed,
        __arrivalLane.name() : __arrivalLane,
        __arrivalPos.name() : __arrivalPos,
        __arrivalSpeed.name() : __arrivalSpeed,
        __departPosLat.name() : __departPosLat,
        __arrivalPosLat.name() : __arrivalPosLat
    })
_module_typeBindings.tripType = tripType
Namespace.addCategoryObject('typeBinding', 'tripType', tripType)


# Complex type vehicleRouteType with content type ELEMENT_ONLY
class vehicleRouteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type vehicleRouteType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'vehicleRouteType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 487, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_vehicleRouteType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 489, 12), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_vehicleRouteType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 490, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_vehicleRouteType_edges', pyxb.binding.datatypes.string, required=True)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 492, 8)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 492, 8)
    
    edges = property(__edges.value, __edges.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_vehicleRouteType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 493, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 493, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute exitTimes uses Python identifier exitTimes
    __exitTimes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exitTimes'), 'exitTimes', '__AbsentNamespace0_vehicleRouteType_exitTimes', pyxb.binding.datatypes.string)
    __exitTimes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 494, 8)
    __exitTimes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 494, 8)
    
    exitTimes = property(__exitTimes.value, __exitTimes.set, None, None)

    _ElementMap.update({
        __stop.name() : __stop,
        __param.name() : __param
    })
    _AttributeMap.update({
        __edges.name() : __edges,
        __color.name() : __color,
        __exitTimes.name() : __exitTimes
    })
_module_typeBindings.vehicleRouteType = vehicleRouteType
Namespace.addCategoryObject('typeBinding', 'vehicleRouteType', vehicleRouteType)


# Complex type routeDistRouteType with content type ELEMENT_ONLY
class routeDistRouteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type routeDistRouteType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routeDistRouteType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 497, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_routeDistRouteType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 499, 12), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_routeDistRouteType_id', pyxb.binding.datatypes.string)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 501, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 501, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_routeDistRouteType_edges', pyxb.binding.datatypes.string)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 502, 8)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 502, 8)
    
    edges = property(__edges.value, __edges.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_routeDistRouteType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 503, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 503, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute cost uses Python identifier cost
    __cost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cost'), 'cost', '__AbsentNamespace0_routeDistRouteType_cost', pyxb.binding.datatypes.float)
    __cost._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 504, 8)
    __cost._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 504, 8)
    
    cost = property(__cost.value, __cost.set, None, None)

    
    # Attribute probability uses Python identifier probability
    __probability = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'probability'), 'probability', '__AbsentNamespace0_routeDistRouteType_probability', pyxb.binding.datatypes.float)
    __probability._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 505, 8)
    __probability._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 505, 8)
    
    probability = property(__probability.value, __probability.set, None, None)

    
    # Attribute exitTimes uses Python identifier exitTimes
    __exitTimes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'exitTimes'), 'exitTimes', '__AbsentNamespace0_routeDistRouteType_exitTimes', pyxb.binding.datatypes.string)
    __exitTimes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 506, 8)
    __exitTimes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 506, 8)
    
    exitTimes = property(__exitTimes.value, __exitTimes.set, None, None)

    
    # Attribute refId uses Python identifier refId
    __refId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'refId'), 'refId', '__AbsentNamespace0_routeDistRouteType_refId', pyxb.binding.datatypes.string)
    __refId._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 507, 8)
    __refId._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 507, 8)
    
    refId = property(__refId.value, __refId.set, None, None)

    
    # Attribute replacedOnEdge uses Python identifier replacedOnEdge
    __replacedOnEdge = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'replacedOnEdge'), 'replacedOnEdge', '__AbsentNamespace0_routeDistRouteType_replacedOnEdge', pyxb.binding.datatypes.string)
    __replacedOnEdge._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 508, 8)
    __replacedOnEdge._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 508, 8)
    
    replacedOnEdge = property(__replacedOnEdge.value, __replacedOnEdge.set, None, None)

    
    # Attribute replacedAtTime uses Python identifier replacedAtTime
    __replacedAtTime = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'replacedAtTime'), 'replacedAtTime', '__AbsentNamespace0_routeDistRouteType_replacedAtTime', _module_typeBindings.nonNegativeFloatType)
    __replacedAtTime._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 509, 8)
    __replacedAtTime._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 509, 8)
    
    replacedAtTime = property(__replacedAtTime.value, __replacedAtTime.set, None, None)

    _ElementMap.update({
        __stop.name() : __stop
    })
    _AttributeMap.update({
        __id.name() : __id,
        __edges.name() : __edges,
        __color.name() : __color,
        __cost.name() : __cost,
        __probability.name() : __probability,
        __exitTimes.name() : __exitTimes,
        __refId.name() : __refId,
        __replacedOnEdge.name() : __replacedOnEdge,
        __replacedAtTime.name() : __replacedAtTime
    })
_module_typeBindings.routeDistRouteType = routeDistRouteType
Namespace.addCategoryObject('typeBinding', 'routeDistRouteType', routeDistRouteType)


# Complex type personType with content type ELEMENT_ONLY
class personType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type personType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'personType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 557, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element personTrip uses Python identifier personTrip
    __personTrip = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'personTrip'), 'personTrip', '__AbsentNamespace0_personType_personTrip', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 559, 12), )

    
    personTrip = property(__personTrip.value, __personTrip.set, None, None)

    
    # Element ride uses Python identifier ride
    __ride = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ride'), 'ride', '__AbsentNamespace0_personType_ride', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 570, 12), )

    
    ride = property(__ride.value, __ride.set, None, None)

    
    # Element walk uses Python identifier walk
    __walk = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'walk'), 'walk', '__AbsentNamespace0_personType_walk', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 580, 12), )

    
    walk = property(__walk.value, __walk.set, None, None)

    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_personType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 595, 12), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_personType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 596, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_personType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 598, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 598, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute depart uses Python identifier depart
    __depart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'depart'), 'depart', '__AbsentNamespace0_personType_depart', pyxb.binding.datatypes.float, required=True)
    __depart._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 599, 8)
    __depart._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 599, 8)
    
    depart = property(__depart.value, __depart.set, None, None)

    
    # Attribute arrival uses Python identifier arrival
    __arrival = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrival'), 'arrival', '__AbsentNamespace0_personType_arrival', _module_typeBindings.nonNegativeFloatType)
    __arrival._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 600, 8)
    __arrival._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 600, 8)
    
    arrival = property(__arrival.value, __arrival.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_personType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 601, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 601, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_personType_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 602, 8)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 602, 8)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_personType_arrivalPos', _module_typeBindings.arrivalPosType)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 603, 8)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 603, 8)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_personType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 604, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 604, 8)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute modes uses Python identifier modes
    __modes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modes'), 'modes', '__AbsentNamespace0_personType_modes', pyxb.binding.datatypes.string)
    __modes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 605, 8)
    __modes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 605, 8)
    
    modes = property(__modes.value, __modes.set, None, None)

    
    # Attribute vTypes uses Python identifier vTypes
    __vTypes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vTypes'), 'vTypes', '__AbsentNamespace0_personType_vTypes', pyxb.binding.datatypes.string)
    __vTypes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 606, 8)
    __vTypes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 606, 8)
    
    vTypes = property(__vTypes.value, __vTypes.set, None, None)

    _ElementMap.update({
        __personTrip.name() : __personTrip,
        __ride.name() : __ride,
        __walk.name() : __walk,
        __stop.name() : __stop,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __depart.name() : __depart,
        __arrival.name() : __arrival,
        __type.name() : __type,
        __departPos.name() : __departPos,
        __arrivalPos.name() : __arrivalPos,
        __color.name() : __color,
        __modes.name() : __modes,
        __vTypes.name() : __vTypes
    })
_module_typeBindings.personType = personType
Namespace.addCategoryObject('typeBinding', 'personType', personType)


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 560, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_CTD_ANON_4_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 561, 20)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 561, 20)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_CTD_ANON_4_to', pyxb.binding.datatypes.string, required=True)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 562, 20)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 562, 20)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute modes uses Python identifier modes
    __modes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'modes'), 'modes', '__AbsentNamespace0_CTD_ANON_4_modes', pyxb.binding.datatypes.string)
    __modes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 563, 20)
    __modes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 563, 20)
    
    modes = property(__modes.value, __modes.set, None, None)

    
    # Attribute vTypes uses Python identifier vTypes
    __vTypes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'vTypes'), 'vTypes', '__AbsentNamespace0_CTD_ANON_4_vTypes', pyxb.binding.datatypes.string)
    __vTypes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 564, 20)
    __vTypes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 564, 20)
    
    vTypes = property(__vTypes.value, __vTypes.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_CTD_ANON_4_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 565, 20)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 565, 20)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_CTD_ANON_4_arrivalPos', _module_typeBindings.arrivalPosType)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 566, 20)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 566, 20)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute walkFactor uses Python identifier walkFactor
    __walkFactor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'walkFactor'), 'walkFactor', '__AbsentNamespace0_CTD_ANON_4_walkFactor', _module_typeBindings.positiveFloatType)
    __walkFactor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 567, 20)
    __walkFactor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 567, 20)
    
    walkFactor = property(__walkFactor.value, __walkFactor.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __from.name() : __from,
        __to.name() : __to,
        __modes.name() : __modes,
        __vTypes.name() : __vTypes,
        __departPos.name() : __departPos,
        __arrivalPos.name() : __arrivalPos,
        __walkFactor.name() : __walkFactor
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 581, 16)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute route uses Python identifier route
    __route = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'route'), 'route', '__AbsentNamespace0_CTD_ANON_5_route', pyxb.binding.datatypes.string)
    __route._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 582, 20)
    __route._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 582, 20)
    
    route = property(__route.value, __route.set, None, None)

    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_CTD_ANON_5_edges', pyxb.binding.datatypes.string)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 583, 20)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 583, 20)
    
    edges = property(__edges.value, __edges.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_CTD_ANON_5_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 584, 20)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 584, 20)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_CTD_ANON_5_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 585, 20)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 585, 20)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute busStop uses Python identifier busStop
    __busStop = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'busStop'), 'busStop', '__AbsentNamespace0_CTD_ANON_5_busStop', pyxb.binding.datatypes.string)
    __busStop._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 586, 20)
    __busStop._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 586, 20)
    
    busStop = property(__busStop.value, __busStop.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_CTD_ANON_5_speed', _module_typeBindings.positiveFloatType)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 587, 20)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 587, 20)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute duration uses Python identifier duration
    __duration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'duration'), 'duration', '__AbsentNamespace0_CTD_ANON_5_duration', _module_typeBindings.positiveFloatType)
    __duration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 588, 20)
    __duration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 588, 20)
    
    duration = property(__duration.value, __duration.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_CTD_ANON_5_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 589, 20)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 589, 20)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute departPosLat uses Python identifier departPosLat
    __departPosLat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPosLat'), 'departPosLat', '__AbsentNamespace0_CTD_ANON_5_departPosLat', pyxb.binding.datatypes.float)
    __departPosLat._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 590, 20)
    __departPosLat._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 590, 20)
    
    departPosLat = property(__departPosLat.value, __departPosLat.set, None, None)

    
    # Attribute arrivalPos uses Python identifier arrivalPos
    __arrivalPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrivalPos'), 'arrivalPos', '__AbsentNamespace0_CTD_ANON_5_arrivalPos', _module_typeBindings.arrivalPosType)
    __arrivalPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 591, 20)
    __arrivalPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 591, 20)
    
    arrivalPos = property(__arrivalPos.value, __arrivalPos.set, None, None)

    
    # Attribute cost uses Python identifier cost
    __cost = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cost'), 'cost', '__AbsentNamespace0_CTD_ANON_5_cost', pyxb.binding.datatypes.float)
    __cost._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 592, 20)
    __cost._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 592, 20)
    
    cost = property(__cost.value, __cost.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __route.name() : __route,
        __edges.name() : __edges,
        __from.name() : __from,
        __to.name() : __to,
        __busStop.name() : __busStop,
        __speed.name() : __speed,
        __duration.name() : __duration,
        __departPos.name() : __departPos,
        __departPosLat.name() : __departPosLat,
        __arrivalPos.name() : __arrivalPos,
        __cost.name() : __cost
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type containerType with content type ELEMENT_ONLY
class containerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type containerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'containerType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 609, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element transport uses Python identifier transport
    __transport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'transport'), 'transport', '__AbsentNamespace0_containerType_transport', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 611, 12), )

    
    transport = property(__transport.value, __transport.set, None, None)

    
    # Element tranship uses Python identifier tranship
    __tranship = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tranship'), 'tranship', '__AbsentNamespace0_containerType_tranship', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 618, 12), )

    
    tranship = property(__tranship.value, __tranship.set, None, None)

    
    # Element stop uses Python identifier stop
    __stop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop'), 'stop', '__AbsentNamespace0_containerType_stop', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 629, 12), )

    
    stop = property(__stop.value, __stop.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_containerType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 630, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_containerType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 632, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 632, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute depart uses Python identifier depart
    __depart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'depart'), 'depart', '__AbsentNamespace0_containerType_depart', pyxb.binding.datatypes.float, required=True)
    __depart._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 633, 8)
    __depart._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 633, 8)
    
    depart = property(__depart.value, __depart.set, None, None)

    
    # Attribute arrival uses Python identifier arrival
    __arrival = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'arrival'), 'arrival', '__AbsentNamespace0_containerType_arrival', _module_typeBindings.nonNegativeFloatType)
    __arrival._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 634, 8)
    __arrival._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 634, 8)
    
    arrival = property(__arrival.value, __arrival.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_containerType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 635, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 635, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute departPos uses Python identifier departPos
    __departPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'departPos'), 'departPos', '__AbsentNamespace0_containerType_departPos', _module_typeBindings.departPosType)
    __departPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 636, 8)
    __departPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 636, 8)
    
    departPos = property(__departPos.value, __departPos.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__AbsentNamespace0_containerType_color', _module_typeBindings.colorType)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 637, 8)
    __color._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 637, 8)
    
    color = property(__color.value, __color.set, None, None)

    _ElementMap.update({
        __transport.name() : __transport,
        __tranship.name() : __tranship,
        __stop.name() : __stop,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __depart.name() : __depart,
        __arrival.name() : __arrival,
        __type.name() : __type,
        __departPos.name() : __departPos,
        __color.name() : __color
    })
_module_typeBindings.containerType = containerType
Namespace.addCategoryObject('typeBinding', 'containerType', containerType)


# Complex type flowCalibratorType with content type ELEMENT_ONLY
class flowCalibratorType (flowWithoutIDType):
    """Complex type flowCalibratorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flowCalibratorType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 331, 4)
    _ElementMap = flowWithoutIDType._ElementMap.copy()
    _AttributeMap = flowWithoutIDType._AttributeMap.copy()
    # Base type is flowWithoutIDType
    
    # Element route (route) inherited from flowWithoutIDType
    
    # Element routeDistribution (routeDistribution) inherited from flowWithoutIDType
    
    # Element stop (stop) inherited from flowWithoutIDType
    
    # Element param (param) inherited from flowWithoutIDType
    
    # Attribute route_ inherited from flowWithoutIDType
    
    # Attribute fromTaz inherited from flowWithoutIDType
    
    # Attribute toTaz inherited from flowWithoutIDType
    
    # Attribute from_ inherited from flowWithoutIDType
    
    # Attribute to inherited from flowWithoutIDType
    
    # Attribute via inherited from flowWithoutIDType
    
    # Attribute type inherited from flowWithoutIDType
    
    # Attribute begin inherited from flowWithoutIDType
    
    # Attribute end inherited from flowWithoutIDType
    
    # Attribute period inherited from flowWithoutIDType
    
    # Attribute vehsPerHour inherited from flowWithoutIDType
    
    # Attribute probability inherited from flowWithoutIDType
    
    # Attribute number inherited from flowWithoutIDType
    
    # Attribute color inherited from flowWithoutIDType
    
    # Attribute departLane inherited from flowWithoutIDType
    
    # Attribute departPos inherited from flowWithoutIDType
    
    # Attribute departSpeed inherited from flowWithoutIDType
    
    # Attribute arrivalLane inherited from flowWithoutIDType
    
    # Attribute arrivalPos inherited from flowWithoutIDType
    
    # Attribute arrivalSpeed inherited from flowWithoutIDType
    
    # Attribute departPosLat inherited from flowWithoutIDType
    
    # Attribute arrivalPosLat inherited from flowWithoutIDType
    
    # Attribute line inherited from flowWithoutIDType
    
    # Attribute personNumber inherited from flowWithoutIDType
    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_flowCalibratorType_speed', _module_typeBindings.nonNegativeFloatType)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 334, 16)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 334, 16)
    
    speed = property(__speed.value, __speed.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __speed.name() : __speed
    })
_module_typeBindings.flowCalibratorType = flowCalibratorType
Namespace.addCategoryObject('typeBinding', 'flowCalibratorType', flowCalibratorType)


# Complex type flowType with content type ELEMENT_ONLY
class flowType (flowWithoutIDType):
    """Complex type flowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'flowType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 339, 4)
    _ElementMap = flowWithoutIDType._ElementMap.copy()
    _AttributeMap = flowWithoutIDType._AttributeMap.copy()
    # Base type is flowWithoutIDType
    
    # Element route (route) inherited from flowWithoutIDType
    
    # Element routeDistribution (routeDistribution) inherited from flowWithoutIDType
    
    # Element stop (stop) inherited from flowWithoutIDType
    
    # Element param (param) inherited from flowWithoutIDType
    
    # Attribute route_ inherited from flowWithoutIDType
    
    # Attribute fromTaz inherited from flowWithoutIDType
    
    # Attribute toTaz inherited from flowWithoutIDType
    
    # Attribute from_ inherited from flowWithoutIDType
    
    # Attribute to inherited from flowWithoutIDType
    
    # Attribute via inherited from flowWithoutIDType
    
    # Attribute type inherited from flowWithoutIDType
    
    # Attribute begin inherited from flowWithoutIDType
    
    # Attribute end inherited from flowWithoutIDType
    
    # Attribute period inherited from flowWithoutIDType
    
    # Attribute vehsPerHour inherited from flowWithoutIDType
    
    # Attribute probability inherited from flowWithoutIDType
    
    # Attribute number inherited from flowWithoutIDType
    
    # Attribute color inherited from flowWithoutIDType
    
    # Attribute departLane inherited from flowWithoutIDType
    
    # Attribute departPos inherited from flowWithoutIDType
    
    # Attribute departSpeed inherited from flowWithoutIDType
    
    # Attribute arrivalLane inherited from flowWithoutIDType
    
    # Attribute arrivalPos inherited from flowWithoutIDType
    
    # Attribute arrivalSpeed inherited from flowWithoutIDType
    
    # Attribute departPosLat inherited from flowWithoutIDType
    
    # Attribute arrivalPosLat inherited from flowWithoutIDType
    
    # Attribute line inherited from flowWithoutIDType
    
    # Attribute personNumber inherited from flowWithoutIDType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_flowType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 342, 16)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 342, 16)
    
    id = property(__id.value, __id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.flowType = flowType
Namespace.addCategoryObject('typeBinding', 'flowType', flowType)


# Complex type routeType with content type ELEMENT_ONLY
class routeType (vehicleRouteType):
    """Complex type routeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 371, 4)
    _ElementMap = vehicleRouteType._ElementMap.copy()
    _AttributeMap = vehicleRouteType._AttributeMap.copy()
    # Base type is vehicleRouteType
    
    # Element stop (stop) inherited from vehicleRouteType
    
    # Element param (param) inherited from vehicleRouteType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_routeType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 374, 16)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 374, 16)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute edges inherited from vehicleRouteType
    
    # Attribute color inherited from vehicleRouteType
    
    # Attribute exitTimes inherited from vehicleRouteType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id
    })
_module_typeBindings.routeType = routeType
Namespace.addCategoryObject('typeBinding', 'routeType', routeType)


routes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'routes'), routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', routes.name().localName(), routes)

route_alternatives = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'route-alternatives'), routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 7, 4))
Namespace.addCategoryObject('elementBinding', route_alternatives.name().localName(), route_alternatives)



vTypeDistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vType'), vTypeType, scope=vTypeDistributionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 533, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 532, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vTypeDistributionType._UseForTag(pyxb.namespace.ExpandedName(None, 'vType')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 533, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vTypeDistributionType._Automaton = _BuildAutomaton()




routeDistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route'), routeDistRouteType, scope=routeDistributionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 541, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 540, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routeDistributionType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 541, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
routeDistributionType._Automaton = _BuildAutomaton_()




vehicleRouteDistributionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route'), routeDistRouteType, scope=vehicleRouteDistributionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 551, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(vehicleRouteDistributionType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 551, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
vehicleRouteDistributionType._Automaton = _BuildAutomaton_2()




routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vTypeDistribution'), vTypeDistributionType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 11, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routeDistribution'), routeDistributionType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 12, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vType'), vTypeType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 13, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehicle'), vehicleType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 14, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route'), routeType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 15, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flow'), flowType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 16, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'trip'), tripType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 17, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'person'), personType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 18, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'container'), containerType, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 19, 12)))

routesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'include'), CTD_ANON_2, scope=routesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 20, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 11, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 12, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 13, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 14, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 15, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 16, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 17, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 18, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 19, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 20, 12))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'vTypeDistribution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeDistribution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 12, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'vType')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 13, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehicle')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 14, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 15, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'flow')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 16, 12))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'trip')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 17, 12))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'person')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 18, 12))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'container')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 19, 12))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(routesType._UseForTag(pyxb.namespace.ExpandedName(None, 'include')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routes_file.xsd', 20, 12))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
routesType._Automaton = _BuildAutomaton_3()




tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase'), phaseType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12)))

tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
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
tlLogicType._Automaton = _BuildAutomaton_4()




typeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restriction'), restrictionType, scope=typeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
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
typeType._Automaton = _BuildAutomaton_5()




vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 8, 12)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-IDM'), cfIDMType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 11, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-IDMM'), cfIDMMType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 12, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-Krauss'), cfKraussType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 13, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-KraussPS'), cfKraussType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 14, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-KraussOrig1'), cfKraussType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 15, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-SmartSK'), cfSmartType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 16, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-Daniel1'), cfSmartType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 17, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-PWagner2009'), cfPWagType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 18, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-BKerner'), cfBKernerType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 19, 20)))

vTypeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carFollowing-Wiedemann'), cfWiedemannType, scope=vTypeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 20, 20)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 8, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 9, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 22, 16))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 8, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-IDM')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 11, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-IDMM')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 12, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-Krauss')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 13, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-KraussPS')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 14, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-KraussOrig1')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 15, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-SmartSK')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 16, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-Daniel1')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 17, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-PWagner2009')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 18, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-BKerner')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 19, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'carFollowing-Wiedemann')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 20, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(vTypeType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 22, 16))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vTypeType._Automaton = _BuildAutomaton_6()




vehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=vehicleType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 260, 12)))

vehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route'), vehicleRouteType, scope=vehicleType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 263, 20)))

vehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routeDistribution'), vehicleRouteDistributionType, scope=vehicleType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 264, 20)))

vehicleType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=vehicleType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 269, 16)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 260, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 261, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 266, 16))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 268, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 270, 16))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vehicleType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vehicleType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 263, 20))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(vehicleType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeDistribution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 264, 20))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(vehicleType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 266, 16))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(vehicleType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 269, 16))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(vehicleType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 270, 16))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False),
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
vehicleType._Automaton = _BuildAutomaton_7()




flowWithoutIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route'), vehicleRouteType, scope=flowWithoutIDType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 299, 16)))

flowWithoutIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routeDistribution'), vehicleRouteDistributionType, scope=flowWithoutIDType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 300, 16)))

flowWithoutIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=flowWithoutIDType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12)))

flowWithoutIDType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=flowWithoutIDType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 298, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flowWithoutIDType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 299, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flowWithoutIDType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeDistribution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 300, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(flowWithoutIDType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(flowWithoutIDType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
flowWithoutIDType._Automaton = _BuildAutomaton_8()




tripType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=tripType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 349, 12)))

tripType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=tripType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 350, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 349, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 350, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tripType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 349, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tripType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 350, 12))
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
tripType._Automaton = _BuildAutomaton_9()




vehicleRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=vehicleRouteType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 489, 12)))

vehicleRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=vehicleRouteType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 490, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 488, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vehicleRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 489, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(vehicleRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 490, 12))
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
vehicleRouteType._Automaton = _BuildAutomaton_10()




routeDistRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=routeDistRouteType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 499, 12)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 499, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routeDistRouteType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 499, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
routeDistRouteType._Automaton = _BuildAutomaton_11()




personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'personTrip'), CTD_ANON_4, scope=personType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 559, 12)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ride'), CTD_ANON, scope=personType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 570, 12)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'walk'), CTD_ANON_5, scope=personType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 580, 12)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=personType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 595, 12)))

personType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=personType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 596, 12)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(None, 'personTrip')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 559, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(None, 'ride')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 570, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(None, 'walk')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 580, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 595, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 596, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personType._Automaton = _BuildAutomaton_12()




containerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'transport'), CTD_ANON_, scope=containerType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 611, 12)))

containerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tranship'), CTD_ANON_3, scope=containerType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 618, 12)))

containerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop'), stopType, scope=containerType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 629, 12)))

containerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=containerType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 630, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(containerType._UseForTag(pyxb.namespace.ExpandedName(None, 'transport')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 611, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(containerType._UseForTag(pyxb.namespace.ExpandedName(None, 'tranship')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 618, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(containerType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 629, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(containerType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 630, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
containerType._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 298, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flowCalibratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 299, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flowCalibratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeDistribution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 300, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(flowCalibratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(flowCalibratorType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
flowCalibratorType._Automaton = _BuildAutomaton_14()




def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 298, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flowType._UseForTag(pyxb.namespace.ExpandedName(None, 'route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 299, 16))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(flowType._UseForTag(pyxb.namespace.ExpandedName(None, 'routeDistribution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 300, 16))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(flowType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 302, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(flowType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 303, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
flowType._Automaton = _BuildAutomaton_15()




def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 488, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routeType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 489, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routeType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/routeTypes.xsd', 490, 12))
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
routeType._Automaton = _BuildAutomaton_16()

