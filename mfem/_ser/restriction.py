# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _restriction
else:
    import _restriction

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _restriction.SWIG_PyInstanceMethod_New
_swig_new_static_method = _restriction.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._ser.element
import mfem._ser.globals
import mfem._ser.array
import mfem._ser.mem_manager
import mfem._ser.densemat
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.geom
import mfem._ser.intrules
import mfem._ser.table
import mfem._ser.hash
import mfem._ser.mesh
import mfem._ser.sort_pairs
import mfem._ser.ncmesh
import mfem._ser.gridfunc
import mfem._ser.coefficient
import mfem._ser.symmat
import mfem._ser.sparsemat
import mfem._ser.eltrans
import mfem._ser.fe
import mfem._ser.fe_base
import mfem._ser.fe_fixed_order
import mfem._ser.fe_h1
import mfem._ser.fe_nd
import mfem._ser.fe_rt
import mfem._ser.fe_l2
import mfem._ser.fe_nurbs
import mfem._ser.fe_pos
import mfem._ser.fe_ser
import mfem._ser.fespace
import mfem._ser.fe_coll
import mfem._ser.lininteg
import mfem._ser.doftrans
import mfem._ser.handle
import mfem._ser.bilininteg
import mfem._ser.linearform
import mfem._ser.nonlininteg
import mfem._ser.vertex
import mfem._ser.vtk
import mfem._ser.std_vectors
class ElementRestriction(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::ElementRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2, arg3):
        r"""__init__(ElementRestriction self, FiniteElementSpace arg2, mfem::ElementDofOrdering arg3) -> ElementRestriction"""
        _restriction.ElementRestriction_swiginit(self, _restriction.new_ElementRestriction(arg2, arg3))

    def Mult(self, x, y):
        r"""Mult(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.ElementRestriction_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.ElementRestriction_MultTranspose)

    def MultUnsigned(self, x, y):
        r"""MultUnsigned(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultUnsigned(self, x, y)
    MultUnsigned = _swig_new_instance_method(_restriction.ElementRestriction_MultUnsigned)

    def MultTransposeUnsigned(self, x, y):
        r"""MultTransposeUnsigned(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultTransposeUnsigned(self, x, y)
    MultTransposeUnsigned = _swig_new_instance_method(_restriction.ElementRestriction_MultTransposeUnsigned)

    def MultLeftInverse(self, x, y):
        r"""MultLeftInverse(ElementRestriction self, Vector x, Vector y)"""
        return _restriction.ElementRestriction_MultLeftInverse(self, x, y)
    MultLeftInverse = _swig_new_instance_method(_restriction.ElementRestriction_MultLeftInverse)

    def BooleanMask(self, y):
        r"""BooleanMask(ElementRestriction self, Vector y)"""
        return _restriction.ElementRestriction_BooleanMask(self, y)
    BooleanMask = _swig_new_instance_method(_restriction.ElementRestriction_BooleanMask)

    def FillSparseMatrix(self, mat_ea, mat):
        r"""FillSparseMatrix(ElementRestriction self, Vector mat_ea, SparseMatrix mat)"""
        return _restriction.ElementRestriction_FillSparseMatrix(self, mat_ea, mat)
    FillSparseMatrix = _swig_new_instance_method(_restriction.ElementRestriction_FillSparseMatrix)

    def FillI(self, mat):
        r"""FillI(ElementRestriction self, SparseMatrix mat) -> int"""
        return _restriction.ElementRestriction_FillI(self, mat)
    FillI = _swig_new_instance_method(_restriction.ElementRestriction_FillI)

    def FillJAndData(self, ea_data, mat):
        r"""FillJAndData(ElementRestriction self, Vector ea_data, SparseMatrix mat)"""
        return _restriction.ElementRestriction_FillJAndData(self, ea_data, mat)
    FillJAndData = _swig_new_instance_method(_restriction.ElementRestriction_FillJAndData)
    __swig_destroy__ = _restriction.delete_ElementRestriction

# Register ElementRestriction in _restriction:
_restriction.ElementRestriction_swigregister(ElementRestriction)

class L2ElementRestriction(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::L2ElementRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, arg2):
        r"""__init__(L2ElementRestriction self, FiniteElementSpace arg2) -> L2ElementRestriction"""
        _restriction.L2ElementRestriction_swiginit(self, _restriction.new_L2ElementRestriction(arg2))

    def Mult(self, x, y):
        r"""Mult(L2ElementRestriction self, Vector x, Vector y)"""
        return _restriction.L2ElementRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.L2ElementRestriction_Mult)

    def MultTranspose(self, x, y):
        r"""MultTranspose(L2ElementRestriction self, Vector x, Vector y)"""
        return _restriction.L2ElementRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.L2ElementRestriction_MultTranspose)

    def FillI(self, mat):
        r"""FillI(L2ElementRestriction self, SparseMatrix mat)"""
        return _restriction.L2ElementRestriction_FillI(self, mat)
    FillI = _swig_new_instance_method(_restriction.L2ElementRestriction_FillI)

    def FillJAndData(self, ea_data, mat):
        r"""FillJAndData(L2ElementRestriction self, Vector ea_data, SparseMatrix mat)"""
        return _restriction.L2ElementRestriction_FillJAndData(self, ea_data, mat)
    FillJAndData = _swig_new_instance_method(_restriction.L2ElementRestriction_FillJAndData)
    __swig_destroy__ = _restriction.delete_L2ElementRestriction

# Register L2ElementRestriction in _restriction:
_restriction.L2ElementRestriction_swigregister(L2ElementRestriction)

L2FaceValues_SingleValued = _restriction.L2FaceValues_SingleValued

L2FaceValues_DoubleValued = _restriction.L2FaceValues_DoubleValued

class FaceRestriction(mfem._ser.operators.Operator):
    r"""Proxy of C++ mfem::FaceRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _restriction.delete_FaceRestriction

    def Mult(self, x, y):
        r"""Mult(FaceRestriction self, Vector x, Vector y)"""
        return _restriction.FaceRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.FaceRestriction_Mult)

    def AddMultTranspose(self, x, y):
        r"""AddMultTranspose(FaceRestriction self, Vector x, Vector y)"""
        return _restriction.FaceRestriction_AddMultTranspose(self, x, y)
    AddMultTranspose = _swig_new_instance_method(_restriction.FaceRestriction_AddMultTranspose)

    def MultTranspose(self, x, y):
        r"""MultTranspose(FaceRestriction self, Vector x, Vector y)"""
        return _restriction.FaceRestriction_MultTranspose(self, x, y)
    MultTranspose = _swig_new_instance_method(_restriction.FaceRestriction_MultTranspose)

# Register FaceRestriction in _restriction:
_restriction.FaceRestriction_swigregister(FaceRestriction)

class H1FaceRestriction(FaceRestriction):
    r"""Proxy of C++ mfem::H1FaceRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, fes, ordering, type):
        r"""__init__(H1FaceRestriction self, FiniteElementSpace fes, mfem::ElementDofOrdering const ordering, mfem::FaceType const type) -> H1FaceRestriction"""
        _restriction.H1FaceRestriction_swiginit(self, _restriction.new_H1FaceRestriction(fes, ordering, type))

    def Mult(self, x, y):
        r"""Mult(H1FaceRestriction self, Vector x, Vector y)"""
        return _restriction.H1FaceRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.H1FaceRestriction_Mult)

    def AddMultTranspose(self, x, y):
        r"""AddMultTranspose(H1FaceRestriction self, Vector x, Vector y)"""
        return _restriction.H1FaceRestriction_AddMultTranspose(self, x, y)
    AddMultTranspose = _swig_new_instance_method(_restriction.H1FaceRestriction_AddMultTranspose)
    __swig_destroy__ = _restriction.delete_H1FaceRestriction

# Register H1FaceRestriction in _restriction:
_restriction.H1FaceRestriction_swigregister(H1FaceRestriction)

class L2FaceRestriction(FaceRestriction):
    r"""Proxy of C++ mfem::L2FaceRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""__init__(L2FaceRestriction self, FiniteElementSpace fes, mfem::ElementDofOrdering const ordering, mfem::FaceType const type, mfem::L2FaceValues const m=DoubleValued) -> L2FaceRestriction"""
        _restriction.L2FaceRestriction_swiginit(self, _restriction.new_L2FaceRestriction(*args))

    def Mult(self, x, y):
        r"""Mult(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.L2FaceRestriction_Mult)

    def AddMultTranspose(self, x, y):
        r"""AddMultTranspose(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_AddMultTranspose(self, x, y)
    AddMultTranspose = _swig_new_instance_method(_restriction.L2FaceRestriction_AddMultTranspose)

    def FillI(self, mat, keep_nbr_block=False):
        r"""FillI(L2FaceRestriction self, SparseMatrix mat, bool const keep_nbr_block=False)"""
        return _restriction.L2FaceRestriction_FillI(self, mat, keep_nbr_block)
    FillI = _swig_new_instance_method(_restriction.L2FaceRestriction_FillI)

    def FillJAndData(self, fea_data, mat, keep_nbr_block=False):
        r"""FillJAndData(L2FaceRestriction self, Vector fea_data, SparseMatrix mat, bool const keep_nbr_block=False)"""
        return _restriction.L2FaceRestriction_FillJAndData(self, fea_data, mat, keep_nbr_block)
    FillJAndData = _swig_new_instance_method(_restriction.L2FaceRestriction_FillJAndData)

    def AddFaceMatricesToElementMatrices(self, fea_data, ea_data):
        r"""AddFaceMatricesToElementMatrices(L2FaceRestriction self, Vector fea_data, Vector ea_data)"""
        return _restriction.L2FaceRestriction_AddFaceMatricesToElementMatrices(self, fea_data, ea_data)
    AddFaceMatricesToElementMatrices = _swig_new_instance_method(_restriction.L2FaceRestriction_AddFaceMatricesToElementMatrices)

    def SingleValuedConformingMult(self, x, y):
        r"""SingleValuedConformingMult(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_SingleValuedConformingMult(self, x, y)
    SingleValuedConformingMult = _swig_new_instance_method(_restriction.L2FaceRestriction_SingleValuedConformingMult)

    def DoubleValuedConformingMult(self, x, y):
        r"""DoubleValuedConformingMult(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_DoubleValuedConformingMult(self, x, y)
    DoubleValuedConformingMult = _swig_new_instance_method(_restriction.L2FaceRestriction_DoubleValuedConformingMult)

    def SingleValuedConformingAddMultTranspose(self, x, y):
        r"""SingleValuedConformingAddMultTranspose(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_SingleValuedConformingAddMultTranspose(self, x, y)
    SingleValuedConformingAddMultTranspose = _swig_new_instance_method(_restriction.L2FaceRestriction_SingleValuedConformingAddMultTranspose)

    def DoubleValuedConformingAddMultTranspose(self, x, y):
        r"""DoubleValuedConformingAddMultTranspose(L2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.L2FaceRestriction_DoubleValuedConformingAddMultTranspose(self, x, y)
    DoubleValuedConformingAddMultTranspose = _swig_new_instance_method(_restriction.L2FaceRestriction_DoubleValuedConformingAddMultTranspose)
    __swig_destroy__ = _restriction.delete_L2FaceRestriction

# Register L2FaceRestriction in _restriction:
_restriction.L2FaceRestriction_swigregister(L2FaceRestriction)

class InterpConfig(object):
    r"""Proxy of C++ mfem::InterpConfig class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    is_non_conforming = property(_restriction.InterpConfig_is_non_conforming_get, _restriction.InterpConfig_is_non_conforming_set, doc=r"""is_non_conforming : uint32_t""")
    master_side = property(_restriction.InterpConfig_master_side_get, _restriction.InterpConfig_master_side_set, doc=r"""master_side : uint32_t""")
    index = property(_restriction.InterpConfig_index_get, _restriction.InterpConfig_index_set, doc=r"""index : uint32_t""")

    def __init__(self, *args):
        r"""
        __init__(InterpConfig self) -> InterpConfig
        __init__(InterpConfig self, int master_side, int nc_index) -> InterpConfig
        __init__(InterpConfig self, InterpConfig arg2) -> InterpConfig
        """
        _restriction.InterpConfig_swiginit(self, _restriction.new_InterpConfig(*args))
    __swig_destroy__ = _restriction.delete_InterpConfig

# Register InterpConfig in _restriction:
_restriction.InterpConfig_swigregister(InterpConfig)

class InterpolationManager(object):
    r"""Proxy of C++ mfem::InterpolationManager class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, fes, ordering, type):
        r"""__init__(InterpolationManager self, FiniteElementSpace fes, mfem::ElementDofOrdering ordering, mfem::FaceType type) -> InterpolationManager"""
        _restriction.InterpolationManager_swiginit(self, _restriction.new_InterpolationManager(fes, ordering, type))

    def RegisterFaceConformingInterpolation(self, face, face_index):
        r"""RegisterFaceConformingInterpolation(InterpolationManager self, mfem::Mesh::FaceInformation const & face, int face_index)"""
        return _restriction.InterpolationManager_RegisterFaceConformingInterpolation(self, face, face_index)
    RegisterFaceConformingInterpolation = _swig_new_instance_method(_restriction.InterpolationManager_RegisterFaceConformingInterpolation)

    def RegisterFaceCoarseToFineInterpolation(self, face, face_index):
        r"""RegisterFaceCoarseToFineInterpolation(InterpolationManager self, mfem::Mesh::FaceInformation const & face, int face_index)"""
        return _restriction.InterpolationManager_RegisterFaceCoarseToFineInterpolation(self, face, face_index)
    RegisterFaceCoarseToFineInterpolation = _swig_new_instance_method(_restriction.InterpolationManager_RegisterFaceCoarseToFineInterpolation)

    def LinearizeInterpolatorMapIntoVector(self):
        r"""LinearizeInterpolatorMapIntoVector(InterpolationManager self)"""
        return _restriction.InterpolationManager_LinearizeInterpolatorMapIntoVector(self)
    LinearizeInterpolatorMapIntoVector = _swig_new_instance_method(_restriction.InterpolationManager_LinearizeInterpolatorMapIntoVector)

    def GetNumInterpolators(self):
        r"""GetNumInterpolators(InterpolationManager self) -> int"""
        return _restriction.InterpolationManager_GetNumInterpolators(self)
    GetNumInterpolators = _swig_new_instance_method(_restriction.InterpolationManager_GetNumInterpolators)

    def GetInterpolators(self):
        r"""GetInterpolators(InterpolationManager self) -> Vector"""
        return _restriction.InterpolationManager_GetInterpolators(self)
    GetInterpolators = _swig_new_instance_method(_restriction.InterpolationManager_GetInterpolators)

    def GetFaceInterpConfig(self):
        r"""GetFaceInterpConfig(InterpolationManager self) -> mfem::Array< mfem::InterpConfig > const &"""
        return _restriction.InterpolationManager_GetFaceInterpConfig(self)
    GetFaceInterpConfig = _swig_new_instance_method(_restriction.InterpolationManager_GetFaceInterpConfig)
    __swig_destroy__ = _restriction.delete_InterpolationManager

# Register InterpolationManager in _restriction:
_restriction.InterpolationManager_swigregister(InterpolationManager)

class NCL2FaceRestriction(L2FaceRestriction):
    r"""Proxy of C++ mfem::NCL2FaceRestriction class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""__init__(NCL2FaceRestriction self, FiniteElementSpace fes, mfem::ElementDofOrdering const ordering, mfem::FaceType const type, mfem::L2FaceValues const m=DoubleValued) -> NCL2FaceRestriction"""
        _restriction.NCL2FaceRestriction_swiginit(self, _restriction.new_NCL2FaceRestriction(*args))

    def Mult(self, x, y):
        r"""Mult(NCL2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.NCL2FaceRestriction_Mult(self, x, y)
    Mult = _swig_new_instance_method(_restriction.NCL2FaceRestriction_Mult)

    def AddMultTranspose(self, x, y):
        r"""AddMultTranspose(NCL2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.NCL2FaceRestriction_AddMultTranspose(self, x, y)
    AddMultTranspose = _swig_new_instance_method(_restriction.NCL2FaceRestriction_AddMultTranspose)

    def FillI(self, mat, keep_nbr_block=False):
        r"""FillI(NCL2FaceRestriction self, SparseMatrix mat, bool const keep_nbr_block=False)"""
        return _restriction.NCL2FaceRestriction_FillI(self, mat, keep_nbr_block)
    FillI = _swig_new_instance_method(_restriction.NCL2FaceRestriction_FillI)

    def FillJAndData(self, fea_data, mat, keep_nbr_block=False):
        r"""FillJAndData(NCL2FaceRestriction self, Vector fea_data, SparseMatrix mat, bool const keep_nbr_block=False)"""
        return _restriction.NCL2FaceRestriction_FillJAndData(self, fea_data, mat, keep_nbr_block)
    FillJAndData = _swig_new_instance_method(_restriction.NCL2FaceRestriction_FillJAndData)

    def AddFaceMatricesToElementMatrices(self, fea_data, ea_data):
        r"""AddFaceMatricesToElementMatrices(NCL2FaceRestriction self, Vector fea_data, Vector ea_data)"""
        return _restriction.NCL2FaceRestriction_AddFaceMatricesToElementMatrices(self, fea_data, ea_data)
    AddFaceMatricesToElementMatrices = _swig_new_instance_method(_restriction.NCL2FaceRestriction_AddFaceMatricesToElementMatrices)

    def DoubleValuedNonconformingMult(self, x, y):
        r"""DoubleValuedNonconformingMult(NCL2FaceRestriction self, Vector x, Vector y)"""
        return _restriction.NCL2FaceRestriction_DoubleValuedNonconformingMult(self, x, y)
    DoubleValuedNonconformingMult = _swig_new_instance_method(_restriction.NCL2FaceRestriction_DoubleValuedNonconformingMult)

    def SingleValuedNonconformingTransposeInterpolation(self, x):
        r"""SingleValuedNonconformingTransposeInterpolation(NCL2FaceRestriction self, Vector x)"""
        return _restriction.NCL2FaceRestriction_SingleValuedNonconformingTransposeInterpolation(self, x)
    SingleValuedNonconformingTransposeInterpolation = _swig_new_instance_method(_restriction.NCL2FaceRestriction_SingleValuedNonconformingTransposeInterpolation)

    def DoubleValuedNonconformingTransposeInterpolation(self, x):
        r"""DoubleValuedNonconformingTransposeInterpolation(NCL2FaceRestriction self, Vector x)"""
        return _restriction.NCL2FaceRestriction_DoubleValuedNonconformingTransposeInterpolation(self, x)
    DoubleValuedNonconformingTransposeInterpolation = _swig_new_instance_method(_restriction.NCL2FaceRestriction_DoubleValuedNonconformingTransposeInterpolation)
    __swig_destroy__ = _restriction.delete_NCL2FaceRestriction

# Register NCL2FaceRestriction in _restriction:
_restriction.NCL2FaceRestriction_swigregister(NCL2FaceRestriction)


def GetFaceDofs(dim, face_id, dof1d, face_map):
    r"""GetFaceDofs(int const dim, int const face_id, int const dof1d, intArray face_map)"""
    return _restriction.GetFaceDofs(dim, face_id, dof1d, face_map)
GetFaceDofs = _restriction.GetFaceDofs

def ToLexOrdering(dim, face_id, size1d, index):
    r"""ToLexOrdering(int const dim, int const face_id, int const size1d, int const index) -> int"""
    return _restriction.ToLexOrdering(dim, face_id, size1d, index)
ToLexOrdering = _restriction.ToLexOrdering

def PermuteFaceL2(dim, face_id1, face_id2, orientation, size1d, index):
    r"""PermuteFaceL2(int const dim, int const face_id1, int const face_id2, int const orientation, int const size1d, int const index) -> int"""
    return _restriction.PermuteFaceL2(dim, face_id1, face_id2, orientation, size1d, index)
PermuteFaceL2 = _restriction.PermuteFaceL2


