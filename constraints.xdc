module moving_average_filter(
    input clk,
    input reset,
    input [7:0] rpi_gpio_tri_io,
    output [7:0] rpi_gpio_tri_io_o
);
assign rpi_gpio_tri_io_o = rpi_gpio_tri_io;
endmodule