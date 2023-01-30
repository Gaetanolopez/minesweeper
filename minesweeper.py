# create grid 2D list
grid=  [["-","-","-","#","#"],
        ["-","#","-","-","-"],
        ["-","-","#","-","-"],
        ["-","#","#","-","-"],
        ["-","-","-","-","-"]
]
# display the grid
for x in grid:
    print(x,"\n")
# for loop that display index and elements of the row
for i,element in enumerate(grid):
    # for loop that display index and elements of the column
    for x,el in enumerate(element):
        # if the element is equal to -
        if el=="-":
            # the element value become 0
            el=0
            # the element in the position of row and column inside the 2d list become 0 as well
            grid[i][x]="0"
            try:
                # check nord west position to respective position and check that the value is equal to x and is not -1(because the last element(-1) shouldn' t be considered)
                if grid[i-1][x-1]=="#" and (i-1)!=(-1) and (x-1)!=(-1): # nw
                    el=el+1
                    grid[i][x]=str(el)
            except:
                # if index is out of range don t do nothing
                pass
            # do the same process for each coordinate
            #
            
            try:    
                if grid[i][x-1]=="#" and x-1!=-1:                       # west
                    el=el+1
                    grid[i][x]=str(el)
            except:
                pass
            try:    
                if grid[i+1][x-1]=="#" and i+1!=-1 and x-1!=-1:          #south west
                    el=el+1
                    grid[i][x]=str(el)
            except:
               pass
            try:  
                if grid[i-1][x]=="#" and (i-1)!=(-1):                   #north
                        el=el+1
                        grid[i][x]=str(el)
            except:
                pass
            try:  
                if grid[i+1][x]=="#" and (i+1)!=(-1):                    # south
                        el=el+1
                        grid[i][x]=str(el)
            except:
                pass
            try:  
                if grid[i-1][x+1]=="#" and (i-1)!=(-1) and x+1!=-1:     # north west
                       el=el+1
                       grid[i][x]=str(el)
            except:
                pass
            try:  
                if grid[i][x+1]=="#" and (x+1)!=(-1):                     # east
                        el=el+1
                        grid[i][x]=str(el)
            except:
                pass
            try:  
                if grid[i+1][x+1]=="#" and (i+1)!=(-1) and x+1!=-1:      # south east
                        el=el+1
                        grid[i][x]=str(el)
            except:
                pass
            # display the respective index row, index column and value inside
            print(i,x,el)
            
# display the new 2d list the the new assigned value for each "-"
for x in grid:
    print(x,"\n")
