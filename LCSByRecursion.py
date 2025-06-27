def LCS(s1,s2,i,j, dp):
    if i==len(s1) or j==len(s2):
        return ""
    if dp[i][j]!="":
        return dp[i][j]
    if(s1[i]==s2[j]):
        dp[i][j]=s1[i]+LCS(s1,s2,i+1,j+1,dp)
    else:
        r1=LCS(s1,s2,i+1,j,dp)
        r2=LCS(s1,s2,i,j+1,dp)
        if len(r1)>len(r2):
            dp[i][j]=r1
        else:
            dp[i][j]=r2
    return dp[i][j]
print("Enter String 1")
s1=input()
print("Enter String 2")
s2=input()
i=0
j=0
dp=[]
for x in range(len(s1)):
    row=[]
    for y in range(len(s2)):
        row.append("")
    dp.append(row)    
ans=LCS(s1,s2,i,j,dp)
print(ans)
