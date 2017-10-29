#!/usr/bin/env python

#Import the dependencies as described in example_pub.py
import rospy
#import ar_track_alvar
#from std_msgs.msg import String
from ar_track_alvar_msgs.msg import AlvarMarkers, AlvarMarker


#Define the callback method which is called whenever this node receives a 
#message on its subscribed topic. The received message is passed as the 
#first argument to callback().
def callback(message):

    #Print the contents of the message to the console
    x = message.markers[1].pose.pose.position.x
    y = message.markers[1].pose.pose.position.y
    x1 = 10*x - int(10*x)
    y1 = 10*y - int (10*y)
    if x1 > 0.5:
       x = (int(10*x)+1)
    elif x1 < 0.5:
       x = (int(10*x))
    if y1 > 0.5:
       y = (int(10*y)+1)
    elif y1 < 0.5:
       y = (int(10*y))    
    #print x,y
    maze = [["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
    maze[x][y] = "box"

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
