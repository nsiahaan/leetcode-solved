class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key = lambda x: x[1], reverse = True) # sort boxes according to units, descending
        units, boxes = 0, 0
        i = 0
        
        print(boxTypes)
        while boxes <= truckSize and i < len(boxTypes):
            validBoxes = truckSize - boxes
            if boxTypes[i][0] <= validBoxes:
                units += boxTypes[i][1] * boxTypes[i][0]
                boxes += boxTypes[i][0]
                #print('1', units, boxes)
            else:
                sub = boxTypes[i][0]
                #print('sub', sub)
                while sub != validBoxes:
                    sub -= 1
                #print('newsub', sub)
                if sub > 0:
                    units += boxTypes[i][1] * sub
                    boxes += sub
                #print('curr', units, boxes)
            i += 1
        return units