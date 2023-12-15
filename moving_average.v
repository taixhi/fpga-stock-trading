module moving_average_filter(
    input clk,
    input [7:0] rpi_gpio_tri_io,
    output reg [7:0] rpi_gpio_tri_io_o
);

reg [13:0] sum;
reg [7:0] stored [31:0];

initial sum = 0;


genvar i;
for (i = 0; i < 32; i = i+1) begin
    initial stored[i] = 0;
end 

integer j; // Declare 'j' outside the always block

initial begin
    j = 0; // Initialize 'j' here
end

always @ (posedge clk) begin
    sum = sum - stored[0] + rpi_gpio_tri_io;
    for (j = 0; j <31; j = j+1) begin
        stored[j] = stored[j+1];
    end
    stored[31] = rpi_gpio_tri_io;
    rpi_gpio_tri_io_o = sum >> 5 ;

end 
endmodule
