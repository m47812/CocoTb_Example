import cocotb
from cocotb.triggers import FallingEdge, ClockCycles
from cocotb.clock import Clock

DUT_LATENCY = 1
result_que = []

async def stimuli(dut, result_que):
    for a in range(256):
        for b in range(256):
            dut.a.value = a
            dut.b.value = b
            result_que.append(ref_result_gen(a, b))
            await FallingEdge(dut.clk)

def ref_result_gen(a, b):
    return a + b

async def monitor(dut, LATENCY, result_que):
    await ClockCycles(dut.clk, LATENCY, rising=False)
    for _ in range(256*256):
        ref_value = result_que.pop(0)
        result_value = int(dut.c.value)
        assert ref_value == result_value, \
            f"Expected {ref_value} but got {result_value}"
        await FallingEdge(dut.clk)

@cocotb.test(timeout_time=10, timeout_unit='ms')
async def exhaustive_adder_test(dut):
    #Start Clock
    clk_200MHz = Clock(dut.clk, 5, units="ns")
    clk_task = cocotb.start_soon(clk_200MHz.start())
    await FallingEdge(dut.clk) #Wait for first falling edge
    #Start stimuli and monitor
    result_que = []
    monitor_task = cocotb.start_soon(monitor(dut, DUT_LATENCY, result_que))
    stimuli_task = cocotb.start_soon(stimuli(dut, result_que))
    await monitor_task, stimuli_task