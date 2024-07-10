# alpha_dict={}
# for i in range(ord('a'),ord('b')+1):
#     alpha_dict[chr(i)]=i
# print(alpha_dict)

#s1=set('a','b','c')
# s2=set(['a','b','c'])
# s3={'a','b','c'}
s4={('a','b','c')}
#print(s1,type(s1))
# print(s2,type(s2))
# print(s3,type(s3))
print(s4,type(s4))

# dict(foo=1,bar=2)
# print(dict)
# d={'foo':100,'bar':200,'baz':300}
# print(d.items())

# d1={} #dict
# d1['foo']=100 
# d1['bar']=200 
# d1['baz']=300

# d2={('foo',100),('bar',200),('baz',300)} #set
# d3=dict(foo=100,bar=200,baz=300) #dict
# d4=dict([('foo',100),('bar',200),('baz',300)]) #dict
# print(d1,type(d1))
# print(d2,type(d2))
# print(d3,type(d3))
# print(d4,type(d4))

c_c={}
def addone(c):
    if c in c_c:
        c_c[c] +=1
    else:
        c_c[c]=1
addone("India")
addone("Japan")
addone("USA")
print(len(c_c))