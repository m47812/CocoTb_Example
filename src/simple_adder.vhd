-- MIT License

-- Copyright (c) 2024 Robin Müller

-- Permission is hereby granted, free of charge, to any person obtaining a copy
-- of this software and associated documentation files (the "Software"), to deal
-- in the Software without restriction, including without limitation the rights
-- to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-- copies of the Software, and to permit persons to whom the Software is
-- furnished to do so, subject to the following conditions:

-- The above copyright notice and this permission notice shall be included in all
-- copies or substantial portions of the Software.

-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-- IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-- FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-- AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-- LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-- OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-- SOFTWARE.


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity simple_adder is
    generic ( g_nb_bits : natural := 8 );
    Port ( 
        clk : in  STD_LOGIC;
        a : in  STD_LOGIC_VECTOR (g_nb_bits - 1 downto 0);
        b : in  STD_LOGIC_VECTOR (g_nb_bits - 1 downto 0);
        c : out  STD_LOGIC_VECTOR (g_nb_bits downto 0)
    );
end simple_adder;

architecture RTL of simple_adder is
    signal c_reg : std_logic_vector(g_nb_bits downto 0);
begin
    process(clk)
    begin
        if rising_edge(clk) then
            c_reg <= std_logic_vector(resize(unsigned(a), g_nb_bits + 1) + resize(unsigned(b), g_nb_bits + 1));
        end if;
    end process;
    c <= c_reg;
end RTL;