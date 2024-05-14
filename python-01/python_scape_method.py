print (" \n_________Escape Methods__________ \n")

# When you try to add Like (it's) you can use (\' )
txt = "Hello I\'m Here"
print (txt)
# it return 
# Hello I'm Here


# When you try to add Like (it \ he) you can use (\\ )
txt = "Hello I\'m\\you\'r Here"
print (txt)
# it return -
# Hello I'm\you'r Here


# When you try to add new line at ant instant you can use (\n )
txt = "Hello this first line Hello this is second line"
# no any new line indication
print (txt)
# it return -
# Hello this first line Hello this is second line


# with new line indication
txt = "Hello this first line\nHello this is second line"
print (txt)
# it return -
# Hello this first line
# Hello this is second line


# When you try to add tab  you can use (\t )
txt = "Hello this first line\tHello this is second line"
print (txt)
# it return -
# Hello this first line   Hello this is second line


# When you try to start new line on those place when first end you can use (\f )
txt = "Hello this first line\fHello this is second line"
print (txt)
# it return -
# Hello this first line
                     # Hello this is second line
