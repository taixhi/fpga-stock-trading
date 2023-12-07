`timescale 1ns / 1ps

module tb_moving_average_filter;

// Inputs
reg clk;
reg [7:0] rpi_gpio_tri_io;

// Outputs
wire [7:0] rpi_gpio_tri_io_o;

// Instantiate the Unit Under Test (UUT)
moving_average_filter uut (
    .clk(clk),
    .rpi_gpio_tri_io(rpi_gpio_tri_io),
    .rpi_gpio_tri_io_o(rpi_gpio_tri_io_o)
);

initial begin
    // Initialize Inputs
    clk = 0;
    rpi_gpio_tri_io = 0;

    // Wait for 100 ns for global reset to finish
    #100;
    
    // Add stimulus here
    rpi_gpio_tri_io = 8'b00000001;
    #10;
    rpi_gpio_tri_io = 8'b00000010;
    #10;
    rpi_gpio_tri_io = 8'b00000100;
    #10;
    rpi_gpio_tri_io = 8'b00001000;
    #10;
    rpi_gpio_tri_io = 8'b00010000;
    #10;
    rpi_gpio_tri_io = 8'b00100000;
    #10;
    rpi_gpio_tri_io = 8'b01000000;
    #10;
    rpi_gpio_tri_io = 8'b10000000;
    #10;

    // Finish the simulation
    $finish;
end

// Clock generation
always #5 clk = ~clk;

endmodule
