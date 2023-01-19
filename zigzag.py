def convert(s: str, numRows: int) -> str:
    index_lst = []
    if numRows == 1 or numRows == len(s):
        return s
    prev_row = list(range(0,len(s), 2*(numRows-1)))
    print(''.join([s[x] for x in prev_row]))
    index_lst.extend(prev_row)
    for row in range(2, numRows+1):
        temp = []
        for i in prev_row:
            if i-1>=0 and i-1 not in index_lst+temp:
                temp.append(i-1)
            if i+2<=len(s) and i+1 not in index_lst+temp:
                temp.append(i+1)
        if (len(s)-1) % (2*(numRows-1)) == 2*(numRows-1)-(row-1):
            temp.append(len(s)-1)
        prev_row = temp
        print(''.join([s[x] for x in temp]))
        index_lst.extend(prev_row)
    return ''.join([s[x] for x in index_lst])

print(convert("ABCD",2))
