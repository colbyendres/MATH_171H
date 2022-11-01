a = 'a'
b = 'b'
c = 'c'
e = 'e'
map = {a:1.0J,b:-1,c:-1.0J,e:1}

list3 = [[e,a,b,c],
         [a,b,c,e],
         [b,c,e,a],
         [c,e,a,b]]

list4 = [[1,1J,-1,-1J],
         [1J,-1,-1J,1],
         [-1,-1J,1,1J],
         [-1J,1,1J,-1]]

dom3 = [e,a,b,c]

for i,a in enumerate(dom3):
    for j,a in enumerate(dom3):
        if map[list3[i][j]] != map[a] * map[b]:
            print("FAIL: ", a, " ", b)

