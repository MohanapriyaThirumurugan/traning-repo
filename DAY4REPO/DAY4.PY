def plusone(digits):
  string=""
  for i in digits:
    val=str(i)
    string+=val
   #coverting str to int

  sum=int(string)+1
  val2=str(sum)
  temp=[]

  for j in val2:
    temp+=j
  return temp
print(plusone([1,2,13]))