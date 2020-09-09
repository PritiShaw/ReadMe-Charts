ReadMe Charts
---
Add Realtime charts from CSV to your README files

**Supported File Formats** : *CSV* , *TSV*  
**Supported Charts** : *Line*, others to be added  
**Output Format** : SVG

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
x | XAxis Label
y | YAxis Label

### Examples

**Sine Curve**  
`https://readmecharts.vercel.app/?src=https://gist.githubusercontent.com/PritiShaw/f4a75e117ba41f4f779732387147142f/raw/061f8d6385f01a32c04172e73fa866392d138698/sine.csv`  
![](https://readmecharts.vercel.app/?src=https://gist.githubusercontent.com/PritiShaw/f4a75e117ba41f4f779732387147142f/raw/061f8d6385f01a32c04172e73fa866392d138698/sine.csv)

**COVID-19 Cases in India**: Using Realtime data  
`https://readmecharts.vercel.app/?src=https://api.covid19india.org/csv/latest/case_time_series.csv&title=COVID-19%20Cases%20in%20India&x=Days`  
![](https://readmecharts.vercel.app/?src=https://api.covid19india.org/csv/latest/case_time_series.csv&title=COVID-19%20Cases%20in%20India&x=Days)
