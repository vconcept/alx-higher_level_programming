#!/usr/bin/python3
def remove_char_at(str, n):
    """this code is used in sting slicing"""
   if n< 0:
       return (str)
   return (str[:n] + str[n+1:])
