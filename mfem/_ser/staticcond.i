%module(package="mfem._ser")  staticcond
%{
#include "mfem.hpp"
#include "numpy/arrayobject.h"  
#include "../common/pyoperator.hpp"        
#include "../common/pycoefficient.hpp"
#include "../common/pyintrules.hpp"
%}

%init %{
import_array();
%}

%include "exception.i"
%import "fespace.i"

%include "fem/staticcond.hpp"
