# initializing list  
test_list=['3', '3', '3', '3', '3', 'Bullish Reversal', 'Bullish Reversal', '3', '3', '3', 'Bullish Reversal', '3', 'Bullish Reversal', '7', '7', '7', '7', 'Bullish Reversal', '3', '3', 'Bullish Reversal', '4', '2', '3', '7', '3', 'Bullish Reversal', '3', 'Bullish Reversal', '3', '4', '4', '3', 'Bullish Reversal', '3', '3', '4', 'Bullish Reversal', 'Bullish Reversal', '3', '3', 'Bullish Reversal', '3', 'Bullish Reversal', '7', 'Bullish Reversal', '3', '4', '3', 'Bullish Reversal', 'Bullish Reversal', 'Bullish Reversal', '3', '5', '5', '5', '5', '5', '5', '5', '5', '2', 'Bullish Reversal', '3', 'Bullish Reversal', 'Bullish Reversal', 'Bullish Reversal', '4', 'Bullish Reversal', '7', '2', '4', '2', '3', '3', '4', '2', '7', '7', 'Bullish Reversal', 'Bullish Reversal', '3', '3', 'Bullish Reversal', '4', '2', '3', 'Bullish Reversal', 'Bullish Reversal', 'Bullish Reversal', '4', '3', 'Bullish Reversal', 'Bullish Reversal', '3', '4', '3', 'Bullish Reversal', '2', '3', '2', '4', '2']

  
# printing original list   
print("The original list : " + str(test_list )) 
  
# using list comprehension + replace() 
# Replace substring in list of strings 
res = [sub.replace('2', 'Bullish Continuation') for sub in test_list]
res2 =[sub.replace('4', 'Bearish Continuation') for sub in res]
res3 =[sub.replace('3', 'Bullish Reversal') for sub in res2]
res4 =[sub.replace('5', 'Continuation') for sub in res3]
res5= [sub.replace('7', 'Indecision') for sub in res4] 
# print result 
print("The list after substring replacement : " + str(res5)) 

