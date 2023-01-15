
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
if operation ==1:
    minimum=int(input())
    maximum=int(input())
    def operation1(img,max_color):
        n_rows = len(img)
        n_cols = len(img[0])
        cha = len(img[0][0])
        # reaching channel values via 3 for loops
        for x in range(n_rows):
            for a in range(n_cols):
                for k in range(cha):
                    m = img[x][a][k]
                    val = ((int(m) - 0) * (maximum - minimum) / (max_color - 0)) + minimum
                    val = round(val, 4)
                    img[x][a][k] = val

    img,max_color = read_ppm_file(filename)
    operation1(img,max_color)
    img_printer(img)

if operation ==2:
    def operation2(img):
        n_rows = len(img)
        n_cols = len(img[0])
        cha = len(img[0][0])
        # pritiorizing rgb for easy iteration
        for k in range(cha):
            sum = 0
            # calculating mean
            for x in range(n_rows):
                for a in range(n_cols):
                    m = img[x][a][k]
                    sum +=m
            mean = sum / (32 * 32)
            sum_standev=0
            # calculating standart deviation
            for x in range(n_rows):
                for a in range(n_cols):
                    m = img[x][a][k]
                    prestandev = (m - mean)**2
                    sum_standev += prestandev
            standev = (sum_standev/(32*32))**0.5
            # normalizing
            for x in range(n_rows):
                for a in range(n_cols):
                    m = img[x][a][k]
                    normal= (m-mean)/standev
                    img[x][a][k]=round(normal,4)



    img, max_color = read_ppm_file(filename)
    operation2(img)
    img_printer(img)

if operation ==3:
    def operation3(img):
        n_rows = len(img)
        n_cols = len(img[0])
        cha = len(img[0][0])
        # calculating averaging
        for x in range(n_rows):
            for a in range(n_cols):
                sum=0
                for k in range(cha):
                    m = img[x][a][k]
                    sum +=m
                average = sum/3
                for k in range(cha):
                    img[x][a][k] = int(average)

    img, max_color = read_ppm_file(filename)
    operation3(img)
    img_printer(img)

if operation ==4:
    def operation4(img):
        file_name = input()
        stride = int(input())
        # converting filter to list
        with open(file_name, "r") as filter_file:
            final_list = [[float(x) for x in line.split()] for line in filter_file]
        length = len(final_list)
        row = len(img)
        col = len(img[0])
        cha = len(img[0][0])
        # creating a big list
        new_img = []
        for i in range(0,row - length + 1,stride):
            new_img_row = []
            for j in range(0, col - length + 1, stride):
                pixel_col = []
                for k in range(cha):
                    sum=0
                    for a in range(i,i+length,1):
                        for m in range(j,j+length,1):
                            sum += float(img[a][m][k])*float(final_list[a-i][m-j])

                    if sum <0:
                        sum=0
                    if sum >255:
                        sum=255
                    pixel_col.append(int(sum))
                new_img_row.append(pixel_col)
            new_img.append(new_img_row)
        return new_img




    img, max_color = read_ppm_file(filename)
    x=operation4(img)
    img_printer(x)

if operation ==5:
    img = read_ppm_file(filename)[0]
    file_name = input()
    stride = int(input())
    with open(file_name, "r") as filter_file:
        final_list = [[float(x) for x in line.split()] for line in filter_file]
    length = len(final_list)
    # creating 0 pixels right before same operation at 4
    new_img = []
    for a in range((length - 1) // 2):
        ara_lst = []
        for i in range(len(img[0]) + length - 1):
            ara_lst.append([0, 0, 0])
        new_img.append(ara_lst)
    for m in img:

        for i in range((length - 1) // 2):
            m.insert(0, [0, 0, 0])
            m.append([0, 0, 0])
        new_img.append(m)

    for a in range((length - 1) // 2):
        ara_lst = []
        for i in range(len(img[0]) + length - 1):
            ara_lst.append([0, 0, 0])
        new_img.append(ara_lst)
    def operation5(img):
        row = len(img)
        col = len(img[0])
        cha = len(img[0][0])
        new_img = []
        for i in range(0, row - length + 1, stride):
            new_img_row = []
            for j in range(0, col - length + 1, stride):
                pixel_col = []
                for k in range(cha):
                    sum = 0
                    for a in range(i, i + length, 1):
                        for m in range(j, j + length, 1):
                            sum += float(img[a][m][k]) * float(final_list[a - i][m - j])

                    if sum < 0:
                        sum = 0
                    if sum > 255:
                        sum = 255
                    pixel_col.append(int(sum))
                new_img_row.append(pixel_col)
            new_img.append(new_img_row)
        return new_img

    # img, max_color = read_ppm_file(filename)
    # x= operation5(img)
    # img_printer(x)

    x=operation5(new_img)
    img_printer(x)

if operation ==6:
    u = int(input())
    def operation6(img,range_input,x=0,y=0,clr=0):
        # base conditions
        if len(img)%2==0:
            if x==0 and y==len(img)-1:
                return img
        if len(img)%2==1:
            if x==len(img)-1 and y==len(img)-1:
                return img
        # column if it is even
        if y%2==0:
            while x<len(img)-1:
                if abs(img[x][y][clr]-img[x+1][y][clr])<range_input and abs(img[x][y][clr+1]-img[x+1][y][clr+1])<range_input and abs(img[x][y][clr+2]-img[x+1][y][clr+2])<range_input:
                    for a in range(3):
                        img[x+1][y][a]=img[x][y][a]

                return operation6(img,range_input,x+1,y,clr)
            if x == len(img)-1:
                if abs(img[x][y][clr]-img[x][y+1][clr])<range_input and abs(img[x][y][clr+1]-img[x][y+1][clr+1])<range_input and abs(img[x][y][clr+2]-img[x][y+1][clr+2])<range_input:
                    for a in range(3):
                        img[x][y+1][a] = img[x][y][a]
                return operation6(img,range_input,x,y+1,clr)
        # column if it is odd
        else:
            while x>0:
                if abs(img[x][y][clr]-img[x-1][y][clr])<range_input and abs(img[x][y][clr+1]-img[x-1][y][clr+1])<range_input and abs(img[x][y][clr+2]-img[x-1][y][clr+2])<range_input:
                    for a in range(3):
                        img[x-1][y][a] = img[x][y][a]
                return operation6(img,range_input, x -1, y, clr)
            if x ==0:
                if abs(img[x][y][clr] - img[x][y + 1][clr]) < range_input and abs(img[x][y][clr + 1] - img[x][y + 1][clr + 1]) < range_input and abs(img[x][y][clr + 2] - img[x][y + 1][clr + 2]) < range_input:
                    for a in range(3):
                        img[x][y+1][a] = img[x][y][a]
                return operation6(img,range_input,x,y+1,clr)

    img, max_color = read_ppm_file(filename)
    x=operation6(img,u,0,0,0)
    img_printer(x)

if operation ==7:
    u = int(input())
    def operation7(img,range_input,rowm=0,colm=0,clr=0):
        # algorithm for image's length is even
        if len(img) % 2 == 0:
            # base condition
            if rowm == 0 and colm == len(img) - 1 and clr==2:
                return img
            if colm%2==0 and clr==0:
                while rowm<len(img)-1:
                    if abs(img[rowm][colm][clr]-img[rowm+1][colm][clr])<range_input:
                        img[rowm+1][colm][clr]=img[rowm][colm][clr]
                    return operation7(img,range_input,rowm+1,colm,clr)
                if rowm==len(img)-1:
                    if abs(img[rowm][colm][clr]-img[rowm][colm+1][clr])<range_input:
                        img[rowm][colm+1][clr] = img[rowm][colm][clr]
                    return operation7(img, range_input, rowm , colm+ 1, clr)

            if colm % 2 == 1 and clr == 0:
                if colm != len(img)-1:
                    while rowm > 0:
                        if abs(img[rowm][colm][clr] - img[rowm - 1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)
                    if rowm == 0:
                        if abs(img[rowm][colm][clr] - img[rowm][colm + 1][clr]) < range_input:
                            img[rowm][colm + 1][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm, colm + 1, clr)
                else:
                    while rowm>0:
                        if abs(img[rowm][colm][clr ] - img[rowm-1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)
                    if rowm==0:
                        if abs(img[rowm][colm][clr+1]-img[rowm][colm][clr])<range_input:
                            img[rowm][colm][clr+1]=img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm, clr+ 1)
            if colm%2==0 and clr==1:
                if colm!=0:
                    while rowm>0:
                        if abs(img[rowm][colm][clr] - img[rowm-1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)
                    if rowm==0:
                        if abs(img[rowm][colm][clr]-img[rowm][colm-1][clr])<range_input:
                            img[rowm][colm-1][clr]=img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm-1, clr)
                else:
                    while rowm>0:
                        if abs(img[rowm][colm][clr] - img[rowm-1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)
                    if rowm==0:
                        if abs(img[rowm][colm][clr]-img[rowm][colm][clr+1])<range_input:
                            img[rowm][colm][clr+1]=img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm, clr+1)

            if colm % 2 == 1 and clr == 1:
                while rowm<len(img)-1:
                    if abs(img[rowm][colm][clr] - img[rowm +1][colm][clr]) < range_input:
                        img[rowm + 1][colm][clr]=img[rowm][colm][clr]
                    return operation7(img, range_input, rowm +1, colm, clr)
                if rowm ==len(img)-1:
                    if abs(img[rowm][colm][clr] - img[rowm ][colm-1][clr]) < range_input:
                        img[rowm][colm - 1][clr]=img[rowm][colm][clr]
                    return operation7(img, range_input, rowm , colm-1, clr)

            if colm %2==0 and clr==2:
                while rowm < len(img) - 1:
                    if abs(img[rowm][colm][clr] - img[rowm + 1][colm][clr]) < range_input:
                        img[rowm + 1][colm][clr] = img[rowm][colm][clr]
                    return operation7(img, range_input, rowm + 1, colm, clr)
                if rowm == len(img) - 1:
                    if abs(img[rowm][colm][clr] - img[rowm][colm + 1][clr]) < range_input:
                        img[rowm][colm + 1][clr] = img[rowm][colm][clr]
                    return operation7(img, range_input, rowm, colm + 1, clr)
            if colm % 2 == 1 and clr == 2:
                if colm != len(img)-1:
                    while rowm > 0:
                        if abs(img[rowm][colm][clr] - img[rowm - 1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)
                    if rowm == 0:
                        if abs(img[rowm][colm][clr] - img[rowm][colm + 1][clr]) < range_input:
                            img[rowm][colm + 1][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm, colm + 1, clr)
                else:
                    while rowm>0:
                        if abs(img[rowm][colm][clr ] - img[rowm-1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)



        # algorithm for image's length is odd
        if len(img)%2==1:
            # base condition
            if rowm==len(img)-1 and colm==len(img)-1 and clr==2:
                return img
            if colm%2==0 and clr==0:
                if colm!=len(img)-1:
                    while rowm<len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm+1][colm][clr])<range_input:
                            img[rowm+1][colm][clr]=img[rowm][colm][clr]
                        return operation7(img,range_input,rowm+1,colm,clr)
                    if rowm==len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm][colm+1][clr])<range_input:
                            img[rowm][colm+1][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm+ 1, clr)
                else:
                    while rowm<len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm+1][colm][clr])<range_input:
                            img[rowm+1][colm][clr]=img[rowm][colm][clr]
                        return operation7(img,range_input,rowm+1,colm,clr)
                    if rowm==len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm][colm][clr+1])<range_input:
                            img[rowm][colm][clr+1]=img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm, clr+ 1)
            if colm%2==1 and clr==0:
                while rowm>0:
                    if abs(img[rowm][colm][clr]-img[rowm-1][colm][clr])<range_input:
                        img[rowm-1][colm][clr]= img[rowm][colm][clr]
                    return operation7(img,range_input,rowm-1,colm,clr)
                if rowm==0:
                    if abs(img[rowm][colm][clr] - img[rowm][colm + 1][clr]) < range_input:
                        img[rowm][colm+1][clr]= img[rowm][colm ][clr]
                    return operation7(img, range_input, rowm , colm+ 1, clr)

            if colm%2==0 and clr==1:
                if colm!=0:
                    while rowm>0:
                        if abs(img[rowm][colm][clr]-img[rowm-1][colm][clr])<range_input:
                            img[rowm-1][colm][clr]=img[rowm][colm][clr]
                        return operation7(img,range_input,rowm-1,colm,clr)
                    if rowm ==0:
                        if abs(img[rowm][colm][clr] - img[rowm][colm-1][clr]) < range_input:
                            img[rowm][colm-1][clr]= img[rowm][colm][clr]
                        return operation7(img,range_input,rowm,colm-1,clr)
                else:
                    while rowm>0:
                        if abs(img[rowm][colm][clr] - img[rowm-1][colm][clr]) < range_input:
                            img[rowm - 1][colm][clr]=img[rowm][colm][clr]
                        return operation7(img, range_input, rowm - 1, colm, clr)
                    if rowm ==0:
                        if abs(img[rowm][colm][clr] - img[rowm][colm][clr+1]) < range_input:
                            img[rowm][colm ][clr+1] =img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm, clr+1)
            if colm % 2 == 0 and clr == 2:
                if colm!= len(img)-1:
                    while rowm<len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm+1][colm][clr])<range_input:
                            img[rowm+1][colm][clr]=img[rowm][colm][clr]
                        return operation7(img,range_input,rowm+1,colm,clr)
                    if rowm==len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm][colm+1][clr])<range_input:
                            img[rowm][colm+1][clr] = img[rowm][colm][clr]
                        return operation7(img, range_input, rowm , colm+ 1, clr)
                else:
                    while rowm<len(img)-1:
                        if abs(img[rowm][colm][clr]-img[rowm+1][colm][clr])<range_input:
                            img[rowm+1][colm][clr]=img[rowm][colm][clr]
                        return operation7(img,range_input,rowm+1,colm,clr)
            if colm%2==1 and clr==2:
                while rowm>0:
                    if abs(img[rowm][colm][clr]-img[rowm-1][colm][clr])<range_input:
                        img[rowm-1][colm][clr]= img[rowm][colm][clr]
                    return operation7(img,range_input,rowm-1,colm,clr)
                if rowm==0:
                    if abs(img[rowm][colm][clr] - img[rowm][colm + 1][clr]) < range_input:
                        img[rowm][colm+1][clr]= img[rowm][colm ][clr]
                    return operation7(img, range_input, rowm , colm+ 1, clr)


    img, max_color = read_ppm_file(filename)
    x = operation7(img, u, 0, 0, 0)
    img_printer(x)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

