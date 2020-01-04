from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import sys
from . import JudgeLeapYear as JLY
from datetime import datetime

# Create your views here.
copyright = str(datetime.now().year)
startyear = '2019'

def index(request):
  year = None
  result = None
  year_text = None
  error = None
  return render(request, 'judgeleapyear/index.html', {
    'result': result,
    'year': year,
    'copyright': copyright,
    'startyear': startyear,
    })
  
  
def calc(request):
  test_year = JLY.JudgeLeapYear()
  year = request.POST.get("year", None)
  if year is None:
    return HttpResponseRedirect('/')
  try:
    test_year.setYear(year)
    try:
      if test_year.isLeapYear("checkBC45","exception"):
        result = "うるう年"
      else:
        result = "平年"
    except Exception as e:
      result = "ユリウス暦以前"
    return render(request, 'judgeleapyear/index.html', {
      'result': result,
      'year': test_year.getYear(),
      'year_text': test_year.getStrYear(),
      'error': None,
      'copyright': copyright,
      'startyear': startyear,
      })
  except Exception as err:
    tb = sys.exc_info()[2]
    return render(request, 'judgeleapyear/index.html', {
      'result': None,
      'year': year,
      'year_text': None,
      'error': "{0}".format(err.with_traceback(tb)),
      'copyright': copyright,
      'startyear': startyear,
      })


