%module equation_solver_base

%{
        #define SWIG_FILE_WITH_INIT
        #include "equation_solver_base.h"

%}

%include "std_vector.i"
%include "std_pair.i"
%template(cdpair) std::pair<char,double>;
%template(vp) std::vector<std::pair<char,double>>;
%include "equation_solver_base.h"
