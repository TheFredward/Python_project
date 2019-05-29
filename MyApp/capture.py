import cv2, time

class capture():

    def __init__(self):
        self.video=cv2.VideoCapture(0)

    def get_frame(self):
        a=0
        while True:
            a = a + 1
            check, frame = self.video.read()

            print(check)
            print(frame)

            cv2.imshow("capturing", frame)

            # cv2.waitKey(0)

            key=cv2.waitKey(1)

            if key == ord('q'):
                break

        print(a)

        self.video.release()
        cv2.destroyAllWindows()
