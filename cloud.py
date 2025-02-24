import pandas as pd
from datetime import datetime

# This Function converts data to InfluxDB line protocol
def convert_to_influxdb_line_protocol(row):
    
    measurement = "cloud_billing"
    tags = f"service={row['Service']},region={row['Region']},usage_type={row['Usage_Type']}"
    fields = f"usage_quantity={row['Usage_Quantity']},cost_usd={row['Cost_USD']}"
    timestamp = int(datetime.now().timestamp() * 1e9)  # Nanoseconds
    return f"{measurement},{tags} {fields} {timestamp}"

# Load the CSV file
csv_file_path = "telegraf_cloud_billing_metrics_large.csv"  
data = pd.read_csv(csv_file_path)

# Convert each row to InfluxDB line protocol
influxdb_lines = data.apply(convert_to_influxdb_line_protocol, axis=1)

# Save the output to a file
output_file_path = "cloud_billing_influxdb_output.txt"
with open(output_file_path, "w") as file:
    file.write("\n".join(influxdb_lines))

print(f"InfluxDB formatted data has been saved to: {output_file_path}")