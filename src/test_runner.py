# MIT License

# Copyright (c) 2024 Robin Müller

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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