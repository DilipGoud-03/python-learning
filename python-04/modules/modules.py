# Module Methods 
import datetime

def sums(firstNumber,secondNumber):
    result = firstNumber + secondNumber
    return result


def substracts(firstNumber,secondNumber):
    result = firstNumber - secondNumber
    return result


def multiplications(firstNumber,secondNumber):
    result = firstNumber * secondNumber
    return result


def devisions(firstNumber,secondNumber):
    result = firstNumber / secondNumber
    return result


def squares(number):
    result = number ** 2
    return result


def day_name(year,month,date):
    result = datetime.datetime(year,month,date)
    return result.strftime("%A")
