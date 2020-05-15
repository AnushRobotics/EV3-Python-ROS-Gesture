#!/usr/bin/env python

import rospy
#!/usr/bin/env python

from geometry_msgs.msg import Twist
from std_msgs.msg import String

fingers = 0
def callback(data):
	global fingers
	fingers = data.data

rospy.init_node('teleop')
rospy.Subscriber("num_of_fingers", String, callback)
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(20)


while not rospy.is_shutdown():
	twist = Twist()
	if fingers == '2':
		twist.linear.x = 0.6
		rospy.loginfo("turn left")
	elif fingers == '3':
		twist.angular.z = 1
		rospy.loginfo("turn right")
	elif fingers =='5':
		twist.angular.z = 5
		rospy.loginfo("pick")
	else:
		rospy.loginfo("place")
	cmd_vel_pub.publish(twist)
	rate.sleep()