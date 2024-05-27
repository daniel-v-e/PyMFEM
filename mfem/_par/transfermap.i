%module(package="mfem._par") transfermap

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

%import "mesh.i"

%include "mesh/submesh/transfermap.hpp"

#endif

