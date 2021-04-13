d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d_1 = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d_1['k1']['k2'])

# Getting a little tricker
d_2 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab hello
conv_str = str(d_2['k1'][0]['nest_key'][1][0])
print(conv_str)


# This will be hard and annoying!
d_3 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d_3['k1'][2]['k2'][1]['tough'][2][0])