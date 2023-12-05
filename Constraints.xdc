# Redefining the constraints for Raspberry Pi GPIO pins
set_property -dict { PACKAGE_PIN W18    IOSTANDARD LVCMOS33 } [get_ports { input[0] }];   # GPIO2
set_property -dict { PACKAGE_PIN W19    IOSTANDARD LVCMOS33 } [get_ports { input[1] }];   # GPIO3
set_property -dict { PACKAGE_PIN Y18    IOSTANDARD LVCMOS33 } [get_ports { input[2] }];   # GPIO4
set_property -dict { PACKAGE_PIN U7 IOSTANDARD LVCMOS33 } [get_ports { input[3] }];   # GPIO17
set_property -dict { PACKAGE_PIN V7 IOSTANDARD LVCMOS33 } [get_ports { input[4] }];   # GPIO27
set_property -dict { PACKAGE_PIN U8 IOSTANDARD LVCMOS33 } [get_ports { input[5] }];   # GPIO22
set_property -dict { PACKAGE_PIN V8 IOSTANDARD LVCMOS33 } [get_ports { input[6] }];   # GPIO10
set_property -dict { PACKAGE_PIN V10 IOSTANDARD LVCMOS33 } [get_ports { input[7] }];   # GPIO9
set_property -dict { PACKAGE_PIN W10 IOSTANDARD LVCMOS33 } [get_ports { output[0] }];   # GPIO11
set_property -dict { PACKAGE_PIN Y16    IOSTANDARD LVCMOS33 } [get_ports { output[1] }];   # GPIO5
set_property -dict { PACKAGE_PIN Y19    IOSTANDARD LVCMOS33 } [get_ports { output[2] }];  # GPIO6
set_property -dict { PACKAGE_PIN Y17 IOSTANDARD LVCMOS33 } [get_ports { output[3] }];  # GPIO13
set_property -dict { PACKAGE_PIN W8 IOSTANDARD LVCMOS33 } [get_ports { output[4] }];  # GPIO19
set_property -dict { PACKAGE_PIN Y8 IOSTANDARD LVCMOS33 } [get_ports { output[5] }];  # GPIO26
set_property -dict { PACKAGE_PIN W9 IOSTANDARD LVCMOS33 } [get_ports { output[6] }];  # GPIO14
set_property -dict { PACKAGE_PIN V6 IOSTANDARD LVCMOS33 } [get_ports { output[7] }];  # GPIO15
