# Moving Average Plotter

## About ##

This script reads in a CSV file containing financial data and plots the original closing prices along with a moving average computed using a sliding window approach.

## Prerequisites

This script requires the following libraries:

- NumPy
- Pandas
- Matplotlib

You can install them via pip, using the command:
```
pip install numpy pandas matplotlib
```

## Installing

1- Clone this repository to your local machine.

2- Navigate to the project directory.

3- Place your CSV file containing financial data under the res directory.

4- Update the kernel_size variable in project.py to set the size of the moving window.

Run the script using the command:
```
python project.py
```
The plot should open in a new window.

## Usage
The script reads in a CSV file containing financial data and expects it to have the following columns:

- `<DTYYYYMMDD>`: Date in YYYYMMDD format.

- `<CLOSE>`: Closing price.

It then computes a moving average of the closing prices using a sliding window approach with the specified kernel_size. Finally, it plots the original closing prices along with the computed moving average.

You can customize the behavior of the script by modifying the value of the kernel_size variable in project.py. The larger the kernel size, the smoother (and less responsive) the resulting moving average curve will be.

Also np.convolve method represent this code:
```
moving_avg[kernel_size:] = np.array([close_values[i : i + kernel_size + 1].mean() for i in range(len(close_values) - kernel_size)])
```

## Example

![sample](https://github.com/sajiniho07/MovingAveragePractice/blob/master/res/output.png)

## License ##

Made with :heart: by <a href="https://github.com/sajiniho07" target="_blank">Sajad Kamali</a>

<a href="#top">Back to top</a>
