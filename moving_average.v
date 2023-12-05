module moving_average (
    input clk,                      // Clock signal
    input reset,                    // Reset signal
    input [7:0] in_data,            // 8-bit input data
    output reg [7:0] out_avg        // 8-bit output average
);

// Parameters
localparam integer DATA_WIDTH = 8;
localparam integer NUM_DAYS = 8;

// Registers
reg [DATA_WIDTH-1:0] data_array[NUM_DAYS-1:0]; // Array to store the last 8 values
reg [10:0] sum = 0;                            // Sum of the last 8 values (11 bits for up to 2040 max sum)

integer i;

// Load new data and calculate sum
always @(posedge clk or posedge reset) begin
    if (reset) begin
        // Reset logic
        sum <= 0;
        for (i = 0; i < NUM_DAYS; i = i + 1) begin
            data_array[i] <= 0;
        end
    end else begin
        // Shift the data array and add new data
        sum <= sum - data_array[NUM_DAYS-1] + in_data;
        for (i = NUM_DAYS-1; i > 0; i = i - 1) begin
            data_array[i] <= data_array[i-1];
        end
        data_array[0] <= in_data;

        // Calculate moving average
        // Note: Right shift by 3 (equivalent to dividing by 8) for the average
        out_avg <= sum >> 3;
    end
end

endmodule
