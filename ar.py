#!/usr/bin/env python

from __future__ import print_function
import cv2
from ar_markers import detect_markers

def lookup_id(marker_id):
        lookup_table = {
                1: "stop",
                2: "left",
                3: "right",
                4: "three way on right",
                5: "three way on straight",
                6: "three way on left",
                7: "four way intersection",
                8: "yield",
                9: "slow",
                10: "duck"
        }

        if marker_id in lookup_table:
                return lookup_table[marker_id]
        return marker_id


if __name__ == '__main__':
        print('Press "q" to quit')
        capture = cv2.VideoCapture(0)

        if capture.isOpened():  # try to get the first frame
                frame_captured, frame = capture.read()
        else:
                frame_captured = False

        while frame_captured:
                markers = detect_markers(frame)
                for marker in markers:
                        marker.id = lookup_id(marker.id)
                        marker.highlite_marker(frame)
                cv2.imshow('Test Frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                frame_captured, frame = capture.read()

        # When everything done, release the capture
        capture.release()
        cv2.destroyAllWindows()