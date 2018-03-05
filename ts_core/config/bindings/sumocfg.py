# ./sumocfg.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2018-02-11 20:56:40.825355 by PyXB version 1.2.6 using Python 3.6.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:f74d8ec8-0f97-11e8-aa1c-186590d9922f')

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


# Complex type configurationType with content type ELEMENT_ONLY
class configurationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type configurationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'configurationType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 8, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input'), 'input', '__AbsentNamespace0_configurationType_input', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 10, 12), )

    
    input = property(__input.value, __input.set, None, None)

    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output'), 'output', '__AbsentNamespace0_configurationType_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 11, 12), )

    
    output = property(__output.value, __output.set, None, None)

    
    # Element time uses Python identifier time
    __time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time'), 'time', '__AbsentNamespace0_configurationType_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 12, 12), )

    
    time = property(__time.value, __time.set, None, None)

    
    # Element processing uses Python identifier processing
    __processing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processing'), 'processing', '__AbsentNamespace0_configurationType_processing', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 13, 12), )

    
    processing = property(__processing.value, __processing.set, None, None)

    
    # Element routing uses Python identifier routing
    __routing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routing'), 'routing', '__AbsentNamespace0_configurationType_routing', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 14, 12), )

    
    routing = property(__routing.value, __routing.set, None, None)

    
    # Element report uses Python identifier report
    __report = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'report'), 'report', '__AbsentNamespace0_configurationType_report', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 15, 12), )

    
    report = property(__report.value, __report.set, None, None)

    
    # Element emissions uses Python identifier emissions
    __emissions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emissions'), 'emissions', '__AbsentNamespace0_configurationType_emissions', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 16, 12), )

    
    emissions = property(__emissions.value, __emissions.set, None, None)

    
    # Element communication uses Python identifier communication
    __communication = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'communication'), 'communication', '__AbsentNamespace0_configurationType_communication', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 17, 12), )

    
    communication = property(__communication.value, __communication.set, None, None)

    
    # Element battery uses Python identifier battery
    __battery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'battery'), 'battery', '__AbsentNamespace0_configurationType_battery', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 18, 12), )

    
    battery = property(__battery.value, __battery.set, None, None)

    
    # Element example_device uses Python identifier example_device
    __example_device = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'example_device'), 'example_device', '__AbsentNamespace0_configurationType_example_device', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 19, 12), )

    
    example_device = property(__example_device.value, __example_device.set, None, None)

    
    # Element ssm_device uses Python identifier ssm_device
    __ssm_device = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ssm_device'), 'ssm_device', '__AbsentNamespace0_configurationType_ssm_device', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 20, 12), )

    
    ssm_device = property(__ssm_device.value, __ssm_device.set, None, None)

    
    # Element bluelight_device uses Python identifier bluelight_device
    __bluelight_device = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bluelight_device'), 'bluelight_device', '__AbsentNamespace0_configurationType_bluelight_device', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 21, 12), )

    
    bluelight_device = property(__bluelight_device.value, __bluelight_device.set, None, None)

    
    # Element traci_server uses Python identifier traci_server
    __traci_server = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'traci_server'), 'traci_server', '__AbsentNamespace0_configurationType_traci_server', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 22, 12), )

    
    traci_server = property(__traci_server.value, __traci_server.set, None, None)

    
    # Element mesoscopic uses Python identifier mesoscopic
    __mesoscopic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mesoscopic'), 'mesoscopic', '__AbsentNamespace0_configurationType_mesoscopic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 23, 12), )

    
    mesoscopic = property(__mesoscopic.value, __mesoscopic.set, None, None)

    
    # Element random_number uses Python identifier random_number
    __random_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'random_number'), 'random_number', '__AbsentNamespace0_configurationType_random_number', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 24, 12), )

    
    random_number = property(__random_number.value, __random_number.set, None, None)

    
    # Element gui_only uses Python identifier gui_only
    __gui_only = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gui_only'), 'gui_only', '__AbsentNamespace0_configurationType_gui_only', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 25, 12), )

    
    gui_only = property(__gui_only.value, __gui_only.set, None, None)

    _ElementMap.update({
        __input.name() : __input,
        __output.name() : __output,
        __time.name() : __time,
        __processing.name() : __processing,
        __routing.name() : __routing,
        __report.name() : __report,
        __emissions.name() : __emissions,
        __communication.name() : __communication,
        __battery.name() : __battery,
        __example_device.name() : __example_device,
        __ssm_device.name() : __ssm_device,
        __bluelight_device.name() : __bluelight_device,
        __traci_server.name() : __traci_server,
        __mesoscopic.name() : __mesoscopic,
        __random_number.name() : __random_number,
        __gui_only.name() : __gui_only
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.configurationType = configurationType
Namespace.addCategoryObject('typeBinding', 'configurationType', configurationType)


# Complex type inputType with content type ELEMENT_ONLY
class inputType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type inputType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'inputType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 29, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element net-file uses Python identifier net_file
    __net_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net-file'), 'net_file', '__AbsentNamespace0_inputType_net_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 31, 12), )

    
    net_file = property(__net_file.value, __net_file.set, None, None)

    
    # Element route-files uses Python identifier route_files
    __route_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route-files'), 'route_files', '__AbsentNamespace0_inputType_route_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 32, 12), )

    
    route_files = property(__route_files.value, __route_files.set, None, None)

    
    # Element additional-files uses Python identifier additional_files
    __additional_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'additional-files'), 'additional_files', '__AbsentNamespace0_inputType_additional_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 33, 12), )

    
    additional_files = property(__additional_files.value, __additional_files.set, None, None)

    
    # Element weight-files uses Python identifier weight_files
    __weight_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weight-files'), 'weight_files', '__AbsentNamespace0_inputType_weight_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 34, 12), )

    
    weight_files = property(__weight_files.value, __weight_files.set, None, None)

    
    # Element weight-attribute uses Python identifier weight_attribute
    __weight_attribute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weight-attribute'), 'weight_attribute', '__AbsentNamespace0_inputType_weight_attribute', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 35, 12), )

    
    weight_attribute = property(__weight_attribute.value, __weight_attribute.set, None, None)

    
    # Element load-state uses Python identifier load_state
    __load_state = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'load-state'), 'load_state', '__AbsentNamespace0_inputType_load_state', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 36, 12), )

    
    load_state = property(__load_state.value, __load_state.set, None, None)

    
    # Element load-state.offset uses Python identifier load_state_offset
    __load_state_offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'load-state.offset'), 'load_state_offset', '__AbsentNamespace0_inputType_load_state_offset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 37, 12), )

    
    load_state_offset = property(__load_state_offset.value, __load_state_offset.set, None, None)

    
    # Element load-state.remove-vehicles uses Python identifier load_state_remove_vehicles
    __load_state_remove_vehicles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'load-state.remove-vehicles'), 'load_state_remove_vehicles', '__AbsentNamespace0_inputType_load_state_remove_vehicles', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 38, 12), )

    
    load_state_remove_vehicles = property(__load_state_remove_vehicles.value, __load_state_remove_vehicles.set, None, None)

    _ElementMap.update({
        __net_file.name() : __net_file,
        __route_files.name() : __route_files,
        __additional_files.name() : __additional_files,
        __weight_files.name() : __weight_files,
        __weight_attribute.name() : __weight_attribute,
        __load_state.name() : __load_state,
        __load_state_offset.name() : __load_state_offset,
        __load_state_remove_vehicles.name() : __load_state_remove_vehicles
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.inputType = inputType
Namespace.addCategoryObject('typeBinding', 'inputType', inputType)


# Complex type outputType with content type ELEMENT_ONLY
class outputType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type outputType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'outputType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 42, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output-prefix uses Python identifier output_prefix
    __output_prefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-prefix'), 'output_prefix', '__AbsentNamespace0_outputType_output_prefix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 44, 12), )

    
    output_prefix = property(__output_prefix.value, __output_prefix.set, None, None)

    
    # Element precision uses Python identifier precision
    __precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__AbsentNamespace0_outputType_precision', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 45, 12), )

    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Element precision.geo uses Python identifier precision_geo
    __precision_geo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'precision.geo'), 'precision_geo', '__AbsentNamespace0_outputType_precision_geo', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 46, 12), )

    
    precision_geo = property(__precision_geo.value, __precision_geo.set, None, None)

    
    # Element netstate-dump uses Python identifier netstate_dump
    __netstate_dump = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'netstate-dump'), 'netstate_dump', '__AbsentNamespace0_outputType_netstate_dump', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 47, 12), )

    
    netstate_dump = property(__netstate_dump.value, __netstate_dump.set, None, None)

    
    # Element netstate-dump.empty-edges uses Python identifier netstate_dump_empty_edges
    __netstate_dump_empty_edges = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'netstate-dump.empty-edges'), 'netstate_dump_empty_edges', '__AbsentNamespace0_outputType_netstate_dump_empty_edges', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 48, 12), )

    
    netstate_dump_empty_edges = property(__netstate_dump_empty_edges.value, __netstate_dump_empty_edges.set, None, None)

    
    # Element netstate-dump.precision uses Python identifier netstate_dump_precision
    __netstate_dump_precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'netstate-dump.precision'), 'netstate_dump_precision', '__AbsentNamespace0_outputType_netstate_dump_precision', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 49, 12), )

    
    netstate_dump_precision = property(__netstate_dump_precision.value, __netstate_dump_precision.set, None, None)

    
    # Element emission-output uses Python identifier emission_output
    __emission_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emission-output'), 'emission_output', '__AbsentNamespace0_outputType_emission_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 50, 12), )

    
    emission_output = property(__emission_output.value, __emission_output.set, None, None)

    
    # Element emission-output.precision uses Python identifier emission_output_precision
    __emission_output_precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'emission-output.precision'), 'emission_output_precision', '__AbsentNamespace0_outputType_emission_output_precision', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 51, 12), )

    
    emission_output_precision = property(__emission_output_precision.value, __emission_output_precision.set, None, None)

    
    # Element battery-output uses Python identifier battery_output
    __battery_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'battery-output'), 'battery_output', '__AbsentNamespace0_outputType_battery_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 52, 12), )

    
    battery_output = property(__battery_output.value, __battery_output.set, None, None)

    
    # Element battery-output.precision uses Python identifier battery_output_precision
    __battery_output_precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'battery-output.precision'), 'battery_output_precision', '__AbsentNamespace0_outputType_battery_output_precision', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 53, 12), )

    
    battery_output_precision = property(__battery_output_precision.value, __battery_output_precision.set, None, None)

    
    # Element chargingstations-output uses Python identifier chargingstations_output
    __chargingstations_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'chargingstations-output'), 'chargingstations_output', '__AbsentNamespace0_outputType_chargingstations_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 54, 12), )

    
    chargingstations_output = property(__chargingstations_output.value, __chargingstations_output.set, None, None)

    
    # Element fcd-output uses Python identifier fcd_output
    __fcd_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fcd-output'), 'fcd_output', '__AbsentNamespace0_outputType_fcd_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 55, 12), )

    
    fcd_output = property(__fcd_output.value, __fcd_output.set, None, None)

    
    # Element fcd-output.geo uses Python identifier fcd_output_geo
    __fcd_output_geo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fcd-output.geo'), 'fcd_output_geo', '__AbsentNamespace0_outputType_fcd_output_geo', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 56, 12), )

    
    fcd_output_geo = property(__fcd_output_geo.value, __fcd_output_geo.set, None, None)

    
    # Element fcd-output.signals uses Python identifier fcd_output_signals
    __fcd_output_signals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'fcd-output.signals'), 'fcd_output_signals', '__AbsentNamespace0_outputType_fcd_output_signals', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 57, 12), )

    
    fcd_output_signals = property(__fcd_output_signals.value, __fcd_output_signals.set, None, None)

    
    # Element full-output uses Python identifier full_output
    __full_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'full-output'), 'full_output', '__AbsentNamespace0_outputType_full_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 58, 12), )

    
    full_output = property(__full_output.value, __full_output.set, None, None)

    
    # Element queue-output uses Python identifier queue_output
    __queue_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'queue-output'), 'queue_output', '__AbsentNamespace0_outputType_queue_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 59, 12), )

    
    queue_output = property(__queue_output.value, __queue_output.set, None, None)

    
    # Element vtk-output uses Python identifier vtk_output
    __vtk_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vtk-output'), 'vtk_output', '__AbsentNamespace0_outputType_vtk_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 60, 12), )

    
    vtk_output = property(__vtk_output.value, __vtk_output.set, None, None)

    
    # Element amitran-output uses Python identifier amitran_output
    __amitran_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'amitran-output'), 'amitran_output', '__AbsentNamespace0_outputType_amitran_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 61, 12), )

    
    amitran_output = property(__amitran_output.value, __amitran_output.set, None, None)

    
    # Element summary-output uses Python identifier summary_output
    __summary_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'summary-output'), 'summary_output', '__AbsentNamespace0_outputType_summary_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 62, 12), )

    
    summary_output = property(__summary_output.value, __summary_output.set, None, None)

    
    # Element tripinfo-output uses Python identifier tripinfo_output
    __tripinfo_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tripinfo-output'), 'tripinfo_output', '__AbsentNamespace0_outputType_tripinfo_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 63, 12), )

    
    tripinfo_output = property(__tripinfo_output.value, __tripinfo_output.set, None, None)

    
    # Element tripinfo-output.write-unfinished uses Python identifier tripinfo_output_write_unfinished
    __tripinfo_output_write_unfinished = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tripinfo-output.write-unfinished'), 'tripinfo_output_write_unfinished', '__AbsentNamespace0_outputType_tripinfo_output_write_unfinished', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 64, 12), )

    
    tripinfo_output_write_unfinished = property(__tripinfo_output_write_unfinished.value, __tripinfo_output_write_unfinished.set, None, None)

    
    # Element vehroute-output uses Python identifier vehroute_output
    __vehroute_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output'), 'vehroute_output', '__AbsentNamespace0_outputType_vehroute_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 65, 12), )

    
    vehroute_output = property(__vehroute_output.value, __vehroute_output.set, None, None)

    
    # Element vehroute-output.exit-times uses Python identifier vehroute_output_exit_times
    __vehroute_output_exit_times = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.exit-times'), 'vehroute_output_exit_times', '__AbsentNamespace0_outputType_vehroute_output_exit_times', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 66, 12), )

    
    vehroute_output_exit_times = property(__vehroute_output_exit_times.value, __vehroute_output_exit_times.set, None, None)

    
    # Element vehroute-output.last-route uses Python identifier vehroute_output_last_route
    __vehroute_output_last_route = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.last-route'), 'vehroute_output_last_route', '__AbsentNamespace0_outputType_vehroute_output_last_route', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 67, 12), )

    
    vehroute_output_last_route = property(__vehroute_output_last_route.value, __vehroute_output_last_route.set, None, None)

    
    # Element vehroute-output.sorted uses Python identifier vehroute_output_sorted
    __vehroute_output_sorted = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.sorted'), 'vehroute_output_sorted', '__AbsentNamespace0_outputType_vehroute_output_sorted', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 68, 12), )

    
    vehroute_output_sorted = property(__vehroute_output_sorted.value, __vehroute_output_sorted.set, None, None)

    
    # Element vehroute-output.dua uses Python identifier vehroute_output_dua
    __vehroute_output_dua = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.dua'), 'vehroute_output_dua', '__AbsentNamespace0_outputType_vehroute_output_dua', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 69, 12), )

    
    vehroute_output_dua = property(__vehroute_output_dua.value, __vehroute_output_dua.set, None, None)

    
    # Element vehroute-output.intended-depart uses Python identifier vehroute_output_intended_depart
    __vehroute_output_intended_depart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.intended-depart'), 'vehroute_output_intended_depart', '__AbsentNamespace0_outputType_vehroute_output_intended_depart', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 70, 12), )

    
    vehroute_output_intended_depart = property(__vehroute_output_intended_depart.value, __vehroute_output_intended_depart.set, None, None)

    
    # Element vehroute-output.route-length uses Python identifier vehroute_output_route_length
    __vehroute_output_route_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.route-length'), 'vehroute_output_route_length', '__AbsentNamespace0_outputType_vehroute_output_route_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 71, 12), )

    
    vehroute_output_route_length = property(__vehroute_output_route_length.value, __vehroute_output_route_length.set, None, None)

    
    # Element vehroute-output.write-unfinished uses Python identifier vehroute_output_write_unfinished
    __vehroute_output_write_unfinished = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vehroute-output.write-unfinished'), 'vehroute_output_write_unfinished', '__AbsentNamespace0_outputType_vehroute_output_write_unfinished', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 72, 12), )

    
    vehroute_output_write_unfinished = property(__vehroute_output_write_unfinished.value, __vehroute_output_write_unfinished.set, None, None)

    
    # Element link-output uses Python identifier link_output
    __link_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'link-output'), 'link_output', '__AbsentNamespace0_outputType_link_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 73, 12), )

    
    link_output = property(__link_output.value, __link_output.set, None, None)

    
    # Element bt-output uses Python identifier bt_output
    __bt_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'bt-output'), 'bt_output', '__AbsentNamespace0_outputType_bt_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 74, 12), )

    
    bt_output = property(__bt_output.value, __bt_output.set, None, None)

    
    # Element lanechange-output uses Python identifier lanechange_output
    __lanechange_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lanechange-output'), 'lanechange_output', '__AbsentNamespace0_outputType_lanechange_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 75, 12), )

    
    lanechange_output = property(__lanechange_output.value, __lanechange_output.set, None, None)

    
    # Element stop-output uses Python identifier stop_output
    __stop_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'stop-output'), 'stop_output', '__AbsentNamespace0_outputType_stop_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 76, 12), )

    
    stop_output = property(__stop_output.value, __stop_output.set, None, None)

    
    # Element save-state.times uses Python identifier save_state_times
    __save_state_times = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'save-state.times'), 'save_state_times', '__AbsentNamespace0_outputType_save_state_times', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 77, 12), )

    
    save_state_times = property(__save_state_times.value, __save_state_times.set, None, None)

    
    # Element save-state.period uses Python identifier save_state_period
    __save_state_period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'save-state.period'), 'save_state_period', '__AbsentNamespace0_outputType_save_state_period', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 78, 12), )

    
    save_state_period = property(__save_state_period.value, __save_state_period.set, None, None)

    
    # Element save-state.prefix uses Python identifier save_state_prefix
    __save_state_prefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'save-state.prefix'), 'save_state_prefix', '__AbsentNamespace0_outputType_save_state_prefix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 79, 12), )

    
    save_state_prefix = property(__save_state_prefix.value, __save_state_prefix.set, None, None)

    
    # Element save-state.suffix uses Python identifier save_state_suffix
    __save_state_suffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'save-state.suffix'), 'save_state_suffix', '__AbsentNamespace0_outputType_save_state_suffix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 80, 12), )

    
    save_state_suffix = property(__save_state_suffix.value, __save_state_suffix.set, None, None)

    
    # Element save-state.files uses Python identifier save_state_files
    __save_state_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'save-state.files'), 'save_state_files', '__AbsentNamespace0_outputType_save_state_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 81, 12), )

    
    save_state_files = property(__save_state_files.value, __save_state_files.set, None, None)

    _ElementMap.update({
        __output_prefix.name() : __output_prefix,
        __precision.name() : __precision,
        __precision_geo.name() : __precision_geo,
        __netstate_dump.name() : __netstate_dump,
        __netstate_dump_empty_edges.name() : __netstate_dump_empty_edges,
        __netstate_dump_precision.name() : __netstate_dump_precision,
        __emission_output.name() : __emission_output,
        __emission_output_precision.name() : __emission_output_precision,
        __battery_output.name() : __battery_output,
        __battery_output_precision.name() : __battery_output_precision,
        __chargingstations_output.name() : __chargingstations_output,
        __fcd_output.name() : __fcd_output,
        __fcd_output_geo.name() : __fcd_output_geo,
        __fcd_output_signals.name() : __fcd_output_signals,
        __full_output.name() : __full_output,
        __queue_output.name() : __queue_output,
        __vtk_output.name() : __vtk_output,
        __amitran_output.name() : __amitran_output,
        __summary_output.name() : __summary_output,
        __tripinfo_output.name() : __tripinfo_output,
        __tripinfo_output_write_unfinished.name() : __tripinfo_output_write_unfinished,
        __vehroute_output.name() : __vehroute_output,
        __vehroute_output_exit_times.name() : __vehroute_output_exit_times,
        __vehroute_output_last_route.name() : __vehroute_output_last_route,
        __vehroute_output_sorted.name() : __vehroute_output_sorted,
        __vehroute_output_dua.name() : __vehroute_output_dua,
        __vehroute_output_intended_depart.name() : __vehroute_output_intended_depart,
        __vehroute_output_route_length.name() : __vehroute_output_route_length,
        __vehroute_output_write_unfinished.name() : __vehroute_output_write_unfinished,
        __link_output.name() : __link_output,
        __bt_output.name() : __bt_output,
        __lanechange_output.name() : __lanechange_output,
        __stop_output.name() : __stop_output,
        __save_state_times.name() : __save_state_times,
        __save_state_period.name() : __save_state_period,
        __save_state_prefix.name() : __save_state_prefix,
        __save_state_suffix.name() : __save_state_suffix,
        __save_state_files.name() : __save_state_files
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.outputType = outputType
Namespace.addCategoryObject('typeBinding', 'outputType', outputType)


# Complex type timeType with content type ELEMENT_ONLY
class timeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type timeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'timeType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 85, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element begin uses Python identifier begin
    __begin = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__AbsentNamespace0_timeType_begin', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 87, 12), )

    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Element end uses Python identifier end
    __end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__AbsentNamespace0_timeType_end', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 88, 12), )

    
    end = property(__end.value, __end.set, None, None)

    
    # Element step-length uses Python identifier step_length
    __step_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step-length'), 'step_length', '__AbsentNamespace0_timeType_step_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 89, 12), )

    
    step_length = property(__step_length.value, __step_length.set, None, None)

    _ElementMap.update({
        __begin.name() : __begin,
        __end.name() : __end,
        __step_length.name() : __step_length
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.timeType = timeType
Namespace.addCategoryObject('typeBinding', 'timeType', timeType)


# Complex type processingType with content type ELEMENT_ONLY
class processingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type processingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'processingType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 93, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element step-method.ballistic uses Python identifier step_method_ballistic
    __step_method_ballistic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'step-method.ballistic'), 'step_method_ballistic', '__AbsentNamespace0_processingType_step_method_ballistic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 95, 12), )

    
    step_method_ballistic = property(__step_method_ballistic.value, __step_method_ballistic.set, None, None)

    
    # Element default.action-step-length uses Python identifier default_action_step_length
    __default_action_step_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.action-step-length'), 'default_action_step_length', '__AbsentNamespace0_processingType_default_action_step_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 96, 12), )

    
    default_action_step_length = property(__default_action_step_length.value, __default_action_step_length.set, None, None)

    
    # Element lateral-resolution uses Python identifier lateral_resolution
    __lateral_resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lateral-resolution'), 'lateral_resolution', '__AbsentNamespace0_processingType_lateral_resolution', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 97, 12), )

    
    lateral_resolution = property(__lateral_resolution.value, __lateral_resolution.set, None, None)

    
    # Element carfollow.model uses Python identifier carfollow_model
    __carfollow_model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'carfollow.model'), 'carfollow_model', '__AbsentNamespace0_processingType_carfollow_model', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 98, 12), )

    
    carfollow_model = property(__carfollow_model.value, __carfollow_model.set, None, None)

    
    # Element route-steps uses Python identifier route_steps
    __route_steps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'route-steps'), 'route_steps', '__AbsentNamespace0_processingType_route_steps', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 99, 12), )

    
    route_steps = property(__route_steps.value, __route_steps.set, None, None)

    
    # Element no-internal-links uses Python identifier no_internal_links
    __no_internal_links = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-internal-links'), 'no_internal_links', '__AbsentNamespace0_processingType_no_internal_links', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 100, 12), )

    
    no_internal_links = property(__no_internal_links.value, __no_internal_links.set, None, None)

    
    # Element ignore-junction-blocker uses Python identifier ignore_junction_blocker
    __ignore_junction_blocker = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore-junction-blocker'), 'ignore_junction_blocker', '__AbsentNamespace0_processingType_ignore_junction_blocker', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 101, 12), )

    
    ignore_junction_blocker = property(__ignore_junction_blocker.value, __ignore_junction_blocker.set, None, None)

    
    # Element ignore-route-errors uses Python identifier ignore_route_errors
    __ignore_route_errors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore-route-errors'), 'ignore_route_errors', '__AbsentNamespace0_processingType_ignore_route_errors', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 102, 12), )

    
    ignore_route_errors = property(__ignore_route_errors.value, __ignore_route_errors.set, None, None)

    
    # Element ignore-accidents uses Python identifier ignore_accidents
    __ignore_accidents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore-accidents'), 'ignore_accidents', '__AbsentNamespace0_processingType_ignore_accidents', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 103, 12), )

    
    ignore_accidents = property(__ignore_accidents.value, __ignore_accidents.set, None, None)

    
    # Element collision.action uses Python identifier collision_action
    __collision_action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collision.action'), 'collision_action', '__AbsentNamespace0_processingType_collision_action', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 104, 12), )

    
    collision_action = property(__collision_action.value, __collision_action.set, None, None)

    
    # Element collision.stoptime uses Python identifier collision_stoptime
    __collision_stoptime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collision.stoptime'), 'collision_stoptime', '__AbsentNamespace0_processingType_collision_stoptime', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 105, 12), )

    
    collision_stoptime = property(__collision_stoptime.value, __collision_stoptime.set, None, None)

    
    # Element collision.check-junctions uses Python identifier collision_check_junctions
    __collision_check_junctions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'collision.check-junctions'), 'collision_check_junctions', '__AbsentNamespace0_processingType_collision_check_junctions', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 106, 12), )

    
    collision_check_junctions = property(__collision_check_junctions.value, __collision_check_junctions.set, None, None)

    
    # Element max-num-vehicles uses Python identifier max_num_vehicles
    __max_num_vehicles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max-num-vehicles'), 'max_num_vehicles', '__AbsentNamespace0_processingType_max_num_vehicles', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 107, 12), )

    
    max_num_vehicles = property(__max_num_vehicles.value, __max_num_vehicles.set, None, None)

    
    # Element max-num-teleports uses Python identifier max_num_teleports
    __max_num_teleports = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max-num-teleports'), 'max_num_teleports', '__AbsentNamespace0_processingType_max_num_teleports', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 108, 12), )

    
    max_num_teleports = property(__max_num_teleports.value, __max_num_teleports.set, None, None)

    
    # Element scale uses Python identifier scale
    __scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'scale'), 'scale', '__AbsentNamespace0_processingType_scale', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 109, 12), )

    
    scale = property(__scale.value, __scale.set, None, None)

    
    # Element time-to-teleport uses Python identifier time_to_teleport
    __time_to_teleport = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time-to-teleport'), 'time_to_teleport', '__AbsentNamespace0_processingType_time_to_teleport', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 110, 12), )

    
    time_to_teleport = property(__time_to_teleport.value, __time_to_teleport.set, None, None)

    
    # Element time-to-teleport.highways uses Python identifier time_to_teleport_highways
    __time_to_teleport_highways = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time-to-teleport.highways'), 'time_to_teleport_highways', '__AbsentNamespace0_processingType_time_to_teleport_highways', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 111, 12), )

    
    time_to_teleport_highways = property(__time_to_teleport_highways.value, __time_to_teleport_highways.set, None, None)

    
    # Element waiting-time-memory uses Python identifier waiting_time_memory
    __waiting_time_memory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'waiting-time-memory'), 'waiting_time_memory', '__AbsentNamespace0_processingType_waiting_time_memory', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 112, 12), )

    
    waiting_time_memory = property(__waiting_time_memory.value, __waiting_time_memory.set, None, None)

    
    # Element max-depart-delay uses Python identifier max_depart_delay
    __max_depart_delay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max-depart-delay'), 'max_depart_delay', '__AbsentNamespace0_processingType_max_depart_delay', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 113, 12), )

    
    max_depart_delay = property(__max_depart_delay.value, __max_depart_delay.set, None, None)

    
    # Element sloppy-insert uses Python identifier sloppy_insert
    __sloppy_insert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sloppy-insert'), 'sloppy_insert', '__AbsentNamespace0_processingType_sloppy_insert', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 114, 12), )

    
    sloppy_insert = property(__sloppy_insert.value, __sloppy_insert.set, None, None)

    
    # Element eager-insert uses Python identifier eager_insert
    __eager_insert = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'eager-insert'), 'eager_insert', '__AbsentNamespace0_processingType_eager_insert', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 115, 12), )

    
    eager_insert = property(__eager_insert.value, __eager_insert.set, None, None)

    
    # Element random-depart-offset uses Python identifier random_depart_offset
    __random_depart_offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'random-depart-offset'), 'random_depart_offset', '__AbsentNamespace0_processingType_random_depart_offset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 116, 12), )

    
    random_depart_offset = property(__random_depart_offset.value, __random_depart_offset.set, None, None)

    
    # Element lanechange.duration uses Python identifier lanechange_duration
    __lanechange_duration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lanechange.duration'), 'lanechange_duration', '__AbsentNamespace0_processingType_lanechange_duration', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 117, 12), )

    
    lanechange_duration = property(__lanechange_duration.value, __lanechange_duration.set, None, None)

    
    # Element lanechange.overtake-right uses Python identifier lanechange_overtake_right
    __lanechange_overtake_right = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lanechange.overtake-right'), 'lanechange_overtake_right', '__AbsentNamespace0_processingType_lanechange_overtake_right', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 118, 12), )

    
    lanechange_overtake_right = property(__lanechange_overtake_right.value, __lanechange_overtake_right.set, None, None)

    
    # Element tls.all-off uses Python identifier tls_all_off
    __tls_all_off = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.all-off'), 'tls_all_off', '__AbsentNamespace0_processingType_tls_all_off', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 119, 12), )

    
    tls_all_off = property(__tls_all_off.value, __tls_all_off.set, None, None)

    
    # Element time-to-impatience uses Python identifier time_to_impatience
    __time_to_impatience = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'time-to-impatience'), 'time_to_impatience', '__AbsentNamespace0_processingType_time_to_impatience', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 120, 12), )

    
    time_to_impatience = property(__time_to_impatience.value, __time_to_impatience.set, None, None)

    
    # Element pedestrian.model uses Python identifier pedestrian_model
    __pedestrian_model = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pedestrian.model'), 'pedestrian_model', '__AbsentNamespace0_processingType_pedestrian_model', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 121, 12), )

    
    pedestrian_model = property(__pedestrian_model.value, __pedestrian_model.set, None, None)

    
    # Element pedestrian.striping.stripe-width uses Python identifier pedestrian_striping_stripe_width
    __pedestrian_striping_stripe_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.stripe-width'), 'pedestrian_striping_stripe_width', '__AbsentNamespace0_processingType_pedestrian_striping_stripe_width', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 122, 12), )

    
    pedestrian_striping_stripe_width = property(__pedestrian_striping_stripe_width.value, __pedestrian_striping_stripe_width.set, None, None)

    
    # Element pedestrian.striping.dawdling uses Python identifier pedestrian_striping_dawdling
    __pedestrian_striping_dawdling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.dawdling'), 'pedestrian_striping_dawdling', '__AbsentNamespace0_processingType_pedestrian_striping_dawdling', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 123, 12), )

    
    pedestrian_striping_dawdling = property(__pedestrian_striping_dawdling.value, __pedestrian_striping_dawdling.set, None, None)

    
    # Element pedestrian.striping.jamtime uses Python identifier pedestrian_striping_jamtime
    __pedestrian_striping_jamtime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.jamtime'), 'pedestrian_striping_jamtime', '__AbsentNamespace0_processingType_pedestrian_striping_jamtime', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 124, 12), )

    
    pedestrian_striping_jamtime = property(__pedestrian_striping_jamtime.value, __pedestrian_striping_jamtime.set, None, None)

    
    # Element pedestrian.remote.address uses Python identifier pedestrian_remote_address
    __pedestrian_remote_address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pedestrian.remote.address'), 'pedestrian_remote_address', '__AbsentNamespace0_processingType_pedestrian_remote_address', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 125, 12), )

    
    pedestrian_remote_address = property(__pedestrian_remote_address.value, __pedestrian_remote_address.set, None, None)

    
    # Element astar.landmark-distances uses Python identifier astar_landmark_distances
    __astar_landmark_distances = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'astar.landmark-distances'), 'astar_landmark_distances', '__AbsentNamespace0_processingType_astar_landmark_distances', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 126, 12), )

    
    astar_landmark_distances = property(__astar_landmark_distances.value, __astar_landmark_distances.set, None, None)

    _ElementMap.update({
        __step_method_ballistic.name() : __step_method_ballistic,
        __default_action_step_length.name() : __default_action_step_length,
        __lateral_resolution.name() : __lateral_resolution,
        __carfollow_model.name() : __carfollow_model,
        __route_steps.name() : __route_steps,
        __no_internal_links.name() : __no_internal_links,
        __ignore_junction_blocker.name() : __ignore_junction_blocker,
        __ignore_route_errors.name() : __ignore_route_errors,
        __ignore_accidents.name() : __ignore_accidents,
        __collision_action.name() : __collision_action,
        __collision_stoptime.name() : __collision_stoptime,
        __collision_check_junctions.name() : __collision_check_junctions,
        __max_num_vehicles.name() : __max_num_vehicles,
        __max_num_teleports.name() : __max_num_teleports,
        __scale.name() : __scale,
        __time_to_teleport.name() : __time_to_teleport,
        __time_to_teleport_highways.name() : __time_to_teleport_highways,
        __waiting_time_memory.name() : __waiting_time_memory,
        __max_depart_delay.name() : __max_depart_delay,
        __sloppy_insert.name() : __sloppy_insert,
        __eager_insert.name() : __eager_insert,
        __random_depart_offset.name() : __random_depart_offset,
        __lanechange_duration.name() : __lanechange_duration,
        __lanechange_overtake_right.name() : __lanechange_overtake_right,
        __tls_all_off.name() : __tls_all_off,
        __time_to_impatience.name() : __time_to_impatience,
        __pedestrian_model.name() : __pedestrian_model,
        __pedestrian_striping_stripe_width.name() : __pedestrian_striping_stripe_width,
        __pedestrian_striping_dawdling.name() : __pedestrian_striping_dawdling,
        __pedestrian_striping_jamtime.name() : __pedestrian_striping_jamtime,
        __pedestrian_remote_address.name() : __pedestrian_remote_address,
        __astar_landmark_distances.name() : __astar_landmark_distances
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.processingType = processingType
Namespace.addCategoryObject('typeBinding', 'processingType', processingType)


# Complex type routingType with content type ELEMENT_ONLY
class routingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type routingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'routingType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 130, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element routing-algorithm uses Python identifier routing_algorithm
    __routing_algorithm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'routing-algorithm'), 'routing_algorithm', '__AbsentNamespace0_routingType_routing_algorithm', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 132, 12), )

    
    routing_algorithm = property(__routing_algorithm.value, __routing_algorithm.set, None, None)

    
    # Element weights.random-factor uses Python identifier weights_random_factor
    __weights_random_factor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'weights.random-factor'), 'weights_random_factor', '__AbsentNamespace0_routingType_weights_random_factor', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 133, 12), )

    
    weights_random_factor = property(__weights_random_factor.value, __weights_random_factor.set, None, None)

    
    # Element astar.all-distances uses Python identifier astar_all_distances
    __astar_all_distances = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'astar.all-distances'), 'astar_all_distances', '__AbsentNamespace0_routingType_astar_all_distances', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 134, 12), )

    
    astar_all_distances = property(__astar_all_distances.value, __astar_all_distances.set, None, None)

    
    # Element device.rerouting.probability uses Python identifier device_rerouting_probability
    __device_rerouting_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.probability'), 'device_rerouting_probability', '__AbsentNamespace0_routingType_device_rerouting_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 135, 12), )

    
    device_rerouting_probability = property(__device_rerouting_probability.value, __device_rerouting_probability.set, None, None)

    
    # Element device.rerouting.explicit uses Python identifier device_rerouting_explicit
    __device_rerouting_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.explicit'), 'device_rerouting_explicit', '__AbsentNamespace0_routingType_device_rerouting_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 136, 12), )

    
    device_rerouting_explicit = property(__device_rerouting_explicit.value, __device_rerouting_explicit.set, None, None)

    
    # Element device.rerouting.deterministic uses Python identifier device_rerouting_deterministic
    __device_rerouting_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.deterministic'), 'device_rerouting_deterministic', '__AbsentNamespace0_routingType_device_rerouting_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 137, 12), )

    
    device_rerouting_deterministic = property(__device_rerouting_deterministic.value, __device_rerouting_deterministic.set, None, None)

    
    # Element device.rerouting.period uses Python identifier device_rerouting_period
    __device_rerouting_period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.period'), 'device_rerouting_period', '__AbsentNamespace0_routingType_device_rerouting_period', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 138, 12), )

    
    device_rerouting_period = property(__device_rerouting_period.value, __device_rerouting_period.set, None, None)

    
    # Element device.rerouting.pre-period uses Python identifier device_rerouting_pre_period
    __device_rerouting_pre_period = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.pre-period'), 'device_rerouting_pre_period', '__AbsentNamespace0_routingType_device_rerouting_pre_period', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 139, 12), )

    
    device_rerouting_pre_period = property(__device_rerouting_pre_period.value, __device_rerouting_pre_period.set, None, None)

    
    # Element device.rerouting.adaptation-weight uses Python identifier device_rerouting_adaptation_weight
    __device_rerouting_adaptation_weight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-weight'), 'device_rerouting_adaptation_weight', '__AbsentNamespace0_routingType_device_rerouting_adaptation_weight', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 140, 12), )

    
    device_rerouting_adaptation_weight = property(__device_rerouting_adaptation_weight.value, __device_rerouting_adaptation_weight.set, None, None)

    
    # Element device.rerouting.adaptation-steps uses Python identifier device_rerouting_adaptation_steps
    __device_rerouting_adaptation_steps = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-steps'), 'device_rerouting_adaptation_steps', '__AbsentNamespace0_routingType_device_rerouting_adaptation_steps', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 141, 12), )

    
    device_rerouting_adaptation_steps = property(__device_rerouting_adaptation_steps.value, __device_rerouting_adaptation_steps.set, None, None)

    
    # Element device.rerouting.adaptation-interval uses Python identifier device_rerouting_adaptation_interval
    __device_rerouting_adaptation_interval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-interval'), 'device_rerouting_adaptation_interval', '__AbsentNamespace0_routingType_device_rerouting_adaptation_interval', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 142, 12), )

    
    device_rerouting_adaptation_interval = property(__device_rerouting_adaptation_interval.value, __device_rerouting_adaptation_interval.set, None, None)

    
    # Element device.rerouting.with-taz uses Python identifier device_rerouting_with_taz
    __device_rerouting_with_taz = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.with-taz'), 'device_rerouting_with_taz', '__AbsentNamespace0_routingType_device_rerouting_with_taz', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 143, 12), )

    
    device_rerouting_with_taz = property(__device_rerouting_with_taz.value, __device_rerouting_with_taz.set, None, None)

    
    # Element device.rerouting.init-with-loaded-weights uses Python identifier device_rerouting_init_with_loaded_weights
    __device_rerouting_init_with_loaded_weights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.init-with-loaded-weights'), 'device_rerouting_init_with_loaded_weights', '__AbsentNamespace0_routingType_device_rerouting_init_with_loaded_weights', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 144, 12), )

    
    device_rerouting_init_with_loaded_weights = property(__device_rerouting_init_with_loaded_weights.value, __device_rerouting_init_with_loaded_weights.set, None, None)

    
    # Element device.rerouting.threads uses Python identifier device_rerouting_threads
    __device_rerouting_threads = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.threads'), 'device_rerouting_threads', '__AbsentNamespace0_routingType_device_rerouting_threads', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 145, 12), )

    
    device_rerouting_threads = property(__device_rerouting_threads.value, __device_rerouting_threads.set, None, None)

    
    # Element device.rerouting.output uses Python identifier device_rerouting_output
    __device_rerouting_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.rerouting.output'), 'device_rerouting_output', '__AbsentNamespace0_routingType_device_rerouting_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 146, 12), )

    
    device_rerouting_output = property(__device_rerouting_output.value, __device_rerouting_output.set, None, None)

    _ElementMap.update({
        __routing_algorithm.name() : __routing_algorithm,
        __weights_random_factor.name() : __weights_random_factor,
        __astar_all_distances.name() : __astar_all_distances,
        __device_rerouting_probability.name() : __device_rerouting_probability,
        __device_rerouting_explicit.name() : __device_rerouting_explicit,
        __device_rerouting_deterministic.name() : __device_rerouting_deterministic,
        __device_rerouting_period.name() : __device_rerouting_period,
        __device_rerouting_pre_period.name() : __device_rerouting_pre_period,
        __device_rerouting_adaptation_weight.name() : __device_rerouting_adaptation_weight,
        __device_rerouting_adaptation_steps.name() : __device_rerouting_adaptation_steps,
        __device_rerouting_adaptation_interval.name() : __device_rerouting_adaptation_interval,
        __device_rerouting_with_taz.name() : __device_rerouting_with_taz,
        __device_rerouting_init_with_loaded_weights.name() : __device_rerouting_init_with_loaded_weights,
        __device_rerouting_threads.name() : __device_rerouting_threads,
        __device_rerouting_output.name() : __device_rerouting_output
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.routingType = routingType
Namespace.addCategoryObject('typeBinding', 'routingType', routingType)


# Complex type reportType with content type ELEMENT_ONLY
class reportType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type reportType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reportType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 150, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element verbose uses Python identifier verbose
    __verbose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'verbose'), 'verbose', '__AbsentNamespace0_reportType_verbose', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 152, 12), )

    
    verbose = property(__verbose.value, __verbose.set, None, None)

    
    # Element print-options uses Python identifier print_options
    __print_options = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'print-options'), 'print_options', '__AbsentNamespace0_reportType_print_options', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 153, 12), )

    
    print_options = property(__print_options.value, __print_options.set, None, None)

    
    # Element help uses Python identifier help
    __help = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_reportType_help', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 154, 12), )

    
    help = property(__help.value, __help.set, None, None)

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_reportType_version', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 155, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element xml-validation uses Python identifier xml_validation
    __xml_validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xml-validation'), 'xml_validation', '__AbsentNamespace0_reportType_xml_validation', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 156, 12), )

    
    xml_validation = property(__xml_validation.value, __xml_validation.set, None, None)

    
    # Element xml-validation.net uses Python identifier xml_validation_net
    __xml_validation_net = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xml-validation.net'), 'xml_validation_net', '__AbsentNamespace0_reportType_xml_validation_net', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 157, 12), )

    
    xml_validation_net = property(__xml_validation_net.value, __xml_validation_net.set, None, None)

    
    # Element no-warnings uses Python identifier no_warnings
    __no_warnings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-warnings'), 'no_warnings', '__AbsentNamespace0_reportType_no_warnings', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 158, 12), )

    
    no_warnings = property(__no_warnings.value, __no_warnings.set, None, None)

    
    # Element log uses Python identifier log
    __log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'log'), 'log', '__AbsentNamespace0_reportType_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 159, 12), )

    
    log = property(__log.value, __log.set, None, None)

    
    # Element message-log uses Python identifier message_log
    __message_log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'message-log'), 'message_log', '__AbsentNamespace0_reportType_message_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 160, 12), )

    
    message_log = property(__message_log.value, __message_log.set, None, None)

    
    # Element error-log uses Python identifier error_log
    __error_log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'error-log'), 'error_log', '__AbsentNamespace0_reportType_error_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 161, 12), )

    
    error_log = property(__error_log.value, __error_log.set, None, None)

    
    # Element duration-log.disable uses Python identifier duration_log_disable
    __duration_log_disable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'duration-log.disable'), 'duration_log_disable', '__AbsentNamespace0_reportType_duration_log_disable', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 162, 12), )

    
    duration_log_disable = property(__duration_log_disable.value, __duration_log_disable.set, None, None)

    
    # Element duration-log.statistics uses Python identifier duration_log_statistics
    __duration_log_statistics = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'duration-log.statistics'), 'duration_log_statistics', '__AbsentNamespace0_reportType_duration_log_statistics', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 163, 12), )

    
    duration_log_statistics = property(__duration_log_statistics.value, __duration_log_statistics.set, None, None)

    
    # Element no-step-log uses Python identifier no_step_log
    __no_step_log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-step-log'), 'no_step_log', '__AbsentNamespace0_reportType_no_step_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 164, 12), )

    
    no_step_log = property(__no_step_log.value, __no_step_log.set, None, None)

    _ElementMap.update({
        __verbose.name() : __verbose,
        __print_options.name() : __print_options,
        __help.name() : __help,
        __version.name() : __version,
        __xml_validation.name() : __xml_validation,
        __xml_validation_net.name() : __xml_validation_net,
        __no_warnings.name() : __no_warnings,
        __log.name() : __log,
        __message_log.name() : __message_log,
        __error_log.name() : __error_log,
        __duration_log_disable.name() : __duration_log_disable,
        __duration_log_statistics.name() : __duration_log_statistics,
        __no_step_log.name() : __no_step_log
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.reportType = reportType
Namespace.addCategoryObject('typeBinding', 'reportType', reportType)


# Complex type emissionsType with content type ELEMENT_ONLY
class emissionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type emissionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'emissionsType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 168, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element phemlight-path uses Python identifier phemlight_path
    __phemlight_path = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'phemlight-path'), 'phemlight_path', '__AbsentNamespace0_emissionsType_phemlight_path', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 170, 12), )

    
    phemlight_path = property(__phemlight_path.value, __phemlight_path.set, None, None)

    
    # Element device.emissions.probability uses Python identifier device_emissions_probability
    __device_emissions_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.emissions.probability'), 'device_emissions_probability', '__AbsentNamespace0_emissionsType_device_emissions_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 171, 12), )

    
    device_emissions_probability = property(__device_emissions_probability.value, __device_emissions_probability.set, None, None)

    
    # Element device.emissions.explicit uses Python identifier device_emissions_explicit
    __device_emissions_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.emissions.explicit'), 'device_emissions_explicit', '__AbsentNamespace0_emissionsType_device_emissions_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 172, 12), )

    
    device_emissions_explicit = property(__device_emissions_explicit.value, __device_emissions_explicit.set, None, None)

    
    # Element device.emissions.deterministic uses Python identifier device_emissions_deterministic
    __device_emissions_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.emissions.deterministic'), 'device_emissions_deterministic', '__AbsentNamespace0_emissionsType_device_emissions_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 173, 12), )

    
    device_emissions_deterministic = property(__device_emissions_deterministic.value, __device_emissions_deterministic.set, None, None)

    _ElementMap.update({
        __phemlight_path.name() : __phemlight_path,
        __device_emissions_probability.name() : __device_emissions_probability,
        __device_emissions_explicit.name() : __device_emissions_explicit,
        __device_emissions_deterministic.name() : __device_emissions_deterministic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.emissionsType = emissionsType
Namespace.addCategoryObject('typeBinding', 'emissionsType', emissionsType)


# Complex type communicationType with content type ELEMENT_ONLY
class communicationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type communicationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'communicationType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 177, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element device.btreceiver.probability uses Python identifier device_btreceiver_probability
    __device_btreceiver_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btreceiver.probability'), 'device_btreceiver_probability', '__AbsentNamespace0_communicationType_device_btreceiver_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 179, 12), )

    
    device_btreceiver_probability = property(__device_btreceiver_probability.value, __device_btreceiver_probability.set, None, None)

    
    # Element device.btreceiver.explicit uses Python identifier device_btreceiver_explicit
    __device_btreceiver_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btreceiver.explicit'), 'device_btreceiver_explicit', '__AbsentNamespace0_communicationType_device_btreceiver_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 180, 12), )

    
    device_btreceiver_explicit = property(__device_btreceiver_explicit.value, __device_btreceiver_explicit.set, None, None)

    
    # Element device.btreceiver.deterministic uses Python identifier device_btreceiver_deterministic
    __device_btreceiver_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btreceiver.deterministic'), 'device_btreceiver_deterministic', '__AbsentNamespace0_communicationType_device_btreceiver_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 181, 12), )

    
    device_btreceiver_deterministic = property(__device_btreceiver_deterministic.value, __device_btreceiver_deterministic.set, None, None)

    
    # Element device.btreceiver.range uses Python identifier device_btreceiver_range
    __device_btreceiver_range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btreceiver.range'), 'device_btreceiver_range', '__AbsentNamespace0_communicationType_device_btreceiver_range', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 182, 12), )

    
    device_btreceiver_range = property(__device_btreceiver_range.value, __device_btreceiver_range.set, None, None)

    
    # Element device.btreceiver.all-recognitions uses Python identifier device_btreceiver_all_recognitions
    __device_btreceiver_all_recognitions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btreceiver.all-recognitions'), 'device_btreceiver_all_recognitions', '__AbsentNamespace0_communicationType_device_btreceiver_all_recognitions', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 183, 12), )

    
    device_btreceiver_all_recognitions = property(__device_btreceiver_all_recognitions.value, __device_btreceiver_all_recognitions.set, None, None)

    
    # Element device.btreceiver.offtime uses Python identifier device_btreceiver_offtime
    __device_btreceiver_offtime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btreceiver.offtime'), 'device_btreceiver_offtime', '__AbsentNamespace0_communicationType_device_btreceiver_offtime', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 184, 12), )

    
    device_btreceiver_offtime = property(__device_btreceiver_offtime.value, __device_btreceiver_offtime.set, None, None)

    
    # Element device.btsender.probability uses Python identifier device_btsender_probability
    __device_btsender_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btsender.probability'), 'device_btsender_probability', '__AbsentNamespace0_communicationType_device_btsender_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 185, 12), )

    
    device_btsender_probability = property(__device_btsender_probability.value, __device_btsender_probability.set, None, None)

    
    # Element device.btsender.explicit uses Python identifier device_btsender_explicit
    __device_btsender_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btsender.explicit'), 'device_btsender_explicit', '__AbsentNamespace0_communicationType_device_btsender_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 186, 12), )

    
    device_btsender_explicit = property(__device_btsender_explicit.value, __device_btsender_explicit.set, None, None)

    
    # Element device.btsender.deterministic uses Python identifier device_btsender_deterministic
    __device_btsender_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.btsender.deterministic'), 'device_btsender_deterministic', '__AbsentNamespace0_communicationType_device_btsender_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 187, 12), )

    
    device_btsender_deterministic = property(__device_btsender_deterministic.value, __device_btsender_deterministic.set, None, None)

    _ElementMap.update({
        __device_btreceiver_probability.name() : __device_btreceiver_probability,
        __device_btreceiver_explicit.name() : __device_btreceiver_explicit,
        __device_btreceiver_deterministic.name() : __device_btreceiver_deterministic,
        __device_btreceiver_range.name() : __device_btreceiver_range,
        __device_btreceiver_all_recognitions.name() : __device_btreceiver_all_recognitions,
        __device_btreceiver_offtime.name() : __device_btreceiver_offtime,
        __device_btsender_probability.name() : __device_btsender_probability,
        __device_btsender_explicit.name() : __device_btsender_explicit,
        __device_btsender_deterministic.name() : __device_btsender_deterministic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.communicationType = communicationType
Namespace.addCategoryObject('typeBinding', 'communicationType', communicationType)


# Complex type batteryType with content type ELEMENT_ONLY
class batteryType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type batteryType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'batteryType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 191, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element device.battery.probability uses Python identifier device_battery_probability
    __device_battery_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.battery.probability'), 'device_battery_probability', '__AbsentNamespace0_batteryType_device_battery_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 193, 12), )

    
    device_battery_probability = property(__device_battery_probability.value, __device_battery_probability.set, None, None)

    
    # Element device.battery.explicit uses Python identifier device_battery_explicit
    __device_battery_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.battery.explicit'), 'device_battery_explicit', '__AbsentNamespace0_batteryType_device_battery_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 194, 12), )

    
    device_battery_explicit = property(__device_battery_explicit.value, __device_battery_explicit.set, None, None)

    
    # Element device.battery.deterministic uses Python identifier device_battery_deterministic
    __device_battery_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.battery.deterministic'), 'device_battery_deterministic', '__AbsentNamespace0_batteryType_device_battery_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 195, 12), )

    
    device_battery_deterministic = property(__device_battery_deterministic.value, __device_battery_deterministic.set, None, None)

    _ElementMap.update({
        __device_battery_probability.name() : __device_battery_probability,
        __device_battery_explicit.name() : __device_battery_explicit,
        __device_battery_deterministic.name() : __device_battery_deterministic
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.batteryType = batteryType
Namespace.addCategoryObject('typeBinding', 'batteryType', batteryType)


# Complex type example_deviceType with content type ELEMENT_ONLY
class example_deviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type example_deviceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'example_deviceType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 199, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element device.example.probability uses Python identifier device_example_probability
    __device_example_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.example.probability'), 'device_example_probability', '__AbsentNamespace0_example_deviceType_device_example_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 201, 12), )

    
    device_example_probability = property(__device_example_probability.value, __device_example_probability.set, None, None)

    
    # Element device.example.explicit uses Python identifier device_example_explicit
    __device_example_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.example.explicit'), 'device_example_explicit', '__AbsentNamespace0_example_deviceType_device_example_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 202, 12), )

    
    device_example_explicit = property(__device_example_explicit.value, __device_example_explicit.set, None, None)

    
    # Element device.example.deterministic uses Python identifier device_example_deterministic
    __device_example_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.example.deterministic'), 'device_example_deterministic', '__AbsentNamespace0_example_deviceType_device_example_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 203, 12), )

    
    device_example_deterministic = property(__device_example_deterministic.value, __device_example_deterministic.set, None, None)

    
    # Element device.example.parameter uses Python identifier device_example_parameter
    __device_example_parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.example.parameter'), 'device_example_parameter', '__AbsentNamespace0_example_deviceType_device_example_parameter', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 204, 12), )

    
    device_example_parameter = property(__device_example_parameter.value, __device_example_parameter.set, None, None)

    _ElementMap.update({
        __device_example_probability.name() : __device_example_probability,
        __device_example_explicit.name() : __device_example_explicit,
        __device_example_deterministic.name() : __device_example_deterministic,
        __device_example_parameter.name() : __device_example_parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.example_deviceType = example_deviceType
Namespace.addCategoryObject('typeBinding', 'example_deviceType', example_deviceType)


# Complex type ssm_deviceType with content type ELEMENT_ONLY
class ssm_deviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ssm_deviceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ssm_deviceType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 208, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element device.ssm.probability uses Python identifier device_ssm_probability
    __device_ssm_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.probability'), 'device_ssm_probability', '__AbsentNamespace0_ssm_deviceType_device_ssm_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 210, 12), )

    
    device_ssm_probability = property(__device_ssm_probability.value, __device_ssm_probability.set, None, None)

    
    # Element device.ssm.explicit uses Python identifier device_ssm_explicit
    __device_ssm_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.explicit'), 'device_ssm_explicit', '__AbsentNamespace0_ssm_deviceType_device_ssm_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 211, 12), )

    
    device_ssm_explicit = property(__device_ssm_explicit.value, __device_ssm_explicit.set, None, None)

    
    # Element device.ssm.deterministic uses Python identifier device_ssm_deterministic
    __device_ssm_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.deterministic'), 'device_ssm_deterministic', '__AbsentNamespace0_ssm_deviceType_device_ssm_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 212, 12), )

    
    device_ssm_deterministic = property(__device_ssm_deterministic.value, __device_ssm_deterministic.set, None, None)

    
    # Element device.ssm.measures uses Python identifier device_ssm_measures
    __device_ssm_measures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.measures'), 'device_ssm_measures', '__AbsentNamespace0_ssm_deviceType_device_ssm_measures', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 213, 12), )

    
    device_ssm_measures = property(__device_ssm_measures.value, __device_ssm_measures.set, None, None)

    
    # Element device.ssm.thresholds uses Python identifier device_ssm_thresholds
    __device_ssm_thresholds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.thresholds'), 'device_ssm_thresholds', '__AbsentNamespace0_ssm_deviceType_device_ssm_thresholds', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 214, 12), )

    
    device_ssm_thresholds = property(__device_ssm_thresholds.value, __device_ssm_thresholds.set, None, None)

    
    # Element device.ssm.trajectories uses Python identifier device_ssm_trajectories
    __device_ssm_trajectories = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.trajectories'), 'device_ssm_trajectories', '__AbsentNamespace0_ssm_deviceType_device_ssm_trajectories', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 215, 12), )

    
    device_ssm_trajectories = property(__device_ssm_trajectories.value, __device_ssm_trajectories.set, None, None)

    
    # Element device.ssm.range uses Python identifier device_ssm_range
    __device_ssm_range = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.range'), 'device_ssm_range', '__AbsentNamespace0_ssm_deviceType_device_ssm_range', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 216, 12), )

    
    device_ssm_range = property(__device_ssm_range.value, __device_ssm_range.set, None, None)

    
    # Element device.ssm.extratime uses Python identifier device_ssm_extratime
    __device_ssm_extratime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.extratime'), 'device_ssm_extratime', '__AbsentNamespace0_ssm_deviceType_device_ssm_extratime', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 217, 12), )

    
    device_ssm_extratime = property(__device_ssm_extratime.value, __device_ssm_extratime.set, None, None)

    
    # Element device.ssm.geo uses Python identifier device_ssm_geo
    __device_ssm_geo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.ssm.geo'), 'device_ssm_geo', '__AbsentNamespace0_ssm_deviceType_device_ssm_geo', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 218, 12), )

    
    device_ssm_geo = property(__device_ssm_geo.value, __device_ssm_geo.set, None, None)

    _ElementMap.update({
        __device_ssm_probability.name() : __device_ssm_probability,
        __device_ssm_explicit.name() : __device_ssm_explicit,
        __device_ssm_deterministic.name() : __device_ssm_deterministic,
        __device_ssm_measures.name() : __device_ssm_measures,
        __device_ssm_thresholds.name() : __device_ssm_thresholds,
        __device_ssm_trajectories.name() : __device_ssm_trajectories,
        __device_ssm_range.name() : __device_ssm_range,
        __device_ssm_extratime.name() : __device_ssm_extratime,
        __device_ssm_geo.name() : __device_ssm_geo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ssm_deviceType = ssm_deviceType
Namespace.addCategoryObject('typeBinding', 'ssm_deviceType', ssm_deviceType)


# Complex type bluelight_deviceType with content type ELEMENT_ONLY
class bluelight_deviceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type bluelight_deviceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'bluelight_deviceType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 222, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element device.bluelight.probability uses Python identifier device_bluelight_probability
    __device_bluelight_probability = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.bluelight.probability'), 'device_bluelight_probability', '__AbsentNamespace0_bluelight_deviceType_device_bluelight_probability', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 224, 12), )

    
    device_bluelight_probability = property(__device_bluelight_probability.value, __device_bluelight_probability.set, None, None)

    
    # Element device.bluelight.explicit uses Python identifier device_bluelight_explicit
    __device_bluelight_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.bluelight.explicit'), 'device_bluelight_explicit', '__AbsentNamespace0_bluelight_deviceType_device_bluelight_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 225, 12), )

    
    device_bluelight_explicit = property(__device_bluelight_explicit.value, __device_bluelight_explicit.set, None, None)

    
    # Element device.bluelight.deterministic uses Python identifier device_bluelight_deterministic
    __device_bluelight_deterministic = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.bluelight.deterministic'), 'device_bluelight_deterministic', '__AbsentNamespace0_bluelight_deviceType_device_bluelight_deterministic', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 226, 12), )

    
    device_bluelight_deterministic = property(__device_bluelight_deterministic.value, __device_bluelight_deterministic.set, None, None)

    
    # Element device.bluelight.parameter uses Python identifier device_bluelight_parameter
    __device_bluelight_parameter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'device.bluelight.parameter'), 'device_bluelight_parameter', '__AbsentNamespace0_bluelight_deviceType_device_bluelight_parameter', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 227, 12), )

    
    device_bluelight_parameter = property(__device_bluelight_parameter.value, __device_bluelight_parameter.set, None, None)

    _ElementMap.update({
        __device_bluelight_probability.name() : __device_bluelight_probability,
        __device_bluelight_explicit.name() : __device_bluelight_explicit,
        __device_bluelight_deterministic.name() : __device_bluelight_deterministic,
        __device_bluelight_parameter.name() : __device_bluelight_parameter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.bluelight_deviceType = bluelight_deviceType
Namespace.addCategoryObject('typeBinding', 'bluelight_deviceType', bluelight_deviceType)


# Complex type traci_serverType with content type ELEMENT_ONLY
class traci_serverType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type traci_serverType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'traci_serverType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 231, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element remote-port uses Python identifier remote_port
    __remote_port = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remote-port'), 'remote_port', '__AbsentNamespace0_traci_serverType_remote_port', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 233, 12), )

    
    remote_port = property(__remote_port.value, __remote_port.set, None, None)

    
    # Element num-clients uses Python identifier num_clients
    __num_clients = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'num-clients'), 'num_clients', '__AbsentNamespace0_traci_serverType_num_clients', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 234, 12), )

    
    num_clients = property(__num_clients.value, __num_clients.set, None, None)

    
    # Element python-script uses Python identifier python_script
    __python_script = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'python-script'), 'python_script', '__AbsentNamespace0_traci_serverType_python_script', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 235, 12), )

    
    python_script = property(__python_script.value, __python_script.set, None, None)

    _ElementMap.update({
        __remote_port.name() : __remote_port,
        __num_clients.name() : __num_clients,
        __python_script.name() : __python_script
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.traci_serverType = traci_serverType
Namespace.addCategoryObject('typeBinding', 'traci_serverType', traci_serverType)


# Complex type mesoscopicType with content type ELEMENT_ONLY
class mesoscopicType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type mesoscopicType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'mesoscopicType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 239, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element mesosim uses Python identifier mesosim
    __mesosim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'mesosim'), 'mesosim', '__AbsentNamespace0_mesoscopicType_mesosim', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 241, 12), )

    
    mesosim = property(__mesosim.value, __mesosim.set, None, None)

    
    # Element meso-edgelength uses Python identifier meso_edgelength
    __meso_edgelength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-edgelength'), 'meso_edgelength', '__AbsentNamespace0_mesoscopicType_meso_edgelength', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 242, 12), )

    
    meso_edgelength = property(__meso_edgelength.value, __meso_edgelength.set, None, None)

    
    # Element meso-tauff uses Python identifier meso_tauff
    __meso_tauff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-tauff'), 'meso_tauff', '__AbsentNamespace0_mesoscopicType_meso_tauff', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 243, 12), )

    
    meso_tauff = property(__meso_tauff.value, __meso_tauff.set, None, None)

    
    # Element meso-taufj uses Python identifier meso_taufj
    __meso_taufj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-taufj'), 'meso_taufj', '__AbsentNamespace0_mesoscopicType_meso_taufj', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 244, 12), )

    
    meso_taufj = property(__meso_taufj.value, __meso_taufj.set, None, None)

    
    # Element meso-taujf uses Python identifier meso_taujf
    __meso_taujf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-taujf'), 'meso_taujf', '__AbsentNamespace0_mesoscopicType_meso_taujf', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 245, 12), )

    
    meso_taujf = property(__meso_taujf.value, __meso_taujf.set, None, None)

    
    # Element meso-taujj uses Python identifier meso_taujj
    __meso_taujj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-taujj'), 'meso_taujj', '__AbsentNamespace0_mesoscopicType_meso_taujj', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 246, 12), )

    
    meso_taujj = property(__meso_taujj.value, __meso_taujj.set, None, None)

    
    # Element meso-jam-threshold uses Python identifier meso_jam_threshold
    __meso_jam_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-jam-threshold'), 'meso_jam_threshold', '__AbsentNamespace0_mesoscopicType_meso_jam_threshold', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 247, 12), )

    
    meso_jam_threshold = property(__meso_jam_threshold.value, __meso_jam_threshold.set, None, None)

    
    # Element meso-multi-queue uses Python identifier meso_multi_queue
    __meso_multi_queue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-multi-queue'), 'meso_multi_queue', '__AbsentNamespace0_mesoscopicType_meso_multi_queue', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 248, 12), )

    
    meso_multi_queue = property(__meso_multi_queue.value, __meso_multi_queue.set, None, None)

    
    # Element meso-junction-control uses Python identifier meso_junction_control
    __meso_junction_control = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-junction-control'), 'meso_junction_control', '__AbsentNamespace0_mesoscopicType_meso_junction_control', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 249, 12), )

    
    meso_junction_control = property(__meso_junction_control.value, __meso_junction_control.set, None, None)

    
    # Element meso-junction-control.limited uses Python identifier meso_junction_control_limited
    __meso_junction_control_limited = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-junction-control.limited'), 'meso_junction_control_limited', '__AbsentNamespace0_mesoscopicType_meso_junction_control_limited', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 250, 12), )

    
    meso_junction_control_limited = property(__meso_junction_control_limited.value, __meso_junction_control_limited.set, None, None)

    
    # Element meso-tls-penalty uses Python identifier meso_tls_penalty
    __meso_tls_penalty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-tls-penalty'), 'meso_tls_penalty', '__AbsentNamespace0_mesoscopicType_meso_tls_penalty', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 251, 12), )

    
    meso_tls_penalty = property(__meso_tls_penalty.value, __meso_tls_penalty.set, None, None)

    
    # Element meso-minor-penalty uses Python identifier meso_minor_penalty
    __meso_minor_penalty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-minor-penalty'), 'meso_minor_penalty', '__AbsentNamespace0_mesoscopicType_meso_minor_penalty', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 252, 12), )

    
    meso_minor_penalty = property(__meso_minor_penalty.value, __meso_minor_penalty.set, None, None)

    
    # Element meso-overtaking uses Python identifier meso_overtaking
    __meso_overtaking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-overtaking'), 'meso_overtaking', '__AbsentNamespace0_mesoscopicType_meso_overtaking', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 253, 12), )

    
    meso_overtaking = property(__meso_overtaking.value, __meso_overtaking.set, None, None)

    
    # Element meso-recheck uses Python identifier meso_recheck
    __meso_recheck = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'meso-recheck'), 'meso_recheck', '__AbsentNamespace0_mesoscopicType_meso_recheck', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 254, 12), )

    
    meso_recheck = property(__meso_recheck.value, __meso_recheck.set, None, None)

    _ElementMap.update({
        __mesosim.name() : __mesosim,
        __meso_edgelength.name() : __meso_edgelength,
        __meso_tauff.name() : __meso_tauff,
        __meso_taufj.name() : __meso_taufj,
        __meso_taujf.name() : __meso_taujf,
        __meso_taujj.name() : __meso_taujj,
        __meso_jam_threshold.name() : __meso_jam_threshold,
        __meso_multi_queue.name() : __meso_multi_queue,
        __meso_junction_control.name() : __meso_junction_control,
        __meso_junction_control_limited.name() : __meso_junction_control_limited,
        __meso_tls_penalty.name() : __meso_tls_penalty,
        __meso_minor_penalty.name() : __meso_minor_penalty,
        __meso_overtaking.name() : __meso_overtaking,
        __meso_recheck.name() : __meso_recheck
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.mesoscopicType = mesoscopicType
Namespace.addCategoryObject('typeBinding', 'mesoscopicType', mesoscopicType)


# Complex type random_numberType with content type ELEMENT_ONLY
class random_numberType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type random_numberType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'random_numberType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element random uses Python identifier random
    __random = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'random'), 'random', '__AbsentNamespace0_random_numberType_random', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 260, 12), )

    
    random = property(__random.value, __random.set, None, None)

    
    # Element seed uses Python identifier seed
    __seed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'seed'), 'seed', '__AbsentNamespace0_random_numberType_seed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 261, 12), )

    
    seed = property(__seed.value, __seed.set, None, None)

    _ElementMap.update({
        __random.name() : __random,
        __seed.name() : __seed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.random_numberType = random_numberType
Namespace.addCategoryObject('typeBinding', 'random_numberType', random_numberType)


# Complex type gui_onlyType with content type ELEMENT_ONLY
class gui_onlyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type gui_onlyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'gui_onlyType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 265, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element gui-settings-file uses Python identifier gui_settings_file
    __gui_settings_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gui-settings-file'), 'gui_settings_file', '__AbsentNamespace0_gui_onlyType_gui_settings_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 267, 12), )

    
    gui_settings_file = property(__gui_settings_file.value, __gui_settings_file.set, None, None)

    
    # Element quit-on-end uses Python identifier quit_on_end
    __quit_on_end = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'quit-on-end'), 'quit_on_end', '__AbsentNamespace0_gui_onlyType_quit_on_end', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 268, 12), )

    
    quit_on_end = property(__quit_on_end.value, __quit_on_end.set, None, None)

    
    # Element game uses Python identifier game
    __game = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'game'), 'game', '__AbsentNamespace0_gui_onlyType_game', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 269, 12), )

    
    game = property(__game.value, __game.set, None, None)

    
    # Element start uses Python identifier start
    __start = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'start'), 'start', '__AbsentNamespace0_gui_onlyType_start', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 270, 12), )

    
    start = property(__start.value, __start.set, None, None)

    
    # Element demo uses Python identifier demo
    __demo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'demo'), 'demo', '__AbsentNamespace0_gui_onlyType_demo', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 271, 12), )

    
    demo = property(__demo.value, __demo.set, None, None)

    
    # Element disable-textures uses Python identifier disable_textures
    __disable_textures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'disable-textures'), 'disable_textures', '__AbsentNamespace0_gui_onlyType_disable_textures', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 272, 12), )

    
    disable_textures = property(__disable_textures.value, __disable_textures.set, None, None)

    
    # Element window-size uses Python identifier window_size
    __window_size = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'window-size'), 'window_size', '__AbsentNamespace0_gui_onlyType_window_size', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 273, 12), )

    
    window_size = property(__window_size.value, __window_size.set, None, None)

    
    # Element window-pos uses Python identifier window_pos
    __window_pos = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'window-pos'), 'window_pos', '__AbsentNamespace0_gui_onlyType_window_pos', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 274, 12), )

    
    window_pos = property(__window_pos.value, __window_pos.set, None, None)

    
    # Element osg-view uses Python identifier osg_view
    __osg_view = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osg-view'), 'osg_view', '__AbsentNamespace0_gui_onlyType_osg_view', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 275, 12), )

    
    osg_view = property(__osg_view.value, __osg_view.set, None, None)

    
    # Element tracker-interval uses Python identifier tracker_interval
    __tracker_interval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tracker-interval'), 'tracker_interval', '__AbsentNamespace0_gui_onlyType_tracker_interval', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 276, 12), )

    
    tracker_interval = property(__tracker_interval.value, __tracker_interval.set, None, None)

    
    # Element gui-testing uses Python identifier gui_testing
    __gui_testing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gui-testing'), 'gui_testing', '__AbsentNamespace0_gui_onlyType_gui_testing', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 277, 12), )

    
    gui_testing = property(__gui_testing.value, __gui_testing.set, None, None)

    
    # Element gui-testing-debug uses Python identifier gui_testing_debug
    __gui_testing_debug = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'gui-testing-debug'), 'gui_testing_debug', '__AbsentNamespace0_gui_onlyType_gui_testing_debug', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 278, 12), )

    
    gui_testing_debug = property(__gui_testing_debug.value, __gui_testing_debug.set, None, None)

    _ElementMap.update({
        __gui_settings_file.name() : __gui_settings_file,
        __quit_on_end.name() : __quit_on_end,
        __game.name() : __game,
        __start.name() : __start,
        __demo.name() : __demo,
        __disable_textures.name() : __disable_textures,
        __window_size.name() : __window_size,
        __window_pos.name() : __window_pos,
        __osg_view.name() : __osg_view,
        __tracker_interval.name() : __tracker_interval,
        __gui_testing.name() : __gui_testing,
        __gui_testing_debug.name() : __gui_testing_debug
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.gui_onlyType = gui_onlyType
Namespace.addCategoryObject('typeBinding', 'gui_onlyType', gui_onlyType)


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


configuration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'configuration'), configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', configuration.name().localName(), configuration)



configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input'), inputType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 10, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output'), outputType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 11, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time'), timeType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 12, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processing'), processingType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 13, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routing'), routingType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 14, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'report'), reportType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 15, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emissions'), emissionsType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 16, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'communication'), communicationType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 17, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'battery'), batteryType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 18, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'example_device'), example_deviceType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 19, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ssm_device'), ssm_deviceType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 20, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bluelight_device'), bluelight_deviceType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 21, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'traci_server'), traci_serverType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 22, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mesoscopic'), mesoscopicType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 23, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'random_number'), random_numberType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 24, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gui_only'), gui_onlyType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 25, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 10, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'input')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 10, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 11, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 11, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 12, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 12, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 13, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'processing')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 13, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 14, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'routing')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 14, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 15, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'report')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 15, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 16, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'emissions')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 16, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 17, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'communication')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 17, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 18, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'battery')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 18, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 19, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'example_device')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 19, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 20, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'ssm_device')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 20, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 21, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'bluelight_device')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 21, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 22, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'traci_server')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 22, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 23, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'mesoscopic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 23, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 24, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'random_number')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 24, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 25, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'gui_only')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 25, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 10, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 11, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 12, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 13, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 14, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 15, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 16, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 17, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 18, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 19, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 20, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 21, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 22, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 23, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 24, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 25, 12))
    counters.add(cc_15)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 9, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
configurationType._Automaton = _BuildAutomaton()




inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net-file'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 31, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 32, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'additional-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 33, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weight-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 34, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weight-attribute'), strOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 35, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'load-state'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 36, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'load-state.offset'), timeOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 37, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'load-state.remove-vehicles'), strOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 38, 12)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 31, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'net-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 31, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 32, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'route-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 32, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 33, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'additional-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 33, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 34, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'weight-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 34, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 35, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'weight-attribute')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 35, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'load-state')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 36, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 37, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'load-state.offset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 37, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 38, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'load-state.remove-vehicles')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 38, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 31, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 32, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 33, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 34, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 35, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 36, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 37, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 38, 12))
    counters.add(cc_7)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 30, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
inputType._Automaton = _BuildAutomaton_17()




outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-prefix'), strOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 44, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'precision'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 45, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'precision.geo'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 46, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'netstate-dump'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 47, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'netstate-dump.empty-edges'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 48, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'netstate-dump.precision'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 49, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emission-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 50, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'emission-output.precision'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 51, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'battery-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 52, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'battery-output.precision'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 53, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'chargingstations-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 54, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fcd-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 55, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fcd-output.geo'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 56, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'fcd-output.signals'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 57, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'full-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 58, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'queue-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 59, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vtk-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 60, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'amitran-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 61, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'summary-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 62, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tripinfo-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 63, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tripinfo-output.write-unfinished'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 64, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 65, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.exit-times'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 66, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.last-route'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 67, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.sorted'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 68, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.dua'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 69, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.intended-depart'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 70, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.route-length'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 71, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vehroute-output.write-unfinished'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 72, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'link-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 73, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'bt-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 74, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lanechange-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 75, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'stop-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 76, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'save-state.times'), intArrayOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 77, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'save-state.period'), timeOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 78, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'save-state.prefix'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 79, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'save-state.suffix'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 80, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'save-state.files'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 81, 12)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 44, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'output-prefix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 44, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 45, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'precision')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 45, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 46, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'precision.geo')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 46, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 47, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'netstate-dump')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 47, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 48, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'netstate-dump.empty-edges')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 49, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'netstate-dump.precision')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 49, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 50, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'emission-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 50, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 51, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'emission-output.precision')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 51, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 52, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'battery-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 52, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 53, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'battery-output.precision')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 53, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 54, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'chargingstations-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 54, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 55, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'fcd-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 55, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 56, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'fcd-output.geo')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 56, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 57, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'fcd-output.signals')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 57, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 58, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'full-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 58, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 59, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'queue-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 59, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 60, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vtk-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 60, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 61, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'amitran-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 61, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 62, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'summary-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 62, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 63, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'tripinfo-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 63, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 64, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'tripinfo-output.write-unfinished')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 64, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 65, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 65, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 66, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.exit-times')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 66, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 67, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.last-route')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 67, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 68, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.sorted')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 68, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 69, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.dua')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 69, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 70, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.intended-depart')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 70, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 71, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.route-length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 71, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 72, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vehroute-output.write-unfinished')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 72, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 73, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'link-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 73, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 74, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'bt-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 74, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 75, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'lanechange-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 75, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 76, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'stop-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 76, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 77, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'save-state.times')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 77, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 78, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'save-state.period')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 78, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 79, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'save-state.prefix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 79, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 80, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'save-state.suffix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 80, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 81, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'save-state.files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 81, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 44, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 45, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 46, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 47, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 48, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 49, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 50, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 51, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 52, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 53, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 54, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 55, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 56, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 57, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 58, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 59, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 60, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 61, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 62, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 63, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 64, 12))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 65, 12))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 66, 12))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 67, 12))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 68, 12))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 69, 12))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 70, 12))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 71, 12))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 72, 12))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 73, 12))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 74, 12))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 75, 12))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 76, 12))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 77, 12))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 78, 12))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 79, 12))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 80, 12))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 81, 12))
    counters.add(cc_37)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_27())
    sub_automata.append(_BuildAutomaton_28())
    sub_automata.append(_BuildAutomaton_29())
    sub_automata.append(_BuildAutomaton_30())
    sub_automata.append(_BuildAutomaton_31())
    sub_automata.append(_BuildAutomaton_32())
    sub_automata.append(_BuildAutomaton_33())
    sub_automata.append(_BuildAutomaton_34())
    sub_automata.append(_BuildAutomaton_35())
    sub_automata.append(_BuildAutomaton_36())
    sub_automata.append(_BuildAutomaton_37())
    sub_automata.append(_BuildAutomaton_38())
    sub_automata.append(_BuildAutomaton_39())
    sub_automata.append(_BuildAutomaton_40())
    sub_automata.append(_BuildAutomaton_41())
    sub_automata.append(_BuildAutomaton_42())
    sub_automata.append(_BuildAutomaton_43())
    sub_automata.append(_BuildAutomaton_44())
    sub_automata.append(_BuildAutomaton_45())
    sub_automata.append(_BuildAutomaton_46())
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    sub_automata.append(_BuildAutomaton_49())
    sub_automata.append(_BuildAutomaton_50())
    sub_automata.append(_BuildAutomaton_51())
    sub_automata.append(_BuildAutomaton_52())
    sub_automata.append(_BuildAutomaton_53())
    sub_automata.append(_BuildAutomaton_54())
    sub_automata.append(_BuildAutomaton_55())
    sub_automata.append(_BuildAutomaton_56())
    sub_automata.append(_BuildAutomaton_57())
    sub_automata.append(_BuildAutomaton_58())
    sub_automata.append(_BuildAutomaton_59())
    sub_automata.append(_BuildAutomaton_60())
    sub_automata.append(_BuildAutomaton_61())
    sub_automata.append(_BuildAutomaton_62())
    sub_automata.append(_BuildAutomaton_63())
    sub_automata.append(_BuildAutomaton_64())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 43, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
outputType._Automaton = _BuildAutomaton_26()




timeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'begin'), timeOptionType, scope=timeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 87, 12)))

timeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'end'), timeOptionType, scope=timeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 88, 12)))

timeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step-length'), timeOptionType, scope=timeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 89, 12)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 87, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(timeType._UseForTag(pyxb.namespace.ExpandedName(None, 'begin')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 87, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 88, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(timeType._UseForTag(pyxb.namespace.ExpandedName(None, 'end')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 88, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 89, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(timeType._UseForTag(pyxb.namespace.ExpandedName(None, 'step-length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 89, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 87, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 88, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 89, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_66())
    sub_automata.append(_BuildAutomaton_67())
    sub_automata.append(_BuildAutomaton_68())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 86, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
timeType._Automaton = _BuildAutomaton_65()




processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'step-method.ballistic'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 95, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.action-step-length'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 96, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lateral-resolution'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 97, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'carfollow.model'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 98, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'route-steps'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 99, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-internal-links'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 100, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore-junction-blocker'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 101, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore-route-errors'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 102, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore-accidents'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 103, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collision.action'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 104, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collision.stoptime'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 105, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'collision.check-junctions'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 106, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max-num-vehicles'), intOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 107, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max-num-teleports'), intOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 108, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'scale'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 109, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time-to-teleport'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 110, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time-to-teleport.highways'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 111, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'waiting-time-memory'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 112, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max-depart-delay'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 113, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sloppy-insert'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 114, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'eager-insert'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 115, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'random-depart-offset'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 116, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lanechange.duration'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 117, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lanechange.overtake-right'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 118, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.all-off'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 119, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'time-to-impatience'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 120, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pedestrian.model'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 121, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.stripe-width'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 122, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.dawdling'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 123, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.jamtime'), timeOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 124, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pedestrian.remote.address'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 125, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'astar.landmark-distances'), fileOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 126, 12)))

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 95, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'step-method.ballistic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 95, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 96, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.action-step-length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 96, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 97, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'lateral-resolution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 97, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 98, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'carfollow.model')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 98, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 99, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'route-steps')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 99, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 100, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-internal-links')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 100, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 101, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore-junction-blocker')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 101, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 102, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore-route-errors')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 102, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 103, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore-accidents')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 103, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 104, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'collision.action')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 104, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 105, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'collision.stoptime')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 105, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 106, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'collision.check-junctions')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 106, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 107, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'max-num-vehicles')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 107, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 108, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'max-num-teleports')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 108, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 109, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'scale')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 109, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 110, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'time-to-teleport')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 110, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 111, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'time-to-teleport.highways')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 111, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 112, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'waiting-time-memory')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 112, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 113, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'max-depart-delay')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 113, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 114, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'sloppy-insert')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 114, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 115, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'eager-insert')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 115, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 116, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'random-depart-offset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 116, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 117, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'lanechange.duration')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 117, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 118, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'lanechange.overtake-right')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 118, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 119, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.all-off')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 119, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 120, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'time-to-impatience')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 120, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 121, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'pedestrian.model')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 121, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 122, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.stripe-width')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 122, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 123, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.dawdling')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 123, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 124, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'pedestrian.striping.jamtime')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 124, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_100 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 125, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'pedestrian.remote.address')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 125, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_101 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 126, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'astar.landmark-distances')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 126, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 95, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 96, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 97, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 98, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 99, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 100, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 101, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 102, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 103, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 104, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 105, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 106, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 107, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 108, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 109, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 110, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 111, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 112, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 113, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 114, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 115, 12))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 116, 12))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 117, 12))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 118, 12))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 119, 12))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 120, 12))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 121, 12))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 122, 12))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 123, 12))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 124, 12))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 125, 12))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 126, 12))
    counters.add(cc_31)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_70())
    sub_automata.append(_BuildAutomaton_71())
    sub_automata.append(_BuildAutomaton_72())
    sub_automata.append(_BuildAutomaton_73())
    sub_automata.append(_BuildAutomaton_74())
    sub_automata.append(_BuildAutomaton_75())
    sub_automata.append(_BuildAutomaton_76())
    sub_automata.append(_BuildAutomaton_77())
    sub_automata.append(_BuildAutomaton_78())
    sub_automata.append(_BuildAutomaton_79())
    sub_automata.append(_BuildAutomaton_80())
    sub_automata.append(_BuildAutomaton_81())
    sub_automata.append(_BuildAutomaton_82())
    sub_automata.append(_BuildAutomaton_83())
    sub_automata.append(_BuildAutomaton_84())
    sub_automata.append(_BuildAutomaton_85())
    sub_automata.append(_BuildAutomaton_86())
    sub_automata.append(_BuildAutomaton_87())
    sub_automata.append(_BuildAutomaton_88())
    sub_automata.append(_BuildAutomaton_89())
    sub_automata.append(_BuildAutomaton_90())
    sub_automata.append(_BuildAutomaton_91())
    sub_automata.append(_BuildAutomaton_92())
    sub_automata.append(_BuildAutomaton_93())
    sub_automata.append(_BuildAutomaton_94())
    sub_automata.append(_BuildAutomaton_95())
    sub_automata.append(_BuildAutomaton_96())
    sub_automata.append(_BuildAutomaton_97())
    sub_automata.append(_BuildAutomaton_98())
    sub_automata.append(_BuildAutomaton_99())
    sub_automata.append(_BuildAutomaton_100())
    sub_automata.append(_BuildAutomaton_101())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 94, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
processingType._Automaton = _BuildAutomaton_69()




routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'routing-algorithm'), strOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 132, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'weights.random-factor'), floatOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 133, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'astar.all-distances'), fileOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 134, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.probability'), floatOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 135, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.explicit'), strOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 136, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.deterministic'), boolOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 137, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.period'), timeOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 138, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.pre-period'), timeOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 139, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-weight'), floatOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 140, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-steps'), intOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 141, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-interval'), timeOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 142, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.with-taz'), boolOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 143, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.init-with-loaded-weights'), boolOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 144, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.threads'), intOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 145, 12)))

routingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.rerouting.output'), fileOptionType, scope=routingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 146, 12)))

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 132, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'routing-algorithm')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 132, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_104 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 133, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'weights.random-factor')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 133, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_105 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 134, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'astar.all-distances')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 134, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_106 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 135, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 135, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 136, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 136, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_108 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_108
    del _BuildAutomaton_108
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 137, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 137, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_109 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_109
    del _BuildAutomaton_109
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 138, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.period')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 138, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_110 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_110
    del _BuildAutomaton_110
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 139, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.pre-period')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 139, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_111 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 140, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-weight')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 140, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_112 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_112
    del _BuildAutomaton_112
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 141, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-steps')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 141, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_113 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_113
    del _BuildAutomaton_113
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 142, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.adaptation-interval')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 142, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_114 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_114
    del _BuildAutomaton_114
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 143, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.with-taz')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 143, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_115 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_115
    del _BuildAutomaton_115
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 144, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.init-with-loaded-weights')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 144, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_116 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_116
    del _BuildAutomaton_116
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 145, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.threads')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 145, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_117 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_117
    del _BuildAutomaton_117
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 146, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(routingType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.rerouting.output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 146, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 132, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 133, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 134, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 135, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 136, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 137, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 138, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 139, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 140, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 141, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 142, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 143, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 144, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 145, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 146, 12))
    counters.add(cc_14)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_103())
    sub_automata.append(_BuildAutomaton_104())
    sub_automata.append(_BuildAutomaton_105())
    sub_automata.append(_BuildAutomaton_106())
    sub_automata.append(_BuildAutomaton_107())
    sub_automata.append(_BuildAutomaton_108())
    sub_automata.append(_BuildAutomaton_109())
    sub_automata.append(_BuildAutomaton_110())
    sub_automata.append(_BuildAutomaton_111())
    sub_automata.append(_BuildAutomaton_112())
    sub_automata.append(_BuildAutomaton_113())
    sub_automata.append(_BuildAutomaton_114())
    sub_automata.append(_BuildAutomaton_115())
    sub_automata.append(_BuildAutomaton_116())
    sub_automata.append(_BuildAutomaton_117())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 131, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
routingType._Automaton = _BuildAutomaton_102()




reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'verbose'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 152, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'print-options'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 153, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'help'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 154, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 155, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xml-validation'), strOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 156, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xml-validation.net'), strOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 157, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-warnings'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 158, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'log'), fileOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 159, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'message-log'), fileOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 160, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'error-log'), fileOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 161, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'duration-log.disable'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 162, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'duration-log.statistics'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 163, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-step-log'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 164, 12)))

def _BuildAutomaton_119 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_119
    del _BuildAutomaton_119
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 152, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'verbose')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 152, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_120 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_120
    del _BuildAutomaton_120
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 153, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'print-options')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 153, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_121 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_121
    del _BuildAutomaton_121
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 154, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'help')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 154, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_122 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_122
    del _BuildAutomaton_122
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 155, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 155, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_123 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_123
    del _BuildAutomaton_123
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 156, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'xml-validation')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 156, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_124 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_124
    del _BuildAutomaton_124
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 157, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'xml-validation.net')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 157, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_125 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_125
    del _BuildAutomaton_125
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 158, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-warnings')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 158, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_126 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_126
    del _BuildAutomaton_126
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 159, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 159, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_127 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_127
    del _BuildAutomaton_127
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 160, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'message-log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 160, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_128 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_128
    del _BuildAutomaton_128
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 161, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'error-log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 161, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_129 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_129
    del _BuildAutomaton_129
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 162, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'duration-log.disable')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 162, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_130 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_130
    del _BuildAutomaton_130
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 163, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'duration-log.statistics')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 163, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_131 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_131
    del _BuildAutomaton_131
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 164, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-step-log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 164, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_118 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_118
    del _BuildAutomaton_118
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 152, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 153, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 154, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 155, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 156, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 157, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 158, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 159, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 160, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 161, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 162, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 163, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 164, 12))
    counters.add(cc_12)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_119())
    sub_automata.append(_BuildAutomaton_120())
    sub_automata.append(_BuildAutomaton_121())
    sub_automata.append(_BuildAutomaton_122())
    sub_automata.append(_BuildAutomaton_123())
    sub_automata.append(_BuildAutomaton_124())
    sub_automata.append(_BuildAutomaton_125())
    sub_automata.append(_BuildAutomaton_126())
    sub_automata.append(_BuildAutomaton_127())
    sub_automata.append(_BuildAutomaton_128())
    sub_automata.append(_BuildAutomaton_129())
    sub_automata.append(_BuildAutomaton_130())
    sub_automata.append(_BuildAutomaton_131())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 151, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
reportType._Automaton = _BuildAutomaton_118()




emissionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phemlight-path'), fileOptionType, scope=emissionsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 170, 12)))

emissionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.emissions.probability'), floatOptionType, scope=emissionsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 171, 12)))

emissionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.emissions.explicit'), strOptionType, scope=emissionsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 172, 12)))

emissionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.emissions.deterministic'), boolOptionType, scope=emissionsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 173, 12)))

def _BuildAutomaton_133 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_133
    del _BuildAutomaton_133
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 170, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(emissionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'phemlight-path')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 170, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_134 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_134
    del _BuildAutomaton_134
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 171, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(emissionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.emissions.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 171, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_135 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_135
    del _BuildAutomaton_135
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 172, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(emissionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.emissions.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 172, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_136 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_136
    del _BuildAutomaton_136
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 173, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(emissionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.emissions.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_132 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_132
    del _BuildAutomaton_132
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 170, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 171, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 172, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 173, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_133())
    sub_automata.append(_BuildAutomaton_134())
    sub_automata.append(_BuildAutomaton_135())
    sub_automata.append(_BuildAutomaton_136())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 169, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
emissionsType._Automaton = _BuildAutomaton_132()




communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btreceiver.probability'), floatOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 179, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btreceiver.explicit'), strOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 180, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btreceiver.deterministic'), boolOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 181, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btreceiver.range'), floatOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 182, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btreceiver.all-recognitions'), boolOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 183, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btreceiver.offtime'), floatOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 184, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btsender.probability'), floatOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 185, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btsender.explicit'), strOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 186, 12)))

communicationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.btsender.deterministic'), boolOptionType, scope=communicationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 187, 12)))

def _BuildAutomaton_138 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_138
    del _BuildAutomaton_138
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 179, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btreceiver.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 179, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_139 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_139
    del _BuildAutomaton_139
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 180, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btreceiver.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 180, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_140 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_140
    del _BuildAutomaton_140
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 181, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btreceiver.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 181, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_141 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_141
    del _BuildAutomaton_141
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 182, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btreceiver.range')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 182, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_142 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_142
    del _BuildAutomaton_142
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 183, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btreceiver.all-recognitions')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 183, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_143 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_143
    del _BuildAutomaton_143
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 184, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btreceiver.offtime')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 184, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_144 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_144
    del _BuildAutomaton_144
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 185, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btsender.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 185, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_145 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_145
    del _BuildAutomaton_145
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 186, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btsender.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 186, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_146 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_146
    del _BuildAutomaton_146
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 187, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(communicationType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.btsender.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 187, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_137 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_137
    del _BuildAutomaton_137
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 179, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 180, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 181, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 182, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 183, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 184, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 185, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 186, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 187, 12))
    counters.add(cc_8)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_138())
    sub_automata.append(_BuildAutomaton_139())
    sub_automata.append(_BuildAutomaton_140())
    sub_automata.append(_BuildAutomaton_141())
    sub_automata.append(_BuildAutomaton_142())
    sub_automata.append(_BuildAutomaton_143())
    sub_automata.append(_BuildAutomaton_144())
    sub_automata.append(_BuildAutomaton_145())
    sub_automata.append(_BuildAutomaton_146())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 178, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
communicationType._Automaton = _BuildAutomaton_137()




batteryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.battery.probability'), floatOptionType, scope=batteryType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 193, 12)))

batteryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.battery.explicit'), strOptionType, scope=batteryType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 194, 12)))

batteryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.battery.deterministic'), boolOptionType, scope=batteryType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 195, 12)))

def _BuildAutomaton_148 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_148
    del _BuildAutomaton_148
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 193, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(batteryType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.battery.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 193, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_149 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_149
    del _BuildAutomaton_149
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 194, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(batteryType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.battery.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 194, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_150 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_150
    del _BuildAutomaton_150
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 195, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(batteryType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.battery.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 195, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_147 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_147
    del _BuildAutomaton_147
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 193, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 194, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 195, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_148())
    sub_automata.append(_BuildAutomaton_149())
    sub_automata.append(_BuildAutomaton_150())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 192, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
batteryType._Automaton = _BuildAutomaton_147()




example_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.example.probability'), floatOptionType, scope=example_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 201, 12)))

example_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.example.explicit'), strOptionType, scope=example_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 202, 12)))

example_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.example.deterministic'), boolOptionType, scope=example_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 203, 12)))

example_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.example.parameter'), floatOptionType, scope=example_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 204, 12)))

def _BuildAutomaton_152 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_152
    del _BuildAutomaton_152
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 201, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(example_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.example.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 201, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_153 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_153
    del _BuildAutomaton_153
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 202, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(example_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.example.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 202, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_154 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_154
    del _BuildAutomaton_154
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 203, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(example_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.example.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 203, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_155 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_155
    del _BuildAutomaton_155
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 204, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(example_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.example.parameter')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 204, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_151 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_151
    del _BuildAutomaton_151
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 201, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 202, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 203, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 204, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_152())
    sub_automata.append(_BuildAutomaton_153())
    sub_automata.append(_BuildAutomaton_154())
    sub_automata.append(_BuildAutomaton_155())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 200, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
example_deviceType._Automaton = _BuildAutomaton_151()




ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.probability'), floatOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 210, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.explicit'), strOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 211, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.deterministic'), boolOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 212, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.measures'), strOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 213, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.thresholds'), strOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 214, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.trajectories'), boolOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 215, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.range'), floatOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 216, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.extratime'), floatOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 217, 12)))

ssm_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.ssm.geo'), boolOptionType, scope=ssm_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 218, 12)))

def _BuildAutomaton_157 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_157
    del _BuildAutomaton_157
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 210, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 210, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_158 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_158
    del _BuildAutomaton_158
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 211, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 211, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_159 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_159
    del _BuildAutomaton_159
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 212, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 212, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_160 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_160
    del _BuildAutomaton_160
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 213, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.measures')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 213, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_161 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_161
    del _BuildAutomaton_161
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 214, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.thresholds')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 214, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_162 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_162
    del _BuildAutomaton_162
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 215, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.trajectories')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 215, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_163 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_163
    del _BuildAutomaton_163
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 216, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.range')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 216, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_164 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_164
    del _BuildAutomaton_164
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 217, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.extratime')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 217, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_165 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_165
    del _BuildAutomaton_165
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 218, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ssm_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.ssm.geo')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 218, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_156 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_156
    del _BuildAutomaton_156
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 210, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 211, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 212, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 213, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 214, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 215, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 216, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 217, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 218, 12))
    counters.add(cc_8)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_157())
    sub_automata.append(_BuildAutomaton_158())
    sub_automata.append(_BuildAutomaton_159())
    sub_automata.append(_BuildAutomaton_160())
    sub_automata.append(_BuildAutomaton_161())
    sub_automata.append(_BuildAutomaton_162())
    sub_automata.append(_BuildAutomaton_163())
    sub_automata.append(_BuildAutomaton_164())
    sub_automata.append(_BuildAutomaton_165())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 209, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ssm_deviceType._Automaton = _BuildAutomaton_156()




bluelight_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.bluelight.probability'), floatOptionType, scope=bluelight_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 224, 12)))

bluelight_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.bluelight.explicit'), strOptionType, scope=bluelight_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 225, 12)))

bluelight_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.bluelight.deterministic'), boolOptionType, scope=bluelight_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 226, 12)))

bluelight_deviceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'device.bluelight.parameter'), floatOptionType, scope=bluelight_deviceType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 227, 12)))

def _BuildAutomaton_167 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_167
    del _BuildAutomaton_167
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 224, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bluelight_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.bluelight.probability')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 224, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_168 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_168
    del _BuildAutomaton_168
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 225, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bluelight_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.bluelight.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 225, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_169 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_169
    del _BuildAutomaton_169
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 226, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bluelight_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.bluelight.deterministic')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 226, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_170 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_170
    del _BuildAutomaton_170
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 227, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(bluelight_deviceType._UseForTag(pyxb.namespace.ExpandedName(None, 'device.bluelight.parameter')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 227, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_166 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_166
    del _BuildAutomaton_166
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 224, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 225, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 226, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 227, 12))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_167())
    sub_automata.append(_BuildAutomaton_168())
    sub_automata.append(_BuildAutomaton_169())
    sub_automata.append(_BuildAutomaton_170())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 223, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
bluelight_deviceType._Automaton = _BuildAutomaton_166()




traci_serverType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remote-port'), intOptionType, scope=traci_serverType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 233, 12)))

traci_serverType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'num-clients'), intOptionType, scope=traci_serverType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 234, 12)))

traci_serverType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'python-script'), strOptionType, scope=traci_serverType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 235, 12)))

def _BuildAutomaton_172 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_172
    del _BuildAutomaton_172
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 233, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(traci_serverType._UseForTag(pyxb.namespace.ExpandedName(None, 'remote-port')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 233, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_173 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_173
    del _BuildAutomaton_173
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 234, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(traci_serverType._UseForTag(pyxb.namespace.ExpandedName(None, 'num-clients')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 234, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_174 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_174
    del _BuildAutomaton_174
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 235, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(traci_serverType._UseForTag(pyxb.namespace.ExpandedName(None, 'python-script')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 235, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_171 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_171
    del _BuildAutomaton_171
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 233, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 234, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 235, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_172())
    sub_automata.append(_BuildAutomaton_173())
    sub_automata.append(_BuildAutomaton_174())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 232, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
traci_serverType._Automaton = _BuildAutomaton_171()




mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'mesosim'), boolOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 241, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-edgelength'), floatOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 242, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-tauff'), timeOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 243, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-taufj'), timeOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 244, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-taujf'), timeOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 245, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-taujj'), timeOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 246, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-jam-threshold'), floatOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 247, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-multi-queue'), boolOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 248, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-junction-control'), boolOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 249, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-junction-control.limited'), boolOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 250, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-tls-penalty'), floatOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 251, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-minor-penalty'), timeOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 252, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-overtaking'), boolOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 253, 12)))

mesoscopicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'meso-recheck'), timeOptionType, scope=mesoscopicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 254, 12)))

def _BuildAutomaton_176 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_176
    del _BuildAutomaton_176
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 241, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'mesosim')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 241, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_177 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_177
    del _BuildAutomaton_177
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 242, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-edgelength')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 242, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_178 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_178
    del _BuildAutomaton_178
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 243, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-tauff')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 243, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_179 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_179
    del _BuildAutomaton_179
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 244, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-taufj')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 244, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_180 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_180
    del _BuildAutomaton_180
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 245, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-taujf')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 245, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_181 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_181
    del _BuildAutomaton_181
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 246, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-taujj')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 246, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_182 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_182
    del _BuildAutomaton_182
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 247, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-jam-threshold')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 247, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_183 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_183
    del _BuildAutomaton_183
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 248, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-multi-queue')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 248, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_184 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_184
    del _BuildAutomaton_184
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 249, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-junction-control')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 249, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_185 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_185
    del _BuildAutomaton_185
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 250, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-junction-control.limited')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 250, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_186 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_186
    del _BuildAutomaton_186
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 251, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-tls-penalty')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 251, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_187 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_187
    del _BuildAutomaton_187
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 252, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-minor-penalty')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 252, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_188 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_188
    del _BuildAutomaton_188
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 253, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-overtaking')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 253, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_189 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_189
    del _BuildAutomaton_189
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 254, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(mesoscopicType._UseForTag(pyxb.namespace.ExpandedName(None, 'meso-recheck')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 254, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_175 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_175
    del _BuildAutomaton_175
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 241, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 242, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 243, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 244, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 245, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 246, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 247, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 248, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 249, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 250, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 251, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 252, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 253, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 254, 12))
    counters.add(cc_13)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_176())
    sub_automata.append(_BuildAutomaton_177())
    sub_automata.append(_BuildAutomaton_178())
    sub_automata.append(_BuildAutomaton_179())
    sub_automata.append(_BuildAutomaton_180())
    sub_automata.append(_BuildAutomaton_181())
    sub_automata.append(_BuildAutomaton_182())
    sub_automata.append(_BuildAutomaton_183())
    sub_automata.append(_BuildAutomaton_184())
    sub_automata.append(_BuildAutomaton_185())
    sub_automata.append(_BuildAutomaton_186())
    sub_automata.append(_BuildAutomaton_187())
    sub_automata.append(_BuildAutomaton_188())
    sub_automata.append(_BuildAutomaton_189())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 240, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
mesoscopicType._Automaton = _BuildAutomaton_175()




random_numberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'random'), boolOptionType, scope=random_numberType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 260, 12)))

random_numberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'seed'), intOptionType, scope=random_numberType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 261, 12)))

def _BuildAutomaton_191 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_191
    del _BuildAutomaton_191
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 260, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(random_numberType._UseForTag(pyxb.namespace.ExpandedName(None, 'random')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_192 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_192
    del _BuildAutomaton_192
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 261, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(random_numberType._UseForTag(pyxb.namespace.ExpandedName(None, 'seed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 261, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_190 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_190
    del _BuildAutomaton_190
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 260, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 261, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_191())
    sub_automata.append(_BuildAutomaton_192())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 259, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
random_numberType._Automaton = _BuildAutomaton_190()




gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gui-settings-file'), fileOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 267, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'quit-on-end'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 268, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'game'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 269, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'start'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 270, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'demo'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 271, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'disable-textures'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 272, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'window-size'), strOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 273, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'window-pos'), strOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 274, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osg-view'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 275, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tracker-interval'), floatOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 276, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gui-testing'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 277, 12)))

gui_onlyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'gui-testing-debug'), boolOptionType, scope=gui_onlyType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 278, 12)))

def _BuildAutomaton_194 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_194
    del _BuildAutomaton_194
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 267, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'gui-settings-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 267, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_195 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_195
    del _BuildAutomaton_195
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'quit-on-end')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 268, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_196 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_196
    del _BuildAutomaton_196
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 269, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'game')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 269, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_197 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_197
    del _BuildAutomaton_197
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 270, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'start')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 270, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_198 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_198
    del _BuildAutomaton_198
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 271, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'demo')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 271, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_199 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_199
    del _BuildAutomaton_199
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 272, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'disable-textures')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 272, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_200 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_200
    del _BuildAutomaton_200
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 273, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'window-size')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 273, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_201 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_201
    del _BuildAutomaton_201
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 274, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'window-pos')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 274, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_202 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_202
    del _BuildAutomaton_202
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 275, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'osg-view')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 275, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_203 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_203
    del _BuildAutomaton_203
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 276, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'tracker-interval')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 276, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_204 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_204
    del _BuildAutomaton_204
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 277, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'gui-testing')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 277, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_205 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_205
    del _BuildAutomaton_205
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 278, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(gui_onlyType._UseForTag(pyxb.namespace.ExpandedName(None, 'gui-testing-debug')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 278, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_193 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_193
    del _BuildAutomaton_193
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 267, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 268, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 269, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 270, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 271, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 272, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 273, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 274, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 275, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 276, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 277, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 278, 12))
    counters.add(cc_11)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_194())
    sub_automata.append(_BuildAutomaton_195())
    sub_automata.append(_BuildAutomaton_196())
    sub_automata.append(_BuildAutomaton_197())
    sub_automata.append(_BuildAutomaton_198())
    sub_automata.append(_BuildAutomaton_199())
    sub_automata.append(_BuildAutomaton_200())
    sub_automata.append(_BuildAutomaton_201())
    sub_automata.append(_BuildAutomaton_202())
    sub_automata.append(_BuildAutomaton_203())
    sub_automata.append(_BuildAutomaton_204())
    sub_automata.append(_BuildAutomaton_205())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/sumoConfiguration.xsd', 266, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
gui_onlyType._Automaton = _BuildAutomaton_193()




tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase'), phaseType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12)))

tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12)))

def _BuildAutomaton_206 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_206
    del _BuildAutomaton_206
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
tlLogicType._Automaton = _BuildAutomaton_206()




typeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restriction'), restrictionType, scope=typeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12)))

def _BuildAutomaton_207 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_207
    del _BuildAutomaton_207
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
typeType._Automaton = _BuildAutomaton_207()

