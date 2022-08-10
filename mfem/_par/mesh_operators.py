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
    from . import _mesh_operators
else:
    import _mesh_operators

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _mesh_operators.SWIG_PyInstanceMethod_New
_swig_new_static_method = _mesh_operators.SWIG_PyStaticMethod_New

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

import mfem._par.array
import mfem._par.mem_manager
import mfem._par.vector
import mfem._par.mesh
import mfem._par.matrix
import mfem._par.operators
import mfem._par.sort_pairs
import mfem._par.ncmesh
import mfem._par.globals
import mfem._par.vtk
import mfem._par.element
import mfem._par.densemat
import mfem._par.geom
import mfem._par.intrules
import mfem._par.table
import mfem._par.hash
import mfem._par.vertex
import mfem._par.gridfunc
import mfem._par.coefficient
import mfem._par.symmat
import mfem._par.sparsemat
import mfem._par.eltrans
import mfem._par.fe
import mfem._par.fe_base
import mfem._par.fe_fixed_order
import mfem._par.fe_h1
import mfem._par.fe_nd
import mfem._par.fe_rt
import mfem._par.fe_l2
import mfem._par.fe_nurbs
import mfem._par.fe_pos
import mfem._par.fe_ser
import mfem._par.fespace
import mfem._par.fe_coll
import mfem._par.lininteg
import mfem._par.doftrans
import mfem._par.handle
import mfem._par.hypre
import mfem._par.restriction
import mfem._par.bilininteg
import mfem._par.linearform
import mfem._par.nonlininteg
import mfem._par.std_vectors
import mfem._par.estimators
import mfem._par.bilinearform
class MeshOperator(object):
    r"""Proxy of C++ mfem::MeshOperator class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    NONE = _mesh_operators.MeshOperator_NONE
    
    CONTINUE = _mesh_operators.MeshOperator_CONTINUE
    
    STOP = _mesh_operators.MeshOperator_STOP
    
    REPEAT = _mesh_operators.MeshOperator_REPEAT
    
    MASK_UPDATE = _mesh_operators.MeshOperator_MASK_UPDATE
    
    MASK_ACTION = _mesh_operators.MeshOperator_MASK_ACTION
    
    REFINED = _mesh_operators.MeshOperator_REFINED
    
    DEREFINED = _mesh_operators.MeshOperator_DEREFINED
    
    REBALANCED = _mesh_operators.MeshOperator_REBALANCED
    
    MASK_INFO = _mesh_operators.MeshOperator_MASK_INFO
    

    def Apply(self, mesh):
        r"""Apply(MeshOperator self, Mesh mesh) -> bool"""
        return _mesh_operators.MeshOperator_Apply(self, mesh)
    Apply = _swig_new_instance_method(_mesh_operators.MeshOperator_Apply)

    def Stop(self):
        r"""Stop(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Stop(self)
    Stop = _swig_new_instance_method(_mesh_operators.MeshOperator_Stop)

    def Repeat(self):
        r"""Repeat(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Repeat(self)
    Repeat = _swig_new_instance_method(_mesh_operators.MeshOperator_Repeat)

    def Continue(self):
        r"""Continue(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Continue(self)
    Continue = _swig_new_instance_method(_mesh_operators.MeshOperator_Continue)

    def Refined(self):
        r"""Refined(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Refined(self)
    Refined = _swig_new_instance_method(_mesh_operators.MeshOperator_Refined)

    def Derefined(self):
        r"""Derefined(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Derefined(self)
    Derefined = _swig_new_instance_method(_mesh_operators.MeshOperator_Derefined)

    def Rebalanced(self):
        r"""Rebalanced(MeshOperator self) -> bool"""
        return _mesh_operators.MeshOperator_Rebalanced(self)
    Rebalanced = _swig_new_instance_method(_mesh_operators.MeshOperator_Rebalanced)

    def GetActionInfo(self):
        r"""GetActionInfo(MeshOperator self) -> int"""
        return _mesh_operators.MeshOperator_GetActionInfo(self)
    GetActionInfo = _swig_new_instance_method(_mesh_operators.MeshOperator_GetActionInfo)

    def Reset(self):
        r"""Reset(MeshOperator self)"""
        return _mesh_operators.MeshOperator_Reset(self)
    Reset = _swig_new_instance_method(_mesh_operators.MeshOperator_Reset)
    __swig_destroy__ = _mesh_operators.delete_MeshOperator

# Register MeshOperator in _mesh_operators:
_mesh_operators.MeshOperator_swigregister(MeshOperator)

class MeshOperatorSequence(MeshOperator):
    r"""Proxy of C++ mfem::MeshOperatorSequence class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        r"""__init__(MeshOperatorSequence self) -> MeshOperatorSequence"""
        _mesh_operators.MeshOperatorSequence_swiginit(self, _mesh_operators.new_MeshOperatorSequence())
    __swig_destroy__ = _mesh_operators.delete_MeshOperatorSequence

    def Append(self, mc):
        r"""Append(MeshOperatorSequence self, MeshOperator mc)"""
        return _mesh_operators.MeshOperatorSequence_Append(self, mc)
    Append = _swig_new_instance_method(_mesh_operators.MeshOperatorSequence_Append)

    def GetSequence(self):
        r"""GetSequence(MeshOperatorSequence self) -> mfem::Array< mfem::MeshOperator * > &"""
        return _mesh_operators.MeshOperatorSequence_GetSequence(self)
    GetSequence = _swig_new_instance_method(_mesh_operators.MeshOperatorSequence_GetSequence)

    def Reset(self):
        r"""Reset(MeshOperatorSequence self)"""
        return _mesh_operators.MeshOperatorSequence_Reset(self)
    Reset = _swig_new_instance_method(_mesh_operators.MeshOperatorSequence_Reset)

# Register MeshOperatorSequence in _mesh_operators:
_mesh_operators.MeshOperatorSequence_swigregister(MeshOperatorSequence)

class ThresholdRefiner(MeshOperator):
    r"""Proxy of C++ mfem::ThresholdRefiner class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, est):
        r"""__init__(ThresholdRefiner self, ErrorEstimator est) -> ThresholdRefiner"""
        _mesh_operators.ThresholdRefiner_swiginit(self, _mesh_operators.new_ThresholdRefiner(est))

    def SetTotalErrorNormP(self, *args, **kwargs):
        r"""SetTotalErrorNormP(ThresholdRefiner self, double norm_p=mfem::infinity())"""
        return _mesh_operators.ThresholdRefiner_SetTotalErrorNormP(self, *args, **kwargs)
    SetTotalErrorNormP = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_SetTotalErrorNormP)

    def SetTotalErrorGoal(self, err_goal):
        r"""SetTotalErrorGoal(ThresholdRefiner self, double err_goal)"""
        return _mesh_operators.ThresholdRefiner_SetTotalErrorGoal(self, err_goal)
    SetTotalErrorGoal = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_SetTotalErrorGoal)

    def SetTotalErrorFraction(self, fraction):
        r"""SetTotalErrorFraction(ThresholdRefiner self, double fraction)"""
        return _mesh_operators.ThresholdRefiner_SetTotalErrorFraction(self, fraction)
    SetTotalErrorFraction = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_SetTotalErrorFraction)

    def SetLocalErrorGoal(self, err_goal):
        r"""SetLocalErrorGoal(ThresholdRefiner self, double err_goal)"""
        return _mesh_operators.ThresholdRefiner_SetLocalErrorGoal(self, err_goal)
    SetLocalErrorGoal = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_SetLocalErrorGoal)

    def SetMaxElements(self, max_elem):
        r"""SetMaxElements(ThresholdRefiner self, long long max_elem)"""
        return _mesh_operators.ThresholdRefiner_SetMaxElements(self, max_elem)
    SetMaxElements = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_SetMaxElements)

    def PreferNonconformingRefinement(self):
        r"""PreferNonconformingRefinement(ThresholdRefiner self)"""
        return _mesh_operators.ThresholdRefiner_PreferNonconformingRefinement(self)
    PreferNonconformingRefinement = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_PreferNonconformingRefinement)

    def PreferConformingRefinement(self):
        r"""PreferConformingRefinement(ThresholdRefiner self)"""
        return _mesh_operators.ThresholdRefiner_PreferConformingRefinement(self)
    PreferConformingRefinement = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_PreferConformingRefinement)

    def SetNCLimit(self, nc_limit_):
        r"""SetNCLimit(ThresholdRefiner self, int nc_limit_)"""
        return _mesh_operators.ThresholdRefiner_SetNCLimit(self, nc_limit_)
    SetNCLimit = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_SetNCLimit)

    def GetNumMarkedElements(self):
        r"""GetNumMarkedElements(ThresholdRefiner self) -> long long"""
        return _mesh_operators.ThresholdRefiner_GetNumMarkedElements(self)
    GetNumMarkedElements = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_GetNumMarkedElements)

    def GetThreshold(self):
        r"""GetThreshold(ThresholdRefiner self) -> double"""
        return _mesh_operators.ThresholdRefiner_GetThreshold(self)
    GetThreshold = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_GetThreshold)

    def Reset(self):
        r"""Reset(ThresholdRefiner self)"""
        return _mesh_operators.ThresholdRefiner_Reset(self)
    Reset = _swig_new_instance_method(_mesh_operators.ThresholdRefiner_Reset)
    __swig_destroy__ = _mesh_operators.delete_ThresholdRefiner

# Register ThresholdRefiner in _mesh_operators:
_mesh_operators.ThresholdRefiner_swigregister(ThresholdRefiner)

class ThresholdDerefiner(MeshOperator):
    r"""Proxy of C++ mfem::ThresholdDerefiner class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, est):
        r"""__init__(ThresholdDerefiner self, ErrorEstimator est) -> ThresholdDerefiner"""
        _mesh_operators.ThresholdDerefiner_swiginit(self, _mesh_operators.new_ThresholdDerefiner(est))

    def SetThreshold(self, thresh):
        r"""SetThreshold(ThresholdDerefiner self, double thresh)"""
        return _mesh_operators.ThresholdDerefiner_SetThreshold(self, thresh)
    SetThreshold = _swig_new_instance_method(_mesh_operators.ThresholdDerefiner_SetThreshold)

    def SetOp(self, oper):
        r"""SetOp(ThresholdDerefiner self, int oper)"""
        return _mesh_operators.ThresholdDerefiner_SetOp(self, oper)
    SetOp = _swig_new_instance_method(_mesh_operators.ThresholdDerefiner_SetOp)

    def SetNCLimit(self, nc_limit_):
        r"""SetNCLimit(ThresholdDerefiner self, int nc_limit_)"""
        return _mesh_operators.ThresholdDerefiner_SetNCLimit(self, nc_limit_)
    SetNCLimit = _swig_new_instance_method(_mesh_operators.ThresholdDerefiner_SetNCLimit)

    def Reset(self):
        r"""Reset(ThresholdDerefiner self)"""
        return _mesh_operators.ThresholdDerefiner_Reset(self)
    Reset = _swig_new_instance_method(_mesh_operators.ThresholdDerefiner_Reset)
    __swig_destroy__ = _mesh_operators.delete_ThresholdDerefiner

# Register ThresholdDerefiner in _mesh_operators:
_mesh_operators.ThresholdDerefiner_swigregister(ThresholdDerefiner)

class CoefficientRefiner(MeshOperator):
    r"""Proxy of C++ mfem::CoefficientRefiner class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, coeff_, order_):
        r"""__init__(CoefficientRefiner self, Coefficient coeff_, int order_) -> CoefficientRefiner"""
        _mesh_operators.CoefficientRefiner_swiginit(self, _mesh_operators.new_CoefficientRefiner(coeff_, order_))

    def PreprocessMesh(self, *args):
        r"""
        PreprocessMesh(CoefficientRefiner self, Mesh mesh, int max_it) -> int
        PreprocessMesh(CoefficientRefiner self, Mesh mesh) -> int
        """
        return _mesh_operators.CoefficientRefiner_PreprocessMesh(self, *args)
    PreprocessMesh = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_PreprocessMesh)

    def SetThreshold(self, threshold_):
        r"""SetThreshold(CoefficientRefiner self, double threshold_)"""
        return _mesh_operators.CoefficientRefiner_SetThreshold(self, threshold_)
    SetThreshold = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_SetThreshold)

    def SetMaxElements(self, max_elements_):
        r"""SetMaxElements(CoefficientRefiner self, long long max_elements_)"""
        return _mesh_operators.CoefficientRefiner_SetMaxElements(self, max_elements_)
    SetMaxElements = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_SetMaxElements)

    def ResetCoefficient(self, coeff_):
        r"""ResetCoefficient(CoefficientRefiner self, Coefficient coeff_)"""
        return _mesh_operators.CoefficientRefiner_ResetCoefficient(self, coeff_)
    ResetCoefficient = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_ResetCoefficient)

    def SetOrder(self, order_):
        r"""SetOrder(CoefficientRefiner self, int order_)"""
        return _mesh_operators.CoefficientRefiner_SetOrder(self, order_)
    SetOrder = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_SetOrder)

    def SetNCLimit(self, nc_limit_):
        r"""SetNCLimit(CoefficientRefiner self, int nc_limit_)"""
        return _mesh_operators.CoefficientRefiner_SetNCLimit(self, nc_limit_)
    SetNCLimit = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_SetNCLimit)

    def SetIntRule(self, irs_):
        r"""SetIntRule(CoefficientRefiner self, mfem::IntegrationRule const *[] irs_)"""
        return _mesh_operators.CoefficientRefiner_SetIntRule(self, irs_)
    SetIntRule = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_SetIntRule)

    def PrintWarnings(self):
        r"""PrintWarnings(CoefficientRefiner self)"""
        return _mesh_operators.CoefficientRefiner_PrintWarnings(self)
    PrintWarnings = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_PrintWarnings)

    def GetOsc(self):
        r"""GetOsc(CoefficientRefiner self) -> double"""
        return _mesh_operators.CoefficientRefiner_GetOsc(self)
    GetOsc = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_GetOsc)

    def GetLocalOscs(self):
        r"""GetLocalOscs(CoefficientRefiner self) -> Vector"""
        return _mesh_operators.CoefficientRefiner_GetLocalOscs(self)
    GetLocalOscs = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_GetLocalOscs)

    def Reset(self):
        r"""Reset(CoefficientRefiner self)"""
        return _mesh_operators.CoefficientRefiner_Reset(self)
    Reset = _swig_new_instance_method(_mesh_operators.CoefficientRefiner_Reset)
    __swig_destroy__ = _mesh_operators.delete_CoefficientRefiner

# Register CoefficientRefiner in _mesh_operators:
_mesh_operators.CoefficientRefiner_swigregister(CoefficientRefiner)

class Rebalancer(MeshOperator):
    r"""Proxy of C++ mfem::Rebalancer class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def Reset(self):
        r"""Reset(Rebalancer self)"""
        return _mesh_operators.Rebalancer_Reset(self)
    Reset = _swig_new_instance_method(_mesh_operators.Rebalancer_Reset)

    def __init__(self):
        r"""__init__(Rebalancer self) -> Rebalancer"""
        _mesh_operators.Rebalancer_swiginit(self, _mesh_operators.new_Rebalancer())
    __swig_destroy__ = _mesh_operators.delete_Rebalancer

# Register Rebalancer in _mesh_operators:
_mesh_operators.Rebalancer_swigregister(Rebalancer)



