# Your desired build settings
SIM ?= questa
TOPLEVEL_LANG ?= vhdl

# Add all vhdl source files
VHDL_SOURCES += $(PWD)/simple_adder.vhd

TOPLEVEL = simple_adder #Name of the top level VHDL entity
MODULE = simple_adder #Name of the python file with the test cases (simple_adder.py)

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim