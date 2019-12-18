<!--
___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!
-->
# leap_year_calculator

Django-Based leap year calculator.
If you have any comments about this, please feel free to [contact @tekupoko3](https://twitter.com/tekupoko3).

# JudgeLeapYear.py

core class definition for leap year calculator.  
Directory: [leap\_year\_calculator/leapyearcalc/judgeleapyear/](https://github.com/tekupoko3/leap_year_calculator/tree/master/leapyearcalc/judgeleapyear)

## class JudgeLeapYear(year)

  - \<int or str\> year: Initial value which is to be judged whether it's leap year or not.  
    If you wont to substitute Type str to year instead of Type int,  
    it must be written with matching regular expr. r'\-?[0-9]+'.  
    Calling without argument year, this constructs with default member argumants (detailed below).  

### Member Arguments
  - \<int\> \_\_year: Type int value which is to be judged whether it's leap year or not.  
    default: Nonetype  
  - \<str\> \_\_str_year: same as 'year' in Type str. (This is automatically corrected whenever year is set.)  
    default: Nonetype  

### Methods
  - \<void\> setYear(year): sets member arguments 'year' which is to be judged whether it's leap year or not.  
    The argument 'year' could be both Type int and str.  
    If you want to substitute Type str to year, it must be written with matching regular expr. r'\-?[0-9]+'.

  - \<int\> getYear(): returns Member \_\_year in Type int.

  - \<str\> getStrYear(): returns Member \_\_str_year in Type int.  
    If year (expressed in Astronomical year numbering) is Before Christ,  
    this returns the absolute value with prefix "紀元前(means B.C.)" automatically.

  - \<Boolean\> isLeapYear(): judge if member arg 'year' is leap year or not in a simple rule based on Gregorian calendar.

  - \<Boolean\> isLeapYear("checkBC45", returnExpr): detailed judge of leap year, which is based on histrical application of Julian calendar.  
    - returnExpr: This option decides the way in case value \_\_year matches before application of Julian calender( <= -45 ).  
      "none": makes return in NoneType.  
      "exception": raise \<Exception\> LeapYearError.  

## Test CLI codes (guidance texts is only written in Japanese)

There are 2 CLI codes at the same directory with JudgeLeapYear.py.  
  - simple_leap_year_calc.py
  - leap_year_calc.py

simple_leap_year_calc.py demonstrates simple judgement of leap year with isLeapYear().  
leap_year_calc.py tests the function of isLeapYear("checkBC45","exception") optional judgement.  

What you have to do with it is just enter the year in single-byte integer digits (including 0 and negative).  
If you want to try number of times after each response, just enter "y" to continue, while enter "n" to exit program.  

