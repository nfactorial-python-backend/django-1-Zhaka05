from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, nfactorial school!")


def add(request, first, second):
    return HttpResponse(first + second)

def upper(request, text):
    return HttpResponse(text.upper())

def palindrome(request, word):
    def valid_palindrome(s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                return False
            L += 1
            R -= 1
        return True
    
    return HttpResponse(valid_palindrome(word))


def calculate(request, first, second, operation):
    def count(val1: int, val2: int, op: str) -> int:
        calc = {
            "*": lambda x, y: x*y,
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "/": lambda x, y: x//y,
        }
        return calc[op](val1, val2)
    return HttpResponse(count(first, second, operation))