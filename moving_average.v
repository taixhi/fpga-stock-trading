module moving_average_filter(
    input clk,
    input [7:0] rpi_gpio_tri_io,
    output reg [7:0] rpi_gpio_tri_io_o
);

// Define the window size for the moving average
//localparam WINDOW_SIZE = 4;

// Declare a register array to store the samples
//reg [7:0] samples[WINDOW_SIZE-1:0];

// Declare a variable for the sum
//reg [7:0] prev = 8'b00000000;  // 10 bits to handle overflow
//reg [7:0] first;
//reg [7:0] second;
//integer i;

reg [9:0] sum;
reg [7:0] prev;
reg [7:0] prev2;
reg [7:0] prev3;
reg [7:0] prev4;

initial sum = 0;
initial prev = 0;
initial prev2 = 0;
initial prev3 = 0;
initial prev4 = 0;

//// working code 
//always @(posedge clk) begin
//    rpi_gpio_tri_io_o = (prev + rpi_gpio_tri_io) / 2;
//end 
//always @(posedge clk) begin
//    prev = rpi_gpio_tri_io;  
//end
////endmodule

always @(posedge clk) begin
    sum = sum - prev + rpi_gpio_tri_io;
    prev = prev2;
    prev2 = prev3;
    prev3 = prev4;
    prev4 = rpi_gpio_tri_io;
    rpi_gpio_tri_io_o = sum / 4;
end 
endmodule
