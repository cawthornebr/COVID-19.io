# Covid-19
## Source of data

Johns Hopkins University (JHU): https://coronavirus.jhu.edu/map.html

JHU GitHub for COVID data - https://github.com/CSSEGISandData/COVID-19

JHU only started breaking cases down by county starting 3/22/2020, because of this, I'll only be using data from that date forward.

## Info

The JHU site above only displays the total number of confirmed, deaths, and recovered cases. I wanted to know the rate that confirmed cases were increasing which isn’t displayed on their site to me that’s all that matters. Originally, I wanted to create charts that displayed the rate increase of cases by day by county for Arizona. After writing this code for just Arizona, I had others who wanted this breakdown for their state as well. I scaled my code so now ‘Step 1 - Split by county’ will require an input of the desired state and it will generate a state specific csv. ‘Step 2 - Display data’ will require an input of the desired state and will then use the csv created from step 1 to generate the accompanying charts.