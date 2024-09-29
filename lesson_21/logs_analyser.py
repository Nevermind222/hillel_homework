import re
from datetime import datetime, timedelta


def analyze_heartbeat_log(input_log_path, output_log_path):
    with open(input_log_path, 'r') as log_file:
        log_lines = log_file.readlines()

    key = "Key TSTFEED0300|7E3E|0400"
    filtered_lines = [line for line in log_lines if key in line]

    prev_timestamp = None

    with open(output_log_path, 'w') as output_log:
        for line in filtered_lines:
            timestamp_idx = line.find("Timestamp ")
            if timestamp_idx == -1:
                continue

            timestamp_str = line[timestamp_idx + len("Timestamp "):timestamp_idx + len("Timestamp ") + 8]

            try:
                current_timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")
            except ValueError:
                continue

            if prev_timestamp:
                time_diff = (prev_timestamp - current_timestamp).total_seconds()

                if 31 < time_diff < 33:
                    output_log.write(f"WARNING at {timestamp_str}: Heartbeat interval {time_diff} seconds.\n")
                elif time_diff >= 33:
                    output_log.write(f"ERROR at {timestamp_str}: Heartbeat interval {time_diff} seconds.\n")

            prev_timestamp = current_timestamp


analyze_heartbeat_log("hblog.txt", "hb_test.log")
