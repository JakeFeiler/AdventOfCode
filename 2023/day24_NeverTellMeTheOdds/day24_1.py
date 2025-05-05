#!/opt/anaconda3/bin/python
#Jake Feiler


import sys

def get_input(text):
    '''Read input from file'''
    input_file = open(text, 'r')
    lines = []
    for line in input_file:
        next_line = line.strip().replace('@', '').replace(',', '').split(' ')
        lines.append(list(filter(None, next_line)))
    return lines


def main():
    s = get_input('input.txt')
    low_bound = 200000000000000
    high_bound = 400000000000000
    
    intersections = 0
    
    for pos,stone_1 in enumerate(s):
        x1, y1, vx1, vy1 = int(stone_1[0]), int(stone_1[1]), int(stone_1[3]), int(stone_1[4])
        for stone_2 in s[pos+1:]:
            x2, y2, vx2, vy2 = int(stone_2[0]), int(stone_2[1]), int(stone_2[3]), int(stone_2[4])

            #Ignore parallels, vy1/vx1 = vy2/vx2
            #No 0=vx exist

            if vy1/vx1 == vy2/vx2:
                continue

            
            #x1 + vx1 * t1 = x2 + vx2 * t2
            #y1 + vy1 * t1 = y2 + vy2 * t2
            
            #vy2 * (x1 + vx1 * t1) = vy2 * x2 + vx2 * vy2 * t2
            #vx2 * (y1 + vy1 * t1) = vx2 * y2 + vx2 * vy2 * t2

            #vy2 * x1 + vx1 * vy2 * t1 - vx2 * y1 - vx2 * vy1 * t1 = vy2 * x2 - vx2 * y2
            
            #vx1 * vy2 * t1 - vx2 * vy1 * t1 = vy2 * x2 - vx2 * y2 - vy2 * x1 + vx2 * y1
            #t1 = (vy2 * x2 - vx2 * y2 - vy2 * x1 + vx2 * y1) / (vx1 * vy2 - vx2 * vy1)

            t1 =  (vy2 * x2 - vx2 * y2 - vy2 * x1 + vx2 * y1) / (vx1 * vy2 - vx2 * vy1)
            
            #Ignore if in the past
            if t1 <=0:
                continue

            x1_final = x1 + vx1 * t1
            y1_final = y1 + vy1 * t1

            #Need to check if stone 2 was in the past
            #x2 + vx2 * t2 = x1_final
            t2 = (x1_final - x2)/vx2
            if t2 <= 0:
                continue

            if (low_bound <= x1_final <= high_bound) and (low_bound <= y1_final <= high_bound):            
                intersections += 1

    print(intersections)

main()
