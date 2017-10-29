#!/usr/bin/env python

#Import the dependencies as described in example_pub.py
import rospy
import math
#import ar_track_alvar
#from std_msgs.msg import String
from ar_track_alvar_msgs.msg import AlvarMarkers, AlvarMarker

def position(a):
    a1 = 10*a - int(10*a)
    if a > 0:
        if a1 > 0.5:
            a = (int(10*x)+1)
        elif a1 < 0.5:
            a = (int(10*x))
    else:
        if a1 < -0.5:
            a = int(10*a)-1
        elif a1 > -0.5:
            a = int(10*a)
    return a


#Define the callback method which is called whenever this node receives a 
#message on its subscribed topic. The received message is passed as the 
#first argument to callback().
def callback(message):

    #Print the contents of the message to the console
    x1 = position(message.markers[1].pose.pose.position.x)
    y1 = position(message.markers[1].pose.pose.position.y)
    x2 = position(message.markers[2].pose.pose.position.x)
    y2 = position(message.markers[2].pose.pose.position.y)
    x3 = position(message.markers[3].pose.pose.position.x)
    y3 = position(message.markers[3].pose.pose.position.y)
    x4 = position(message.markers[4].pose.pose.position.x)
    y4 = position(message.markers[4].pose.pose.position.y)
    '''x1 = 10*x - int(10*x)
    y1 = 10*y - int (10*y)
    if x1 > 0.5:
       x = (int(10*x)+1)
    elif x1 < 0.5:
       x = (int(10*x))
    if y1 > 0.5:
       y = (int(10*y)+1)
    elif y1 < 0.5:
       y = (int(10*y))  '''  
    #print x,y
    maze = [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    maze[y1][3-x1] = "wall"
    maze[y2][3-x2] = "des"
    maze[y3][3-x3] = "box1"
    maze[y4][3-x4] = "box2"
    #rospy.sleep(3)
    print maze
    #print message
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)

#Define the method which contains the node's main functionality
def listener():

    #Run this program as a new node in the ROS computation graph
    #called /listener_<id>, where <id> is a randomly generated numeric
    #string. This randomly generated name means we can start multiple
    #copies of this node without having multiple nodes with the same
    #name, which ROS doesn't allow.
    rospy.init_node('listener', anonymous=True)

    #Create a new instance of the rospy.Subscriber object which we can 
    #use to receive messages of type std_msgs/String from the topic /chatter_talk.
    #Whenever a new message is received, the method callback() will be called
    #with the received message as its first argument.

    rospy.Subscriber("ar_pose_marker", AlvarMarkers, callback)


    #Wait for messages to arrive on the subscribed topics, and exit the node
    #when it is killed with Ctrl+C
    rospy.spin()


#Python's syntax for a main() method
if __name__ == '__main__':
     listener()