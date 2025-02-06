# System Performance Monitor

This script monitors system performance metrics such as CPU usage, memory usage, disk usage, swap usage, network statistics, and system load. It logs the collected data into a CSV file at regular intervals.

## Features
- Logs system performance metrics to `system_performance.csv`.
- Monitors CPU, memory, swap, disk, and network usage.
- Tracks system load over 1, 5, and 15 minutes.
- Identifies the top process consuming CPU and memory.

## Prerequisites
Ensure you have Python installed along with the `psutil` library:

```sh
pip install psutil
```

## Usage
1. Clone the repository:

```sh
git clone https://github.com/rinas21/System-Performance-Monitor.git
cd system-monitor
```

2. Run the script:

```sh
python3 monitor.py
```

## Output
- The script generates a `system_performance.csv` file containing logged performance data.

## Customization
- Modify the `time.sleep()` interval in the script to adjust logging frequency.
- Extend the script to capture additional system metrics as needed.

## License
This project is open-source under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the script.

## Author
A.M.Rinas

