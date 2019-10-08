import re 

phoneNumRegEx = re.compile(r'\d{3}-\d{3}-\d{4}')
nums = phoneNumRegEx.findall('888-888-8888asdfasdf934-234-3434ad111-111-1111f')

for x in nums:
    print(x)