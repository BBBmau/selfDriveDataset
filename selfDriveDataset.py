selfDrivingString = '''
category:		image	Person	Lane		drivableArea		trafficSign		car		trafficLight		bus
name		0000f77c-6257be58.jpg												
														
weather		        clear												
scene		     city street												
timeofday		daytime												
														
occluded			FALSE					        FALSE		      FALSE		FALSE		        TRUE
truncated			FALSE					        FALSE		      FALSE		FALSE		        FALSE
trafficLightColor		none					        none		      none		green		        none
														
areaType						direct								
														
manualShape			TRUE	TRUE		TRUE		        TRUE		      TRUE		TRUE		        TRUE
manualAttributes		TRUE	TRUE		TRUE		        TRUE		      TRUE		TRUE		        TRUE
box2d
x1                           423.158909	                                        1101.731743,	      45.240919		1125.902264		261.497704
y1	         	     336.241987					        211.122087,	      254.530367,	133.184488		329.95095,
x2			     434.176547					        1170.79037,	      357.805838,	1156.978645		325.32238
y2			     358.277263					        233.566141	      487.906215	210.875445		352.432578
														
id				6       4		    3		            2		         1		    0		          5
laneDirection				parallel										
laneStyle				solid										
laneType				road curb										
types				        LL		LLLLLLLLCCC								
closed				        FALSE		TRUE								
														
poly2d				        503.674413,	1280.195648,								
				        373.137193	626.372529								
														
														
				        357.797732,	1280.195648,								
				        374.672737	371.830705								
														
														
						        927.081254,								
						        366.839689								
														
														
						        872.180076,								
						        427.979637								
														
														
						        658.814135,								
                                                        450.439209								
														
														
                                                        585.196646,								
                                                        426.731883								
														
														
                                                        0,								
                                                        517.817928								
														
														
                                                        0,								
                                                        602.665203								
														
														
                                                        497.853863,								
                                                        540.2775								
														
														
                                                        927.081254,								
                                                        571.471352								
														
														
                                                        1280.195648,								
                                                        626.372529								
			
'''
print(selfDrivingString)
print(type(selfDrivingString))

image = ('0000f77c-6257be58.jpg', 'clear', 'city street', 'daytime')
Person = (6, 'FALSE', 'FALSE', 'none', 'TRUE', 'TRUE', 423.158909, 336.241987, 434.176547, 358.277263)
Lane = (4, 'TRUE', 'TRUE', 'parallel', 'solid', 'road curb', 'LL', 'FALSE', 503.674413, 373.137193, 357.797732, 374.672737)
poly2d_Drivable = (1280.195648, 626.372529, 1280.195648, 371.830705, 927.081254, 366.839689, 872.180076, 427.97963, 658.814135, 450.439209, 585.196646, 426.731883, 0, 517.817928, 0, 602.665203, 497.853863, 540.2775, 927.081254, 571.471352, 1280.195648, 626.372529)
drivableArea = (3, 'direct', 'TRUE', 'TRUE', 'LLLLLLLLCCC', 'TRUE', poly2d_Drivable)

trafficSign = (2, 'FALSE', 'FALSE', 'none', 'TRUE', 'TRUE', 1101.731743, 211.122087, 1170.79037, 233.566141)

car = (1, 'FALSE', 'FALSE', 'none', 'TRUE', 'TRUE', 45.240919, 254.530367, 357.805838, 487.906215)

trafficLight = (0, 'FALSE', 'FALSE', 'green', 'TRUE', 'TRUE', 1125.902264, 133.184488, 1156.978645, 210.875445)

bus = (5, 'TRUE', 'FALSE', 'none', 'TRUE', 'TRUE', 261.497704, 329.95095, 325.32238, 352.432578)


list_of_tuple = [image,Person,Lane,poly2d_Drivable,trafficSign,car,trafficLight,bus]

print(list_of_tuple)

class LaneLabel:
    def __init__(self, manualShape:str, manualAttributes, laneDirection, laneStyle, laneType, types, closed, poly2d):
        self.manualShape = manualShape
        #Bool
        self.manualAttributes = manualAttributes
        # The Lane Direction
        self.laneDirection = laneDirection
        # Style of Lane
        self.laneStyle = laneStyle
        # Type of Lane
        self.laneType = laneType
        # Type
        self.types = types
        #Bool
        self.closed = closed
        # Array of poly coordinates
        self.poly2d = poly2d


        
class drivableAreaLabel:
    def __init__(self, areaType:str, manualShape, manualAttributes, types, closed, poly2d):
        # Type of Area
        self.areaType = areaType
        # Bool in string
        self.manualShape = manualShape
        # Bool in string
        self.manualAttributes = manualAttributes
        # Type
        self.types = types
        # Bool in string
        self.closed = closed
        # Array of poly coordinates
        self.poly2d = poly2d
        
class boxLabel:
    def __init__(self, occluded, truncated, trafficColor, manualShape, manualAttributes, box2d):
        #Bools in string
        self.occluded = occluded
        self.truncated = truncated
        #Color
        self.trafficColor = trafficColor
        #Bool in string
        self.manualShape = manualShape
        #Bool in string
        self.manualAttributes = manualAttributes
        # Array of 4 elements
        self.box2d = box2d

Person = boxLabel('false', 'false', 'none', 'true', 'true', (423.158909, 336.241987, 434.176547, 358.277263))

print("The traffic color is : " + Person.trafficColor)

                 
