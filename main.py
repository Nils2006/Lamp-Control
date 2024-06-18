import time

import requests
import random
import threading

lines = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], [18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35], [36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53], [54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71], [72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89], [90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107], [108,109,110,112,113,114,115,116,116,117,118,119,120,121,122,123,124,125], [126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143], [144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161]]
status = [[0 for y in range(3)] for x in range(162)]

lamp = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   52,   53],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   50,   51, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   48,   49, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   46,   47, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   44,   45, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   42,   43, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   40,   41, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   38,   39, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  127,  126, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   36,   37, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  129,  128, None, None,  125, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  131,  130, None, None, None, None,  124, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   55,   54, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  133,  132, None, None, None, None, None, None,  123, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   57,   56, None, None,   35, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  135,  134, None, None, None, None, None, None, None, None,  122, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   59,   58, None, None, None, None,   34, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  137,  136, None, None, None, None, None, None, None, None, None, None,  121, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   61,   60, None, None, None, None, None, None,   33, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  139,  138, None, None, None, None, None, None, None, None, None, None, None, None,  120, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   63,   62, None, None, None, None, None, None, None, None,   32, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  141,  140, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  119, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   65,   64, None, None, None, None, None, None, None, None, None, None,   31, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  143,  142, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  118, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   67,   66, None, None, None, None, None, None, None, None, None, None, None, None,   30, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  145,  144, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  117, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   69,   68, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   29, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None,  147,  146, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  116, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   71,   70, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   28, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None,  149,  148, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  115, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   73,   72, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   27, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None,  151,  150, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  114, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   75,   74, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   26, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None,  153,  152, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  113, None, None, None, None, None, None, None, None, None, None, None, None,   77,   76, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   25, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   16,   17],
        [None, None, None, None, None, None,  155,  154, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  112, None, None, None, None, None, None, None, None, None, None,   79,   78, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   24, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   14,   15, None, None],
        [None, None, None, None,  157,  156, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  111, None, None, None, None, None, None, None, None,   81,   80, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   23, None, None, None, None, None, None, None, None, None, None, None, None,   12,   13, None, None, None, None],
        [None, None,  159,  158, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  110, None, None, None, None, None, None,   83,   82, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   22, None, None, None, None, None, None, None, None, None, None,   10,   11, None, None, None, None, None, None],
        [ 161,  160, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  109, None, None, None, None,   85,   84, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   21, None, None, None, None, None, None, None, None,    8,    9, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  108, None, None,   87,   86, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   20, None, None, None, None, None, None,    6,    7, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   89,   88, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   29, None, None, None, None,    4,    5, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   91,   90, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   18, None, None,    2,    3, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   93,   92, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,    0,    1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   95,   94, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   97,   96, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,   99,   98, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  101,  100, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  103,  102, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  105,  104, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,  107,  106, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],]



basic_json = {
  "0": { "r": 0, "g": 0, "b": 0 },
  "1": { "r": 0, "g": 0, "b": 0 },
  "2": { "r": 0, "g": 0, "b": 0 },
  "3": { "r": 0, "g": 0, "b": 0 },
  "4": { "r": 0, "g": 0, "b": 0 },
  "5": { "r": 0, "g": 0, "b": 0 },
  "6": { "r": 0, "g": 0, "b": 0 },
  "7": { "r": 0, "g": 0, "b": 0 },
  "8": { "r": 0, "g": 0, "b": 0 },
  "9": { "r": 0, "g": 0, "b": 0 },
  "10": { "r": 0, "g": 0, "b": 0 },
  "11": { "r": 0, "g": 0, "b": 0 },
  "12": { "r": 0, "g": 0, "b": 0 },
  "13": { "r": 0, "g": 0, "b": 0 },
  "14": { "r": 0, "g": 0, "b": 0 },
  "15": { "r": 0, "g": 0, "b": 0 },
  "16": { "r": 0, "g": 0, "b": 0 },
  "17": { "r": 0, "g": 0, "b": 0 },
  "18": { "r": 0, "g": 0, "b": 0 },
  "19": { "r": 0, "g": 0, "b": 0 },
  "20": { "r": 0, "g": 0, "b": 0 },
  "21": { "r": 0, "g": 0, "b": 0 },
  "22": { "r": 0, "g": 0, "b": 0 },
  "23": { "r": 0, "g": 0, "b": 0 },
  "24": { "r": 0, "g": 0, "b": 0 },
  "25": { "r": 0, "g": 0, "b": 0 },
  "26": { "r": 0, "g": 0, "b": 0 },
  "27": { "r": 0, "g": 0, "b": 0 },
  "28": { "r": 0, "g": 0, "b": 0 },
  "29": { "r": 0, "g": 0, "b": 0 },
  "30": { "r": 0, "g": 0, "b": 0 },
  "31": { "r": 0, "g": 0, "b": 0 },
  "32": { "r": 0, "g": 0, "b": 0 },
  "33": { "r": 0, "g": 0, "b": 0 },
  "34": { "r": 0, "g": 0, "b": 0 },
  "35": { "r": 0, "g": 0, "b": 0 },
  "36": { "r": 0, "g": 0, "b": 0 },
  "37": { "r": 0, "g": 0, "b": 0 },
  "38": { "r": 0, "g": 0, "b": 0 },
  "39": { "r": 0, "g": 0, "b": 0 },
  "40": { "r": 0, "g": 0, "b": 0 },
  "41": { "r": 0, "g": 0, "b": 0 },
  "42": { "r": 0, "g": 0, "b": 0 },
  "43": { "r": 0, "g": 0, "b": 0 },
  "44": { "r": 0, "g": 0, "b": 0 },
  "45": { "r": 0, "g": 0, "b": 0 },
  "46": { "r": 0, "g": 0, "b": 0 },
  "47": { "r": 0, "g": 0, "b": 0 },
  "48": { "r": 0, "g": 0, "b": 0 },
  "49": { "r": 0, "g": 0, "b": 0 },
  "50": { "r": 0, "g": 0, "b": 0 },
  "51": { "r": 0, "g": 0, "b": 0 },
  "52": { "r": 0, "g": 0, "b": 0 },
  "53": { "r": 0, "g": 0, "b": 0 },
  "54": { "r": 0, "g": 0, "b": 0 },
  "55": { "r": 0, "g": 0, "b": 0 },
  "56": { "r": 0, "g": 0, "b": 0 },
  "57": { "r": 0, "g": 0, "b": 0 },
  "58": { "r": 0, "g": 0, "b": 0 },
  "59": { "r": 0, "g": 0, "b": 0 },
  "60": { "r": 0, "g": 0, "b": 0 },
  "61": { "r": 0, "g": 0, "b": 0 },
  "62": { "r": 0, "g": 0, "b": 0 },
  "63": { "r": 0, "g": 0, "b": 0 },
  "64": { "r": 0, "g": 0, "b": 0 },
  "65": { "r": 0, "g": 0, "b": 0 },
  "66": { "r": 0, "g": 0, "b": 0 },
  "67": { "r": 0, "g": 0, "b": 0 },
  "68": { "r": 0, "g": 0, "b": 0 },
  "69": { "r": 0, "g": 0, "b": 0 },
  "70": { "r": 0, "g": 0, "b": 0 },
  "71": { "r": 0, "g": 0, "b": 0 },
  "72": { "r": 0, "g": 0, "b": 0 },
  "73": { "r": 0, "g": 0, "b": 0 },
  "74": { "r": 0, "g": 0, "b": 0 },
  "75": { "r": 5, "g": 0, "b": 0 },
  "76": { "r": 0, "g": 0, "b": 0 },
  "77": { "r": 0, "g": 0, "b": 0 },
  "78": { "r": 0, "g": 0, "b": 0 },
  "79": { "r": 0, "g": 0, "b": 0 },
  "80": { "r": 0, "g": 0, "b": 0 },
  "81": { "r": 0, "g": 0, "b": 0 },
  "82": { "r": 0, "g": 0, "b": 0 },
  "83": { "r": 0, "g": 0, "b": 0 },
  "84": { "r": 0, "g": 0, "b": 0 },
  "85": { "r": 0, "g": 0, "b": 0 },
  "86": { "r": 0, "g": 0, "b": 0 },
  "87": { "r": 0, "g": 0, "b": 0 },
  "88": { "r": 0, "g": 0, "b": 0 },
  "89": { "r": 0, "g": 0, "b": 0 },
  "90": { "r": 0, "g": 0, "b": 0 },
  "91": { "r": 0, "g": 0, "b": 0 },
  "92": { "r": 0, "g": 0, "b": 0 },
  "93": { "r": 0, "g": 0, "b": 0 },
  "94": { "r": 0, "g": 0, "b": 0 },
  "95": { "r": 0, "g": 0, "b": 0 },
  "96": { "r": 0, "g": 0, "b": 0 },
  "97": { "r": 0, "g": 0, "b": 0 },
  "98": { "r": 0, "g": 0, "b": 0 },
  "99": { "r": 0, "g": 0, "b": 0 },
  "100": { "r": 0, "g": 0, "b": 0 },
  "101": { "r": 0, "g": 0, "b": 0 },
  "102": { "r": 0, "g": 0, "b": 0 },
  "103": { "r": 0, "g": 0, "b": 0 },
  "104": { "r": 0, "g": 0, "b": 0 },
  "105": { "r": 0, "g": 0, "b": 0 },
  "106": { "r": 0, "g": 0, "b": 0 },
  "107": { "r": 0, "g": 0, "b": 0 },
  "108": { "r": 0, "g": 0, "b": 0 },
  "109": { "r": 0, "g": 0, "b": 0 },
  "110": { "r": 0, "g": 0, "b": 0 },
  "111": { "r": 0, "g": 0, "b": 0 },
  "112": { "r": 0, "g": 0, "b": 0 },
  "113": { "r": 0, "g": 0, "b": 0 },
  "114": { "r": 0, "g": 0, "b": 0 },
  "115": { "r": 0, "g": 0, "b": 0 },
  "116": { "r": 0, "g": 0, "b": 0 },
  "117": { "r": 0, "g": 0, "b": 0 },
  "118": { "r": 0, "g": 0, "b": 0 },
  "119": { "r": 0, "g": 0, "b": 0 },
  "120": { "r": 0, "g": 0, "b": 0 },
  "121": { "r": 0, "g": 0, "b": 0 },
  "122": { "r": 0, "g": 0, "b": 0 },
  "123": { "r": 0, "g": 0, "b": 0 },
  "124": { "r": 0, "g": 0, "b": 0 },
  "125": { "r": 0, "g": 0, "b": 0 },
  "126": { "r": 0, "g": 0, "b": 0 },
  "127": { "r": 0, "g": 0, "b": 0 },
  "128": { "r": 0, "g": 0, "b": 0 },
  "129": { "r": 0, "g": 0, "b": 0 },
  "130": { "r": 0, "g": 0, "b": 0 },
  "131": { "r": 0, "g": 0, "b": 0 },
  "132": { "r": 0, "g": 0, "b": 0 },
  "133": { "r": 0, "g": 0, "b": 0 },
  "134": { "r": 0, "g": 0, "b": 0 },
  "135": { "r": 0, "g": 0, "b": 0 },
  "136": { "r": 0, "g": 0, "b": 0 },
  "137": { "r": 0, "g": 0, "b": 0 },
  "138": { "r": 0, "g": 0, "b": 0 },
  "139": { "r": 0, "g": 0, "b": 0 },
  "140": { "r": 0, "g": 0, "b": 0 },
  "141": { "r": 0, "g": 0, "b": 0 },
  "142": { "r": 0, "g": 0, "b": 0 },
  "143": { "r": 0, "g": 0, "b": 0 },
  "144": { "r": 0, "g": 0, "b": 0 },
  "145": { "r": 0, "g": 0, "b": 0 },
  "146": { "r": 0, "g": 0, "b": 0 },
  "147": { "r": 0, "g": 0, "b": 0 },
  "148": { "r": 0, "g": 0, "b": 0 },
  "149": { "r": 0, "g": 0, "b": 0 },
  "150": { "r": 0, "g": 0, "b": 0 },
  "151": { "r": 0, "g": 0, "b": 0 },
  "152": { "r": 0, "g": 0, "b": 0 },
  "153": { "r": 0, "g": 0, "b": 0 },
  "154": { "r": 0, "g": 0, "b": 0 },
  "155": { "r": 0, "g": 0, "b": 0 },
  "156": { "r": 0, "g": 0, "b": 0 },
  "157": { "r": 0, "g": 0, "b": 0 },
  "158": { "r": 0, "g": 0, "b": 0 },
  "159": { "r": 0, "g": 0, "b": 0 },
  "160": { "r": 0, "g": 0, "b": 0 },
  "161": { "r": 0, "g": 0, "b": 0 }
}

def color_line(line_num, r, g, b):
  x = 0
  for line in lines:
    if x == line_num:
      for pixel in line:
        status[pixel][0] = r
        status[pixel][1] = g
        status[pixel][2] = b
      return
    x = x + 1

def random_color_line():
  for i in range(9):
    color_line(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
  send()

def random_color_line_cycle():
  for i in range(9):
    color_line(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    time.sleep(0.1)
    send()

def runner(r,g,b):
  status[0] = [r,g,b]
  for i in range(161):
    for y in range(161):
      if status[y] == [r,g,b]:
        status[y] = [0,0,0]
        y = y + 1
        status[y] = [r,g,b]
        time.sleep(0.01)
        send()
      y = y + 1
    i = i + 1
  status[161] = [0,0,0]

def color_lamp_side(line_num, r, g, b):
  x = 0
  for row in lamp:
    if x == line_num:
      for pixel in row:
        if pixel != None:
            status[pixel][0] = r
            status[pixel][1] = g
            status[pixel][2] = b
      send()
      return
    x = x + 1

def send():
    final_json = basic_json
    i = 0
    y = 0
    for pixel in status:
        for value in pixel:
            if y == 0:
                final_json[str(i)]["r"] = value
            if y == 1:
                final_json[str(i)]["g"] = value
            if y == 2:
                final_json[str(i)]["b"] = value
            y = y + 1
        i = i + 1
        y = 0
    requests.post("http://192.168.2.225", json=final_json)

while True:
    for i in range(162):
        color_lamp_side(i, 255,255,0)
    for i in range(162):
        color_lamp_side(i, 0,0,0)



#send()