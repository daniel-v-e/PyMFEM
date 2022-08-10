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
    from . import _symmat
else:
    import _symmat

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _symmat.SWIG_PyInstanceMethod_New
_swig_new_static_method = _symmat.SWIG_PyStaticMethod_New

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

import mfem._par.globals
import mfem._par.matrix
import mfem._par.vector
import mfem._par.array
import mfem._par.mem_manager
import mfem._par.operators
class DenseSymmetricMatrix(mfem._par.matrix.Matrix):
    r"""Proxy of C++ mfem::DenseSymmetricMatrix class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(DenseSymmetricMatrix self) -> DenseSymmetricMatrix
        __init__(DenseSymmetricMatrix self, int s) -> DenseSymmetricMatrix
        __init__(DenseSymmetricMatrix self, double * d, int s) -> DenseSymmetricMatrix
        """
        _symmat.DenseSymmetricMatrix_swiginit(self, _symmat.new_DenseSymmetricMatrix(*args))

    def UseExternalData(self, d, s):
        r"""UseExternalData(DenseSymmetricMatrix self, double * d, int s)"""
        return _symmat.DenseSymmetricMatrix_UseExternalData(self, d, s)
    UseExternalData = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_UseExternalData)

    def Reset(self, d, s):
        r"""Reset(DenseSymmetricMatrix self, double * d, int s)"""
        return _symmat.DenseSymmetricMatrix_Reset(self, d, s)
    Reset = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Reset)

    def ClearExternalData(self):
        r"""ClearExternalData(DenseSymmetricMatrix self)"""
        return _symmat.DenseSymmetricMatrix_ClearExternalData(self)
    ClearExternalData = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_ClearExternalData)

    def Clear(self):
        r"""Clear(DenseSymmetricMatrix self)"""
        return _symmat.DenseSymmetricMatrix_Clear(self)
    Clear = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Clear)

    def SetSize(self, s):
        r"""SetSize(DenseSymmetricMatrix self, int s)"""
        return _symmat.DenseSymmetricMatrix_SetSize(self, s)
    SetSize = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_SetSize)

    def Data(self):
        r"""Data(DenseSymmetricMatrix self) -> double *"""
        return _symmat.DenseSymmetricMatrix_Data(self)
    Data = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Data)

    def GetData(self):
        r"""GetData(DenseSymmetricMatrix self) -> double *"""
        return _symmat.DenseSymmetricMatrix_GetData(self)
    GetData = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_GetData)

    def GetMemory(self, *args):
        r"""
        GetMemory(DenseSymmetricMatrix self) -> mfem::Memory< double >
        GetMemory(DenseSymmetricMatrix self) -> mfem::Memory< double > const &
        """
        return _symmat.DenseSymmetricMatrix_GetMemory(self, *args)
    GetMemory = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_GetMemory)

    def OwnsData(self):
        r"""OwnsData(DenseSymmetricMatrix self) -> bool"""
        return _symmat.DenseSymmetricMatrix_OwnsData(self)
    OwnsData = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_OwnsData)

    def __call__(self, *args):
        r"""
        __call__(DenseSymmetricMatrix self, int i, int j) -> double
        __call__(DenseSymmetricMatrix self, int i, int j) -> double const &
        """
        return _symmat.DenseSymmetricMatrix___call__(self, *args)
    __call__ = _swig_new_instance_method(_symmat.DenseSymmetricMatrix___call__)

    def Elem(self, *args):
        r"""
        Elem(DenseSymmetricMatrix self, int i, int j) -> double
        Elem(DenseSymmetricMatrix self, int i, int j) -> double const &
        """
        return _symmat.DenseSymmetricMatrix_Elem(self, *args)
    Elem = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Elem)

    def __imul__(self, c):
        r"""__imul__(DenseSymmetricMatrix self, double c) -> DenseSymmetricMatrix"""
        return _symmat.DenseSymmetricMatrix___imul__(self, c)
    __imul__ = _swig_new_instance_method(_symmat.DenseSymmetricMatrix___imul__)

    def MemoryUsage(self):
        r"""MemoryUsage(DenseSymmetricMatrix self) -> std::size_t"""
        return _symmat.DenseSymmetricMatrix_MemoryUsage(self)
    MemoryUsage = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_MemoryUsage)

    def Read(self, on_dev=True):
        r"""Read(DenseSymmetricMatrix self, bool on_dev=True) -> double const *"""
        return _symmat.DenseSymmetricMatrix_Read(self, on_dev)
    Read = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Read)

    def HostRead(self):
        r"""HostRead(DenseSymmetricMatrix self) -> double const *"""
        return _symmat.DenseSymmetricMatrix_HostRead(self)
    HostRead = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_HostRead)

    def Write(self, on_dev=True):
        r"""Write(DenseSymmetricMatrix self, bool on_dev=True) -> double *"""
        return _symmat.DenseSymmetricMatrix_Write(self, on_dev)
    Write = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Write)

    def HostWrite(self):
        r"""HostWrite(DenseSymmetricMatrix self) -> double *"""
        return _symmat.DenseSymmetricMatrix_HostWrite(self)
    HostWrite = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_HostWrite)

    def ReadWrite(self, on_dev=True):
        r"""ReadWrite(DenseSymmetricMatrix self, bool on_dev=True) -> double *"""
        return _symmat.DenseSymmetricMatrix_ReadWrite(self, on_dev)
    ReadWrite = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_ReadWrite)

    def HostReadWrite(self):
        r"""HostReadWrite(DenseSymmetricMatrix self) -> double *"""
        return _symmat.DenseSymmetricMatrix_HostReadWrite(self)
    HostReadWrite = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_HostReadWrite)

    def Mult(self, x, y):
        r"""Mult(DenseSymmetricMatrix self, Vector x, Vector y)"""
        return _symmat.DenseSymmetricMatrix_Mult(self, x, y)
    Mult = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Mult)

    def Inverse(self):
        r"""Inverse(DenseSymmetricMatrix self) -> MatrixInverse"""
        return _symmat.DenseSymmetricMatrix_Inverse(self)
    Inverse = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Inverse)
    __swig_destroy__ = _symmat.delete_DenseSymmetricMatrix

    def Print(self, *args):
        r"""
        Print(DenseSymmetricMatrix self, std::ostream & out=out, int width_=4)
        Print(DenseSymmetricMatrix self, char const * file, int precision=16)
        """
        return _symmat.DenseSymmetricMatrix_Print(self, *args)
    Print = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_Print)

    def PrintGZ(self, file, precision=16):
        r"""PrintGZ(DenseSymmetricMatrix self, char const * file, int precision=16)"""
        return _symmat.DenseSymmetricMatrix_PrintGZ(self, file, precision)
    PrintGZ = _swig_new_instance_method(_symmat.DenseSymmetricMatrix_PrintGZ)

# Register DenseSymmetricMatrix in _symmat:
_symmat.DenseSymmetricMatrix_swigregister(DenseSymmetricMatrix)



