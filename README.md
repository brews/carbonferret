# carbonferret

Simple Python library to quickly query carbon reservoir records at the Marine Reservoir Correction database (http://calib.org/marine/).

## Example

Here is a quick example. The package has a single function:

    import carbonferret as cf

    results = cf.find_near(lat = 0, lon = 0, n = 2)

`results` is a [pandas](http://pandas.pydata.org/) DataFrame with information on sample location and the reservoir values for the two points nearest to 0° latitude and 0° longitude.
