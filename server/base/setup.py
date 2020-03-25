from distutils.core import setup, Extension

setup(ext_modules=[Extension("_equation_solver_base",
						sources=["equation_solver_base.cpp", "equation_solver_base_wrap.cxx"])])
