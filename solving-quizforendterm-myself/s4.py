a1 = int(input("a1? : "))
n = int(input("n? : "))
mode = int(input("mode? : "))

match (mode) :
    case 1 :
        d = int(input("d? : "))
        print ("rst = ", d * n + a1 - d)
        
    case 2 :
        r = int(input("r? : "))
        print ("rst = ", a1 * (r ** (n - 1)))