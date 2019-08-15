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

        while success:
            # function extract frames
            success, nextimage = vidObj.read()

            try:
                # Comparing frames
                if compare_mse(nextimage, image) > 2:
                    print(compare_mse(nextimage, image))
                    # Saves the frames with frame-count
                    cv2.imwrite("<path to extract frames>"
                                + file + "_frame%d.jpg" % count, nextimage)
                    # else:
                    image = nextimage
                # Advance 60 frames = 1 sec
                count += 60
                vidObj.set(1, count)
            except AttributeError:
                print('Next')


# Driver Code
if __name__ == '__main__':
    # Calling the function

    framecapture("<source video list path>")
