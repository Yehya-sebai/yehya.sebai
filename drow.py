white = '\x1b[48;5;15m'
stop = '\033[0m'
file = open("sequence.txt")
file_ms = [float(i) for i in file]
cor_dig = [i for i in file_ms if ((i <= 5) and (i >= -5))]
print(cor_dig)
print(len(cor_dig))
less_0 = len([i for i in cor_dig if (i > 0)])
more_0 = len(cor_dig) - less_0

def draw_line(count):
    print(white*(count < less_0), '  ', stop, ' ',white*(count < more_0), '  ', stop,)

def chart():
    for i in range(max(less_0, more_0), 0, -1):
        draw_line(i)
chart()
print(' <0     >0')

white = '\x1b[48;5;15m'
stop = '\033[0m'

def draw_v(count):
  if count < less_0:
    print(white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, ' ', stop, ' ',white, '