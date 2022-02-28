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
    from . import _nonlininteg
else:
    import _nonlininteg

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _nonlininteg.SWIG_PyInstanceMethod_New
_swig_new_static_method = _nonlininteg.SWIG_PyStaticMethod_New

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

import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
import mfem._par.fespace
import mfem._par.coefficient
import mfem._par.globals
import mfem._par.matrix
import mfem._par.symmat
import mfem._par.intrules
import mfem._par.sparsemat
import mfem._par.densemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.geom
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.element
import mfem._par.table
import mfem._par.hash
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.mesh
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.vtk
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.bilininteg
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.linearform
import mfem._par.std_vectors
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
class NonlinearFormIntegrator(object):
    r"""Proxy of C++ mfem::NonlinearFormIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, ir=None):
        r"""__init__(NonlinearFormIntegrator self, IntegrationRule ir=None) -> NonlinearFormIntegrator"""
        if self.__class__ == NonlinearFormIntegrator:
            _self = None
        else:
            _self = self
        _nonlininteg.NonlinearFormIntegrator_swiginit(self, _nonlininteg.new_NonlinearFormIntegrator(_self, ir))

    def SetIntRule(self, ir):
        r"""SetIntRule(NonlinearFormIntegrator self, IntegrationRule ir)"""
        return _nonlininteg.NonlinearFormIntegrator_SetIntRule(self, ir)
    SetIntRule = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_SetIntRule)

    def SetIntegrationRule(self, ir):
        r"""SetIntegrationRule(NonlinearFormIntegrator self, IntegrationRule ir)"""
        return _nonlininteg.NonlinearFormIntegrator_SetIntegrationRule(self, ir)
    SetIntegrationRule = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_SetIntegrationRule)

    def SetPAMemoryType(self, mt):
        r"""SetPAMemoryType(NonlinearFormIntegrator self, mfem::MemoryType mt)"""
        return _nonlininteg.NonlinearFormIntegrator_SetPAMemoryType(self, mt)
    SetPAMemoryType = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_SetPAMemoryType)

    def GetIntegrationRule(self):
        r"""GetIntegrationRule(NonlinearFormIntegrator self) -> IntegrationRule"""
        return _nonlininteg.NonlinearFormIntegrator_GetIntegrationRule(self)
    GetIntegrationRule = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_GetIntegrationRule)

    def AssembleElementVector(self, el, Tr, elfun, elvect):
        r"""AssembleElementVector(NonlinearFormIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elfun, Vector elvect)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleElementVector(self, el, Tr, elfun, elvect)
    AssembleElementVector = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleElementVector)

    def AssembleFaceVector(self, el1, el2, Tr, elfun, elvect):
        r"""AssembleFaceVector(NonlinearFormIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elfun, Vector elvect)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleFaceVector(self, el1, el2, Tr, elfun, elvect)
    AssembleFaceVector = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleFaceVector)

    def AssembleElementGrad(self, el, Tr, elfun, elmat):
        r"""AssembleElementGrad(NonlinearFormIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elfun, DenseMatrix elmat)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleElementGrad(self, el, Tr, elfun, elmat)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleElementGrad)

    def AssembleFaceGrad(self, el1, el2, Tr, elfun, elmat):
        r"""AssembleFaceGrad(NonlinearFormIntegrator self, FiniteElement el1, FiniteElement el2, FaceElementTransformations Tr, Vector elfun, DenseMatrix elmat)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleFaceGrad(self, el1, el2, Tr, elfun, elmat)
    AssembleFaceGrad = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleFaceGrad)

    def GetElementEnergy(self, el, Tr, elfun):
        r"""GetElementEnergy(NonlinearFormIntegrator self, FiniteElement el, ElementTransformation Tr, Vector elfun) -> double"""
        return _nonlininteg.NonlinearFormIntegrator_GetElementEnergy(self, el, Tr, elfun)
    GetElementEnergy = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_GetElementEnergy)

    def AssemblePA(self, *args):
        r"""
        AssemblePA(NonlinearFormIntegrator self, FiniteElementSpace fes)
        AssemblePA(NonlinearFormIntegrator self, FiniteElementSpace trial_fes, FiniteElementSpace test_fes)
        """
        return _nonlininteg.NonlinearFormIntegrator_AssemblePA(self, *args)
    AssemblePA = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssemblePA)

    def AssembleGradPA(self, x, fes):
        r"""AssembleGradPA(NonlinearFormIntegrator self, Vector x, FiniteElementSpace fes)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleGradPA(self, x, fes)
    AssembleGradPA = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleGradPA)

    def GetLocalStateEnergyPA(self, x):
        r"""GetLocalStateEnergyPA(NonlinearFormIntegrator self, Vector x) -> double"""
        return _nonlininteg.NonlinearFormIntegrator_GetLocalStateEnergyPA(self, x)
    GetLocalStateEnergyPA = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_GetLocalStateEnergyPA)

    def AddMultPA(self, x, y):
        r"""AddMultPA(NonlinearFormIntegrator self, Vector x, Vector y)"""
        return _nonlininteg.NonlinearFormIntegrator_AddMultPA(self, x, y)
    AddMultPA = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AddMultPA)

    def AddMultGradPA(self, x, y):
        r"""AddMultGradPA(NonlinearFormIntegrator self, Vector x, Vector y)"""
        return _nonlininteg.NonlinearFormIntegrator_AddMultGradPA(self, x, y)
    AddMultGradPA = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AddMultGradPA)

    def AssembleGradDiagonalPA(self, diag):
        r"""AssembleGradDiagonalPA(NonlinearFormIntegrator self, Vector diag)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleGradDiagonalPA(self, diag)
    AssembleGradDiagonalPA = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleGradDiagonalPA)

    def SupportsCeed(self):
        r"""SupportsCeed(NonlinearFormIntegrator self) -> bool"""
        return _nonlininteg.NonlinearFormIntegrator_SupportsCeed(self)
    SupportsCeed = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_SupportsCeed)

    def AssembleMF(self, fes):
        r"""AssembleMF(NonlinearFormIntegrator self, FiniteElementSpace fes)"""
        return _nonlininteg.NonlinearFormIntegrator_AssembleMF(self, fes)
    AssembleMF = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AssembleMF)

    def AddMultMF(self, x, y):
        r"""AddMultMF(NonlinearFormIntegrator self, Vector x, Vector y)"""
        return _nonlininteg.NonlinearFormIntegrator_AddMultMF(self, x, y)
    AddMultMF = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_AddMultMF)

    def GetCeedOp(self):
        r"""GetCeedOp(NonlinearFormIntegrator self) -> ceed::Operator &"""
        return _nonlininteg.NonlinearFormIntegrator_GetCeedOp(self)
    GetCeedOp = _swig_new_instance_method(_nonlininteg.NonlinearFormIntegrator_GetCeedOp)
    __swig_destroy__ = _nonlininteg.delete_NonlinearFormIntegrator
    def __disown__(self):
        self.this.disown()
        _nonlininteg.disown_NonlinearFormIntegrator(self)
        return weakref.proxy(self)

# Register NonlinearFormIntegrator in _nonlininteg:
_nonlininteg.NonlinearFormIntegrator_swigregister(NonlinearFormIntegrator)

class BlockNonlinearFormIntegrator(object):
    r"""Proxy of C++ mfem::BlockNonlinearFormIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def GetElementEnergy(self, el, Tr, elfun):
        r"""GetElementEnergy(BlockNonlinearFormIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el, ElementTransformation Tr, mfem::Array< mfem::Vector const * > const & elfun) -> double"""
        return _nonlininteg.BlockNonlinearFormIntegrator_GetElementEnergy(self, el, Tr, elfun)
    GetElementEnergy = _swig_new_instance_method(_nonlininteg.BlockNonlinearFormIntegrator_GetElementEnergy)

    def AssembleElementVector(self, el, Tr, elfun, elvec):
        r"""AssembleElementVector(BlockNonlinearFormIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el, ElementTransformation Tr, mfem::Array< mfem::Vector const * > const & elfun, VectorPtrArray elvec)"""
        return _nonlininteg.BlockNonlinearFormIntegrator_AssembleElementVector(self, el, Tr, elfun, elvec)
    AssembleElementVector = _swig_new_instance_method(_nonlininteg.BlockNonlinearFormIntegrator_AssembleElementVector)

    def AssembleFaceVector(self, el1, el2, Tr, elfun, elvect):
        r"""AssembleFaceVector(BlockNonlinearFormIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el1, mfem::Array< mfem::FiniteElement const * > const & el2, FaceElementTransformations Tr, mfem::Array< mfem::Vector const * > const & elfun, VectorPtrArray elvect)"""
        return _nonlininteg.BlockNonlinearFormIntegrator_AssembleFaceVector(self, el1, el2, Tr, elfun, elvect)
    AssembleFaceVector = _swig_new_instance_method(_nonlininteg.BlockNonlinearFormIntegrator_AssembleFaceVector)

    def AssembleElementGrad(self, el, Tr, elfun, elmats):
        r"""AssembleElementGrad(BlockNonlinearFormIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el, ElementTransformation Tr, mfem::Array< mfem::Vector const * > const & elfun, mfem::Array2D< mfem::DenseMatrix * > const & elmats)"""
        return _nonlininteg.BlockNonlinearFormIntegrator_AssembleElementGrad(self, el, Tr, elfun, elmats)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.BlockNonlinearFormIntegrator_AssembleElementGrad)

    def AssembleFaceGrad(self, el1, el2, Tr, elfun, elmats):
        r"""AssembleFaceGrad(BlockNonlinearFormIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el1, mfem::Array< mfem::FiniteElement const * > const & el2, FaceElementTransformations Tr, mfem::Array< mfem::Vector const * > const & elfun, mfem::Array2D< mfem::DenseMatrix * > const & elmats)"""
        return _nonlininteg.BlockNonlinearFormIntegrator_AssembleFaceGrad(self, el1, el2, Tr, elfun, elmats)
    AssembleFaceGrad = _swig_new_instance_method(_nonlininteg.BlockNonlinearFormIntegrator_AssembleFaceGrad)
    __swig_destroy__ = _nonlininteg.delete_BlockNonlinearFormIntegrator

    def __init__(self):
        r"""__init__(BlockNonlinearFormIntegrator self) -> BlockNonlinearFormIntegrator"""
        _nonlininteg.BlockNonlinearFormIntegrator_swiginit(self, _nonlininteg.new_BlockNonlinearFormIntegrator())

# Register BlockNonlinearFormIntegrator in _nonlininteg:
_nonlininteg.BlockNonlinearFormIntegrator_swigregister(BlockNonlinearFormIntegrator)

class HyperelasticModel(object):
    r"""Proxy of C++ mfem::HyperelasticModel class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _nonlininteg.delete_HyperelasticModel

    def SetTransformation(self, Ttr_):
        r"""SetTransformation(HyperelasticModel self, ElementTransformation Ttr_)"""
        return _nonlininteg.HyperelasticModel_SetTransformation(self, Ttr_)
    SetTransformation = _swig_new_instance_method(_nonlininteg.HyperelasticModel_SetTransformation)

    def EvalW(self, Jpt):
        r"""EvalW(HyperelasticModel self, DenseMatrix Jpt) -> double"""
        return _nonlininteg.HyperelasticModel_EvalW(self, Jpt)
    EvalW = _swig_new_instance_method(_nonlininteg.HyperelasticModel_EvalW)

    def EvalP(self, Jpt, P):
        r"""EvalP(HyperelasticModel self, DenseMatrix Jpt, DenseMatrix P)"""
        return _nonlininteg.HyperelasticModel_EvalP(self, Jpt, P)
    EvalP = _swig_new_instance_method(_nonlininteg.HyperelasticModel_EvalP)

    def AssembleH(self, Jpt, DS, weight, A):
        r"""AssembleH(HyperelasticModel self, DenseMatrix Jpt, DenseMatrix DS, double const weight, DenseMatrix A)"""
        return _nonlininteg.HyperelasticModel_AssembleH(self, Jpt, DS, weight, A)
    AssembleH = _swig_new_instance_method(_nonlininteg.HyperelasticModel_AssembleH)

# Register HyperelasticModel in _nonlininteg:
_nonlininteg.HyperelasticModel_swigregister(HyperelasticModel)

class InverseHarmonicModel(HyperelasticModel):
    r"""Proxy of C++ mfem::InverseHarmonicModel class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def EvalW(self, J):
        r"""EvalW(InverseHarmonicModel self, DenseMatrix J) -> double"""
        return _nonlininteg.InverseHarmonicModel_EvalW(self, J)
    EvalW = _swig_new_instance_method(_nonlininteg.InverseHarmonicModel_EvalW)

    def EvalP(self, J, P):
        r"""EvalP(InverseHarmonicModel self, DenseMatrix J, DenseMatrix P)"""
        return _nonlininteg.InverseHarmonicModel_EvalP(self, J, P)
    EvalP = _swig_new_instance_method(_nonlininteg.InverseHarmonicModel_EvalP)

    def AssembleH(self, J, DS, weight, A):
        r"""AssembleH(InverseHarmonicModel self, DenseMatrix J, DenseMatrix DS, double const weight, DenseMatrix A)"""
        return _nonlininteg.InverseHarmonicModel_AssembleH(self, J, DS, weight, A)
    AssembleH = _swig_new_instance_method(_nonlininteg.InverseHarmonicModel_AssembleH)

    def __init__(self):
        r"""__init__(InverseHarmonicModel self) -> InverseHarmonicModel"""
        _nonlininteg.InverseHarmonicModel_swiginit(self, _nonlininteg.new_InverseHarmonicModel())
    __swig_destroy__ = _nonlininteg.delete_InverseHarmonicModel

# Register InverseHarmonicModel in _nonlininteg:
_nonlininteg.InverseHarmonicModel_swigregister(InverseHarmonicModel)

class NeoHookeanModel(HyperelasticModel):
    r"""Proxy of C++ mfem::NeoHookeanModel class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(NeoHookeanModel self, double mu_, double K_, double g_=1.0) -> NeoHookeanModel
        __init__(NeoHookeanModel self, Coefficient mu_, Coefficient K_, Coefficient g_=None) -> NeoHookeanModel
        """
        _nonlininteg.NeoHookeanModel_swiginit(self, _nonlininteg.new_NeoHookeanModel(*args))

    def EvalW(self, J):
        r"""EvalW(NeoHookeanModel self, DenseMatrix J) -> double"""
        return _nonlininteg.NeoHookeanModel_EvalW(self, J)
    EvalW = _swig_new_instance_method(_nonlininteg.NeoHookeanModel_EvalW)

    def EvalP(self, J, P):
        r"""EvalP(NeoHookeanModel self, DenseMatrix J, DenseMatrix P)"""
        return _nonlininteg.NeoHookeanModel_EvalP(self, J, P)
    EvalP = _swig_new_instance_method(_nonlininteg.NeoHookeanModel_EvalP)

    def AssembleH(self, J, DS, weight, A):
        r"""AssembleH(NeoHookeanModel self, DenseMatrix J, DenseMatrix DS, double const weight, DenseMatrix A)"""
        return _nonlininteg.NeoHookeanModel_AssembleH(self, J, DS, weight, A)
    AssembleH = _swig_new_instance_method(_nonlininteg.NeoHookeanModel_AssembleH)
    __swig_destroy__ = _nonlininteg.delete_NeoHookeanModel

# Register NeoHookeanModel in _nonlininteg:
_nonlininteg.NeoHookeanModel_swigregister(NeoHookeanModel)

class HyperelasticNLFIntegrator(NonlinearFormIntegrator):
    r"""Proxy of C++ mfem::HyperelasticNLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, m):
        r"""__init__(HyperelasticNLFIntegrator self, HyperelasticModel m) -> HyperelasticNLFIntegrator"""
        _nonlininteg.HyperelasticNLFIntegrator_swiginit(self, _nonlininteg.new_HyperelasticNLFIntegrator(m))

    def GetElementEnergy(self, el, Ttr, elfun):
        r"""GetElementEnergy(HyperelasticNLFIntegrator self, FiniteElement el, ElementTransformation Ttr, Vector elfun) -> double"""
        return _nonlininteg.HyperelasticNLFIntegrator_GetElementEnergy(self, el, Ttr, elfun)
    GetElementEnergy = _swig_new_instance_method(_nonlininteg.HyperelasticNLFIntegrator_GetElementEnergy)

    def AssembleElementVector(self, el, Ttr, elfun, elvect):
        r"""AssembleElementVector(HyperelasticNLFIntegrator self, FiniteElement el, ElementTransformation Ttr, Vector elfun, Vector elvect)"""
        return _nonlininteg.HyperelasticNLFIntegrator_AssembleElementVector(self, el, Ttr, elfun, elvect)
    AssembleElementVector = _swig_new_instance_method(_nonlininteg.HyperelasticNLFIntegrator_AssembleElementVector)

    def AssembleElementGrad(self, el, Ttr, elfun, elmat):
        r"""AssembleElementGrad(HyperelasticNLFIntegrator self, FiniteElement el, ElementTransformation Ttr, Vector elfun, DenseMatrix elmat)"""
        return _nonlininteg.HyperelasticNLFIntegrator_AssembleElementGrad(self, el, Ttr, elfun, elmat)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.HyperelasticNLFIntegrator_AssembleElementGrad)
    __swig_destroy__ = _nonlininteg.delete_HyperelasticNLFIntegrator

# Register HyperelasticNLFIntegrator in _nonlininteg:
_nonlininteg.HyperelasticNLFIntegrator_swigregister(HyperelasticNLFIntegrator)

class IncompressibleNeoHookeanIntegrator(BlockNonlinearFormIntegrator):
    r"""Proxy of C++ mfem::IncompressibleNeoHookeanIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mu_):
        r"""__init__(IncompressibleNeoHookeanIntegrator self, Coefficient mu_) -> IncompressibleNeoHookeanIntegrator"""
        _nonlininteg.IncompressibleNeoHookeanIntegrator_swiginit(self, _nonlininteg.new_IncompressibleNeoHookeanIntegrator(mu_))

    def GetElementEnergy(self, el, Tr, elfun):
        r"""GetElementEnergy(IncompressibleNeoHookeanIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el, ElementTransformation Tr, mfem::Array< mfem::Vector const * > const & elfun) -> double"""
        return _nonlininteg.IncompressibleNeoHookeanIntegrator_GetElementEnergy(self, el, Tr, elfun)
    GetElementEnergy = _swig_new_instance_method(_nonlininteg.IncompressibleNeoHookeanIntegrator_GetElementEnergy)

    def AssembleElementVector(self, el, Tr, elfun, elvec):
        r"""AssembleElementVector(IncompressibleNeoHookeanIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el, ElementTransformation Tr, mfem::Array< mfem::Vector const * > const & elfun, VectorPtrArray elvec)"""
        return _nonlininteg.IncompressibleNeoHookeanIntegrator_AssembleElementVector(self, el, Tr, elfun, elvec)
    AssembleElementVector = _swig_new_instance_method(_nonlininteg.IncompressibleNeoHookeanIntegrator_AssembleElementVector)

    def AssembleElementGrad(self, el, Tr, elfun, elmats):
        r"""AssembleElementGrad(IncompressibleNeoHookeanIntegrator self, mfem::Array< mfem::FiniteElement const * > const & el, ElementTransformation Tr, mfem::Array< mfem::Vector const * > const & elfun, mfem::Array2D< mfem::DenseMatrix * > const & elmats)"""
        return _nonlininteg.IncompressibleNeoHookeanIntegrator_AssembleElementGrad(self, el, Tr, elfun, elmats)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.IncompressibleNeoHookeanIntegrator_AssembleElementGrad)
    __swig_destroy__ = _nonlininteg.delete_IncompressibleNeoHookeanIntegrator

# Register IncompressibleNeoHookeanIntegrator in _nonlininteg:
_nonlininteg.IncompressibleNeoHookeanIntegrator_swigregister(IncompressibleNeoHookeanIntegrator)

class VectorConvectionNLFIntegrator(NonlinearFormIntegrator):
    r"""Proxy of C++ mfem::VectorConvectionNLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(VectorConvectionNLFIntegrator self, Coefficient q) -> VectorConvectionNLFIntegrator
        __init__(VectorConvectionNLFIntegrator self) -> VectorConvectionNLFIntegrator
        """
        _nonlininteg.VectorConvectionNLFIntegrator_swiginit(self, _nonlininteg.new_VectorConvectionNLFIntegrator(*args))

    @staticmethod
    def GetRule(fe, T):
        r"""GetRule(FiniteElement fe, ElementTransformation T) -> IntegrationRule"""
        return _nonlininteg.VectorConvectionNLFIntegrator_GetRule(fe, T)
    GetRule = _swig_new_static_method(_nonlininteg.VectorConvectionNLFIntegrator_GetRule)

    def AssembleElementVector(self, el, trans, elfun, elvect):
        r"""AssembleElementVector(VectorConvectionNLFIntegrator self, FiniteElement el, ElementTransformation trans, Vector elfun, Vector elvect)"""
        return _nonlininteg.VectorConvectionNLFIntegrator_AssembleElementVector(self, el, trans, elfun, elvect)
    AssembleElementVector = _swig_new_instance_method(_nonlininteg.VectorConvectionNLFIntegrator_AssembleElementVector)

    def AssembleElementGrad(self, el, trans, elfun, elmat):
        r"""AssembleElementGrad(VectorConvectionNLFIntegrator self, FiniteElement el, ElementTransformation trans, Vector elfun, DenseMatrix elmat)"""
        return _nonlininteg.VectorConvectionNLFIntegrator_AssembleElementGrad(self, el, trans, elfun, elmat)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.VectorConvectionNLFIntegrator_AssembleElementGrad)

    def AssemblePA(self, *args):
        r"""
        AssemblePA(VectorConvectionNLFIntegrator self, FiniteElementSpace fes)
        AssemblePA(VectorConvectionNLFIntegrator self, FiniteElementSpace trial_fes, FiniteElementSpace test_fes)
        AssemblePA(VectorConvectionNLFIntegrator self, FiniteElementSpace fes)
        """
        return _nonlininteg.VectorConvectionNLFIntegrator_AssemblePA(self, *args)
    AssemblePA = _swig_new_instance_method(_nonlininteg.VectorConvectionNLFIntegrator_AssemblePA)

    def AssembleMF(self, fes):
        r"""AssembleMF(VectorConvectionNLFIntegrator self, FiniteElementSpace fes)"""
        return _nonlininteg.VectorConvectionNLFIntegrator_AssembleMF(self, fes)
    AssembleMF = _swig_new_instance_method(_nonlininteg.VectorConvectionNLFIntegrator_AssembleMF)

    def AddMultPA(self, x, y):
        r"""AddMultPA(VectorConvectionNLFIntegrator self, Vector x, Vector y)"""
        return _nonlininteg.VectorConvectionNLFIntegrator_AddMultPA(self, x, y)
    AddMultPA = _swig_new_instance_method(_nonlininteg.VectorConvectionNLFIntegrator_AddMultPA)

    def AddMultMF(self, x, y):
        r"""AddMultMF(VectorConvectionNLFIntegrator self, Vector x, Vector y)"""
        return _nonlininteg.VectorConvectionNLFIntegrator_AddMultMF(self, x, y)
    AddMultMF = _swig_new_instance_method(_nonlininteg.VectorConvectionNLFIntegrator_AddMultMF)
    __swig_destroy__ = _nonlininteg.delete_VectorConvectionNLFIntegrator

# Register VectorConvectionNLFIntegrator in _nonlininteg:
_nonlininteg.VectorConvectionNLFIntegrator_swigregister(VectorConvectionNLFIntegrator)

def VectorConvectionNLFIntegrator_GetRule(fe, T):
    r"""VectorConvectionNLFIntegrator_GetRule(FiniteElement fe, ElementTransformation T) -> IntegrationRule"""
    return _nonlininteg.VectorConvectionNLFIntegrator_GetRule(fe, T)
VectorConvectionNLFIntegrator_GetRule = _nonlininteg.VectorConvectionNLFIntegrator_GetRule

class ConvectiveVectorConvectionNLFIntegrator(VectorConvectionNLFIntegrator):
    r"""Proxy of C++ mfem::ConvectiveVectorConvectionNLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(ConvectiveVectorConvectionNLFIntegrator self, Coefficient q) -> ConvectiveVectorConvectionNLFIntegrator
        __init__(ConvectiveVectorConvectionNLFIntegrator self) -> ConvectiveVectorConvectionNLFIntegrator
        """
        _nonlininteg.ConvectiveVectorConvectionNLFIntegrator_swiginit(self, _nonlininteg.new_ConvectiveVectorConvectionNLFIntegrator(*args))

    def AssembleElementGrad(self, el, trans, elfun, elmat):
        r"""AssembleElementGrad(ConvectiveVectorConvectionNLFIntegrator self, FiniteElement el, ElementTransformation trans, Vector elfun, DenseMatrix elmat)"""
        return _nonlininteg.ConvectiveVectorConvectionNLFIntegrator_AssembleElementGrad(self, el, trans, elfun, elmat)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.ConvectiveVectorConvectionNLFIntegrator_AssembleElementGrad)
    __swig_destroy__ = _nonlininteg.delete_ConvectiveVectorConvectionNLFIntegrator

# Register ConvectiveVectorConvectionNLFIntegrator in _nonlininteg:
_nonlininteg.ConvectiveVectorConvectionNLFIntegrator_swigregister(ConvectiveVectorConvectionNLFIntegrator)

class SkewSymmetricVectorConvectionNLFIntegrator(VectorConvectionNLFIntegrator):
    r"""Proxy of C++ mfem::SkewSymmetricVectorConvectionNLFIntegrator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(SkewSymmetricVectorConvectionNLFIntegrator self, Coefficient q) -> SkewSymmetricVectorConvectionNLFIntegrator
        __init__(SkewSymmetricVectorConvectionNLFIntegrator self) -> SkewSymmetricVectorConvectionNLFIntegrator
        """
        _nonlininteg.SkewSymmetricVectorConvectionNLFIntegrator_swiginit(self, _nonlininteg.new_SkewSymmetricVectorConvectionNLFIntegrator(*args))

    def AssembleElementGrad(self, el, trans, elfun, elmat):
        r"""AssembleElementGrad(SkewSymmetricVectorConvectionNLFIntegrator self, FiniteElement el, ElementTransformation trans, Vector elfun, DenseMatrix elmat)"""
        return _nonlininteg.SkewSymmetricVectorConvectionNLFIntegrator_AssembleElementGrad(self, el, trans, elfun, elmat)
    AssembleElementGrad = _swig_new_instance_method(_nonlininteg.SkewSymmetricVectorConvectionNLFIntegrator_AssembleElementGrad)
    __swig_destroy__ = _nonlininteg.delete_SkewSymmetricVectorConvectionNLFIntegrator

# Register SkewSymmetricVectorConvectionNLFIntegrator in _nonlininteg:
_nonlininteg.SkewSymmetricVectorConvectionNLFIntegrator_swigregister(SkewSymmetricVectorConvectionNLFIntegrator)



