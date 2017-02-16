#!/usr/bin/env python
import rospy
from learn_ball.msg import ballCor
from collections import deque
import numpy as np
import argparse
import imutils
import cv2






def talker():
	
	rospy.init_node('green_talker', anonymous=True)
	pub = rospy.Publisher('green_chatter', ballCor, queue_size=50)
	r = rospy.Rate(10) #10hz
	# Initialize the Green ball color 
	greenLower = (29,86,100)
	greenUpper = (60,255,255)
	pts = deque(maxlen=64)


	#Grab webCam
	camera = cv2.VideoCapture(0)
	msg = ballCor()
	msg.x = 11
	msg.y = 12
	msg.radius = 33
   
	while not rospy.is_shutdown():
		# grab the current frame
		(grabbed, frame) = camera.read()

		# resize the frame, blur it, and convert it to the HSV
		# color space
		frame = imutils.resize(frame, width=600)
		# blurred = cv2.GaussianBlur(frame, (11, 11), 0)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

		# construct a mask for the color "green", then perform
		# a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, greenLower, greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)

		# find contours in the mask and initialize the current
		# (x, y) center of the ball
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
			cv2.CHAIN_APPROX_SIMPLE)[-2]
		center = None

		# only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

			# only proceed if the radius meets a minimum size
			if radius > 5:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
				cv2.circle(frame, center, 5, (0, 0, 255), -1)
				msg.x=int(x)
				msg.y=int(y)
				msg.radius=int(radius)

		# update the points queue
		pts.appendleft(center)

		# loop over the set of tracked points
		for i in xrange(1, len(pts)):
			# if either of the tracked points are None, ignore
			# them
			if pts[i - 1] is None or pts[i] is None:
				continue

			# otherwise, compute the thickness of the line and
			# draw the connecting lines
			thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
			cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

		# show the frame to our screen
		cv2.imshow("Frame", frame)
	
		rospy.loginfo(msg)
		pub.publish(msg)
		r.sleep()
	
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: 
		pass
