#!/usr/bin/env python
# Design space sweep definition.
#
# THIS IS AN EXAMPLE OF SUCH A FILE. This example should list all the parameters
# that we currently support sweeping. To use, make a copy of this file and call
# it sweep_config.py.
#
# To dynamically change the set of swept parameters, edit the
# generate_all_configs() function inside generate_design_sweeps.py.

from design_sweep_types import *

# Sweep parameters. If a certain parameter should not be swept, set the value of
# step_type to NO_SWEEP, and the value of start will be used as a constant. end
# will be ignored. Unless step_type is NO_SWEEP, step should never be less than
# 1.
cycle_time = SweepParam(
    "cycle_time", start=1, end=1, step=2, step_type=NO_SWEEP)
unrolling = SweepParam(
    "unrolling", start=8, end=32, step=2, step_type=NO_SWEEP)
partition = SweepParam(
    "partition", start=1, end=32, step=2, step_type=EXP_SWEEP)
pipelining = SweepParam(
    "pipelining", start=1, end=1, step=1, step_type=NO_SWEEP)
tlb_entries = SweepParam(
    "tlb_entries", start=64, end=64, step=2, step_type=NO_SWEEP)
tlb_max_outstanding_walks = SweepParam(
    "tlb_max_outstanding_walks", start=2, end=2, step=0, step_type=NO_SWEEP)
tlb_bandwidth = SweepParam(
    "tlb_bandwidth", start=3, end=3, step=2, step_type=NO_SWEEP)
load_bandwidth = SweepParam(
    "load_bandwidth", start=3, end=3, step=2, step_type=NO_SWEEP)
load_queue_size = SweepParam(
    "load_queue_size", start=32, end=64, step=2, step_type=NO_SWEEP)
store_queue_size = SweepParam(
    "store_queue_size", start=32, end=64, step=2, step_type=NO_SWEEP)
cache_size = SweepParam(
     "cache_size", start=32768, end=32768, step=2, step_type=NO_SWEEP,
     sweep_per_kernel=False)
cache_hit_latency = SweepParam(
    "cache_hit_latency", start=1, end=1, step=1, step_type=NO_SWEEP)
cache_assoc = SweepParam(
    "cache_assoc", start=4, end=4, step=2, step_type=NO_SWEEP)
cache_line_sz = SweepParam(
    "cache_line_sz", start=8, end=128, step=2, step_type=EXP_SWEEP)
dma_setup_latency = SweepParam(
    "dma_setup_latency", start=1, end=1, step=1, step_type=NO_SWEEP)
l2cache_size = SweepParam(
    "l2cache_size", start=131072, end=262144, step=2, step_type=NO_SWEEP)
SWEEP_PER_KERNEL = True
