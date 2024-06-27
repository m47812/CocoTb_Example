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