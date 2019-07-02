import sys
import cv2
import aircv as ac

def draw_circle(img, pos, circle_radius, color, line_width):
    cv2.circle(img, pos, circle_radius, color, line_width)
    cv2.imshow('objDetect', imsrc)
    cv2.waitKey(500)  # wait for 500ms
    # cv2.destroyAllWindows()
    cv2.imwrite('DetecImg.png', imsrc)

if __name__ == "__main__":
    InputImg1 = sys.argv[1]  # image1.jpg
    InputImg2 = sys.argv[2]  # image2.jpg
    imsrc = ac.imread(InputImg1)
    imobj = ac.imread(InputImg2)
    # find the match position
    pos = ac.find_all_template(imsrc, imobj)
    NumOfObj = len(pos)
    List_Of_Position = []
    for i in range(NumOfObj):
        circle_center_pos = tuple(list(map(int, list(pos[i]['result']))))
        circle_radius = 50
        color = (0, 255, 0)
        line_width = 10
        # draw circle
        draw_circle(imsrc, circle_center_pos, circle_radius, color, line_width)
        # pos['result'] is float tuple, circle_center_pos need to be transformed to inter
        # Because tuple elements can't be transformed
        x = int(circle_center_pos[0])
        y = int(circle_center_pos[1])
        # position is still tuple type () not []
        position = (x, y)
        print(position)
        # Save the coordinates of the four corners of the object
        List_Of_Position.append(pos[i]['rectangle'])

    # Output and print detection information
    if NumOfObj <= 1:
        print("%d target were found in the background image!" % NumOfObj)
    else:
        print("%d targets were found in the background image!" % NumOfObj)
    print(List_Of_Position)

