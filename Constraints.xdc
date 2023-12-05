# Redefining the constraints for Raspberry Pi GPIO pins
set_property -dict { PACKAGE_PIN W18    IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[0] }];   # GPIO2
set_property -dict { PACKAGE_PIN W19    IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[1] }];   # GPIO3
set_property -dict { PACKAGE_PIN Y18    IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[2] }];   # GPIO4
set_property -dict { PACKAGE_PIN U7 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[3] }];   # GPIO17
set_property -dict { PACKAGE_PIN V7 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[4] }];   # GPIO27
set_property -dict { PACKAGE_PIN U8 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[5] }];   # GPIO22
set_property -dict { PACKAGE_PIN V8 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[6] }];   # GPIO10
set_property -dict { PACKAGE_PIN V10 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[7] }];   # GPIO9
set_property -dict { PACKAGE_PIN W10 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[8] }];   # GPIO11
set_property -dict { PACKAGE_PIN Y16    IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[9] }];   # GPIO5
set_property -dict { PACKAGE_PIN Y19    IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[10] }];  # GPIO6
set_property -dict { PACKAGE_PIN Y17 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[11]] }];  # GPIO13
set_property -dict { PACKAGE_PIN W8 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[12] }];  # GPIO19
set_property -dict { PACKAGE_PIN Y8 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[13] }];  # GPIO26
set_property -dict { PACKAGE_PIN W9 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[14] }];  # GPIO14
set_property -dict { PACKAGE_PIN V6 IOSTANDARD LVCMOS33 } [get_ports { rpi_gpio_tri_io[15] }];  # GPIO15
