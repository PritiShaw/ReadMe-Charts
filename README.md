ReadMe Charts
---
Add Charts from CSV to your README files

**Supported File Formats** : *CSV* , *TSV*  
**Supported Charts** : *Line*, others to be added  
**Output Format** : png, svg, pdf, jpeg, jpg, eps, pgf, ps, raw, rgba, svgz, tif, tiff

### How to Use
Host or upload the source file and make sure it is accessible publicly.  
The chart will be visible at following link  
`https://readmecharts.vercel.app/?src=<Link to Source File>`  
**Limitation** : First row is consider as Header row

### Configuration
You can provide following parameters using URL Query String  

Parameter | Description
---|---
src| [**Required**] Link to source file
title| Title of the Chart
legend | Show Legend, `legend=1` for showing, dont give `legend` param if you dont want legend
x | XAxis Label
y | YAxis Label
xmin | X minimum threshold
xmax | X maximum threshold
ymin | Y minimum threshold
ymax | Y maximum threshold
dark | `dark=1` will render in dark, dont give `dark` param if you need light theme

### Examples

**Sine Curve**  
`https://readmecharts.vercel.app/?src=https://gist.githubusercontent.com/PritiShaw/f4a75e117ba41f4f779732387147142f/raw/061f8d6385f01a32c04172e73fa866392d138698/sine.csv&dark=1`  
![](https://readmecharts.vercel.app/?src=https://gist.githubusercontent.com/PritiShaw/f4a75e117ba41f4f779732387147142f/raw/061f8d6385f01a32c04172e73fa866392d138698/sine.csv&dark=1&legend=1)

**Using Realtime data***

**COVID-19 Cases in India**

`https://readmecharts.vercel.app/?src=https://api.covid19india.org/csv/latest/case_time_series.csv&title=COVID-19%20Cases%20in%20India&x=Days`  
![](https://readmecharts.vercel.app/?src=https://api.covid19india.org/csv/latest/case_time_series.csv&title=COVID-19%20Cases%20in%20India&x=Days&legend=1)   

**COVID-19 Cases in USA**  
`https://readmecharts.vercel.app/?src=https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv&x=Days&title=COVID-19%20Cases%20in%20USA&legend=1`  
![](https://readmecharts.vercel.app/?src=https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv&x=Days&title=COVID-19%20Cases%20in%20USA&legend=1)  
