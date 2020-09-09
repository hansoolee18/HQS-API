# HQS API: HQS automation module for quantification of user types

HQS API that grasps the user's foreground app usage time event in real time, classifies what category each app is in, calculates the total amount of usage time for each category, and compares it with the reference value of 80 users

## Function Description
### Built-in Functions

#### 1. findctg

* A function to classify categories by package name

#### 2. delovr

* Excluding duplicate elements in the list

#### 3. che_time

* Entering the number of timestamp returns a datetime object with year, month, day, hour, and minute information.

#### 4. oclock

* If you enter the year, month, day, hour, and minute, it will be converted to a number in a timestamp format.

#### 5. che_wday

* Entering an 8-digit string as a string returns the day of the week

#### 6. statistic

* Putting in a list returns the sum, average, maximum, minimum, and median values ​​based on the elements of the list. Total is used when calculating percentage option

#### 7. sumproduct

* It is used to make a group from the standard HQS value data and calculate the weighted average for each group.

#### 8. make_s_week
* Used to create 's_week0' ~ 's_week6' variables from standard data for each day of the week

### Output Functions

#### 1. finding

  It is a function that informs the time zone and date in which the input data was recorded, and is necessary to facilitate the user's parameter setting.

**paramters:**
  * inputdata: list-like of shape [n_samples, 4]
  
Examples
```
>>> inputdata = [[1557275299.311, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_RESUMED'], [1557275313.169, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_PAUSED'],...]

>>> HQS.finding(inputdata)
```

**return:**

```
>>> [['DATE', '0시', '1시', '2시', '3시', '4시', '5시', '6시', '7시', '8시', '9시', '10시', '11시', '12시', '13시', '14시', '15시', '16시', '17시', '18시', '19시', '20시', '21시', '22시', '23시'], [20190516, 0, 0, 0, 0, 0, 0, 0, 0, 0, 32.0843499938647, 49.57675000031788, 10.33324999809265, 37.07876663605373, 13.894100010395045, 3.6712499936421708, 33.336099986235304, 11.578566666444141, 16.713666713237767, 17.198833362261457, 15.619833342234296, 10.405233319600425, 13.398050010204319, 3.4780499935150146, 6.409583334128062],,,]
```

#### 2. misscategory

If the package name of inputdata does not include the package name of the category list, it is classified as unclassified.

**paramters:**
  * inputdata: list-like of shape [n_samples, 4]
  
Examples
```
>>> inputdata = [[1557275299.311, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_RESUMED'], [1557275313.169, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_PAUSED'],...]

>>> HQS.miscategory(inputdata)
```

**return:**

```
>>> [['missing', '날씨', 'com.sec.android.daemonapp'],
 ['missing', '날씨', 'com.lge.sizechangable.weather'],
.....
 ['missing', '동영상', 'com.lge.videoplayer'],
 ['missing', '동영상 다운로더', 'video.downloader.videodownloader'],,,]
```

#### 3. digital

When input data comes in, a function that compares each app name and package name with the existing app category list of 80 users, gives statistics of usage time by category according to the set time and number of days after matching, and compares it with the standard value of 80 app categories
```
digital(inputlist, timeunit ='h', timeunit_n=1, divisionmethod ='section', comparisonvaluetype='timeofday', 
```

**paramters:**

 * inputdata: list-like of shape [n_samples, 4]
 
   * receive timestamp, name, packagename and type
 
 * timeunit: {‘h’, ‘am’, ‘pm’, ‘d’, ‘all’}, default = ‘h’ 
 * timeunit_n: int n, default = 1
 * divisionmethod: {‘section’, ‘nonsection’}, default = ‘section’ 
 * comparisonvaluetype: {‘timeofday’, ‘dayofweek’}, default = ‘timeofday’
 * comparisionstatistics: {‘mean’, ‘max’, ‘min’, ‘median’, ‘percentage’}, default = ‘mean
 

Examples
```
>>> inputdata = [[1557275299.311, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_RESUMED'], [1557275313.169, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_PAUSED'],...]

>>> HQS.digital(inputdata, ‘h’, ‘3’, ‘section’, ‘typeofday’, 'mean’)
```

**return:**

```
{'Art & Design': {'compare': 0.71, 'input': 0.05, 'standard': 0.07},
 'Beauty': {'compare': 1.0, 'input': 0.1, 'standard': 0.1},
 'Books & Reference': {'compare': 1.76, 'input': 5.34, 'standard': 3.04},
 'Communication': {'compare': 1.33, 'input': 1436.64, 'standard': 1079.06},
 'Education': {'compare': 0.86, 'input': 19.89, 'standard': 23.16},
 'Entertainment': {'compare': 0.07, 'input': 4.21, 'standard': 63.61},
 'Finance': {'compare': 0.3, 'input': 10.67, 'standard': 35.39},
 'Food & Drink': {'compare': 0.41, 'input': 2.93, 'standard': 7.1},
 'Game': {'compare': 0.0, 'input': 0.04, 'standard': 19.46},
 'Health & Fitness': {'compare': 0.16, 'input': 0.26, 'standard': 1.62},
 'Libraries & Demo': {'compare': 1.38, 'input': 19.05, 'standard': 13.81},
 'Lifestyle': {'compare': 0.09, 'input': 10.19, 'standard': 110.02},
 'Maps & Navigation': {'compare': 0.34, 'input': 27.41, 'standard': 80.88},
 'Social': {'compare': 0.39, 'input': 260.99, 'standard': 662.43},
 'Tools': {'compare': 0.25, 'input': 40.66, 'standard': 159.51},
 'Total': {'compare': 0.74, 'input': 2255.15, 'standard': 3064.17}}
```

#### 4. social

```
social(inputlist, timeunit ='h', timeunit_n=1, divisionmethod ='section', comparisonvaluetype='timeofday', 
```

**paramters:**

 * inputdata: list-like of shape [n_samples, 4]
 
   * receive timestamp, name, packagename and type
 
 * timeunit: {‘h’, ‘am’, ‘pm’, ‘d’, ‘all’}, default = ‘h’ 
 * timeunit_n: int n, default = 1
 * divisionmethod: {‘section’, ‘nonsection’}, default = ‘section’ 
 * comparisonvaluetype: {‘timeofday’, ‘dayofweek’}, default = ‘timeofday’
 * comparisionstatistics: {‘mean’, ‘max’, ‘min’, ‘median’, ‘percentage’}, default = ‘mean
 

Examples
```
>>> inputdata = [[1557275299.311, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_RESUMED'], [1557275313.169, 'Samsung Experience 홈', 'com.sec.android.app.launcher', 'ACTIVITY_PAUSED'],...]

>>> HQS.digital(inputdata, ‘h’, ‘1’, ‘section’, ‘timeofday’, 'mean’)
```

**return:**
```
{'Communication': {'compare': 1.33, 'input': 1436.64, 'standard': 1079.06},
 'Social': {'compare': 0.39, 'input': 260.99, 'standard': 662.43},
 'Total': {'compare': 0.74, 'input': 2255.15, 'standard': 3064.17}}
```

### Variables Printing Fuction

#### 1. list2xl
#### 2. dic2xl
#### 3. var2xl
#### 4. ipt2x1
#### 5. grp2xl


## Test example

**Output variables**
#### dic01: {date: {datetime, [input data])}
#### dic02: {date: [['category, 'appname', time of day, usage time, packagename, foreground, background],,,],,} 
#### dic03: Classify
#### dic04: 
#### dic05: 
#### dic06: 
#### ipt01:
#### grp10:
#### grp20:
#### grp21:

### End-to-End test



```

```



## Contribution

## Version control

## Copywriter holders

* **Hansoo Lee**


## License

