# -*- coding: utf-8 -*-
from __future__ import unicode_literals






class rawDataSet:





    def __init__(self,data,ratioSet):

        self.wishedTension = []
        self.current = []
        self.resistance = []
        self.time = []
        self.tension = []
        for i in range(len(data[0])):
            self.wishedTension.append(data[0][i])
            self.current.append(data[1][i])
            self.resistance.append(data[2][i])
            self.time.append(data[3][i])
            self.tension.append(data[4][i])
        onTension = 'no set'
        onCurrent = 'no set'
        onResistance = 'no set'

#Finds the largest instantaneous reduction of resistance and gives the on resistance near 0 V.
        maxDelta = 0.
        delta = abs(ratioSet * self.current[1])
        if self.wishedTension[3]-self.wishedTension[2]>0:
            for i in range((len(self.tension))-1):#/2)):
                    if -(-self.current[i+1] + self.current[i]) > delta and -(-self.current[i+1] + self.current[i]) > maxDelta:
                        onTension = self.wishedTension[i]
                        onCurrent = self.current[i+1]
                        onResistance = self.resistance[len(self.tension)-2]
                        maxDelta = abs(-self.current[i+1] + self.current[i])    
        else:
            for i in range((len(self.tension))-1):#/2)):
                    if (-self.current[i+1] + self.current[i]) > delta and (-self.current[i+1] + self.current[i]) > maxDelta:
                        onTension = self.wishedTension[i]
                        onCurrent = self.current[i+1]
                        onResistance = self.resistance[len(self.tension)-2]
                        maxDelta = abs(-self.current[i+1] + self.current[i])    
        self.set = [onTension,onCurrent,onResistance]







class rawDataReset:





    def __init__(self,data,ratioReset):

        self.wishedTension = []
        self.current = []
        self.resistance = []
        self.time = []
        self.tension = []
        for i in range(len(data[0])):
            self.wishedTension.append(data[0][i])
            self.current.append(data[1][i])
            self.resistance.append(data[2][i])
            self.time.append(data[3][i])
            self.tension.append(data[4][i])
        offTension = 'no reset'
        offCurrent = 'no reset'
        offResistance = 'no reset'

#Finds the largest drop of electrical current and gives the off resistance near 0 V.
        maxDelta = 0.
        if self.wishedTension[3]-self.wishedTension[2]>0:
            for i in range((len(self.tension))-2):#/2)):
                    delta = abs(ratioReset * self.current[i])
                    if (-self.current[i+1] + self.current[i]) > delta and (-self.current[i+1] + self.current[i]) > maxDelta:
                        offTension = self.wishedTension[i]
                        offCurrent = self.current[i]
                        offResistance = self.resistance[len(self.tension)-2]
                        maxDelta = abs(-self.current[i+1] + self.current[i])    
        else:
            for i in range((len(self.tension))-2):#/2)):
                    delta = -abs(ratioReset * self.current[i])
                    if -(-self.current[i+1] + self.current[i]) > delta and -(-self.current[i+1] + self.current[i]) > maxDelta:
                        offTension = self.wishedTension[i]
                        offCurrent = self.current[i]
                        offResistance = self.resistance[len(self.tension)-2]
                        maxDelta = abs(-self.current[i+1] + self.current[i])    
        self.reset = [offTension,offCurrent,offResistance]


##Finds the smallest instantaneous increase of resistance and gives the off resistance near 0 V.              
#        maxDelta = 0.
#        delta = abs(ratioReset * self.resistance[2])
#        for i in range((len(self.tension))-1):#/2):
#                if (self.resistance[i+1]-self.resistance[i]) > delta and (self.resistance[i+1] - self.resistance[i]) > maxDelta:
#                    offTension = self.wishedTension[i]
#                    offCurrent = self.current[i]           
#                    offResistance = self.resistance[len(self.tension)-2]
#                    maxDelta = (self.resistance[i+1]-self.resistance[i])     
#        self.reset = [offTension,offCurrent,offResistance]