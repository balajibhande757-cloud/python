import argparse

parser=argparse.ArgumentParser(description="simple calculator")


parser.add_argument("num1",type=float,help="first number")
parser.add_argument("num2",type=float,help="second number")
parser.add_argument("operations",choices=["add","sub","mul","div"],help="operations want to perform")
args=parser.parse_args()
if(args.operations=="add"):
    print(f"the result is {args.num1+args.num2}")
elif(args.operations=="sub"):
    print(f"the result is {args.num1-args.num2}")
elif(args.operations=="mul"):
    print(f"the result is {args.num1*args.num2}")
elif(args.operations=="div"):
    print(f"the result is {args.num1/args.num2}")
else:
    print("something went wrong")
    
    
# sirf ye dalo python 09_file_handeliing/03_argparse.py  6 7 add