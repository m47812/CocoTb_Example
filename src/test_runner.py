import os
from cocotb.runner import get_runner

def test_adder():
    # Base directory where test_runner.py is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct absolute paths
    vhdl_sources = [os.path.join(base_dir, "simple_adder.vhd")]  # Absolute path to VHDL sources
    build_dir = os.path.join(base_dir, "sim_build")  # Absolute path to build directory
    
    runner = get_runner("questa")  # Specify your simulator
    
    # Compile
    runner.build(
        vhdl_sources=vhdl_sources,
        hdl_toplevel="simple_adder",
        build_dir=build_dir
    )
    
    # Run Test
    runner.test(
        hdl_toplevel="simple_adder",  # Name of the top level entity
        test_dir=base_dir,  # Directory of the test
        test_module="simple_adder",  # Test python file (needs to be located in test_dir)
        hdl_toplevel_library="./sim_build/top",  # Specifies where the build results are located relative to test_dir
        test_args=['-t', '1ps']  # Sets Simulator timescale from 'ns' to 'ps'
    )