# To Read video and Extract Unique Frames
# Paste the file in the directory with videos

import cv2
import os
from skimage.measure import compare_mse


# Function to extract frames
def frame_capture(path):

    # Get file list sorted by date modified
    file_list = [s for s in os.listdir(path)
         if os.path.isfile(os.path.join(path, s))]
    file_list.sort(key=lambda s: os.path.getmtime(os.path.join(path, s)))

    for file in file_list:
        # Path to video file
        vid_obj = cv2.VideoCapture(os.path.join(path, file))
        print(file)
        # Frame counter
        count = 0

        # Get first frame
        # success = 1
        success, image = vid_obj.read()
        try:
            os.mkdir(path + "\\Frames")
        except FileExistsError:
            pass
        while success:
            # function extract frames
            success, next_image = vid_obj.read()
            try:
                # Comparing frames
                if compare_mse(next_image, image) > 3:
                    print("Difference Factor : " + str(compare_mse(next_image, image)))
                    # Saves the frames with frame-count
                    cv2.imwrite(path + '\\Frames\\' + file + "_frame%d.jpg" % count, next_image)
                    # # resize image
                    # scale_percent = 20  # percent of original size
                    # width = int(next_image.shape[1] * scale_percent / 100)
                    # height = int(next_image.shape[0] * scale_percent / 100)
                    # dim = (width, height)
                    # cv2.imshow('image', cv2.resize(next_image, dim, interpolation=cv2.INTER_AREA))
                    # cv2.waitKey(1000)
                    print("Path : " + path + '\\Frames\\' + file + "_frame%d.jpg" % count)
                    print("--------------------------------------------------------")
                    # else:
                    image = next_image
                # Advance 60 frames = 1 sec
                count += 60
                vid_obj.set(1, count)
            except AttributeError:
                print('Next')
                print("--------------------------------------------------------")
    cv2.destroyAllWindows()


# Driver Code
if __name__ == '__main__':

    # Calling the function
    frame_capture(os.getcwd())
