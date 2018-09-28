#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros

"""
#with user input


# define state Red
class Red(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Wait'], output_keys=['prev_state'])
        self.counter = 0

    def execute(self, userdata):
    	rospy.loginfo('***Executing state Red***')
        rospy.sleep(1)
	userdata.prev_state = 'red'
        return 'Wait'

# define state Yellow
class Yellow(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Continue', 'Stop'], input_keys=['prev_state'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('***Executing state Yellow***')
        rospy.sleep(1)
	if userdata.prev_state == 'green':       
	    return 'Stop'
	if userdata.prev_state == 'red':
	    return 'Continue'

#define state green
class Green(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Wait'],output_keys=['prev_state'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('***Executing state Green***')
        rospy.sleep(1)
	userdata.prev_state = 'green'
	return 'Wait'
def main():
    rospy.init_node('traffic_lights')

    # flag=0
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['Done'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('RED', Red(),
                               transitions={'Wait':'YELLOW'})
        smach.StateMachine.add('YELLOW', Yellow(),
                               transitions={'Stop':'RED',
					    'Continue':'GREEN'})
        smach.StateMachine.add('GREEN', Green(),
                               transitions={'Wait':'YELLOW'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()
"""


# define state Red
class Red(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Stop','Continue'])
        self.counter = 0

    def execute(self, userdata):
    	rospy.loginfo('***Executing state Red***')
    	rospy.sleep(1)
    #return 'Stop'
    	if self.counter<3:
	    self.counter +=1
	    return 'Stop'
    	else:
	    return 'Continue'

# define state Yellow
class Yellow(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Stop', 'Continue'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('***Executing state Yellow***')
        rospy.sleep(1)
	if self.counter<3:
	    self.counter+=1        
	    return 'Continue'
	else:
	    return 'Stop'

#define state green
class Green(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Go', 'Stop'])
        self.counter = 0

    def execute(self, userdata):
        rospy.loginfo('***Executing state Green***')
        rospy.sleep(1)
	#return 'Go'
	if self.counter<3:
	    self.counter +=1
            return 'Go'
	else:
	    return 'Stop'
def main():
    rospy.init_node('traffic_lights')

    # flag=0
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['Done'])

    # Open the container
    with sm:
        # Add states to the container
        smach.StateMachine.add('RED', Red(),
                               transitions={'Stop':'RED',
					    'Continue':'YELLOW'})
        smach.StateMachine.add('YELLOW', Yellow(),
                               transitions={'Stop':'RED',
					    'Continue':'GREEN'})
        smach.StateMachine.add('GREEN', Green(),
                               transitions={'Stop':'YELLOW',
					    'Go':'GREEN'})

    # Execute SMACH plan
    outcome = sm.execute()


if __name__ == '__main__':
    main()

