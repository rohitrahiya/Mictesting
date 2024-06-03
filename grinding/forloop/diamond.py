n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))   
#" "*(n-i) to print no of space, "*"*(2*i-1) to print no of star
# now the inverted part of diamond
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))
