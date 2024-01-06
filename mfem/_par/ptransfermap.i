%module(package="mfem._par") ptransfermap

%feature("autodoc", "1");

%{
#include  "mfem.hpp"
#include "numpy/arrayobject.h"
#include "../common/pyoperator.hpp"
#include "../common/pycoefficient.hpp"
#include "../common/pyintrules.hpp"  
%}

%include "../common/existing_mfem_headers.i"
#ifdef FILE_EXISTS_MESH_SUBMESH_TRANSFERMAP

%init %{
import_array();
%}

%include "exception.i"
%include "../common/exception.i"

%import "hypre.i"
%import "pmesh.i"
%import "pgridfunc.i"

%include "mesh/submesh/ptransfermap.hpp"

#endif

