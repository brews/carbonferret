# carbonferret

[![Travis-CI Build Status](https://travis-ci.org/brews/carbonferret.svg?branch=master)](https://travis-ci.org/brews/carbonferret)

A Python package to quickly fetch carbon reservoir records at the Marine Reservoir Correction database (http://calib.org/marine/).

## Example

The carbonferret package is simple, but powerful. For instance, let's say we want to find two sediment records 
nearest 0° latitude, 0° longitude. We can open a python session and run:

```python
import carbonferret as cf

results = cf.find_near(lat=0, lon=0, n=2)
```

The variable `results` is for a [pandas](http://pandas.pydata.org/) DataFrame with information on sample location and 
reservoir values, among other variables provided by the Marine Reservoir Correction database.

We can take advantage of this by, for example, findind the average ΔR of these sites.

```python
results['DeltaR'].mean()
```
Of course, there are several other variables that we can look at, such as site references or site location.

This can be extremely useful if you want to look up a few quick numbers in the lab, or if you are writing a script to 
analyze hundreds of marine sediment cores.

## Installation

You can install the package [from PyPI](https://pypi.python.org/pypi/carbonferret) with

```
pip install carbonferret
```

## Development and Support

Source code is [hosted online](https://github.com/brews/carbonferret) under an Open Source license. Please feel free to 
file any [bugs and issues](https://github.com/brews/carbonferret/issues) you find.
