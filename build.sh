cd server/base
swig -c++ -python equation_solver_base.i
python3 setup.py build_ext --inplace
cd ..
cd ..
