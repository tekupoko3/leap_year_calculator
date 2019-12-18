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

## class JudgeLeapYear(year)

  - \<int or str\> year: Initial value which is to be judged whether it's leap year or not.
    If you wont to substitute Type str to year, it must be written with matching regular expr. r'\-[0-9]'.

### Member Arguments
  - \<int\> \_\_year: Type int value which is to be judged whether it's leap year or not.
  - \<str\> \_\_str_year: same as 'year' in Type str. (This is automatically corrected whenever year is set.)

### Methods
  - \<void\> setYear(year): sets member arguments 'year' which is to be judged whether it's leap year or not.
    argument 'year' could be both Type int and str.
    If you wont to substitute Type str to year, it must be written with matching regular expr. r'\-[0-9]'.

  - \<int\> getYear(): returns Member \_\_year in Type int.

  - \<str\> getStrYear(): returns Member \_\_str_year in Type int.  
    if year expressed in Astronomical year numbering is Before Christ, this corrects the absolute value with prefix "紀元前(means B.C.)" automatically.

  - \<void\> setYear(year): sets member arguments 'year' which is to be judged whether it's leap year or not.
    argument 'year' could be both Type int and str.  
    If you wont to substitute Type str to year, it must be written with matching regular expr. r'\-[0-9]'.

  - \<Boolean\> isLeapYear(): judge if member arg 'year' is leap year or not in a simple rule based on Gregorian calendar.

  - \<Boolean\> isLeapYear("checkBC46", returnExpr): detailed judge of leap year, which is based on histrical application of Julian calendar.  
    - returnExpr: this option decides the way in case of exception.  
      "none": makes return in NoneType (not in Boolean).  
      "exception": raise \<Exception\> LeapYearError.  

