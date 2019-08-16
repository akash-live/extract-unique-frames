# Program To Read video and Extract Unique Frames
import cv2
import os
from skimage.measure import compare_mse, compare_nrmse, compare_ssim, compare_psnr


# Function to extract frames
def framecapture(path):

    # Get file list sorted by date modified
    filelist = [s for s in os.listdir(path)
         if os.path.isfile(os.path.join(path, s))]
    filelist.sort(key=lambda s: os.path.getmtime(os.path.join(path, s)))

    for file in filelist:
        # Path to video file
        vidObj = cv2.VideoCapture(os.path.join(path, file))
        print(file)
        # Frame counter
        count = 0

        # Get first frame
        # success = 1
        success, image = vidObj.read()
        try:
            os.mkdir(path + "\\Frames")
        except FileExistsError:
            pass
        while success:
            # function extract frames
            success, nextimage = vidObj.read()

            try:
                # Comparing frames
                if compare_mse(nextimage, image) > 3:
                    print("Diffrence Factor : " + str(compare_mse(nextimage, image)))
                    # Saves the frames with frame-count
                    cv2.imwrite(path + '\\Frames\\' + file + "_frame%d.jpg" % count, nextimage)
                    print("Path : " + path + '\\Frames\\' + file + "_frame%d.jpg" % count)
                    print("--------------------------------------------------------")
                    # else:
                    image = nextimage
                # Advance 60 frames = 1 sec
                count += 60
                vidObj.set(1, count)
            except AttributeError:
                print('Next')
                print("--------------------------------------------------------")


# Driver Code
if __name__ == '__main__':
    # Calling the function

    framecapture(input("Enter path : "))
