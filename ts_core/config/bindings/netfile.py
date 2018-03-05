# ./netfile.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2018-02-11 20:57:47.997669 by PyXB version 1.2.6 using Python 3.6.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1efb5a54-0f98-11e8-83e3-186590d9922f')

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
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 34, 12)
    _Documentation = None
STD_ANON_11._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_11._CF_pattern.addPattern(pattern='\\d+.\\d+')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_pattern)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 54, 12)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.normal = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='normal', tag='normal')
STD_ANON_12.internal = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='internal', tag='internal')
STD_ANON_12.connector = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='connector', tag='connector')
STD_ANON_12.crossing = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='crossing', tag='crossing')
STD_ANON_12.walkingarea = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='walkingarea', tag='walkingarea')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 72, 12)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.center = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='center', tag='center')
STD_ANON_13.right = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='right', tag='right')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 111, 12)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.traffic_light = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='traffic_light', tag='traffic_light')
STD_ANON_14.traffic_light_unregulated = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='traffic_light_unregulated', tag='traffic_light_unregulated')
STD_ANON_14.traffic_light_right_on_red = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='traffic_light_right_on_red', tag='traffic_light_right_on_red')
STD_ANON_14.rail_signal = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='rail_signal', tag='rail_signal')
STD_ANON_14.rail_crossing = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='rail_crossing', tag='rail_crossing')
STD_ANON_14.priority = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='priority', tag='priority')
STD_ANON_14.priority_stop = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='priority_stop', tag='priority_stop')
STD_ANON_14.right_before_left = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='right_before_left', tag='right_before_left')
STD_ANON_14.allway_stop = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='allway_stop', tag='allway_stop')
STD_ANON_14.zipper = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='zipper', tag='zipper')
STD_ANON_14.district = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='district', tag='district')
STD_ANON_14.unregulated = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='unregulated', tag='unregulated')
STD_ANON_14.internal = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='internal', tag='internal')
STD_ANON_14.dead_end = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='dead_end', tag='dead_end')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 140, 12)
    _Documentation = None
STD_ANON_15._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_15._CF_pattern.addPattern(pattern='[01]+')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_pattern)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 149, 12)
    _Documentation = None
STD_ANON_16._CF_pattern = pyxb.binding.facets.CF_pattern()
STD_ANON_16._CF_pattern.addPattern(pattern='[01]+')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_pattern)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 175, 12)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.s = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='s', tag='s')
STD_ANON_17.t = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='t', tag='t')
STD_ANON_17.T = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='T', tag='T')
STD_ANON_17.l = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='l', tag='l')
STD_ANON_17.r = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='r', tag='r')
STD_ANON_17.L = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='L', tag='L')
STD_ANON_17.R = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='R', tag='R')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 188, 12)
    _Documentation = None
STD_ANON_18._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_18, enum_prefix=None)
STD_ANON_18.M = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='M', tag='M')
STD_ANON_18.m = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='m', tag='m')
STD_ANON_18.o = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='o', tag='o')
STD_ANON_18.emptyString = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='=', tag='emptyString')
STD_ANON_18.emptyString_ = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='-', tag='emptyString_')
STD_ANON_18.s = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='s', tag='s')
STD_ANON_18.w = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='w', tag='w')
STD_ANON_18.Z = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='Z', tag='Z')
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_enumeration)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

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


# Complex type prohibitionType with content type EMPTY
class prohibitionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type prohibitionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'prohibitionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 203, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute prohibitor uses Python identifier prohibitor
    __prohibitor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prohibitor'), 'prohibitor', '__AbsentNamespace0_prohibitionType_prohibitor', pyxb.binding.datatypes.string, required=True)
    __prohibitor._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 204, 8)
    __prohibitor._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 204, 8)
    
    prohibitor = property(__prohibitor.value, __prohibitor.set, None, None)

    
    # Attribute prohibited uses Python identifier prohibited
    __prohibited = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prohibited'), 'prohibited', '__AbsentNamespace0_prohibitionType_prohibited', pyxb.binding.datatypes.string, required=True)
    __prohibited._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 205, 8)
    __prohibited._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 205, 8)
    
    prohibited = property(__prohibited.value, __prohibited.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __prohibitor.name() : __prohibitor,
        __prohibited.name() : __prohibited
    })
_module_typeBindings.prohibitionType = prohibitionType
Namespace.addCategoryObject('typeBinding', 'prohibitionType', prohibitionType)


# Complex type roundaboutType with content type EMPTY
class roundaboutType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type roundaboutType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'roundaboutType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 208, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute nodes uses Python identifier nodes
    __nodes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'nodes'), 'nodes', '__AbsentNamespace0_roundaboutType_nodes', pyxb.binding.datatypes.string, required=True)
    __nodes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 209, 8)
    __nodes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 209, 8)
    
    nodes = property(__nodes.value, __nodes.set, None, None)

    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_roundaboutType_edges', pyxb.binding.datatypes.string, required=True)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 210, 8)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 210, 8)
    
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
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 213, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute lane uses Python identifier lane
    __lane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lane'), 'lane', '__AbsentNamespace0_neighType_lane', pyxb.binding.datatypes.string, required=True)
    __lane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 214, 8)
    __lane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 214, 8)
    
    lane = property(__lane.value, __lane.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __lane.name() : __lane
    })
_module_typeBindings.neighType = neighType
Namespace.addCategoryObject('typeBinding', 'neighType', neighType)


# Complex type tazsType with content type ELEMENT_ONLY
class tazsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tazsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tazsType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 8, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element taz uses Python identifier taz
    __taz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'taz'), 'taz', '__AbsentNamespace0_tazsType_taz', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 10, 12), )

    
    taz = property(__taz.value, __taz.set, None, None)

    _ElementMap.update({
        __taz.name() : __taz
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tazsType = tazsType
Namespace.addCategoryObject('typeBinding', 'tazsType', tazsType)


# Complex type tazSubType with content type EMPTY
class tazSubType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tazSubType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tazSubType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_tazSubType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 25, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 25, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute weight uses Python identifier weight
    __weight = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'weight'), 'weight', '__AbsentNamespace0_tazSubType_weight', pyxb.binding.datatypes.float, required=True)
    __weight._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 26, 8)
    __weight._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 26, 8)
    
    weight = property(__weight.value, __weight.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __weight.name() : __weight
    })
_module_typeBindings.tazSubType = tazSubType
Namespace.addCategoryObject('typeBinding', 'tazSubType', tazSubType)


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


# Complex type netType with content type ELEMENT_ONLY
class netType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type netType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'netType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 21, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element location uses Python identifier location
    __location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'location'), 'location', '__AbsentNamespace0_netType_location', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 23, 12), )

    
    location = property(__location.value, __location.set, None, None)

    
    # Element type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_netType_type', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 24, 12), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element edge uses Python identifier edge
    __edge = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edge'), 'edge', '__AbsentNamespace0_netType_edge', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 25, 12), )

    
    edge = property(__edge.value, __edge.set, None, None)

    
    # Element tlLogic uses Python identifier tlLogic
    __tlLogic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tlLogic'), 'tlLogic', '__AbsentNamespace0_netType_tlLogic', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 26, 12), )

    
    tlLogic = property(__tlLogic.value, __tlLogic.set, None, None)

    
    # Element junction uses Python identifier junction
    __junction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junction'), 'junction', '__AbsentNamespace0_netType_junction', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 27, 12), )

    
    junction = property(__junction.value, __junction.set, None, None)

    
    # Element connection uses Python identifier connection
    __connection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'connection'), 'connection', '__AbsentNamespace0_netType_connection', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 28, 12), )

    
    connection = property(__connection.value, __connection.set, None, None)

    
    # Element prohibition uses Python identifier prohibition
    __prohibition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'prohibition'), 'prohibition', '__AbsentNamespace0_netType_prohibition', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 29, 12), )

    
    prohibition = property(__prohibition.value, __prohibition.set, None, None)

    
    # Element roundabout uses Python identifier roundabout
    __roundabout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'roundabout'), 'roundabout', '__AbsentNamespace0_netType_roundabout', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 30, 12), )

    
    roundabout = property(__roundabout.value, __roundabout.set, None, None)

    
    # Element taz uses Python identifier taz
    __taz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'taz'), 'taz', '__AbsentNamespace0_netType_taz', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 31, 12), )

    
    taz = property(__taz.value, __taz.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_netType_version', _module_typeBindings.STD_ANON_11)
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 33, 8)
    __version._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 33, 8)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute junctionCornerDetail uses Python identifier junctionCornerDetail
    __junctionCornerDetail = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'junctionCornerDetail'), 'junctionCornerDetail', '__AbsentNamespace0_netType_junctionCornerDetail', pyxb.binding.datatypes.int)
    __junctionCornerDetail._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 40, 8)
    __junctionCornerDetail._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 40, 8)
    
    junctionCornerDetail = property(__junctionCornerDetail.value, __junctionCornerDetail.set, None, None)

    
    # Attribute junctionLinkDetail uses Python identifier junctionLinkDetail
    __junctionLinkDetail = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'junctionLinkDetail'), 'junctionLinkDetail', '__AbsentNamespace0_netType_junctionLinkDetail', pyxb.binding.datatypes.int)
    __junctionLinkDetail._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 41, 8)
    __junctionLinkDetail._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 41, 8)
    
    junctionLinkDetail = property(__junctionLinkDetail.value, __junctionLinkDetail.set, None, None)

    
    # Attribute lefthand uses Python identifier lefthand
    __lefthand = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lefthand'), 'lefthand', '__AbsentNamespace0_netType_lefthand', _module_typeBindings.boolType)
    __lefthand._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 42, 8)
    __lefthand._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 42, 8)
    
    lefthand = property(__lefthand.value, __lefthand.set, None, None)

    
    # Attribute rectangularLaneCut uses Python identifier rectangularLaneCut
    __rectangularLaneCut = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rectangularLaneCut'), 'rectangularLaneCut', '__AbsentNamespace0_netType_rectangularLaneCut', _module_typeBindings.boolType)
    __rectangularLaneCut._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 43, 8)
    __rectangularLaneCut._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 43, 8)
    
    rectangularLaneCut = property(__rectangularLaneCut.value, __rectangularLaneCut.set, None, None)

    
    # Attribute walkingareas uses Python identifier walkingareas
    __walkingareas = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'walkingareas'), 'walkingareas', '__AbsentNamespace0_netType_walkingareas', _module_typeBindings.boolType)
    __walkingareas._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 44, 8)
    __walkingareas._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 44, 8)
    
    walkingareas = property(__walkingareas.value, __walkingareas.set, None, None)

    _ElementMap.update({
        __location.name() : __location,
        __type.name() : __type,
        __edge.name() : __edge,
        __tlLogic.name() : __tlLogic,
        __junction.name() : __junction,
        __connection.name() : __connection,
        __prohibition.name() : __prohibition,
        __roundabout.name() : __roundabout,
        __taz.name() : __taz
    })
    _AttributeMap.update({
        __version.name() : __version,
        __junctionCornerDetail.name() : __junctionCornerDetail,
        __junctionLinkDetail.name() : __junctionLinkDetail,
        __lefthand.name() : __lefthand,
        __rectangularLaneCut.name() : __rectangularLaneCut,
        __walkingareas.name() : __walkingareas
    })
_module_typeBindings.netType = netType
Namespace.addCategoryObject('typeBinding', 'netType', netType)


# Complex type edgeType with content type ELEMENT_ONLY
class edgeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type edgeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'edgeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 47, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element lane uses Python identifier lane
    __lane = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lane'), 'lane', '__AbsentNamespace0_edgeType_lane', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 49, 12), )

    
    lane = property(__lane.value, __lane.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_edgeType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 50, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_edgeType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 52, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 52, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute function uses Python identifier function
    __function = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'function'), 'function', '__AbsentNamespace0_edgeType_function', _module_typeBindings.STD_ANON_12)
    __function._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 53, 8)
    __function._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 53, 8)
    
    function = property(__function.value, __function.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_edgeType_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 64, 8)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 64, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_edgeType_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 65, 8)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 65, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_edgeType_name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 66, 8)
    __name._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 66, 8)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute priority uses Python identifier priority
    __priority = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'priority'), 'priority', '__AbsentNamespace0_edgeType_priority', pyxb.binding.datatypes.integer)
    __priority._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 67, 8)
    __priority._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 67, 8)
    
    priority = property(__priority.value, __priority.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_edgeType_length', _module_typeBindings.positiveFloatType)
    __length._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 68, 8)
    __length._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 68, 8)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_edgeType_type', pyxb.binding.datatypes.string)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 69, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 69, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_edgeType_shape', _module_typeBindings.shapeTypeTwo)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 70, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 70, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute spreadType uses Python identifier spreadType
    __spreadType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'spreadType'), 'spreadType', '__AbsentNamespace0_edgeType_spreadType', _module_typeBindings.STD_ANON_13)
    __spreadType._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 71, 8)
    __spreadType._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 71, 8)
    
    spreadType = property(__spreadType.value, __spreadType.set, None, None)

    
    # Attribute crossingEdges uses Python identifier crossingEdges
    __crossingEdges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'crossingEdges'), 'crossingEdges', '__AbsentNamespace0_edgeType_crossingEdges', pyxb.binding.datatypes.string)
    __crossingEdges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 79, 8)
    __crossingEdges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 79, 8)
    
    crossingEdges = property(__crossingEdges.value, __crossingEdges.set, None, None)

    _ElementMap.update({
        __lane.name() : __lane,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __function.name() : __function,
        __from.name() : __from,
        __to.name() : __to,
        __name.name() : __name,
        __priority.name() : __priority,
        __length.name() : __length,
        __type.name() : __type,
        __shape.name() : __shape,
        __spreadType.name() : __spreadType,
        __crossingEdges.name() : __crossingEdges
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
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 82, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element neigh uses Python identifier neigh
    __neigh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'neigh'), 'neigh', '__AbsentNamespace0_laneType_neigh', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 84, 12), )

    
    neigh = property(__neigh.value, __neigh.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_laneType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 85, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_laneType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 87, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 87, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_laneType_index', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 88, 8)
    __index._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 88, 8)
    
    index = property(__index.value, __index.set, None, None)

    
    # Attribute allow uses Python identifier allow
    __allow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'allow'), 'allow', '__AbsentNamespace0_laneType_allow', pyxb.binding.datatypes.string)
    __allow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 89, 8)
    __allow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 89, 8)
    
    allow = property(__allow.value, __allow.set, None, None)

    
    # Attribute disallow uses Python identifier disallow
    __disallow = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'disallow'), 'disallow', '__AbsentNamespace0_laneType_disallow', pyxb.binding.datatypes.string)
    __disallow._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 90, 8)
    __disallow._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 90, 8)
    
    disallow = property(__disallow.value, __disallow.set, None, None)

    
    # Attribute prefer uses Python identifier prefer
    __prefer = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'prefer'), 'prefer', '__AbsentNamespace0_laneType_prefer', pyxb.binding.datatypes.string)
    __prefer._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 91, 8)
    __prefer._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 91, 8)
    
    prefer = property(__prefer.value, __prefer.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_laneType_speed', _module_typeBindings.positiveFloatType, required=True)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 92, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 92, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute length uses Python identifier length
    __length = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'length'), 'length', '__AbsentNamespace0_laneType_length', _module_typeBindings.positiveFloatType, required=True)
    __length._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 93, 8)
    __length._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 93, 8)
    
    length = property(__length.value, __length.set, None, None)

    
    # Attribute endOffset uses Python identifier endOffset
    __endOffset = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'endOffset'), 'endOffset', '__AbsentNamespace0_laneType_endOffset', _module_typeBindings.positiveFloatType)
    __endOffset._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 94, 8)
    __endOffset._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 94, 8)
    
    endOffset = property(__endOffset.value, __endOffset.set, None, None)

    
    # Attribute width uses Python identifier width
    __width = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'width'), 'width', '__AbsentNamespace0_laneType_width', _module_typeBindings.nonNegativeFloatType)
    __width._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 95, 8)
    __width._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 95, 8)
    
    width = property(__width.value, __width.set, None, None)

    
    # Attribute acceleration uses Python identifier acceleration
    __acceleration = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'acceleration'), 'acceleration', '__AbsentNamespace0_laneType_acceleration', _module_typeBindings.boolType)
    __acceleration._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 96, 8)
    __acceleration._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 96, 8)
    
    acceleration = property(__acceleration.value, __acceleration.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_laneType_shape', _module_typeBindings.shapeTypeTwo, required=True)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 97, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 97, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute customShape uses Python identifier customShape
    __customShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'customShape'), 'customShape', '__AbsentNamespace0_laneType_customShape', _module_typeBindings.boolType)
    __customShape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 98, 8)
    __customShape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 98, 8)
    
    customShape = property(__customShape.value, __customShape.set, None, None)

    _ElementMap.update({
        __neigh.name() : __neigh,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __index.name() : __index,
        __allow.name() : __allow,
        __disallow.name() : __disallow,
        __prefer.name() : __prefer,
        __speed.name() : __speed,
        __length.name() : __length,
        __endOffset.name() : __endOffset,
        __width.name() : __width,
        __acceleration.name() : __acceleration,
        __shape.name() : __shape,
        __customShape.name() : __customShape
    })
_module_typeBindings.laneType = laneType
Namespace.addCategoryObject('typeBinding', 'laneType', laneType)


# Complex type junctionType with content type ELEMENT_ONLY
class junctionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type junctionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'junctionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 101, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element request uses Python identifier request
    __request = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'request'), 'request', '__AbsentNamespace0_junctionType_request', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 103, 12), )

    
    request = property(__request.value, __request.set, None, None)

    
    # Element param uses Python identifier param
    __param = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'param'), 'param', '__AbsentNamespace0_junctionType_param', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 104, 12), )

    
    param = property(__param.value, __param.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_junctionType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 106, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 106, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute x uses Python identifier x
    __x = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'x'), 'x', '__AbsentNamespace0_junctionType_x', pyxb.binding.datatypes.float, required=True)
    __x._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 107, 8)
    __x._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 107, 8)
    
    x = property(__x.value, __x.set, None, None)

    
    # Attribute y uses Python identifier y
    __y = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'y'), 'y', '__AbsentNamespace0_junctionType_y', pyxb.binding.datatypes.float, required=True)
    __y._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 108, 8)
    __y._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 108, 8)
    
    y = property(__y.value, __y.set, None, None)

    
    # Attribute z uses Python identifier z
    __z = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'z'), 'z', '__AbsentNamespace0_junctionType_z', pyxb.binding.datatypes.float)
    __z._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 109, 8)
    __z._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 109, 8)
    
    z = property(__z.value, __z.set, None, None)

    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_junctionType_type', _module_typeBindings.STD_ANON_14, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 110, 8)
    __type._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 110, 8)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute incLanes uses Python identifier incLanes
    __incLanes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'incLanes'), 'incLanes', '__AbsentNamespace0_junctionType_incLanes', pyxb.binding.datatypes.string, required=True)
    __incLanes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 130, 8)
    __incLanes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 130, 8)
    
    incLanes = property(__incLanes.value, __incLanes.set, None, None)

    
    # Attribute intLanes uses Python identifier intLanes
    __intLanes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'intLanes'), 'intLanes', '__AbsentNamespace0_junctionType_intLanes', pyxb.binding.datatypes.string, required=True)
    __intLanes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 131, 8)
    __intLanes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 131, 8)
    
    intLanes = property(__intLanes.value, __intLanes.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_junctionType_shape', _module_typeBindings.shapeType)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 132, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 132, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute radius uses Python identifier radius
    __radius = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'radius'), 'radius', '__AbsentNamespace0_junctionType_radius', _module_typeBindings.nonNegativeFloatType)
    __radius._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 133, 8)
    __radius._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 133, 8)
    
    radius = property(__radius.value, __radius.set, None, None)

    
    # Attribute customShape uses Python identifier customShape
    __customShape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'customShape'), 'customShape', '__AbsentNamespace0_junctionType_customShape', _module_typeBindings.boolType)
    __customShape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 134, 8)
    __customShape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 134, 8)
    
    customShape = property(__customShape.value, __customShape.set, None, None)

    _ElementMap.update({
        __request.name() : __request,
        __param.name() : __param
    })
    _AttributeMap.update({
        __id.name() : __id,
        __x.name() : __x,
        __y.name() : __y,
        __z.name() : __z,
        __type.name() : __type,
        __incLanes.name() : __incLanes,
        __intLanes.name() : __intLanes,
        __shape.name() : __shape,
        __radius.name() : __radius,
        __customShape.name() : __customShape
    })
_module_typeBindings.junctionType = junctionType
Namespace.addCategoryObject('typeBinding', 'junctionType', junctionType)


# Complex type requestType with content type EMPTY
class requestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type requestType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'requestType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 137, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute index uses Python identifier index
    __index = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'index'), 'index', '__AbsentNamespace0_requestType_index', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __index._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 138, 8)
    __index._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 138, 8)
    
    index = property(__index.value, __index.set, None, None)

    
    # Attribute response uses Python identifier response
    __response = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'response'), 'response', '__AbsentNamespace0_requestType_response', _module_typeBindings.STD_ANON_15, required=True)
    __response._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 139, 8)
    __response._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 139, 8)
    
    response = property(__response.value, __response.set, None, None)

    
    # Attribute foes uses Python identifier foes
    __foes = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'foes'), 'foes', '__AbsentNamespace0_requestType_foes', _module_typeBindings.STD_ANON_16, required=True)
    __foes._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 148, 8)
    __foes._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 148, 8)
    
    foes = property(__foes.value, __foes.set, None, None)

    
    # Attribute cont uses Python identifier cont
    __cont = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'cont'), 'cont', '__AbsentNamespace0_requestType_cont', _module_typeBindings.boolType)
    __cont._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 157, 8)
    __cont._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 157, 8)
    
    cont = property(__cont.value, __cont.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __index.name() : __index,
        __response.name() : __response,
        __foes.name() : __foes,
        __cont.name() : __cont
    })
_module_typeBindings.requestType = requestType
Namespace.addCategoryObject('typeBinding', 'requestType', requestType)


# Complex type connectionType with content type EMPTY
class connectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type connectionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'connectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 160, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__AbsentNamespace0_connectionType_from', pyxb.binding.datatypes.string, required=True)
    __from._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 161, 8)
    __from._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 161, 8)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__AbsentNamespace0_connectionType_to', pyxb.binding.datatypes.string, required=True)
    __to._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 162, 8)
    __to._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 162, 8)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute fromLane uses Python identifier fromLane
    __fromLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fromLane'), 'fromLane', '__AbsentNamespace0_connectionType_fromLane', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __fromLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 163, 8)
    __fromLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 163, 8)
    
    fromLane = property(__fromLane.value, __fromLane.set, None, None)

    
    # Attribute toLane uses Python identifier toLane
    __toLane = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'toLane'), 'toLane', '__AbsentNamespace0_connectionType_toLane', pyxb.binding.datatypes.nonNegativeInteger, required=True)
    __toLane._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 164, 8)
    __toLane._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 164, 8)
    
    toLane = property(__toLane.value, __toLane.set, None, None)

    
    # Attribute pass uses Python identifier pass_
    __pass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'pass'), 'pass_', '__AbsentNamespace0_connectionType_pass', _module_typeBindings.boolType)
    __pass._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 165, 8)
    __pass._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 165, 8)
    
    pass_ = property(__pass.value, __pass.set, None, None)

    
    # Attribute keepClear uses Python identifier keepClear
    __keepClear = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'keepClear'), 'keepClear', '__AbsentNamespace0_connectionType_keepClear', _module_typeBindings.boolType)
    __keepClear._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 166, 8)
    __keepClear._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 166, 8)
    
    keepClear = property(__keepClear.value, __keepClear.set, None, None)

    
    # Attribute contPos uses Python identifier contPos
    __contPos = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'contPos'), 'contPos', '__AbsentNamespace0_connectionType_contPos', pyxb.binding.datatypes.float)
    __contPos._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 167, 8)
    __contPos._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 167, 8)
    
    contPos = property(__contPos.value, __contPos.set, None, None)

    
    # Attribute visibility uses Python identifier visibility
    __visibility = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'visibility'), 'visibility', '__AbsentNamespace0_connectionType_visibility', pyxb.binding.datatypes.float)
    __visibility._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 168, 8)
    __visibility._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 168, 8)
    
    visibility = property(__visibility.value, __visibility.set, None, None)

    
    # Attribute speed uses Python identifier speed
    __speed = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'speed'), 'speed', '__AbsentNamespace0_connectionType_speed', pyxb.binding.datatypes.float)
    __speed._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 169, 8)
    __speed._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 169, 8)
    
    speed = property(__speed.value, __speed.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_connectionType_shape', _module_typeBindings.shapeType)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 170, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 170, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    
    # Attribute via uses Python identifier via
    __via = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'via'), 'via', '__AbsentNamespace0_connectionType_via', pyxb.binding.datatypes.string)
    __via._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 171, 8)
    __via._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 171, 8)
    
    via = property(__via.value, __via.set, None, None)

    
    # Attribute tl uses Python identifier tl
    __tl = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tl'), 'tl', '__AbsentNamespace0_connectionType_tl', pyxb.binding.datatypes.string)
    __tl._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 172, 8)
    __tl._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 172, 8)
    
    tl = property(__tl.value, __tl.set, None, None)

    
    # Attribute linkIndex uses Python identifier linkIndex
    __linkIndex = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'linkIndex'), 'linkIndex', '__AbsentNamespace0_connectionType_linkIndex', pyxb.binding.datatypes.integer)
    __linkIndex._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 173, 8)
    __linkIndex._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 173, 8)
    
    linkIndex = property(__linkIndex.value, __linkIndex.set, None, None)

    
    # Attribute dir uses Python identifier dir
    __dir = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dir'), 'dir', '__AbsentNamespace0_connectionType_dir', _module_typeBindings.STD_ANON_17, required=True)
    __dir._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 174, 8)
    __dir._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 174, 8)
    
    dir = property(__dir.value, __dir.set, None, None)

    
    # Attribute state uses Python identifier state
    __state = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'state'), 'state', '__AbsentNamespace0_connectionType_state', _module_typeBindings.STD_ANON_18, required=True)
    __state._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 187, 8)
    __state._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 187, 8)
    
    state = property(__state.value, __state.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __from.name() : __from,
        __to.name() : __to,
        __fromLane.name() : __fromLane,
        __toLane.name() : __toLane,
        __pass.name() : __pass,
        __keepClear.name() : __keepClear,
        __contPos.name() : __contPos,
        __visibility.name() : __visibility,
        __speed.name() : __speed,
        __shape.name() : __shape,
        __via.name() : __via,
        __tl.name() : __tl,
        __linkIndex.name() : __linkIndex,
        __dir.name() : __dir,
        __state.name() : __state
    })
_module_typeBindings.connectionType = connectionType
Namespace.addCategoryObject('typeBinding', 'connectionType', connectionType)


# Complex type tazType with content type ELEMENT_ONLY
class tazType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tazType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tazType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element tazSource uses Python identifier tazSource
    __tazSource = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tazSource'), 'tazSource', '__AbsentNamespace0_tazType_tazSource', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 16, 12), )

    
    tazSource = property(__tazSource.value, __tazSource.set, None, None)

    
    # Element tazSink uses Python identifier tazSink
    __tazSink = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tazSink'), 'tazSink', '__AbsentNamespace0_tazType_tazSink', True, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 17, 12), )

    
    tazSink = property(__tazSink.value, __tazSink.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_tazType_id', pyxb.binding.datatypes.string, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 19, 8)
    __id._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 19, 8)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute edges uses Python identifier edges
    __edges = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'edges'), 'edges', '__AbsentNamespace0_tazType_edges', pyxb.binding.datatypes.string)
    __edges._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 20, 8)
    __edges._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 20, 8)
    
    edges = property(__edges.value, __edges.set, None, None)

    
    # Attribute shape uses Python identifier shape
    __shape = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'shape'), 'shape', '__AbsentNamespace0_tazType_shape', _module_typeBindings.shapeType)
    __shape._DeclarationLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 21, 8)
    __shape._UseLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 21, 8)
    
    shape = property(__shape.value, __shape.set, None, None)

    _ElementMap.update({
        __tazSource.name() : __tazSource,
        __tazSink.name() : __tazSink
    })
    _AttributeMap.update({
        __id.name() : __id,
        __edges.name() : __edges,
        __shape.name() : __shape
    })
_module_typeBindings.tazType = tazType
Namespace.addCategoryObject('typeBinding', 'tazType', tazType)


tazs = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tazs'), tazsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', tazs.name().localName(), tazs)

net = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net'), netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', net.name().localName(), net)



tazsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'taz'), tazType, scope=tazsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 10, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 10, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tazsType._UseForTag(pyxb.namespace.ExpandedName(None, 'taz')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 10, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tazsType._Automaton = _BuildAutomaton()




tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase'), phaseType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12)))

tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
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
tlLogicType._Automaton = _BuildAutomaton_()




typeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restriction'), restrictionType, scope=typeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
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
typeType._Automaton = _BuildAutomaton_2()




netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'location'), locationType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 23, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type'), typeType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 24, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edge'), edgeType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 25, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tlLogic'), tlLogicType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 26, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junction'), junctionType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 27, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'connection'), connectionType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 28, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'prohibition'), prohibitionType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 29, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'roundabout'), roundaboutType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 30, 12)))

netType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'taz'), tazType, scope=netType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 31, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 24, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 25, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 26, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 27, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 28, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 29, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 30, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 31, 12))
    counters.add(cc_7)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'location')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'type')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 24, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'edge')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 25, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'tlLogic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 26, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'junction')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 27, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'connection')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 28, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'prohibition')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 29, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'roundabout')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 30, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(netType._UseForTag(pyxb.namespace.ExpandedName(None, 'taz')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 31, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
netType._Automaton = _BuildAutomaton_3()




edgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lane'), laneType, scope=edgeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 49, 12)))

edgeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=edgeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 50, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=1, max=63, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 49, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 50, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edgeType._UseForTag(pyxb.namespace.ExpandedName(None, 'lane')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 49, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(edgeType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 50, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
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
    return fac.Automaton(states, counters, False, containing_state=None)
edgeType._Automaton = _BuildAutomaton_4()




laneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'neigh'), neighType, scope=laneType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 84, 12)))

laneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=laneType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 85, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 84, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 85, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(laneType._UseForTag(pyxb.namespace.ExpandedName(None, 'neigh')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 84, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(laneType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 85, 12))
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
laneType._Automaton = _BuildAutomaton_5()




junctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'request'), requestType, scope=junctionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 103, 12)))

junctionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=junctionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 104, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 103, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 104, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(junctionType._UseForTag(pyxb.namespace.ExpandedName(None, 'request')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 103, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(junctionType._UseForTag(pyxb.namespace.ExpandedName(None, 'param')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/net_file.xsd', 104, 12))
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
junctionType._Automaton = _BuildAutomaton_6()




tazType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tazSource'), tazSubType, scope=tazType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 16, 12)))

tazType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tazSink'), tazSubType, scope=tazType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 17, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 16, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 17, 12))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tazType._UseForTag(pyxb.namespace.ExpandedName(None, 'tazSource')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tazType._UseForTag(pyxb.namespace.ExpandedName(None, 'tazSink')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/taz_file.xsd', 17, 12))
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
tazType._Automaton = _BuildAutomaton_7()

