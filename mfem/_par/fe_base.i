%module(package="mfem._par") fe_base
%{
#include  "mfem.hpp"
#include "fem/fe/fe_base.hpp"  
#include "fem/fe/fe_h1.hpp"
#include "mesh/hexahedron.hpp"
#include "numpy/arrayobject.h"    
%}

%init %{
import_array();
%}
%include "exception.i"
%import "intrules.i"
%import "geom.i"
%include "../common/typemap_macros.i"
%include "../common/exception.i"

 //%ignore FE;
namespace mfem{
  class FiniteElement;
}

%include "fem/fe/fe_base.hpp"