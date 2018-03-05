# ./netconvert_xml.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2018-02-11 21:04:23.732940 by PyXB version 1.2.6 using Python 3.6.3.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:0b03f992-0f99-11e8-8443-186590d9922f')

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
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 8, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element input uses Python identifier input
    __input = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'input'), 'input', '__AbsentNamespace0_configurationType_input', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 10, 12), )

    
    input = property(__input.value, __input.set, None, None)

    
    # Element output uses Python identifier output
    __output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output'), 'output', '__AbsentNamespace0_configurationType_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 11, 12), )

    
    output = property(__output.value, __output.set, None, None)

    
    # Element projection uses Python identifier projection
    __projection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'projection'), 'projection', '__AbsentNamespace0_configurationType_projection', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 12, 12), )

    
    projection = property(__projection.value, __projection.set, None, None)

    
    # Element tls_building uses Python identifier tls_building
    __tls_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls_building'), 'tls_building', '__AbsentNamespace0_configurationType_tls_building', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 13, 12), )

    
    tls_building = property(__tls_building.value, __tls_building.set, None, None)

    
    # Element ramp_guessing uses Python identifier ramp_guessing
    __ramp_guessing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramp_guessing'), 'ramp_guessing', '__AbsentNamespace0_configurationType_ramp_guessing', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 14, 12), )

    
    ramp_guessing = property(__ramp_guessing.value, __ramp_guessing.set, None, None)

    
    # Element edge_removal uses Python identifier edge_removal
    __edge_removal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edge_removal'), 'edge_removal', '__AbsentNamespace0_configurationType_edge_removal', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 15, 12), )

    
    edge_removal = property(__edge_removal.value, __edge_removal.set, None, None)

    
    # Element unregulated_nodes uses Python identifier unregulated_nodes
    __unregulated_nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'unregulated_nodes'), 'unregulated_nodes', '__AbsentNamespace0_configurationType_unregulated_nodes', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 16, 12), )

    
    unregulated_nodes = property(__unregulated_nodes.value, __unregulated_nodes.set, None, None)

    
    # Element processing uses Python identifier processing
    __processing = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'processing'), 'processing', '__AbsentNamespace0_configurationType_processing', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 17, 12), )

    
    processing = property(__processing.value, __processing.set, None, None)

    
    # Element building_defaults uses Python identifier building_defaults
    __building_defaults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_defaults'), 'building_defaults', '__AbsentNamespace0_configurationType_building_defaults', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 18, 12), )

    
    building_defaults = property(__building_defaults.value, __building_defaults.set, None, None)

    
    # Element report uses Python identifier report
    __report = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'report'), 'report', '__AbsentNamespace0_configurationType_report', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 19, 12), )

    
    report = property(__report.value, __report.set, None, None)

    
    # Element random_number uses Python identifier random_number
    __random_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'random_number'), 'random_number', '__AbsentNamespace0_configurationType_random_number', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 20, 12), )

    
    random_number = property(__random_number.value, __random_number.set, None, None)

    _ElementMap.update({
        __input.name() : __input,
        __output.name() : __output,
        __projection.name() : __projection,
        __tls_building.name() : __tls_building,
        __ramp_guessing.name() : __ramp_guessing,
        __edge_removal.name() : __edge_removal,
        __unregulated_nodes.name() : __unregulated_nodes,
        __processing.name() : __processing,
        __building_defaults.name() : __building_defaults,
        __report.name() : __report,
        __random_number.name() : __random_number
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
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element sumo-net-file uses Python identifier sumo_net_file
    __sumo_net_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sumo-net-file'), 'sumo_net_file', '__AbsentNamespace0_inputType_sumo_net_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 26, 12), )

    
    sumo_net_file = property(__sumo_net_file.value, __sumo_net_file.set, None, None)

    
    # Element node-files uses Python identifier node_files
    __node_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'node-files'), 'node_files', '__AbsentNamespace0_inputType_node_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 27, 12), )

    
    node_files = property(__node_files.value, __node_files.set, None, None)

    
    # Element edge-files uses Python identifier edge_files
    __edge_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edge-files'), 'edge_files', '__AbsentNamespace0_inputType_edge_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 28, 12), )

    
    edge_files = property(__edge_files.value, __edge_files.set, None, None)

    
    # Element connection-files uses Python identifier connection_files
    __connection_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'connection-files'), 'connection_files', '__AbsentNamespace0_inputType_connection_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 29, 12), )

    
    connection_files = property(__connection_files.value, __connection_files.set, None, None)

    
    # Element tllogic-files uses Python identifier tllogic_files
    __tllogic_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tllogic-files'), 'tllogic_files', '__AbsentNamespace0_inputType_tllogic_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 30, 12), )

    
    tllogic_files = property(__tllogic_files.value, __tllogic_files.set, None, None)

    
    # Element type-files uses Python identifier type_files
    __type_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type-files'), 'type_files', '__AbsentNamespace0_inputType_type_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 31, 12), )

    
    type_files = property(__type_files.value, __type_files.set, None, None)

    
    # Element shapefile-prefix uses Python identifier shapefile_prefix
    __shapefile_prefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile-prefix'), 'shapefile_prefix', '__AbsentNamespace0_inputType_shapefile_prefix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 32, 12), )

    
    shapefile_prefix = property(__shapefile_prefix.value, __shapefile_prefix.set, None, None)

    
    # Element dlr-navteq-prefix uses Python identifier dlr_navteq_prefix
    __dlr_navteq_prefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dlr-navteq-prefix'), 'dlr_navteq_prefix', '__AbsentNamespace0_inputType_dlr_navteq_prefix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 33, 12), )

    
    dlr_navteq_prefix = property(__dlr_navteq_prefix.value, __dlr_navteq_prefix.set, None, None)

    
    # Element osm-files uses Python identifier osm_files
    __osm_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm-files'), 'osm_files', '__AbsentNamespace0_inputType_osm_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 34, 12), )

    
    osm_files = property(__osm_files.value, __osm_files.set, None, None)

    
    # Element opendrive-files uses Python identifier opendrive_files
    __opendrive_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive-files'), 'opendrive_files', '__AbsentNamespace0_inputType_opendrive_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 35, 12), )

    
    opendrive_files = property(__opendrive_files.value, __opendrive_files.set, None, None)

    
    # Element visum-file uses Python identifier visum_file
    __visum_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum-file'), 'visum_file', '__AbsentNamespace0_inputType_visum_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 36, 12), )

    
    visum_file = property(__visum_file.value, __visum_file.set, None, None)

    
    # Element vissim-file uses Python identifier vissim_file
    __vissim_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vissim-file'), 'vissim_file', '__AbsentNamespace0_inputType_vissim_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 37, 12), )

    
    vissim_file = property(__vissim_file.value, __vissim_file.set, None, None)

    
    # Element robocup-dir uses Python identifier robocup_dir
    __robocup_dir = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'robocup-dir'), 'robocup_dir', '__AbsentNamespace0_inputType_robocup_dir', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 38, 12), )

    
    robocup_dir = property(__robocup_dir.value, __robocup_dir.set, None, None)

    
    # Element matsim-files uses Python identifier matsim_files
    __matsim_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'matsim-files'), 'matsim_files', '__AbsentNamespace0_inputType_matsim_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 39, 12), )

    
    matsim_files = property(__matsim_files.value, __matsim_files.set, None, None)

    
    # Element itsumo-files uses Python identifier itsumo_files
    __itsumo_files = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'itsumo-files'), 'itsumo_files', '__AbsentNamespace0_inputType_itsumo_files', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 40, 12), )

    
    itsumo_files = property(__itsumo_files.value, __itsumo_files.set, None, None)

    
    # Element heightmap.shapefiles uses Python identifier heightmap_shapefiles
    __heightmap_shapefiles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'heightmap.shapefiles'), 'heightmap_shapefiles', '__AbsentNamespace0_inputType_heightmap_shapefiles', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 41, 12), )

    
    heightmap_shapefiles = property(__heightmap_shapefiles.value, __heightmap_shapefiles.set, None, None)

    
    # Element heightmap.geotiff uses Python identifier heightmap_geotiff
    __heightmap_geotiff = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'heightmap.geotiff'), 'heightmap_geotiff', '__AbsentNamespace0_inputType_heightmap_geotiff', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 42, 12), )

    
    heightmap_geotiff = property(__heightmap_geotiff.value, __heightmap_geotiff.set, None, None)

    _ElementMap.update({
        __sumo_net_file.name() : __sumo_net_file,
        __node_files.name() : __node_files,
        __edge_files.name() : __edge_files,
        __connection_files.name() : __connection_files,
        __tllogic_files.name() : __tllogic_files,
        __type_files.name() : __type_files,
        __shapefile_prefix.name() : __shapefile_prefix,
        __dlr_navteq_prefix.name() : __dlr_navteq_prefix,
        __osm_files.name() : __osm_files,
        __opendrive_files.name() : __opendrive_files,
        __visum_file.name() : __visum_file,
        __vissim_file.name() : __vissim_file,
        __robocup_dir.name() : __robocup_dir,
        __matsim_files.name() : __matsim_files,
        __itsumo_files.name() : __itsumo_files,
        __heightmap_shapefiles.name() : __heightmap_shapefiles,
        __heightmap_geotiff.name() : __heightmap_geotiff
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
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 46, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element output-prefix uses Python identifier output_prefix
    __output_prefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-prefix'), 'output_prefix', '__AbsentNamespace0_outputType_output_prefix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 48, 12), )

    
    output_prefix = property(__output_prefix.value, __output_prefix.set, None, None)

    
    # Element precision uses Python identifier precision
    __precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'precision'), 'precision', '__AbsentNamespace0_outputType_precision', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 49, 12), )

    
    precision = property(__precision.value, __precision.set, None, None)

    
    # Element precision.geo uses Python identifier precision_geo
    __precision_geo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'precision.geo'), 'precision_geo', '__AbsentNamespace0_outputType_precision_geo', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 50, 12), )

    
    precision_geo = property(__precision_geo.value, __precision_geo.set, None, None)

    
    # Element output-file uses Python identifier output_file
    __output_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output-file'), 'output_file', '__AbsentNamespace0_outputType_output_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 51, 12), )

    
    output_file = property(__output_file.value, __output_file.set, None, None)

    
    # Element plain-output-prefix uses Python identifier plain_output_prefix
    __plain_output_prefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'plain-output-prefix'), 'plain_output_prefix', '__AbsentNamespace0_outputType_plain_output_prefix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 52, 12), )

    
    plain_output_prefix = property(__plain_output_prefix.value, __plain_output_prefix.set, None, None)

    
    # Element junctions.join-output uses Python identifier junctions_join_output
    __junctions_join_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.join-output'), 'junctions_join_output', '__AbsentNamespace0_outputType_junctions_join_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 53, 12), )

    
    junctions_join_output = property(__junctions_join_output.value, __junctions_join_output.set, None, None)

    
    # Element amitran-output uses Python identifier amitran_output
    __amitran_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'amitran-output'), 'amitran_output', '__AbsentNamespace0_outputType_amitran_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 54, 12), )

    
    amitran_output = property(__amitran_output.value, __amitran_output.set, None, None)

    
    # Element matsim-output uses Python identifier matsim_output
    __matsim_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'matsim-output'), 'matsim_output', '__AbsentNamespace0_outputType_matsim_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 55, 12), )

    
    matsim_output = property(__matsim_output.value, __matsim_output.set, None, None)

    
    # Element opendrive-output uses Python identifier opendrive_output
    __opendrive_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive-output'), 'opendrive_output', '__AbsentNamespace0_outputType_opendrive_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 56, 12), )

    
    opendrive_output = property(__opendrive_output.value, __opendrive_output.set, None, None)

    
    # Element dlr-navteq-output uses Python identifier dlr_navteq_output
    __dlr_navteq_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dlr-navteq-output'), 'dlr_navteq_output', '__AbsentNamespace0_outputType_dlr_navteq_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 57, 12), )

    
    dlr_navteq_output = property(__dlr_navteq_output.value, __dlr_navteq_output.set, None, None)

    
    # Element dlr-navteq.precision uses Python identifier dlr_navteq_precision
    __dlr_navteq_precision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dlr-navteq.precision'), 'dlr_navteq_precision', '__AbsentNamespace0_outputType_dlr_navteq_precision', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 58, 12), )

    
    dlr_navteq_precision = property(__dlr_navteq_precision.value, __dlr_navteq_precision.set, None, None)

    
    # Element output.street-names uses Python identifier output_street_names
    __output_street_names = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output.street-names'), 'output_street_names', '__AbsentNamespace0_outputType_output_street_names', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 59, 12), )

    
    output_street_names = property(__output_street_names.value, __output_street_names.set, None, None)

    
    # Element output.original-names uses Python identifier output_original_names
    __output_original_names = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'output.original-names'), 'output_original_names', '__AbsentNamespace0_outputType_output_original_names', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 60, 12), )

    
    output_original_names = property(__output_original_names.value, __output_original_names.set, None, None)

    
    # Element street-sign-output uses Python identifier street_sign_output
    __street_sign_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'street-sign-output'), 'street_sign_output', '__AbsentNamespace0_outputType_street_sign_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 61, 12), )

    
    street_sign_output = property(__street_sign_output.value, __street_sign_output.set, None, None)

    
    # Element ptstop-output uses Python identifier ptstop_output
    __ptstop_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ptstop-output'), 'ptstop_output', '__AbsentNamespace0_outputType_ptstop_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 62, 12), )

    
    ptstop_output = property(__ptstop_output.value, __ptstop_output.set, None, None)

    
    # Element ptline-output uses Python identifier ptline_output
    __ptline_output = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ptline-output'), 'ptline_output', '__AbsentNamespace0_outputType_ptline_output', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 63, 12), )

    
    ptline_output = property(__ptline_output.value, __ptline_output.set, None, None)

    
    # Element opendrive-output.straight-threshold uses Python identifier opendrive_output_straight_threshold
    __opendrive_output_straight_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive-output.straight-threshold'), 'opendrive_output_straight_threshold', '__AbsentNamespace0_outputType_opendrive_output_straight_threshold', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 64, 12), )

    
    opendrive_output_straight_threshold = property(__opendrive_output_straight_threshold.value, __opendrive_output_straight_threshold.set, None, None)

    _ElementMap.update({
        __output_prefix.name() : __output_prefix,
        __precision.name() : __precision,
        __precision_geo.name() : __precision_geo,
        __output_file.name() : __output_file,
        __plain_output_prefix.name() : __plain_output_prefix,
        __junctions_join_output.name() : __junctions_join_output,
        __amitran_output.name() : __amitran_output,
        __matsim_output.name() : __matsim_output,
        __opendrive_output.name() : __opendrive_output,
        __dlr_navteq_output.name() : __dlr_navteq_output,
        __dlr_navteq_precision.name() : __dlr_navteq_precision,
        __output_street_names.name() : __output_street_names,
        __output_original_names.name() : __output_original_names,
        __street_sign_output.name() : __street_sign_output,
        __ptstop_output.name() : __ptstop_output,
        __ptline_output.name() : __ptline_output,
        __opendrive_output_straight_threshold.name() : __opendrive_output_straight_threshold
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.outputType = outputType
Namespace.addCategoryObject('typeBinding', 'outputType', outputType)


# Complex type projectionType with content type ELEMENT_ONLY
class projectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type projectionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'projectionType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 68, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element simple-projection uses Python identifier simple_projection
    __simple_projection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'simple-projection'), 'simple_projection', '__AbsentNamespace0_projectionType_simple_projection', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 70, 12), )

    
    simple_projection = property(__simple_projection.value, __simple_projection.set, None, None)

    
    # Element proj.scale uses Python identifier proj_scale
    __proj_scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj.scale'), 'proj_scale', '__AbsentNamespace0_projectionType_proj_scale', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 71, 12), )

    
    proj_scale = property(__proj_scale.value, __proj_scale.set, None, None)

    
    # Element proj.utm uses Python identifier proj_utm
    __proj_utm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj.utm'), 'proj_utm', '__AbsentNamespace0_projectionType_proj_utm', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 72, 12), )

    
    proj_utm = property(__proj_utm.value, __proj_utm.set, None, None)

    
    # Element proj.dhdn uses Python identifier proj_dhdn
    __proj_dhdn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj.dhdn'), 'proj_dhdn', '__AbsentNamespace0_projectionType_proj_dhdn', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 73, 12), )

    
    proj_dhdn = property(__proj_dhdn.value, __proj_dhdn.set, None, None)

    
    # Element proj uses Python identifier proj
    __proj = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj'), 'proj', '__AbsentNamespace0_projectionType_proj', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 74, 12), )

    
    proj = property(__proj.value, __proj.set, None, None)

    
    # Element proj.inverse uses Python identifier proj_inverse
    __proj_inverse = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj.inverse'), 'proj_inverse', '__AbsentNamespace0_projectionType_proj_inverse', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 75, 12), )

    
    proj_inverse = property(__proj_inverse.value, __proj_inverse.set, None, None)

    
    # Element proj.dhdnutm uses Python identifier proj_dhdnutm
    __proj_dhdnutm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj.dhdnutm'), 'proj_dhdnutm', '__AbsentNamespace0_projectionType_proj_dhdnutm', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 76, 12), )

    
    proj_dhdnutm = property(__proj_dhdnutm.value, __proj_dhdnutm.set, None, None)

    
    # Element proj.plain-geo uses Python identifier proj_plain_geo
    __proj_plain_geo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'proj.plain-geo'), 'proj_plain_geo', '__AbsentNamespace0_projectionType_proj_plain_geo', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 77, 12), )

    
    proj_plain_geo = property(__proj_plain_geo.value, __proj_plain_geo.set, None, None)

    _ElementMap.update({
        __simple_projection.name() : __simple_projection,
        __proj_scale.name() : __proj_scale,
        __proj_utm.name() : __proj_utm,
        __proj_dhdn.name() : __proj_dhdn,
        __proj.name() : __proj,
        __proj_inverse.name() : __proj_inverse,
        __proj_dhdnutm.name() : __proj_dhdnutm,
        __proj_plain_geo.name() : __proj_plain_geo
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.projectionType = projectionType
Namespace.addCategoryObject('typeBinding', 'projectionType', projectionType)


# Complex type tls_buildingType with content type ELEMENT_ONLY
class tls_buildingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type tls_buildingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tls_buildingType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 81, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element tls.discard-loaded uses Python identifier tls_discard_loaded
    __tls_discard_loaded = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.discard-loaded'), 'tls_discard_loaded', '__AbsentNamespace0_tls_buildingType_tls_discard_loaded', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 83, 12), )

    
    tls_discard_loaded = property(__tls_discard_loaded.value, __tls_discard_loaded.set, None, None)

    
    # Element tls.discard-simple uses Python identifier tls_discard_simple
    __tls_discard_simple = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.discard-simple'), 'tls_discard_simple', '__AbsentNamespace0_tls_buildingType_tls_discard_simple', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 84, 12), )

    
    tls_discard_simple = property(__tls_discard_simple.value, __tls_discard_simple.set, None, None)

    
    # Element tls.set uses Python identifier tls_set
    __tls_set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.set'), 'tls_set', '__AbsentNamespace0_tls_buildingType_tls_set', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 85, 12), )

    
    tls_set = property(__tls_set.value, __tls_set.set, None, None)

    
    # Element tls.unset uses Python identifier tls_unset
    __tls_unset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.unset'), 'tls_unset', '__AbsentNamespace0_tls_buildingType_tls_unset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 86, 12), )

    
    tls_unset = property(__tls_unset.value, __tls_unset.set, None, None)

    
    # Element tls.guess uses Python identifier tls_guess
    __tls_guess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.guess'), 'tls_guess', '__AbsentNamespace0_tls_buildingType_tls_guess', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 87, 12), )

    
    tls_guess = property(__tls_guess.value, __tls_guess.set, None, None)

    
    # Element tls.taz-nodes uses Python identifier tls_taz_nodes
    __tls_taz_nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.taz-nodes'), 'tls_taz_nodes', '__AbsentNamespace0_tls_buildingType_tls_taz_nodes', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 88, 12), )

    
    tls_taz_nodes = property(__tls_taz_nodes.value, __tls_taz_nodes.set, None, None)

    
    # Element tls-guess.joining uses Python identifier tls_guess_joining
    __tls_guess_joining = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls-guess.joining'), 'tls_guess_joining', '__AbsentNamespace0_tls_buildingType_tls_guess_joining', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 89, 12), )

    
    tls_guess_joining = property(__tls_guess_joining.value, __tls_guess_joining.set, None, None)

    
    # Element tls.join uses Python identifier tls_join
    __tls_join = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.join'), 'tls_join', '__AbsentNamespace0_tls_buildingType_tls_join', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 90, 12), )

    
    tls_join = property(__tls_join.value, __tls_join.set, None, None)

    
    # Element tls.join-dist uses Python identifier tls_join_dist
    __tls_join_dist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.join-dist'), 'tls_join_dist', '__AbsentNamespace0_tls_buildingType_tls_join_dist', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 91, 12), )

    
    tls_join_dist = property(__tls_join_dist.value, __tls_join_dist.set, None, None)

    
    # Element tls.uncontrolled-within uses Python identifier tls_uncontrolled_within
    __tls_uncontrolled_within = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.uncontrolled-within'), 'tls_uncontrolled_within', '__AbsentNamespace0_tls_buildingType_tls_uncontrolled_within', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 92, 12), )

    
    tls_uncontrolled_within = property(__tls_uncontrolled_within.value, __tls_uncontrolled_within.set, None, None)

    
    # Element tls.guess-signals uses Python identifier tls_guess_signals
    __tls_guess_signals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.guess-signals'), 'tls_guess_signals', '__AbsentNamespace0_tls_buildingType_tls_guess_signals', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 93, 12), )

    
    tls_guess_signals = property(__tls_guess_signals.value, __tls_guess_signals.set, None, None)

    
    # Element tls.guess-signals.dist uses Python identifier tls_guess_signals_dist
    __tls_guess_signals_dist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.guess-signals.dist'), 'tls_guess_signals_dist', '__AbsentNamespace0_tls_buildingType_tls_guess_signals_dist', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 94, 12), )

    
    tls_guess_signals_dist = property(__tls_guess_signals_dist.value, __tls_guess_signals_dist.set, None, None)

    
    # Element tls.cycle.time uses Python identifier tls_cycle_time
    __tls_cycle_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.cycle.time'), 'tls_cycle_time', '__AbsentNamespace0_tls_buildingType_tls_cycle_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 95, 12), )

    
    tls_cycle_time = property(__tls_cycle_time.value, __tls_cycle_time.set, None, None)

    
    # Element tls.green.time uses Python identifier tls_green_time
    __tls_green_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.green.time'), 'tls_green_time', '__AbsentNamespace0_tls_buildingType_tls_green_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 96, 12), )

    
    tls_green_time = property(__tls_green_time.value, __tls_green_time.set, None, None)

    
    # Element tls.yellow.min-decel uses Python identifier tls_yellow_min_decel
    __tls_yellow_min_decel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.yellow.min-decel'), 'tls_yellow_min_decel', '__AbsentNamespace0_tls_buildingType_tls_yellow_min_decel', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 97, 12), )

    
    tls_yellow_min_decel = property(__tls_yellow_min_decel.value, __tls_yellow_min_decel.set, None, None)

    
    # Element tls.yellow.patch-small uses Python identifier tls_yellow_patch_small
    __tls_yellow_patch_small = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.yellow.patch-small'), 'tls_yellow_patch_small', '__AbsentNamespace0_tls_buildingType_tls_yellow_patch_small', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 98, 12), )

    
    tls_yellow_patch_small = property(__tls_yellow_patch_small.value, __tls_yellow_patch_small.set, None, None)

    
    # Element tls.yellow.time uses Python identifier tls_yellow_time
    __tls_yellow_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.yellow.time'), 'tls_yellow_time', '__AbsentNamespace0_tls_buildingType_tls_yellow_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 99, 12), )

    
    tls_yellow_time = property(__tls_yellow_time.value, __tls_yellow_time.set, None, None)

    
    # Element tls.red.time uses Python identifier tls_red_time
    __tls_red_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.red.time'), 'tls_red_time', '__AbsentNamespace0_tls_buildingType_tls_red_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 100, 12), )

    
    tls_red_time = property(__tls_red_time.value, __tls_red_time.set, None, None)

    
    # Element tls.allred.time uses Python identifier tls_allred_time
    __tls_allred_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.allred.time'), 'tls_allred_time', '__AbsentNamespace0_tls_buildingType_tls_allred_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 101, 12), )

    
    tls_allred_time = property(__tls_allred_time.value, __tls_allred_time.set, None, None)

    
    # Element tls.left-green.time uses Python identifier tls_left_green_time
    __tls_left_green_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.left-green.time'), 'tls_left_green_time', '__AbsentNamespace0_tls_buildingType_tls_left_green_time', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 102, 12), )

    
    tls_left_green_time = property(__tls_left_green_time.value, __tls_left_green_time.set, None, None)

    
    # Element tls.half-offset uses Python identifier tls_half_offset
    __tls_half_offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.half-offset'), 'tls_half_offset', '__AbsentNamespace0_tls_buildingType_tls_half_offset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 103, 12), )

    
    tls_half_offset = property(__tls_half_offset.value, __tls_half_offset.set, None, None)

    
    # Element tls.quarter-offset uses Python identifier tls_quarter_offset
    __tls_quarter_offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.quarter-offset'), 'tls_quarter_offset', '__AbsentNamespace0_tls_buildingType_tls_quarter_offset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 104, 12), )

    
    tls_quarter_offset = property(__tls_quarter_offset.value, __tls_quarter_offset.set, None, None)

    
    # Element tls.default-type uses Python identifier tls_default_type
    __tls_default_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.default-type'), 'tls_default_type', '__AbsentNamespace0_tls_buildingType_tls_default_type', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 105, 12), )

    
    tls_default_type = property(__tls_default_type.value, __tls_default_type.set, None, None)

    
    # Element tls.min-dur uses Python identifier tls_min_dur
    __tls_min_dur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.min-dur'), 'tls_min_dur', '__AbsentNamespace0_tls_buildingType_tls_min_dur', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 106, 12), )

    
    tls_min_dur = property(__tls_min_dur.value, __tls_min_dur.set, None, None)

    
    # Element tls.max-dur uses Python identifier tls_max_dur
    __tls_max_dur = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tls.max-dur'), 'tls_max_dur', '__AbsentNamespace0_tls_buildingType_tls_max_dur', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 107, 12), )

    
    tls_max_dur = property(__tls_max_dur.value, __tls_max_dur.set, None, None)

    _ElementMap.update({
        __tls_discard_loaded.name() : __tls_discard_loaded,
        __tls_discard_simple.name() : __tls_discard_simple,
        __tls_set.name() : __tls_set,
        __tls_unset.name() : __tls_unset,
        __tls_guess.name() : __tls_guess,
        __tls_taz_nodes.name() : __tls_taz_nodes,
        __tls_guess_joining.name() : __tls_guess_joining,
        __tls_join.name() : __tls_join,
        __tls_join_dist.name() : __tls_join_dist,
        __tls_uncontrolled_within.name() : __tls_uncontrolled_within,
        __tls_guess_signals.name() : __tls_guess_signals,
        __tls_guess_signals_dist.name() : __tls_guess_signals_dist,
        __tls_cycle_time.name() : __tls_cycle_time,
        __tls_green_time.name() : __tls_green_time,
        __tls_yellow_min_decel.name() : __tls_yellow_min_decel,
        __tls_yellow_patch_small.name() : __tls_yellow_patch_small,
        __tls_yellow_time.name() : __tls_yellow_time,
        __tls_red_time.name() : __tls_red_time,
        __tls_allred_time.name() : __tls_allred_time,
        __tls_left_green_time.name() : __tls_left_green_time,
        __tls_half_offset.name() : __tls_half_offset,
        __tls_quarter_offset.name() : __tls_quarter_offset,
        __tls_default_type.name() : __tls_default_type,
        __tls_min_dur.name() : __tls_min_dur,
        __tls_max_dur.name() : __tls_max_dur
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.tls_buildingType = tls_buildingType
Namespace.addCategoryObject('typeBinding', 'tls_buildingType', tls_buildingType)


# Complex type ramp_guessingType with content type ELEMENT_ONLY
class ramp_guessingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ramp_guessingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ramp_guessingType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 111, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ramps.guess uses Python identifier ramps_guess
    __ramps_guess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.guess'), 'ramps_guess', '__AbsentNamespace0_ramp_guessingType_ramps_guess', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 113, 12), )

    
    ramps_guess = property(__ramps_guess.value, __ramps_guess.set, None, None)

    
    # Element ramps.max-ramp-speed uses Python identifier ramps_max_ramp_speed
    __ramps_max_ramp_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.max-ramp-speed'), 'ramps_max_ramp_speed', '__AbsentNamespace0_ramp_guessingType_ramps_max_ramp_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 114, 12), )

    
    ramps_max_ramp_speed = property(__ramps_max_ramp_speed.value, __ramps_max_ramp_speed.set, None, None)

    
    # Element ramps.min-highway-speed uses Python identifier ramps_min_highway_speed
    __ramps_min_highway_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.min-highway-speed'), 'ramps_min_highway_speed', '__AbsentNamespace0_ramp_guessingType_ramps_min_highway_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 115, 12), )

    
    ramps_min_highway_speed = property(__ramps_min_highway_speed.value, __ramps_min_highway_speed.set, None, None)

    
    # Element ramps.ramp-length uses Python identifier ramps_ramp_length
    __ramps_ramp_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.ramp-length'), 'ramps_ramp_length', '__AbsentNamespace0_ramp_guessingType_ramps_ramp_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 116, 12), )

    
    ramps_ramp_length = property(__ramps_ramp_length.value, __ramps_ramp_length.set, None, None)

    
    # Element ramps.set uses Python identifier ramps_set
    __ramps_set = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.set'), 'ramps_set', '__AbsentNamespace0_ramp_guessingType_ramps_set', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 117, 12), )

    
    ramps_set = property(__ramps_set.value, __ramps_set.set, None, None)

    
    # Element ramps.unset uses Python identifier ramps_unset
    __ramps_unset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.unset'), 'ramps_unset', '__AbsentNamespace0_ramp_guessingType_ramps_unset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 118, 12), )

    
    ramps_unset = property(__ramps_unset.value, __ramps_unset.set, None, None)

    
    # Element ramps.no-split uses Python identifier ramps_no_split
    __ramps_no_split = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ramps.no-split'), 'ramps_no_split', '__AbsentNamespace0_ramp_guessingType_ramps_no_split', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 119, 12), )

    
    ramps_no_split = property(__ramps_no_split.value, __ramps_no_split.set, None, None)

    _ElementMap.update({
        __ramps_guess.name() : __ramps_guess,
        __ramps_max_ramp_speed.name() : __ramps_max_ramp_speed,
        __ramps_min_highway_speed.name() : __ramps_min_highway_speed,
        __ramps_ramp_length.name() : __ramps_ramp_length,
        __ramps_set.name() : __ramps_set,
        __ramps_unset.name() : __ramps_unset,
        __ramps_no_split.name() : __ramps_no_split
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ramp_guessingType = ramp_guessingType
Namespace.addCategoryObject('typeBinding', 'ramp_guessingType', ramp_guessingType)


# Complex type edge_removalType with content type ELEMENT_ONLY
class edge_removalType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type edge_removalType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'edge_removalType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 123, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element keep-edges.min-speed uses Python identifier keep_edges_min_speed
    __keep_edges_min_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.min-speed'), 'keep_edges_min_speed', '__AbsentNamespace0_edge_removalType_keep_edges_min_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 125, 12), )

    
    keep_edges_min_speed = property(__keep_edges_min_speed.value, __keep_edges_min_speed.set, None, None)

    
    # Element remove-edges.explicit uses Python identifier remove_edges_explicit
    __remove_edges_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remove-edges.explicit'), 'remove_edges_explicit', '__AbsentNamespace0_edge_removalType_remove_edges_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 126, 12), )

    
    remove_edges_explicit = property(__remove_edges_explicit.value, __remove_edges_explicit.set, None, None)

    
    # Element keep-edges.explicit uses Python identifier keep_edges_explicit
    __keep_edges_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.explicit'), 'keep_edges_explicit', '__AbsentNamespace0_edge_removalType_keep_edges_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 127, 12), )

    
    keep_edges_explicit = property(__keep_edges_explicit.value, __keep_edges_explicit.set, None, None)

    
    # Element keep-edges.input-file uses Python identifier keep_edges_input_file
    __keep_edges_input_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.input-file'), 'keep_edges_input_file', '__AbsentNamespace0_edge_removalType_keep_edges_input_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 128, 12), )

    
    keep_edges_input_file = property(__keep_edges_input_file.value, __keep_edges_input_file.set, None, None)

    
    # Element remove-edges.input-file uses Python identifier remove_edges_input_file
    __remove_edges_input_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remove-edges.input-file'), 'remove_edges_input_file', '__AbsentNamespace0_edge_removalType_remove_edges_input_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 129, 12), )

    
    remove_edges_input_file = property(__remove_edges_input_file.value, __remove_edges_input_file.set, None, None)

    
    # Element keep-edges.postload uses Python identifier keep_edges_postload
    __keep_edges_postload = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.postload'), 'keep_edges_postload', '__AbsentNamespace0_edge_removalType_keep_edges_postload', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 130, 12), )

    
    keep_edges_postload = property(__keep_edges_postload.value, __keep_edges_postload.set, None, None)

    
    # Element keep-edges.in-boundary uses Python identifier keep_edges_in_boundary
    __keep_edges_in_boundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.in-boundary'), 'keep_edges_in_boundary', '__AbsentNamespace0_edge_removalType_keep_edges_in_boundary', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 131, 12), )

    
    keep_edges_in_boundary = property(__keep_edges_in_boundary.value, __keep_edges_in_boundary.set, None, None)

    
    # Element keep-edges.in-geo-boundary uses Python identifier keep_edges_in_geo_boundary
    __keep_edges_in_geo_boundary = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.in-geo-boundary'), 'keep_edges_in_geo_boundary', '__AbsentNamespace0_edge_removalType_keep_edges_in_geo_boundary', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 132, 12), )

    
    keep_edges_in_geo_boundary = property(__keep_edges_in_geo_boundary.value, __keep_edges_in_geo_boundary.set, None, None)

    
    # Element keep-edges.by-vclass uses Python identifier keep_edges_by_vclass
    __keep_edges_by_vclass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.by-vclass'), 'keep_edges_by_vclass', '__AbsentNamespace0_edge_removalType_keep_edges_by_vclass', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 133, 12), )

    
    keep_edges_by_vclass = property(__keep_edges_by_vclass.value, __keep_edges_by_vclass.set, None, None)

    
    # Element remove-edges.by-vclass uses Python identifier remove_edges_by_vclass
    __remove_edges_by_vclass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remove-edges.by-vclass'), 'remove_edges_by_vclass', '__AbsentNamespace0_edge_removalType_remove_edges_by_vclass', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 134, 12), )

    
    remove_edges_by_vclass = property(__remove_edges_by_vclass.value, __remove_edges_by_vclass.set, None, None)

    
    # Element keep-edges.by-type uses Python identifier keep_edges_by_type
    __keep_edges_by_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.by-type'), 'keep_edges_by_type', '__AbsentNamespace0_edge_removalType_keep_edges_by_type', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 135, 12), )

    
    keep_edges_by_type = property(__keep_edges_by_type.value, __keep_edges_by_type.set, None, None)

    
    # Element keep-edges.components uses Python identifier keep_edges_components
    __keep_edges_components = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-edges.components'), 'keep_edges_components', '__AbsentNamespace0_edge_removalType_keep_edges_components', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 136, 12), )

    
    keep_edges_components = property(__keep_edges_components.value, __keep_edges_components.set, None, None)

    
    # Element remove-edges.by-type uses Python identifier remove_edges_by_type
    __remove_edges_by_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remove-edges.by-type'), 'remove_edges_by_type', '__AbsentNamespace0_edge_removalType_remove_edges_by_type', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 137, 12), )

    
    remove_edges_by_type = property(__remove_edges_by_type.value, __remove_edges_by_type.set, None, None)

    
    # Element remove-edges.isolated uses Python identifier remove_edges_isolated
    __remove_edges_isolated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'remove-edges.isolated'), 'remove_edges_isolated', '__AbsentNamespace0_edge_removalType_remove_edges_isolated', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 138, 12), )

    
    remove_edges_isolated = property(__remove_edges_isolated.value, __remove_edges_isolated.set, None, None)

    _ElementMap.update({
        __keep_edges_min_speed.name() : __keep_edges_min_speed,
        __remove_edges_explicit.name() : __remove_edges_explicit,
        __keep_edges_explicit.name() : __keep_edges_explicit,
        __keep_edges_input_file.name() : __keep_edges_input_file,
        __remove_edges_input_file.name() : __remove_edges_input_file,
        __keep_edges_postload.name() : __keep_edges_postload,
        __keep_edges_in_boundary.name() : __keep_edges_in_boundary,
        __keep_edges_in_geo_boundary.name() : __keep_edges_in_geo_boundary,
        __keep_edges_by_vclass.name() : __keep_edges_by_vclass,
        __remove_edges_by_vclass.name() : __remove_edges_by_vclass,
        __keep_edges_by_type.name() : __keep_edges_by_type,
        __keep_edges_components.name() : __keep_edges_components,
        __remove_edges_by_type.name() : __remove_edges_by_type,
        __remove_edges_isolated.name() : __remove_edges_isolated
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.edge_removalType = edge_removalType
Namespace.addCategoryObject('typeBinding', 'edge_removalType', edge_removalType)


# Complex type unregulated_nodesType with content type ELEMENT_ONLY
class unregulated_nodesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type unregulated_nodesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'unregulated_nodesType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 142, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element keep-nodes-unregulated uses Python identifier keep_nodes_unregulated
    __keep_nodes_unregulated = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated'), 'keep_nodes_unregulated', '__AbsentNamespace0_unregulated_nodesType_keep_nodes_unregulated', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 144, 12), )

    
    keep_nodes_unregulated = property(__keep_nodes_unregulated.value, __keep_nodes_unregulated.set, None, None)

    
    # Element keep-nodes-unregulated.explicit uses Python identifier keep_nodes_unregulated_explicit
    __keep_nodes_unregulated_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated.explicit'), 'keep_nodes_unregulated_explicit', '__AbsentNamespace0_unregulated_nodesType_keep_nodes_unregulated_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 145, 12), )

    
    keep_nodes_unregulated_explicit = property(__keep_nodes_unregulated_explicit.value, __keep_nodes_unregulated_explicit.set, None, None)

    
    # Element keep-nodes-unregulated.district-nodes uses Python identifier keep_nodes_unregulated_district_nodes
    __keep_nodes_unregulated_district_nodes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated.district-nodes'), 'keep_nodes_unregulated_district_nodes', '__AbsentNamespace0_unregulated_nodesType_keep_nodes_unregulated_district_nodes', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 146, 12), )

    
    keep_nodes_unregulated_district_nodes = property(__keep_nodes_unregulated_district_nodes.value, __keep_nodes_unregulated_district_nodes.set, None, None)

    _ElementMap.update({
        __keep_nodes_unregulated.name() : __keep_nodes_unregulated,
        __keep_nodes_unregulated_explicit.name() : __keep_nodes_unregulated_explicit,
        __keep_nodes_unregulated_district_nodes.name() : __keep_nodes_unregulated_district_nodes
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.unregulated_nodesType = unregulated_nodesType
Namespace.addCategoryObject('typeBinding', 'unregulated_nodesType', unregulated_nodesType)


# Complex type processingType with content type ELEMENT_ONLY
class processingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type processingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'processingType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 150, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element ignore-errors uses Python identifier ignore_errors
    __ignore_errors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore-errors'), 'ignore_errors', '__AbsentNamespace0_processingType_ignore_errors', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 152, 12), )

    
    ignore_errors = property(__ignore_errors.value, __ignore_errors.set, None, None)

    
    # Element ignore-errors.connections uses Python identifier ignore_errors_connections
    __ignore_errors_connections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore-errors.connections'), 'ignore_errors_connections', '__AbsentNamespace0_processingType_ignore_errors_connections', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 153, 12), )

    
    ignore_errors_connections = property(__ignore_errors_connections.value, __ignore_errors_connections.set, None, None)

    
    # Element show-errors.connections-first-try uses Python identifier show_errors_connections_first_try
    __show_errors_connections_first_try = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'show-errors.connections-first-try'), 'show_errors_connections_first_try', '__AbsentNamespace0_processingType_show_errors_connections_first_try', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 154, 12), )

    
    show_errors_connections_first_try = property(__show_errors_connections_first_try.value, __show_errors_connections_first_try.set, None, None)

    
    # Element ignore-errors.edge-type uses Python identifier ignore_errors_edge_type
    __ignore_errors_edge_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ignore-errors.edge-type'), 'ignore_errors_edge_type', '__AbsentNamespace0_processingType_ignore_errors_edge_type', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 155, 12), )

    
    ignore_errors_edge_type = property(__ignore_errors_edge_type.value, __ignore_errors_edge_type.set, None, None)

    
    # Element lanes-from-capacity.norm uses Python identifier lanes_from_capacity_norm
    __lanes_from_capacity_norm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lanes-from-capacity.norm'), 'lanes_from_capacity_norm', '__AbsentNamespace0_processingType_lanes_from_capacity_norm', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 156, 12), )

    
    lanes_from_capacity_norm = property(__lanes_from_capacity_norm.value, __lanes_from_capacity_norm.set, None, None)

    
    # Element speed-in-kmh uses Python identifier speed_in_kmh
    __speed_in_kmh = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'speed-in-kmh'), 'speed_in_kmh', '__AbsentNamespace0_processingType_speed_in_kmh', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 157, 12), )

    
    speed_in_kmh = property(__speed_in_kmh.value, __speed_in_kmh.set, None, None)

    
    # Element construction-date uses Python identifier construction_date
    __construction_date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction-date'), 'construction_date', '__AbsentNamespace0_processingType_construction_date', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 158, 12), )

    
    construction_date = property(__construction_date.value, __construction_date.set, None, None)

    
    # Element plain.extend-edge-shape uses Python identifier plain_extend_edge_shape
    __plain_extend_edge_shape = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'plain.extend-edge-shape'), 'plain_extend_edge_shape', '__AbsentNamespace0_processingType_plain_extend_edge_shape', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 159, 12), )

    
    plain_extend_edge_shape = property(__plain_extend_edge_shape.value, __plain_extend_edge_shape.set, None, None)

    
    # Element matsim.keep-length uses Python identifier matsim_keep_length
    __matsim_keep_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'matsim.keep-length'), 'matsim_keep_length', '__AbsentNamespace0_processingType_matsim_keep_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 160, 12), )

    
    matsim_keep_length = property(__matsim_keep_length.value, __matsim_keep_length.set, None, None)

    
    # Element matsim.lanes-from-capacity uses Python identifier matsim_lanes_from_capacity
    __matsim_lanes_from_capacity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'matsim.lanes-from-capacity'), 'matsim_lanes_from_capacity', '__AbsentNamespace0_processingType_matsim_lanes_from_capacity', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 161, 12), )

    
    matsim_lanes_from_capacity = property(__matsim_lanes_from_capacity.value, __matsim_lanes_from_capacity.set, None, None)

    
    # Element shapefile.street-id uses Python identifier shapefile_street_id
    __shapefile_street_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.street-id'), 'shapefile_street_id', '__AbsentNamespace0_processingType_shapefile_street_id', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 162, 12), )

    
    shapefile_street_id = property(__shapefile_street_id.value, __shapefile_street_id.set, None, None)

    
    # Element shapefile.from-id uses Python identifier shapefile_from_id
    __shapefile_from_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.from-id'), 'shapefile_from_id', '__AbsentNamespace0_processingType_shapefile_from_id', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 163, 12), )

    
    shapefile_from_id = property(__shapefile_from_id.value, __shapefile_from_id.set, None, None)

    
    # Element shapefile.to-id uses Python identifier shapefile_to_id
    __shapefile_to_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.to-id'), 'shapefile_to_id', '__AbsentNamespace0_processingType_shapefile_to_id', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 164, 12), )

    
    shapefile_to_id = property(__shapefile_to_id.value, __shapefile_to_id.set, None, None)

    
    # Element shapefile.type-id uses Python identifier shapefile_type_id
    __shapefile_type_id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.type-id'), 'shapefile_type_id', '__AbsentNamespace0_processingType_shapefile_type_id', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 165, 12), )

    
    shapefile_type_id = property(__shapefile_type_id.value, __shapefile_type_id.set, None, None)

    
    # Element shapefile.use-defaults-on-failure uses Python identifier shapefile_use_defaults_on_failure
    __shapefile_use_defaults_on_failure = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.use-defaults-on-failure'), 'shapefile_use_defaults_on_failure', '__AbsentNamespace0_processingType_shapefile_use_defaults_on_failure', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 166, 12), )

    
    shapefile_use_defaults_on_failure = property(__shapefile_use_defaults_on_failure.value, __shapefile_use_defaults_on_failure.set, None, None)

    
    # Element shapefile.all-bidirectional uses Python identifier shapefile_all_bidirectional
    __shapefile_all_bidirectional = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.all-bidirectional'), 'shapefile_all_bidirectional', '__AbsentNamespace0_processingType_shapefile_all_bidirectional', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 167, 12), )

    
    shapefile_all_bidirectional = property(__shapefile_all_bidirectional.value, __shapefile_all_bidirectional.set, None, None)

    
    # Element shapefile.guess-projection uses Python identifier shapefile_guess_projection
    __shapefile_guess_projection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shapefile.guess-projection'), 'shapefile_guess_projection', '__AbsentNamespace0_processingType_shapefile_guess_projection', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 168, 12), )

    
    shapefile_guess_projection = property(__shapefile_guess_projection.value, __shapefile_guess_projection.set, None, None)

    
    # Element vissim.join-distance uses Python identifier vissim_join_distance
    __vissim_join_distance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vissim.join-distance'), 'vissim_join_distance', '__AbsentNamespace0_processingType_vissim_join_distance', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 169, 12), )

    
    vissim_join_distance = property(__vissim_join_distance.value, __vissim_join_distance.set, None, None)

    
    # Element vissim.default-speed uses Python identifier vissim_default_speed
    __vissim_default_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vissim.default-speed'), 'vissim_default_speed', '__AbsentNamespace0_processingType_vissim_default_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 170, 12), )

    
    vissim_default_speed = property(__vissim_default_speed.value, __vissim_default_speed.set, None, None)

    
    # Element vissim.speed-norm uses Python identifier vissim_speed_norm
    __vissim_speed_norm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vissim.speed-norm'), 'vissim_speed_norm', '__AbsentNamespace0_processingType_vissim_speed_norm', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 171, 12), )

    
    vissim_speed_norm = property(__vissim_speed_norm.value, __vissim_speed_norm.set, None, None)

    
    # Element vissim.report-unset-speeds uses Python identifier vissim_report_unset_speeds
    __vissim_report_unset_speeds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'vissim.report-unset-speeds'), 'vissim_report_unset_speeds', '__AbsentNamespace0_processingType_vissim_report_unset_speeds', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 172, 12), )

    
    vissim_report_unset_speeds = property(__vissim_report_unset_speeds.value, __vissim_report_unset_speeds.set, None, None)

    
    # Element visum.use-type-priority uses Python identifier visum_use_type_priority
    __visum_use_type_priority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.use-type-priority'), 'visum_use_type_priority', '__AbsentNamespace0_processingType_visum_use_type_priority', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 173, 12), )

    
    visum_use_type_priority = property(__visum_use_type_priority.value, __visum_use_type_priority.set, None, None)

    
    # Element visum.use-type-laneno uses Python identifier visum_use_type_laneno
    __visum_use_type_laneno = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.use-type-laneno'), 'visum_use_type_laneno', '__AbsentNamespace0_processingType_visum_use_type_laneno', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 174, 12), )

    
    visum_use_type_laneno = property(__visum_use_type_laneno.value, __visum_use_type_laneno.set, None, None)

    
    # Element visum.use-type-speed uses Python identifier visum_use_type_speed
    __visum_use_type_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.use-type-speed'), 'visum_use_type_speed', '__AbsentNamespace0_processingType_visum_use_type_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 175, 12), )

    
    visum_use_type_speed = property(__visum_use_type_speed.value, __visum_use_type_speed.set, None, None)

    
    # Element visum.connector-speeds uses Python identifier visum_connector_speeds
    __visum_connector_speeds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.connector-speeds'), 'visum_connector_speeds', '__AbsentNamespace0_processingType_visum_connector_speeds', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 176, 12), )

    
    visum_connector_speeds = property(__visum_connector_speeds.value, __visum_connector_speeds.set, None, None)

    
    # Element visum.connectors-lane-number uses Python identifier visum_connectors_lane_number
    __visum_connectors_lane_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.connectors-lane-number'), 'visum_connectors_lane_number', '__AbsentNamespace0_processingType_visum_connectors_lane_number', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 177, 12), )

    
    visum_connectors_lane_number = property(__visum_connectors_lane_number.value, __visum_connectors_lane_number.set, None, None)

    
    # Element visum.no-connectors uses Python identifier visum_no_connectors
    __visum_no_connectors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.no-connectors'), 'visum_no_connectors', '__AbsentNamespace0_processingType_visum_no_connectors', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 178, 12), )

    
    visum_no_connectors = property(__visum_no_connectors.value, __visum_no_connectors.set, None, None)

    
    # Element visum.recompute-lane-number uses Python identifier visum_recompute_lane_number
    __visum_recompute_lane_number = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.recompute-lane-number'), 'visum_recompute_lane_number', '__AbsentNamespace0_processingType_visum_recompute_lane_number', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 179, 12), )

    
    visum_recompute_lane_number = property(__visum_recompute_lane_number.value, __visum_recompute_lane_number.set, None, None)

    
    # Element visum.verbose-warnings uses Python identifier visum_verbose_warnings
    __visum_verbose_warnings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'visum.verbose-warnings'), 'visum_verbose_warnings', '__AbsentNamespace0_processingType_visum_verbose_warnings', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 180, 12), )

    
    visum_verbose_warnings = property(__visum_verbose_warnings.value, __visum_verbose_warnings.set, None, None)

    
    # Element osm.skip-duplicates-check uses Python identifier osm_skip_duplicates_check
    __osm_skip_duplicates_check = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm.skip-duplicates-check'), 'osm_skip_duplicates_check', '__AbsentNamespace0_processingType_osm_skip_duplicates_check', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 181, 12), )

    
    osm_skip_duplicates_check = property(__osm_skip_duplicates_check.value, __osm_skip_duplicates_check.set, None, None)

    
    # Element osm.elevation uses Python identifier osm_elevation
    __osm_elevation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm.elevation'), 'osm_elevation', '__AbsentNamespace0_processingType_osm_elevation', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 182, 12), )

    
    osm_elevation = property(__osm_elevation.value, __osm_elevation.set, None, None)

    
    # Element osm.layer-elevation uses Python identifier osm_layer_elevation
    __osm_layer_elevation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm.layer-elevation'), 'osm_layer_elevation', '__AbsentNamespace0_processingType_osm_layer_elevation', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 183, 12), )

    
    osm_layer_elevation = property(__osm_layer_elevation.value, __osm_layer_elevation.set, None, None)

    
    # Element osm.layer-elevation.max-grade uses Python identifier osm_layer_elevation_max_grade
    __osm_layer_elevation_max_grade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm.layer-elevation.max-grade'), 'osm_layer_elevation_max_grade', '__AbsentNamespace0_processingType_osm_layer_elevation_max_grade', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 184, 12), )

    
    osm_layer_elevation_max_grade = property(__osm_layer_elevation_max_grade.value, __osm_layer_elevation_max_grade.set, None, None)

    
    # Element osm.oneway-spread-right uses Python identifier osm_oneway_spread_right
    __osm_oneway_spread_right = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm.oneway-spread-right'), 'osm_oneway_spread_right', '__AbsentNamespace0_processingType_osm_oneway_spread_right', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 185, 12), )

    
    osm_oneway_spread_right = property(__osm_oneway_spread_right.value, __osm_oneway_spread_right.set, None, None)

    
    # Element osm.stop-output.length uses Python identifier osm_stop_output_length
    __osm_stop_output_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'osm.stop-output.length'), 'osm_stop_output_length', '__AbsentNamespace0_processingType_osm_stop_output_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 186, 12), )

    
    osm_stop_output_length = property(__osm_stop_output_length.value, __osm_stop_output_length.set, None, None)

    
    # Element opendrive.import-all-lanes uses Python identifier opendrive_import_all_lanes
    __opendrive_import_all_lanes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive.import-all-lanes'), 'opendrive_import_all_lanes', '__AbsentNamespace0_processingType_opendrive_import_all_lanes', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 187, 12), )

    
    opendrive_import_all_lanes = property(__opendrive_import_all_lanes.value, __opendrive_import_all_lanes.set, None, None)

    
    # Element opendrive.ignore-widths uses Python identifier opendrive_ignore_widths
    __opendrive_ignore_widths = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive.ignore-widths'), 'opendrive_ignore_widths', '__AbsentNamespace0_processingType_opendrive_ignore_widths', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 188, 12), )

    
    opendrive_ignore_widths = property(__opendrive_ignore_widths.value, __opendrive_ignore_widths.set, None, None)

    
    # Element opendrive.curve-resolution uses Python identifier opendrive_curve_resolution
    __opendrive_curve_resolution = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive.curve-resolution'), 'opendrive_curve_resolution', '__AbsentNamespace0_processingType_opendrive_curve_resolution', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 189, 12), )

    
    opendrive_curve_resolution = property(__opendrive_curve_resolution.value, __opendrive_curve_resolution.set, None, None)

    
    # Element opendrive.advance-stopline uses Python identifier opendrive_advance_stopline
    __opendrive_advance_stopline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive.advance-stopline'), 'opendrive_advance_stopline', '__AbsentNamespace0_processingType_opendrive_advance_stopline', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 190, 12), )

    
    opendrive_advance_stopline = property(__opendrive_advance_stopline.value, __opendrive_advance_stopline.set, None, None)

    
    # Element opendrive.min-width uses Python identifier opendrive_min_width
    __opendrive_min_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opendrive.min-width'), 'opendrive_min_width', '__AbsentNamespace0_processingType_opendrive_min_width', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 191, 12), )

    
    opendrive_min_width = property(__opendrive_min_width.value, __opendrive_min_width.set, None, None)

    
    # Element no-internal-links uses Python identifier no_internal_links
    __no_internal_links = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-internal-links'), 'no_internal_links', '__AbsentNamespace0_processingType_no_internal_links', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 192, 12), )

    
    no_internal_links = property(__no_internal_links.value, __no_internal_links.set, None, None)

    
    # Element numerical-ids uses Python identifier numerical_ids
    __numerical_ids = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'numerical-ids'), 'numerical_ids', '__AbsentNamespace0_processingType_numerical_ids', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 193, 12), )

    
    numerical_ids = property(__numerical_ids.value, __numerical_ids.set, None, None)

    
    # Element reserved-ids uses Python identifier reserved_ids
    __reserved_ids = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'reserved-ids'), 'reserved_ids', '__AbsentNamespace0_processingType_reserved_ids', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 194, 12), )

    
    reserved_ids = property(__reserved_ids.value, __reserved_ids.set, None, None)

    
    # Element dismiss-vclasses uses Python identifier dismiss_vclasses
    __dismiss_vclasses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'dismiss-vclasses'), 'dismiss_vclasses', '__AbsentNamespace0_processingType_dismiss_vclasses', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 195, 12), )

    
    dismiss_vclasses = property(__dismiss_vclasses.value, __dismiss_vclasses.set, None, None)

    
    # Element no-turnarounds uses Python identifier no_turnarounds
    __no_turnarounds = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-turnarounds'), 'no_turnarounds', '__AbsentNamespace0_processingType_no_turnarounds', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 196, 12), )

    
    no_turnarounds = property(__no_turnarounds.value, __no_turnarounds.set, None, None)

    
    # Element no-turnarounds.tls uses Python identifier no_turnarounds_tls
    __no_turnarounds_tls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-turnarounds.tls'), 'no_turnarounds_tls', '__AbsentNamespace0_processingType_no_turnarounds_tls', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 197, 12), )

    
    no_turnarounds_tls = property(__no_turnarounds_tls.value, __no_turnarounds_tls.set, None, None)

    
    # Element no-left-connections uses Python identifier no_left_connections
    __no_left_connections = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-left-connections'), 'no_left_connections', '__AbsentNamespace0_processingType_no_left_connections', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 198, 12), )

    
    no_left_connections = property(__no_left_connections.value, __no_left_connections.set, None, None)

    
    # Element geometry.split uses Python identifier geometry_split
    __geometry_split = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.split'), 'geometry_split', '__AbsentNamespace0_processingType_geometry_split', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 199, 12), )

    
    geometry_split = property(__geometry_split.value, __geometry_split.set, None, None)

    
    # Element geometry.remove uses Python identifier geometry_remove
    __geometry_remove = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.remove'), 'geometry_remove', '__AbsentNamespace0_processingType_geometry_remove', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 200, 12), )

    
    geometry_remove = property(__geometry_remove.value, __geometry_remove.set, None, None)

    
    # Element geometry.remove.keep-edges.explicit uses Python identifier geometry_remove_keep_edges_explicit
    __geometry_remove_keep_edges_explicit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.remove.keep-edges.explicit'), 'geometry_remove_keep_edges_explicit', '__AbsentNamespace0_processingType_geometry_remove_keep_edges_explicit', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 201, 12), )

    
    geometry_remove_keep_edges_explicit = property(__geometry_remove_keep_edges_explicit.value, __geometry_remove_keep_edges_explicit.set, None, None)

    
    # Element geometry.remove.keep-edges.input-file uses Python identifier geometry_remove_keep_edges_input_file
    __geometry_remove_keep_edges_input_file = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.remove.keep-edges.input-file'), 'geometry_remove_keep_edges_input_file', '__AbsentNamespace0_processingType_geometry_remove_keep_edges_input_file', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 202, 12), )

    
    geometry_remove_keep_edges_input_file = property(__geometry_remove_keep_edges_input_file.value, __geometry_remove_keep_edges_input_file.set, None, None)

    
    # Element geometry.max-segment-length uses Python identifier geometry_max_segment_length
    __geometry_max_segment_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.max-segment-length'), 'geometry_max_segment_length', '__AbsentNamespace0_processingType_geometry_max_segment_length', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 203, 12), )

    
    geometry_max_segment_length = property(__geometry_max_segment_length.value, __geometry_max_segment_length.set, None, None)

    
    # Element geometry.min-dist uses Python identifier geometry_min_dist
    __geometry_min_dist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.min-dist'), 'geometry_min_dist', '__AbsentNamespace0_processingType_geometry_min_dist', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 204, 12), )

    
    geometry_min_dist = property(__geometry_min_dist.value, __geometry_min_dist.set, None, None)

    
    # Element geometry.max-angle uses Python identifier geometry_max_angle
    __geometry_max_angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.max-angle'), 'geometry_max_angle', '__AbsentNamespace0_processingType_geometry_max_angle', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 205, 12), )

    
    geometry_max_angle = property(__geometry_max_angle.value, __geometry_max_angle.set, None, None)

    
    # Element geometry.min-radius uses Python identifier geometry_min_radius
    __geometry_min_radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.min-radius'), 'geometry_min_radius', '__AbsentNamespace0_processingType_geometry_min_radius', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 206, 12), )

    
    geometry_min_radius = property(__geometry_min_radius.value, __geometry_min_radius.set, None, None)

    
    # Element geometry.min-radius.fix uses Python identifier geometry_min_radius_fix
    __geometry_min_radius_fix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.min-radius.fix'), 'geometry_min_radius_fix', '__AbsentNamespace0_processingType_geometry_min_radius_fix', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 207, 12), )

    
    geometry_min_radius_fix = property(__geometry_min_radius_fix.value, __geometry_min_radius_fix.set, None, None)

    
    # Element geometry.junction-mismatch-threshold uses Python identifier geometry_junction_mismatch_threshold
    __geometry_junction_mismatch_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.junction-mismatch-threshold'), 'geometry_junction_mismatch_threshold', '__AbsentNamespace0_processingType_geometry_junction_mismatch_threshold', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 208, 12), )

    
    geometry_junction_mismatch_threshold = property(__geometry_junction_mismatch_threshold.value, __geometry_junction_mismatch_threshold.set, None, None)

    
    # Element geometry.check-overlap uses Python identifier geometry_check_overlap
    __geometry_check_overlap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.check-overlap'), 'geometry_check_overlap', '__AbsentNamespace0_processingType_geometry_check_overlap', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 209, 12), )

    
    geometry_check_overlap = property(__geometry_check_overlap.value, __geometry_check_overlap.set, None, None)

    
    # Element geometry.check-overlap.vertical-threshold uses Python identifier geometry_check_overlap_vertical_threshold
    __geometry_check_overlap_vertical_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.check-overlap.vertical-threshold'), 'geometry_check_overlap_vertical_threshold', '__AbsentNamespace0_processingType_geometry_check_overlap_vertical_threshold', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 210, 12), )

    
    geometry_check_overlap_vertical_threshold = property(__geometry_check_overlap_vertical_threshold.value, __geometry_check_overlap_vertical_threshold.set, None, None)

    
    # Element geometry.max-grade uses Python identifier geometry_max_grade
    __geometry_max_grade = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'geometry.max-grade'), 'geometry_max_grade', '__AbsentNamespace0_processingType_geometry_max_grade', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 211, 12), )

    
    geometry_max_grade = property(__geometry_max_grade.value, __geometry_max_grade.set, None, None)

    
    # Element offset.disable-normalization uses Python identifier offset_disable_normalization
    __offset_disable_normalization = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offset.disable-normalization'), 'offset_disable_normalization', '__AbsentNamespace0_processingType_offset_disable_normalization', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 212, 12), )

    
    offset_disable_normalization = property(__offset_disable_normalization.value, __offset_disable_normalization.set, None, None)

    
    # Element offset.x uses Python identifier offset_x
    __offset_x = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offset.x'), 'offset_x', '__AbsentNamespace0_processingType_offset_x', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 213, 12), )

    
    offset_x = property(__offset_x.value, __offset_x.set, None, None)

    
    # Element offset.y uses Python identifier offset_y
    __offset_y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'offset.y'), 'offset_y', '__AbsentNamespace0_processingType_offset_y', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 214, 12), )

    
    offset_y = property(__offset_y.value, __offset_y.set, None, None)

    
    # Element flip-y-axis uses Python identifier flip_y_axis
    __flip_y_axis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'flip-y-axis'), 'flip_y_axis', '__AbsentNamespace0_processingType_flip_y_axis', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 215, 12), )

    
    flip_y_axis = property(__flip_y_axis.value, __flip_y_axis.set, None, None)

    
    # Element roundabouts.guess uses Python identifier roundabouts_guess
    __roundabouts_guess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'roundabouts.guess'), 'roundabouts_guess', '__AbsentNamespace0_processingType_roundabouts_guess', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 216, 12), )

    
    roundabouts_guess = property(__roundabouts_guess.value, __roundabouts_guess.set, None, None)

    
    # Element opposites.guess uses Python identifier opposites_guess
    __opposites_guess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opposites.guess'), 'opposites_guess', '__AbsentNamespace0_processingType_opposites_guess', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 217, 12), )

    
    opposites_guess = property(__opposites_guess.value, __opposites_guess.set, None, None)

    
    # Element opposites.guess.fix-lengths uses Python identifier opposites_guess_fix_lengths
    __opposites_guess_fix_lengths = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'opposites.guess.fix-lengths'), 'opposites_guess_fix_lengths', '__AbsentNamespace0_processingType_opposites_guess_fix_lengths', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 218, 12), )

    
    opposites_guess_fix_lengths = property(__opposites_guess_fix_lengths.value, __opposites_guess_fix_lengths.set, None, None)

    
    # Element lefthand uses Python identifier lefthand
    __lefthand = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lefthand'), 'lefthand', '__AbsentNamespace0_processingType_lefthand', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 219, 12), )

    
    lefthand = property(__lefthand.value, __lefthand.set, None, None)

    
    # Element edges.join uses Python identifier edges_join
    __edges_join = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'edges.join'), 'edges_join', '__AbsentNamespace0_processingType_edges_join', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 220, 12), )

    
    edges_join = property(__edges_join.value, __edges_join.set, None, None)

    
    # Element junctions.join uses Python identifier junctions_join
    __junctions_join = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.join'), 'junctions_join', '__AbsentNamespace0_processingType_junctions_join', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 221, 12), )

    
    junctions_join = property(__junctions_join.value, __junctions_join.set, None, None)

    
    # Element junctions.join-dist uses Python identifier junctions_join_dist
    __junctions_join_dist = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.join-dist'), 'junctions_join_dist', '__AbsentNamespace0_processingType_junctions_join_dist', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 222, 12), )

    
    junctions_join_dist = property(__junctions_join_dist.value, __junctions_join_dist.set, None, None)

    
    # Element junctions.join-exclude uses Python identifier junctions_join_exclude
    __junctions_join_exclude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.join-exclude'), 'junctions_join_exclude', '__AbsentNamespace0_processingType_junctions_join_exclude', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 223, 12), )

    
    junctions_join_exclude = property(__junctions_join_exclude.value, __junctions_join_exclude.set, None, None)

    
    # Element speed.offset uses Python identifier speed_offset
    __speed_offset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'speed.offset'), 'speed_offset', '__AbsentNamespace0_processingType_speed_offset', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 224, 12), )

    
    speed_offset = property(__speed_offset.value, __speed_offset.set, None, None)

    
    # Element speed.factor uses Python identifier speed_factor
    __speed_factor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'speed.factor'), 'speed_factor', '__AbsentNamespace0_processingType_speed_factor', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 225, 12), )

    
    speed_factor = property(__speed_factor.value, __speed_factor.set, None, None)

    
    # Element speed.minimum uses Python identifier speed_minimum
    __speed_minimum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'speed.minimum'), 'speed_minimum', '__AbsentNamespace0_processingType_speed_minimum', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 226, 12), )

    
    speed_minimum = property(__speed_minimum.value, __speed_minimum.set, None, None)

    
    # Element junctions.corner-detail uses Python identifier junctions_corner_detail
    __junctions_corner_detail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.corner-detail'), 'junctions_corner_detail', '__AbsentNamespace0_processingType_junctions_corner_detail', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 227, 12), )

    
    junctions_corner_detail = property(__junctions_corner_detail.value, __junctions_corner_detail.set, None, None)

    
    # Element junctions.internal-link-detail uses Python identifier junctions_internal_link_detail
    __junctions_internal_link_detail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.internal-link-detail'), 'junctions_internal_link_detail', '__AbsentNamespace0_processingType_junctions_internal_link_detail', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 228, 12), )

    
    junctions_internal_link_detail = property(__junctions_internal_link_detail.value, __junctions_internal_link_detail.set, None, None)

    
    # Element junctions.scurve-stretch uses Python identifier junctions_scurve_stretch
    __junctions_scurve_stretch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.scurve-stretch'), 'junctions_scurve_stretch', '__AbsentNamespace0_processingType_junctions_scurve_stretch', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 229, 12), )

    
    junctions_scurve_stretch = property(__junctions_scurve_stretch.value, __junctions_scurve_stretch.set, None, None)

    
    # Element junctions.join-turns uses Python identifier junctions_join_turns
    __junctions_join_turns = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'junctions.join-turns'), 'junctions_join_turns', '__AbsentNamespace0_processingType_junctions_join_turns', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 230, 12), )

    
    junctions_join_turns = property(__junctions_join_turns.value, __junctions_join_turns.set, None, None)

    
    # Element rectangular-lane-cut uses Python identifier rectangular_lane_cut
    __rectangular_lane_cut = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rectangular-lane-cut'), 'rectangular_lane_cut', '__AbsentNamespace0_processingType_rectangular_lane_cut', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 231, 12), )

    
    rectangular_lane_cut = property(__rectangular_lane_cut.value, __rectangular_lane_cut.set, None, None)

    
    # Element check-lane-foes.roundabout uses Python identifier check_lane_foes_roundabout
    __check_lane_foes_roundabout = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'check-lane-foes.roundabout'), 'check_lane_foes_roundabout', '__AbsentNamespace0_processingType_check_lane_foes_roundabout', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 232, 12), )

    
    check_lane_foes_roundabout = property(__check_lane_foes_roundabout.value, __check_lane_foes_roundabout.set, None, None)

    
    # Element check-lane-foes.all uses Python identifier check_lane_foes_all
    __check_lane_foes_all = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'check-lane-foes.all'), 'check_lane_foes_all', '__AbsentNamespace0_processingType_check_lane_foes_all', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 233, 12), )

    
    check_lane_foes_all = property(__check_lane_foes_all.value, __check_lane_foes_all.set, None, None)

    
    # Element sidewalks.guess uses Python identifier sidewalks_guess
    __sidewalks_guess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sidewalks.guess'), 'sidewalks_guess', '__AbsentNamespace0_processingType_sidewalks_guess', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 234, 12), )

    
    sidewalks_guess = property(__sidewalks_guess.value, __sidewalks_guess.set, None, None)

    
    # Element sidewalks.guess.max-speed uses Python identifier sidewalks_guess_max_speed
    __sidewalks_guess_max_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.max-speed'), 'sidewalks_guess_max_speed', '__AbsentNamespace0_processingType_sidewalks_guess_max_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 235, 12), )

    
    sidewalks_guess_max_speed = property(__sidewalks_guess_max_speed.value, __sidewalks_guess_max_speed.set, None, None)

    
    # Element sidewalks.guess.min-speed uses Python identifier sidewalks_guess_min_speed
    __sidewalks_guess_min_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.min-speed'), 'sidewalks_guess_min_speed', '__AbsentNamespace0_processingType_sidewalks_guess_min_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 236, 12), )

    
    sidewalks_guess_min_speed = property(__sidewalks_guess_min_speed.value, __sidewalks_guess_min_speed.set, None, None)

    
    # Element sidewalks.guess.from-permissions uses Python identifier sidewalks_guess_from_permissions
    __sidewalks_guess_from_permissions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.from-permissions'), 'sidewalks_guess_from_permissions', '__AbsentNamespace0_processingType_sidewalks_guess_from_permissions', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 237, 12), )

    
    sidewalks_guess_from_permissions = property(__sidewalks_guess_from_permissions.value, __sidewalks_guess_from_permissions.set, None, None)

    
    # Element sidewalks.guess.exclude uses Python identifier sidewalks_guess_exclude
    __sidewalks_guess_exclude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.exclude'), 'sidewalks_guess_exclude', '__AbsentNamespace0_processingType_sidewalks_guess_exclude', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 238, 12), )

    
    sidewalks_guess_exclude = property(__sidewalks_guess_exclude.value, __sidewalks_guess_exclude.set, None, None)

    
    # Element crossings.guess uses Python identifier crossings_guess
    __crossings_guess = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'crossings.guess'), 'crossings_guess', '__AbsentNamespace0_processingType_crossings_guess', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 239, 12), )

    
    crossings_guess = property(__crossings_guess.value, __crossings_guess.set, None, None)

    
    # Element crossings.guess.speed-threshold uses Python identifier crossings_guess_speed_threshold
    __crossings_guess_speed_threshold = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'crossings.guess.speed-threshold'), 'crossings_guess_speed_threshold', '__AbsentNamespace0_processingType_crossings_guess_speed_threshold', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 240, 12), )

    
    crossings_guess_speed_threshold = property(__crossings_guess_speed_threshold.value, __crossings_guess_speed_threshold.set, None, None)

    
    # Element walkingareas uses Python identifier walkingareas
    __walkingareas = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'walkingareas'), 'walkingareas', '__AbsentNamespace0_processingType_walkingareas', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 241, 12), )

    
    walkingareas = property(__walkingareas.value, __walkingareas.set, None, None)

    _ElementMap.update({
        __ignore_errors.name() : __ignore_errors,
        __ignore_errors_connections.name() : __ignore_errors_connections,
        __show_errors_connections_first_try.name() : __show_errors_connections_first_try,
        __ignore_errors_edge_type.name() : __ignore_errors_edge_type,
        __lanes_from_capacity_norm.name() : __lanes_from_capacity_norm,
        __speed_in_kmh.name() : __speed_in_kmh,
        __construction_date.name() : __construction_date,
        __plain_extend_edge_shape.name() : __plain_extend_edge_shape,
        __matsim_keep_length.name() : __matsim_keep_length,
        __matsim_lanes_from_capacity.name() : __matsim_lanes_from_capacity,
        __shapefile_street_id.name() : __shapefile_street_id,
        __shapefile_from_id.name() : __shapefile_from_id,
        __shapefile_to_id.name() : __shapefile_to_id,
        __shapefile_type_id.name() : __shapefile_type_id,
        __shapefile_use_defaults_on_failure.name() : __shapefile_use_defaults_on_failure,
        __shapefile_all_bidirectional.name() : __shapefile_all_bidirectional,
        __shapefile_guess_projection.name() : __shapefile_guess_projection,
        __vissim_join_distance.name() : __vissim_join_distance,
        __vissim_default_speed.name() : __vissim_default_speed,
        __vissim_speed_norm.name() : __vissim_speed_norm,
        __vissim_report_unset_speeds.name() : __vissim_report_unset_speeds,
        __visum_use_type_priority.name() : __visum_use_type_priority,
        __visum_use_type_laneno.name() : __visum_use_type_laneno,
        __visum_use_type_speed.name() : __visum_use_type_speed,
        __visum_connector_speeds.name() : __visum_connector_speeds,
        __visum_connectors_lane_number.name() : __visum_connectors_lane_number,
        __visum_no_connectors.name() : __visum_no_connectors,
        __visum_recompute_lane_number.name() : __visum_recompute_lane_number,
        __visum_verbose_warnings.name() : __visum_verbose_warnings,
        __osm_skip_duplicates_check.name() : __osm_skip_duplicates_check,
        __osm_elevation.name() : __osm_elevation,
        __osm_layer_elevation.name() : __osm_layer_elevation,
        __osm_layer_elevation_max_grade.name() : __osm_layer_elevation_max_grade,
        __osm_oneway_spread_right.name() : __osm_oneway_spread_right,
        __osm_stop_output_length.name() : __osm_stop_output_length,
        __opendrive_import_all_lanes.name() : __opendrive_import_all_lanes,
        __opendrive_ignore_widths.name() : __opendrive_ignore_widths,
        __opendrive_curve_resolution.name() : __opendrive_curve_resolution,
        __opendrive_advance_stopline.name() : __opendrive_advance_stopline,
        __opendrive_min_width.name() : __opendrive_min_width,
        __no_internal_links.name() : __no_internal_links,
        __numerical_ids.name() : __numerical_ids,
        __reserved_ids.name() : __reserved_ids,
        __dismiss_vclasses.name() : __dismiss_vclasses,
        __no_turnarounds.name() : __no_turnarounds,
        __no_turnarounds_tls.name() : __no_turnarounds_tls,
        __no_left_connections.name() : __no_left_connections,
        __geometry_split.name() : __geometry_split,
        __geometry_remove.name() : __geometry_remove,
        __geometry_remove_keep_edges_explicit.name() : __geometry_remove_keep_edges_explicit,
        __geometry_remove_keep_edges_input_file.name() : __geometry_remove_keep_edges_input_file,
        __geometry_max_segment_length.name() : __geometry_max_segment_length,
        __geometry_min_dist.name() : __geometry_min_dist,
        __geometry_max_angle.name() : __geometry_max_angle,
        __geometry_min_radius.name() : __geometry_min_radius,
        __geometry_min_radius_fix.name() : __geometry_min_radius_fix,
        __geometry_junction_mismatch_threshold.name() : __geometry_junction_mismatch_threshold,
        __geometry_check_overlap.name() : __geometry_check_overlap,
        __geometry_check_overlap_vertical_threshold.name() : __geometry_check_overlap_vertical_threshold,
        __geometry_max_grade.name() : __geometry_max_grade,
        __offset_disable_normalization.name() : __offset_disable_normalization,
        __offset_x.name() : __offset_x,
        __offset_y.name() : __offset_y,
        __flip_y_axis.name() : __flip_y_axis,
        __roundabouts_guess.name() : __roundabouts_guess,
        __opposites_guess.name() : __opposites_guess,
        __opposites_guess_fix_lengths.name() : __opposites_guess_fix_lengths,
        __lefthand.name() : __lefthand,
        __edges_join.name() : __edges_join,
        __junctions_join.name() : __junctions_join,
        __junctions_join_dist.name() : __junctions_join_dist,
        __junctions_join_exclude.name() : __junctions_join_exclude,
        __speed_offset.name() : __speed_offset,
        __speed_factor.name() : __speed_factor,
        __speed_minimum.name() : __speed_minimum,
        __junctions_corner_detail.name() : __junctions_corner_detail,
        __junctions_internal_link_detail.name() : __junctions_internal_link_detail,
        __junctions_scurve_stretch.name() : __junctions_scurve_stretch,
        __junctions_join_turns.name() : __junctions_join_turns,
        __rectangular_lane_cut.name() : __rectangular_lane_cut,
        __check_lane_foes_roundabout.name() : __check_lane_foes_roundabout,
        __check_lane_foes_all.name() : __check_lane_foes_all,
        __sidewalks_guess.name() : __sidewalks_guess,
        __sidewalks_guess_max_speed.name() : __sidewalks_guess_max_speed,
        __sidewalks_guess_min_speed.name() : __sidewalks_guess_min_speed,
        __sidewalks_guess_from_permissions.name() : __sidewalks_guess_from_permissions,
        __sidewalks_guess_exclude.name() : __sidewalks_guess_exclude,
        __crossings_guess.name() : __crossings_guess,
        __crossings_guess_speed_threshold.name() : __crossings_guess_speed_threshold,
        __walkingareas.name() : __walkingareas
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.processingType = processingType
Namespace.addCategoryObject('typeBinding', 'processingType', processingType)


# Complex type building_defaultsType with content type ELEMENT_ONLY
class building_defaultsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type building_defaultsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'building_defaultsType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 245, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element default.lanenumber uses Python identifier default_lanenumber
    __default_lanenumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.lanenumber'), 'default_lanenumber', '__AbsentNamespace0_building_defaultsType_default_lanenumber', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 247, 12), )

    
    default_lanenumber = property(__default_lanenumber.value, __default_lanenumber.set, None, None)

    
    # Element default.lanewidth uses Python identifier default_lanewidth
    __default_lanewidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.lanewidth'), 'default_lanewidth', '__AbsentNamespace0_building_defaultsType_default_lanewidth', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 248, 12), )

    
    default_lanewidth = property(__default_lanewidth.value, __default_lanewidth.set, None, None)

    
    # Element default.speed uses Python identifier default_speed
    __default_speed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.speed'), 'default_speed', '__AbsentNamespace0_building_defaultsType_default_speed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 249, 12), )

    
    default_speed = property(__default_speed.value, __default_speed.set, None, None)

    
    # Element default.priority uses Python identifier default_priority
    __default_priority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.priority'), 'default_priority', '__AbsentNamespace0_building_defaultsType_default_priority', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 250, 12), )

    
    default_priority = property(__default_priority.value, __default_priority.set, None, None)

    
    # Element default.sidewalk-width uses Python identifier default_sidewalk_width
    __default_sidewalk_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.sidewalk-width'), 'default_sidewalk_width', '__AbsentNamespace0_building_defaultsType_default_sidewalk_width', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 251, 12), )

    
    default_sidewalk_width = property(__default_sidewalk_width.value, __default_sidewalk_width.set, None, None)

    
    # Element default.disallow uses Python identifier default_disallow
    __default_disallow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.disallow'), 'default_disallow', '__AbsentNamespace0_building_defaultsType_default_disallow', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 252, 12), )

    
    default_disallow = property(__default_disallow.value, __default_disallow.set, None, None)

    
    # Element default.junctions.keep-clear uses Python identifier default_junctions_keep_clear
    __default_junctions_keep_clear = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.junctions.keep-clear'), 'default_junctions_keep_clear', '__AbsentNamespace0_building_defaultsType_default_junctions_keep_clear', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 253, 12), )

    
    default_junctions_keep_clear = property(__default_junctions_keep_clear.value, __default_junctions_keep_clear.set, None, None)

    
    # Element default.junctions.radius uses Python identifier default_junctions_radius
    __default_junctions_radius = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'default.junctions.radius'), 'default_junctions_radius', '__AbsentNamespace0_building_defaultsType_default_junctions_radius', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 254, 12), )

    
    default_junctions_radius = property(__default_junctions_radius.value, __default_junctions_radius.set, None, None)

    _ElementMap.update({
        __default_lanenumber.name() : __default_lanenumber,
        __default_lanewidth.name() : __default_lanewidth,
        __default_speed.name() : __default_speed,
        __default_priority.name() : __default_priority,
        __default_sidewalk_width.name() : __default_sidewalk_width,
        __default_disallow.name() : __default_disallow,
        __default_junctions_keep_clear.name() : __default_junctions_keep_clear,
        __default_junctions_radius.name() : __default_junctions_radius
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.building_defaultsType = building_defaultsType
Namespace.addCategoryObject('typeBinding', 'building_defaultsType', building_defaultsType)


# Complex type reportType with content type ELEMENT_ONLY
class reportType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type reportType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'reportType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 258, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element verbose uses Python identifier verbose
    __verbose = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'verbose'), 'verbose', '__AbsentNamespace0_reportType_verbose', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 260, 12), )

    
    verbose = property(__verbose.value, __verbose.set, None, None)

    
    # Element print-options uses Python identifier print_options
    __print_options = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'print-options'), 'print_options', '__AbsentNamespace0_reportType_print_options', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 261, 12), )

    
    print_options = property(__print_options.value, __print_options.set, None, None)

    
    # Element help uses Python identifier help
    __help = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'help'), 'help', '__AbsentNamespace0_reportType_help', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 262, 12), )

    
    help = property(__help.value, __help.set, None, None)

    
    # Element version uses Python identifier version
    __version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_reportType_version', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 263, 12), )

    
    version = property(__version.value, __version.set, None, None)

    
    # Element xml-validation uses Python identifier xml_validation
    __xml_validation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xml-validation'), 'xml_validation', '__AbsentNamespace0_reportType_xml_validation', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 264, 12), )

    
    xml_validation = property(__xml_validation.value, __xml_validation.set, None, None)

    
    # Element xml-validation.net uses Python identifier xml_validation_net
    __xml_validation_net = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'xml-validation.net'), 'xml_validation_net', '__AbsentNamespace0_reportType_xml_validation_net', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 265, 12), )

    
    xml_validation_net = property(__xml_validation_net.value, __xml_validation_net.set, None, None)

    
    # Element no-warnings uses Python identifier no_warnings
    __no_warnings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'no-warnings'), 'no_warnings', '__AbsentNamespace0_reportType_no_warnings', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 266, 12), )

    
    no_warnings = property(__no_warnings.value, __no_warnings.set, None, None)

    
    # Element log uses Python identifier log
    __log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'log'), 'log', '__AbsentNamespace0_reportType_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 267, 12), )

    
    log = property(__log.value, __log.set, None, None)

    
    # Element message-log uses Python identifier message_log
    __message_log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'message-log'), 'message_log', '__AbsentNamespace0_reportType_message_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 268, 12), )

    
    message_log = property(__message_log.value, __message_log.set, None, None)

    
    # Element error-log uses Python identifier error_log
    __error_log = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'error-log'), 'error_log', '__AbsentNamespace0_reportType_error_log', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 269, 12), )

    
    error_log = property(__error_log.value, __error_log.set, None, None)

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
        __error_log.name() : __error_log
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.reportType = reportType
Namespace.addCategoryObject('typeBinding', 'reportType', reportType)


# Complex type random_numberType with content type ELEMENT_ONLY
class random_numberType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type random_numberType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'random_numberType')
    _XSDLocation = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 273, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element random uses Python identifier random
    __random = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'random'), 'random', '__AbsentNamespace0_random_numberType_random', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 275, 12), )

    
    random = property(__random.value, __random.set, None, None)

    
    # Element seed uses Python identifier seed
    __seed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'seed'), 'seed', '__AbsentNamespace0_random_numberType_seed', False, pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 276, 12), )

    
    seed = property(__seed.value, __seed.set, None, None)

    _ElementMap.update({
        __random.name() : __random,
        __seed.name() : __seed
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.random_numberType = random_numberType
Namespace.addCategoryObject('typeBinding', 'random_numberType', random_numberType)


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


configuration = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'configuration'), configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 6, 4))
Namespace.addCategoryObject('elementBinding', configuration.name().localName(), configuration)



configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'input'), inputType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 10, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output'), outputType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 11, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'projection'), projectionType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 12, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls_building'), tls_buildingType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 13, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramp_guessing'), ramp_guessingType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 14, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edge_removal'), edge_removalType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 15, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'unregulated_nodes'), unregulated_nodesType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 16, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'processing'), processingType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 17, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_defaults'), building_defaultsType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 18, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'report'), reportType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 19, 12)))

configurationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'random_number'), random_numberType, scope=configurationType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 20, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 10, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'input')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 10, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 11, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 11, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 12, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'projection')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 12, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 13, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls_building')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 13, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 14, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramp_guessing')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 14, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 15, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'edge_removal')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 15, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 16, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'unregulated_nodes')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 16, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 17, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'processing')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 17, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 18, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_defaults')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 18, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 19, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'report')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 19, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 20, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(configurationType._UseForTag(pyxb.namespace.ExpandedName(None, 'random_number')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 20, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 10, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 11, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 12, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 13, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 14, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 15, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 16, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 17, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 18, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 19, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 20, 12))
    counters.add(cc_10)
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
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 9, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
configurationType._Automaton = _BuildAutomaton()




inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sumo-net-file'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 26, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'node-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 27, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edge-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 28, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'connection-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 29, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tllogic-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 30, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 31, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile-prefix'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 32, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dlr-navteq-prefix'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 33, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 34, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 35, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum-file'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 36, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vissim-file'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 37, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'robocup-dir'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 38, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'matsim-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 39, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'itsumo-files'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 40, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'heightmap.shapefiles'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 41, 12)))

inputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'heightmap.geotiff'), fileOptionType, scope=inputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 42, 12)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 26, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'sumo-net-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 26, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 27, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'node-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 27, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 28, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'edge-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 28, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 29, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'connection-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 29, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 30, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'tllogic-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 30, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 31, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'type-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 31, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 32, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile-prefix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 32, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 33, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'dlr-navteq-prefix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 33, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 34, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 34, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 35, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 35, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 36, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 36, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 37, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'vissim-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 37, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 38, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'robocup-dir')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 38, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 39, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'matsim-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 40, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'itsumo-files')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 40, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 41, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'heightmap.shapefiles')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 41, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 42, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(inputType._UseForTag(pyxb.namespace.ExpandedName(None, 'heightmap.geotiff')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 42, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 26, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 27, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 28, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 29, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 30, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 31, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 32, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 33, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 34, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 35, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 36, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 37, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 38, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 39, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 40, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 41, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 42, 12))
    counters.add(cc_16)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    sub_automata.append(_BuildAutomaton_27())
    sub_automata.append(_BuildAutomaton_28())
    sub_automata.append(_BuildAutomaton_29())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 25, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
inputType._Automaton = _BuildAutomaton_12()




outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-prefix'), strOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 48, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'precision'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 49, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'precision.geo'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 50, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output-file'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 51, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'plain-output-prefix'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 52, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.join-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 53, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'amitran-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 54, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'matsim-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 55, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 56, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dlr-navteq-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 57, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dlr-navteq.precision'), intOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 58, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output.street-names'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 59, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'output.original-names'), boolOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 60, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'street-sign-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 61, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ptstop-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 62, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ptline-output'), fileOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 63, 12)))

outputType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive-output.straight-threshold'), floatOptionType, scope=outputType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 64, 12)))

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 48, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'output-prefix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 48, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 49, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'precision')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 49, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 50, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'precision.geo')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 50, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 51, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'output-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 51, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 52, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'plain-output-prefix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 52, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 53, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.join-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 53, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 54, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'amitran-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 54, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 55, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'matsim-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 55, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 56, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 56, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 57, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'dlr-navteq-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 57, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 58, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'dlr-navteq.precision')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 58, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 59, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'output.street-names')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 59, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 60, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'output.original-names')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 60, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 61, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'street-sign-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 61, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 62, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'ptstop-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 62, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 63, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'ptline-output')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 63, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 64, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(outputType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive-output.straight-threshold')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 64, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 48, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 49, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 50, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 51, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 52, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 53, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 54, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 55, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 56, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 57, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 58, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 59, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 60, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 61, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 62, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 63, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 64, 12))
    counters.add(cc_16)
    states = []
    sub_automata = []
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
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 47, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
outputType._Automaton = _BuildAutomaton_30()




projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'simple-projection'), boolOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 70, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj.scale'), floatOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 71, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj.utm'), boolOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 72, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj.dhdn'), boolOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 73, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj'), strOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 74, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj.inverse'), boolOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 75, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj.dhdnutm'), boolOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 76, 12)))

projectionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'proj.plain-geo'), boolOptionType, scope=projectionType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 77, 12)))

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 70, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'simple-projection')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 70, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 71, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj.scale')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 71, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 72, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj.utm')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 72, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 73, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj.dhdn')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 73, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 74, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 74, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 75, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj.inverse')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 75, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 76, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj.dhdnutm')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 76, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 77, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(projectionType._UseForTag(pyxb.namespace.ExpandedName(None, 'proj.plain-geo')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 77, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 70, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 71, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 72, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 73, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 74, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 75, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 76, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 77, 12))
    counters.add(cc_7)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_49())
    sub_automata.append(_BuildAutomaton_50())
    sub_automata.append(_BuildAutomaton_51())
    sub_automata.append(_BuildAutomaton_52())
    sub_automata.append(_BuildAutomaton_53())
    sub_automata.append(_BuildAutomaton_54())
    sub_automata.append(_BuildAutomaton_55())
    sub_automata.append(_BuildAutomaton_56())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 69, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
projectionType._Automaton = _BuildAutomaton_48()




tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.discard-loaded'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 83, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.discard-simple'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 84, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.set'), strOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 85, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.unset'), strOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 86, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.guess'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 87, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.taz-nodes'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 88, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls-guess.joining'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 89, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.join'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 90, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.join-dist'), floatOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 91, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.uncontrolled-within'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 92, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.guess-signals'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 93, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.guess-signals.dist'), floatOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 94, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.cycle.time'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 95, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.green.time'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 96, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.yellow.min-decel'), floatOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 97, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.yellow.patch-small'), boolOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 98, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.yellow.time'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 99, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.red.time'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 100, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.allred.time'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 101, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.left-green.time'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 102, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.half-offset'), strOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 103, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.quarter-offset'), strOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 104, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.default-type'), strOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 105, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.min-dur'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 106, 12)))

tls_buildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tls.max-dur'), intOptionType, scope=tls_buildingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 107, 12)))

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 83, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.discard-loaded')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 83, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 84, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.discard-simple')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 84, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 85, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.set')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 85, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 86, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.unset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 86, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 87, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.guess')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 87, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 88, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.taz-nodes')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 88, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 89, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls-guess.joining')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 89, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 90, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.join')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 90, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 91, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.join-dist')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 91, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 92, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.uncontrolled-within')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 92, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 93, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.guess-signals')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 93, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 94, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.guess-signals.dist')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 94, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 95, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.cycle.time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 95, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 96, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.green.time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 96, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 97, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.yellow.min-decel')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 97, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 98, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.yellow.patch-small')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 98, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 99, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.yellow.time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 99, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 100, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.red.time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 100, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 101, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.allred.time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 101, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 102, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.left-green.time')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 102, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 103, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.half-offset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 103, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 104, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.quarter-offset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 104, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 105, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.default-type')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 105, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 106, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.min-dur')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 106, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 107, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tls_buildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tls.max-dur')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 107, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 83, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 84, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 85, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 86, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 87, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 88, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 89, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 90, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 91, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 92, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 93, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 94, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 95, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 96, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 97, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 98, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 99, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 100, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 101, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 102, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 103, 12))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 104, 12))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 105, 12))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 106, 12))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 107, 12))
    counters.add(cc_24)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_58())
    sub_automata.append(_BuildAutomaton_59())
    sub_automata.append(_BuildAutomaton_60())
    sub_automata.append(_BuildAutomaton_61())
    sub_automata.append(_BuildAutomaton_62())
    sub_automata.append(_BuildAutomaton_63())
    sub_automata.append(_BuildAutomaton_64())
    sub_automata.append(_BuildAutomaton_65())
    sub_automata.append(_BuildAutomaton_66())
    sub_automata.append(_BuildAutomaton_67())
    sub_automata.append(_BuildAutomaton_68())
    sub_automata.append(_BuildAutomaton_69())
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
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 82, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tls_buildingType._Automaton = _BuildAutomaton_57()




ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.guess'), boolOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 113, 12)))

ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.max-ramp-speed'), floatOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 114, 12)))

ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.min-highway-speed'), floatOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 115, 12)))

ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.ramp-length'), floatOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 116, 12)))

ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.set'), strOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 117, 12)))

ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.unset'), strOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 118, 12)))

ramp_guessingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ramps.no-split'), boolOptionType, scope=ramp_guessingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 119, 12)))

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 113, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.guess')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 113, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 114, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.max-ramp-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 114, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 115, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.min-highway-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 115, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 116, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.ramp-length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 116, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 117, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.set')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 117, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 118, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.unset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 118, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 119, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ramp_guessingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ramps.no-split')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 119, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 113, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 114, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 115, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 116, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 117, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 118, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 119, 12))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_84())
    sub_automata.append(_BuildAutomaton_85())
    sub_automata.append(_BuildAutomaton_86())
    sub_automata.append(_BuildAutomaton_87())
    sub_automata.append(_BuildAutomaton_88())
    sub_automata.append(_BuildAutomaton_89())
    sub_automata.append(_BuildAutomaton_90())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 112, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ramp_guessingType._Automaton = _BuildAutomaton_83()




edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.min-speed'), floatOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 125, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remove-edges.explicit'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 126, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.explicit'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 127, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.input-file'), fileOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 128, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remove-edges.input-file'), fileOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 129, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.postload'), boolOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 130, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.in-boundary'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 131, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.in-geo-boundary'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 132, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.by-vclass'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 133, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remove-edges.by-vclass'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 134, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.by-type'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 135, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-edges.components'), intOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 136, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remove-edges.by-type'), strOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 137, 12)))

edge_removalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'remove-edges.isolated'), boolOptionType, scope=edge_removalType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 138, 12)))

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 125, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.min-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 125, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 126, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'remove-edges.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 126, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 127, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 127, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 128, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.input-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 128, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 129, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'remove-edges.input-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 129, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 130, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.postload')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 130, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 131, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.in-boundary')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 131, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 132, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.in-geo-boundary')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 132, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 133, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.by-vclass')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 133, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 134, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'remove-edges.by-vclass')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 134, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 135, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.by-type')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 135, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 136, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-edges.components')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 136, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 137, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'remove-edges.by-type')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 137, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 138, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(edge_removalType._UseForTag(pyxb.namespace.ExpandedName(None, 'remove-edges.isolated')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 138, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 125, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 126, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 127, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 128, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 129, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 130, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 131, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 132, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 133, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 134, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 135, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 136, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 137, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 138, 12))
    counters.add(cc_13)
    states = []
    sub_automata = []
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
    sub_automata.append(_BuildAutomaton_102())
    sub_automata.append(_BuildAutomaton_103())
    sub_automata.append(_BuildAutomaton_104())
    sub_automata.append(_BuildAutomaton_105())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 124, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
edge_removalType._Automaton = _BuildAutomaton_91()




unregulated_nodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated'), boolOptionType, scope=unregulated_nodesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 144, 12)))

unregulated_nodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated.explicit'), strOptionType, scope=unregulated_nodesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 145, 12)))

unregulated_nodesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated.district-nodes'), boolOptionType, scope=unregulated_nodesType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 146, 12)))

def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 144, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(unregulated_nodesType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 144, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 145, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(unregulated_nodesType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 145, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 146, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(unregulated_nodesType._UseForTag(pyxb.namespace.ExpandedName(None, 'keep-nodes-unregulated.district-nodes')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 146, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 144, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 145, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 146, 12))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_107())
    sub_automata.append(_BuildAutomaton_108())
    sub_automata.append(_BuildAutomaton_109())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 143, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
unregulated_nodesType._Automaton = _BuildAutomaton_106()




processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore-errors'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 152, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore-errors.connections'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 153, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'show-errors.connections-first-try'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 154, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ignore-errors.edge-type'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 155, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lanes-from-capacity.norm'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 156, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'speed-in-kmh'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 157, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction-date'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 158, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'plain.extend-edge-shape'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 159, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'matsim.keep-length'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 160, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'matsim.lanes-from-capacity'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 161, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.street-id'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 162, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.from-id'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 163, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.to-id'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 164, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.type-id'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 165, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.use-defaults-on-failure'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 166, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.all-bidirectional'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 167, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shapefile.guess-projection'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 168, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vissim.join-distance'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 169, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vissim.default-speed'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 170, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vissim.speed-norm'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 171, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'vissim.report-unset-speeds'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 172, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.use-type-priority'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 173, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.use-type-laneno'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 174, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.use-type-speed'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 175, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.connector-speeds'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 176, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.connectors-lane-number'), intOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 177, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.no-connectors'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 178, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.recompute-lane-number'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 179, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'visum.verbose-warnings'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 180, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm.skip-duplicates-check'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 181, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm.elevation'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 182, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm.layer-elevation'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 183, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm.layer-elevation.max-grade'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 184, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm.oneway-spread-right'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 185, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'osm.stop-output.length'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 186, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive.import-all-lanes'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 187, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive.ignore-widths'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 188, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive.curve-resolution'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 189, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive.advance-stopline'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 190, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opendrive.min-width'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 191, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-internal-links'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 192, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'numerical-ids'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 193, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'reserved-ids'), fileOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 194, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'dismiss-vclasses'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 195, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-turnarounds'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 196, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-turnarounds.tls'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 197, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-left-connections'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 198, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.split'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 199, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.remove'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 200, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.remove.keep-edges.explicit'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 201, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.remove.keep-edges.input-file'), fileOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 202, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.max-segment-length'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 203, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.min-dist'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 204, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.max-angle'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 205, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.min-radius'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 206, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.min-radius.fix'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 207, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.junction-mismatch-threshold'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 208, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.check-overlap'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 209, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.check-overlap.vertical-threshold'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 210, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'geometry.max-grade'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 211, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offset.disable-normalization'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 212, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offset.x'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 213, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'offset.y'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 214, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'flip-y-axis'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 215, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'roundabouts.guess'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 216, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opposites.guess'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 217, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'opposites.guess.fix-lengths'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 218, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lefthand'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 219, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'edges.join'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 220, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.join'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 221, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.join-dist'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 222, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.join-exclude'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 223, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'speed.offset'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 224, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'speed.factor'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 225, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'speed.minimum'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 226, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.corner-detail'), intOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 227, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.internal-link-detail'), intOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 228, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.scurve-stretch'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 229, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'junctions.join-turns'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 230, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rectangular-lane-cut'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 231, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'check-lane-foes.roundabout'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 232, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'check-lane-foes.all'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 233, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sidewalks.guess'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 234, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.max-speed'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 235, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.min-speed'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 236, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.from-permissions'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 237, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.exclude'), strOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 238, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'crossings.guess'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 239, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'crossings.guess.speed-threshold'), floatOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 240, 12)))

processingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'walkingareas'), boolOptionType, scope=processingType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 241, 12)))

def _BuildAutomaton_111 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 152, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore-errors')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 152, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 153, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore-errors.connections')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 153, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 154, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'show-errors.connections-first-try')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 154, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 155, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ignore-errors.edge-type')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 155, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 156, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'lanes-from-capacity.norm')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 156, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 157, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'speed-in-kmh')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 157, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 158, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction-date')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 158, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 159, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'plain.extend-edge-shape')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 159, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_119 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_119
    del _BuildAutomaton_119
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 160, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'matsim.keep-length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 160, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 161, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'matsim.lanes-from-capacity')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 161, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 162, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.street-id')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 162, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 163, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.from-id')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 163, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 164, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.to-id')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 164, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 165, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.type-id')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 165, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 166, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.use-defaults-on-failure')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 166, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 167, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.all-bidirectional')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 167, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 168, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'shapefile.guess-projection')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 168, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 169, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'vissim.join-distance')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 169, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 170, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'vissim.default-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 170, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 171, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'vissim.speed-norm')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 171, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 172, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'vissim.report-unset-speeds')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 172, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 173, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.use-type-priority')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_133 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_133
    del _BuildAutomaton_133
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 174, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.use-type-laneno')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 174, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 175, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.use-type-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 175, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 176, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.connector-speeds')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 176, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 177, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.connectors-lane-number')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 177, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 178, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.no-connectors')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 178, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_138 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_138
    del _BuildAutomaton_138
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 179, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.recompute-lane-number')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 179, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 180, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'visum.verbose-warnings')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 180, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 181, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm.skip-duplicates-check')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 181, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 182, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm.elevation')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 182, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 183, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm.layer-elevation')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 183, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 184, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm.layer-elevation.max-grade')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 184, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 185, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm.oneway-spread-right')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 185, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 186, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'osm.stop-output.length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 186, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 187, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive.import-all-lanes')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 187, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 188, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive.ignore-widths')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 188, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_148 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_148
    del _BuildAutomaton_148
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 189, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive.curve-resolution')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 189, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 190, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive.advance-stopline')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 190, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 191, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opendrive.min-width')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 191, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 192, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-internal-links')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 192, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_152 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_152
    del _BuildAutomaton_152
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 193, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'numerical-ids')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 193, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 194, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'reserved-ids')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 194, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 195, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'dismiss-vclasses')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 195, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 196, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-turnarounds')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 196, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 197, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-turnarounds.tls')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 197, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_157 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_157
    del _BuildAutomaton_157
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 198, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-left-connections')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 198, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 199, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.split')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 199, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 200, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.remove')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 200, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 201, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.remove.keep-edges.explicit')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 201, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 202, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.remove.keep-edges.input-file')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 202, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 203, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.max-segment-length')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 203, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 204, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.min-dist')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 204, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 205, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.max-angle')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 205, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 206, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.min-radius')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 206, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 207, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.min-radius.fix')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 207, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_167 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_167
    del _BuildAutomaton_167
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 208, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.junction-mismatch-threshold')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 208, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 209, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.check-overlap')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 209, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 210, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.check-overlap.vertical-threshold')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 210, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 211, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'geometry.max-grade')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 211, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 212, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'offset.disable-normalization')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 212, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_172 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_172
    del _BuildAutomaton_172
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 213, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'offset.x')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 213, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 214, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'offset.y')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 214, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 215, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'flip-y-axis')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 215, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 216, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'roundabouts.guess')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 216, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_176 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_176
    del _BuildAutomaton_176
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 217, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opposites.guess')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 217, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 218, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'opposites.guess.fix-lengths')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 218, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 219, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'lefthand')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 219, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 220, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'edges.join')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 220, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 221, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.join')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 221, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 222, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.join-dist')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 222, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 223, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.join-exclude')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 223, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 224, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'speed.offset')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 224, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 225, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'speed.factor')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 225, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 226, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'speed.minimum')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 226, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 227, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.corner-detail')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 227, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 228, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.internal-link-detail')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 228, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 229, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.scurve-stretch')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 229, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 230, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'junctions.join-turns')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 230, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 231, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'rectangular-lane-cut')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 231, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_191 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_191
    del _BuildAutomaton_191
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 232, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'check-lane-foes.roundabout')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 232, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 233, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'check-lane-foes.all')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 233, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 234, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'sidewalks.guess')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 234, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_194 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_194
    del _BuildAutomaton_194
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 235, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.max-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 235, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 236, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.min-speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 236, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 237, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.from-permissions')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 237, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 238, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'sidewalks.guess.exclude')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 238, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 239, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'crossings.guess')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 239, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 240, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'crossings.guess.speed-threshold')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 240, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 241, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(processingType._UseForTag(pyxb.namespace.ExpandedName(None, 'walkingareas')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 241, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 152, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 153, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 154, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 155, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 156, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 157, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 158, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 159, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 160, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 161, 12))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 162, 12))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 163, 12))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 164, 12))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 165, 12))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 166, 12))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 167, 12))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 168, 12))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 169, 12))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 170, 12))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 171, 12))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 172, 12))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 173, 12))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 174, 12))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 175, 12))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 176, 12))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 177, 12))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 178, 12))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 179, 12))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 180, 12))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 181, 12))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 182, 12))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 183, 12))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 184, 12))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 185, 12))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 186, 12))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 187, 12))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 188, 12))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 189, 12))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 190, 12))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 191, 12))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 192, 12))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 193, 12))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 194, 12))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 195, 12))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 196, 12))
    counters.add(cc_44)
    cc_45 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 197, 12))
    counters.add(cc_45)
    cc_46 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 198, 12))
    counters.add(cc_46)
    cc_47 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 199, 12))
    counters.add(cc_47)
    cc_48 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 200, 12))
    counters.add(cc_48)
    cc_49 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 201, 12))
    counters.add(cc_49)
    cc_50 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 202, 12))
    counters.add(cc_50)
    cc_51 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 203, 12))
    counters.add(cc_51)
    cc_52 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 204, 12))
    counters.add(cc_52)
    cc_53 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 205, 12))
    counters.add(cc_53)
    cc_54 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 206, 12))
    counters.add(cc_54)
    cc_55 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 207, 12))
    counters.add(cc_55)
    cc_56 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 208, 12))
    counters.add(cc_56)
    cc_57 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 209, 12))
    counters.add(cc_57)
    cc_58 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 210, 12))
    counters.add(cc_58)
    cc_59 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 211, 12))
    counters.add(cc_59)
    cc_60 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 212, 12))
    counters.add(cc_60)
    cc_61 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 213, 12))
    counters.add(cc_61)
    cc_62 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 214, 12))
    counters.add(cc_62)
    cc_63 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 215, 12))
    counters.add(cc_63)
    cc_64 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 216, 12))
    counters.add(cc_64)
    cc_65 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 217, 12))
    counters.add(cc_65)
    cc_66 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 218, 12))
    counters.add(cc_66)
    cc_67 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 219, 12))
    counters.add(cc_67)
    cc_68 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 220, 12))
    counters.add(cc_68)
    cc_69 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 221, 12))
    counters.add(cc_69)
    cc_70 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 222, 12))
    counters.add(cc_70)
    cc_71 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 223, 12))
    counters.add(cc_71)
    cc_72 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 224, 12))
    counters.add(cc_72)
    cc_73 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 225, 12))
    counters.add(cc_73)
    cc_74 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 226, 12))
    counters.add(cc_74)
    cc_75 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 227, 12))
    counters.add(cc_75)
    cc_76 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 228, 12))
    counters.add(cc_76)
    cc_77 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 229, 12))
    counters.add(cc_77)
    cc_78 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 230, 12))
    counters.add(cc_78)
    cc_79 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 231, 12))
    counters.add(cc_79)
    cc_80 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 232, 12))
    counters.add(cc_80)
    cc_81 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 233, 12))
    counters.add(cc_81)
    cc_82 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 234, 12))
    counters.add(cc_82)
    cc_83 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 235, 12))
    counters.add(cc_83)
    cc_84 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 236, 12))
    counters.add(cc_84)
    cc_85 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 237, 12))
    counters.add(cc_85)
    cc_86 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 238, 12))
    counters.add(cc_86)
    cc_87 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 239, 12))
    counters.add(cc_87)
    cc_88 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 240, 12))
    counters.add(cc_88)
    cc_89 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 241, 12))
    counters.add(cc_89)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_111())
    sub_automata.append(_BuildAutomaton_112())
    sub_automata.append(_BuildAutomaton_113())
    sub_automata.append(_BuildAutomaton_114())
    sub_automata.append(_BuildAutomaton_115())
    sub_automata.append(_BuildAutomaton_116())
    sub_automata.append(_BuildAutomaton_117())
    sub_automata.append(_BuildAutomaton_118())
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
    sub_automata.append(_BuildAutomaton_132())
    sub_automata.append(_BuildAutomaton_133())
    sub_automata.append(_BuildAutomaton_134())
    sub_automata.append(_BuildAutomaton_135())
    sub_automata.append(_BuildAutomaton_136())
    sub_automata.append(_BuildAutomaton_137())
    sub_automata.append(_BuildAutomaton_138())
    sub_automata.append(_BuildAutomaton_139())
    sub_automata.append(_BuildAutomaton_140())
    sub_automata.append(_BuildAutomaton_141())
    sub_automata.append(_BuildAutomaton_142())
    sub_automata.append(_BuildAutomaton_143())
    sub_automata.append(_BuildAutomaton_144())
    sub_automata.append(_BuildAutomaton_145())
    sub_automata.append(_BuildAutomaton_146())
    sub_automata.append(_BuildAutomaton_147())
    sub_automata.append(_BuildAutomaton_148())
    sub_automata.append(_BuildAutomaton_149())
    sub_automata.append(_BuildAutomaton_150())
    sub_automata.append(_BuildAutomaton_151())
    sub_automata.append(_BuildAutomaton_152())
    sub_automata.append(_BuildAutomaton_153())
    sub_automata.append(_BuildAutomaton_154())
    sub_automata.append(_BuildAutomaton_155())
    sub_automata.append(_BuildAutomaton_156())
    sub_automata.append(_BuildAutomaton_157())
    sub_automata.append(_BuildAutomaton_158())
    sub_automata.append(_BuildAutomaton_159())
    sub_automata.append(_BuildAutomaton_160())
    sub_automata.append(_BuildAutomaton_161())
    sub_automata.append(_BuildAutomaton_162())
    sub_automata.append(_BuildAutomaton_163())
    sub_automata.append(_BuildAutomaton_164())
    sub_automata.append(_BuildAutomaton_165())
    sub_automata.append(_BuildAutomaton_166())
    sub_automata.append(_BuildAutomaton_167())
    sub_automata.append(_BuildAutomaton_168())
    sub_automata.append(_BuildAutomaton_169())
    sub_automata.append(_BuildAutomaton_170())
    sub_automata.append(_BuildAutomaton_171())
    sub_automata.append(_BuildAutomaton_172())
    sub_automata.append(_BuildAutomaton_173())
    sub_automata.append(_BuildAutomaton_174())
    sub_automata.append(_BuildAutomaton_175())
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
    sub_automata.append(_BuildAutomaton_190())
    sub_automata.append(_BuildAutomaton_191())
    sub_automata.append(_BuildAutomaton_192())
    sub_automata.append(_BuildAutomaton_193())
    sub_automata.append(_BuildAutomaton_194())
    sub_automata.append(_BuildAutomaton_195())
    sub_automata.append(_BuildAutomaton_196())
    sub_automata.append(_BuildAutomaton_197())
    sub_automata.append(_BuildAutomaton_198())
    sub_automata.append(_BuildAutomaton_199())
    sub_automata.append(_BuildAutomaton_200())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 151, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
processingType._Automaton = _BuildAutomaton_110()




building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.lanenumber'), intOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 247, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.lanewidth'), floatOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 248, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.speed'), floatOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 249, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.priority'), intOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 250, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.sidewalk-width'), floatOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 251, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.disallow'), strOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 252, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.junctions.keep-clear'), boolOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 253, 12)))

building_defaultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'default.junctions.radius'), floatOptionType, scope=building_defaultsType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 254, 12)))

def _BuildAutomaton_202 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_202
    del _BuildAutomaton_202
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 247, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.lanenumber')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 247, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 248, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.lanewidth')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 248, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 249, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.speed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 249, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 250, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.priority')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 250, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_206 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_206
    del _BuildAutomaton_206
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 251, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.sidewalk-width')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 251, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_207 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_207
    del _BuildAutomaton_207
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 252, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.disallow')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 252, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_208 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_208
    del _BuildAutomaton_208
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 253, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.junctions.keep-clear')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 253, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_209 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_209
    del _BuildAutomaton_209
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 254, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(building_defaultsType._UseForTag(pyxb.namespace.ExpandedName(None, 'default.junctions.radius')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 254, 12))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 247, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 248, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 249, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 250, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 251, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 252, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 253, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 254, 12))
    counters.add(cc_7)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_202())
    sub_automata.append(_BuildAutomaton_203())
    sub_automata.append(_BuildAutomaton_204())
    sub_automata.append(_BuildAutomaton_205())
    sub_automata.append(_BuildAutomaton_206())
    sub_automata.append(_BuildAutomaton_207())
    sub_automata.append(_BuildAutomaton_208())
    sub_automata.append(_BuildAutomaton_209())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 246, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
building_defaultsType._Automaton = _BuildAutomaton_201()




reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'verbose'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 260, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'print-options'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 261, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'help'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 262, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'version'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 263, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xml-validation'), strOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 264, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'xml-validation.net'), strOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 265, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'no-warnings'), boolOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 266, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'log'), fileOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 267, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'message-log'), fileOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 268, 12)))

reportType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'error-log'), fileOptionType, scope=reportType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 269, 12)))

def _BuildAutomaton_211 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_211
    del _BuildAutomaton_211
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 260, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'verbose')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 260, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_212 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_212
    del _BuildAutomaton_212
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 261, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'print-options')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 261, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_213 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_213
    del _BuildAutomaton_213
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 262, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'help')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 262, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_214 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_214
    del _BuildAutomaton_214
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 263, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'version')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 263, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_215 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_215
    del _BuildAutomaton_215
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 264, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'xml-validation')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 264, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_216 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_216
    del _BuildAutomaton_216
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 265, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'xml-validation.net')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 265, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_217 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_217
    del _BuildAutomaton_217
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 266, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'no-warnings')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 266, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_218 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_218
    del _BuildAutomaton_218
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 267, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 267, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_219 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_219
    del _BuildAutomaton_219
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 268, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'message-log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 268, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_220 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_220
    del _BuildAutomaton_220
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 269, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(reportType._UseForTag(pyxb.namespace.ExpandedName(None, 'error-log')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 269, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_210 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_210
    del _BuildAutomaton_210
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 260, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 261, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 262, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 263, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 264, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 265, 12))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 266, 12))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 267, 12))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 268, 12))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 269, 12))
    counters.add(cc_9)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_211())
    sub_automata.append(_BuildAutomaton_212())
    sub_automata.append(_BuildAutomaton_213())
    sub_automata.append(_BuildAutomaton_214())
    sub_automata.append(_BuildAutomaton_215())
    sub_automata.append(_BuildAutomaton_216())
    sub_automata.append(_BuildAutomaton_217())
    sub_automata.append(_BuildAutomaton_218())
    sub_automata.append(_BuildAutomaton_219())
    sub_automata.append(_BuildAutomaton_220())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 259, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
reportType._Automaton = _BuildAutomaton_210()




random_numberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'random'), boolOptionType, scope=random_numberType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 275, 12)))

random_numberType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'seed'), intOptionType, scope=random_numberType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 276, 12)))

def _BuildAutomaton_222 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_222
    del _BuildAutomaton_222
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 275, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(random_numberType._UseForTag(pyxb.namespace.ExpandedName(None, 'random')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 275, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_223 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_223
    del _BuildAutomaton_223
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 276, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(random_numberType._UseForTag(pyxb.namespace.ExpandedName(None, 'seed')), pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 276, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_221 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_221
    del _BuildAutomaton_221
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 275, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 276, 12))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_222())
    sub_automata.append(_BuildAutomaton_223())
    final_update = set()
    symbol = pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/netconvertConfiguration.xsd', 274, 8)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
random_numberType._Automaton = _BuildAutomaton_221()




tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'phase'), phaseType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 199, 12)))

tlLogicType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'param'), paramType, scope=tlLogicType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 200, 12)))

def _BuildAutomaton_224 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_224
    del _BuildAutomaton_224
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
tlLogicType._Automaton = _BuildAutomaton_224()




typeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'restriction'), restrictionType, scope=typeType, location=pyxb.utils.utility.Location('http://sumo.dlr.de/xsd/baseTypes.xsd', 237, 12)))

def _BuildAutomaton_225 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_225
    del _BuildAutomaton_225
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
typeType._Automaton = _BuildAutomaton_225()

