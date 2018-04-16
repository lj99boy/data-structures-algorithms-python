import re
# create regex
r1 = re.compile('abc')

# search api match substring revolved long string
###print('re.search',re.search(r1,"aaabc"),end='\n\n')
###print('re.search',re.search("abc","aaabc"),end='\n\n')
# match api match pre-substring revolved long string
###print('re.match',re.match(r1,"aaabc"),end='\n\n')

# split
###print('re.split',re.split(" ",'aa bb cc dddd  ',2))
###print('re.split',re.split(" ",'aa bb cc dddd  ',0))

# findall
###print('re.findall',re.findall('[a-b]','aabbccdda'))
# finditer   seems like findall but return a iterator

# group pattern
# match all the un-blank string
# example [34ad-fs-z] [^\t\v\n\f\r]
# - ] ^ should be escaped to \- \] \^
# . means all the char
###print('findall .',re.findall('.','aaabbbccc'))

# re.sub(pattern,repl,string,count=0,flags=0)

# \d [0-9]
# \D [^0-9]
# \s [\t\f\r\n\v]
# \S [^\t\v\r\n\v]
# \w match all the visibility chars
###print(re.findall('\w','mmm喵喵喵'))
# \W ^ match all the visibility chars
# assert re.findall('\w','mmm喵喵喵') == ['m', 'm', 'm', '喵', '喵', '喵']

# repeat pattern
# * ==> 0 1 more  * == {0,infinity}
# ? ==> 0 1       ? == {0,1}
# + ==> 1 more  \d+ == \d\d*  + == {1,infinity}

# {n} n times match

# un greedy tag
# *? +? ?? {m,n}?

# alternative
# (ab)|(cd)  [abc] == a|b|c

# print(re.search('^for',"books\nfor bbb"))
# print(re.search('\Afor','foraac\nbbb'))
# print(re.search('b{2}\Z','bbb'))
# print(re.search("^for","forxxxvvv"))

# mat = re.search('\\baaa\\b','xx,aaa,xx')
# print(mat.group())

# group
# groupMat = re.search('.((.)e)f','abcdef')
# print(groupMat.group(1))
print(re.search(r'(.{2}) \1','ok ok'))