

# WP3T31-03	Safety and security hardware support

This repository contains SELENE hardware platform instrumented with Register File Randomization (RFR) mechanism.
As explained in [1], RFR allows to:
- mitigate the impact of common-cause faults in the multicore CPUs (NOEL-V in this case), and 
- balance the usage of physical registers, and thus to extend the lifetime of the register file.
  
This component is included as a submodule from the SELENE repository:
https://gitlab.com/selene-riscv-platform/selene-hardware/-/tree/regfile_randomization.   
Remember to clone this repository recursively, as interconnect/axi and interconnect/common\_cells are submodules.

The directories are organized as follows:

grlib                               GRLIB IP core library
grlib/bin                           GRLIB infrastructure
grlib/boards                        Board description files
grlib/designs                       Template designs
grlib/doc                           GRLIB documentation
grlib/lib                           GRLIB IP core RTL code
grlib/software                      NOEL-V example software
selene-soc                          SELENE SoC directory
selene-soc/rtl                      Design files common to all FPGAs
selene-soc/selene-generic           Generic template design
selene-soc/selene-xilinx-vcu118     Template design tailored for VCU118

## References

[1] Tuzov I, Andreu P, Medina L, Picornell T, Robles A, Lopez P, Flich J, Hernández C. Improving the Robustness of Redundant Execution with Register File Randomization. In2021 IEEE/ACM International Conference On Computer Aided Design (ICCAD) 2021 Nov 1 (pp. 1-9). IEEE. doi: 10.1109/ICCAD51958.2021.9643466
