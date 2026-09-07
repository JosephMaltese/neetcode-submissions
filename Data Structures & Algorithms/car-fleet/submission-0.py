class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedArray = list(zip(position, speed))
        positionSpeedArray.sort(key = lambda x: x[0], reverse=True)

        fleetArrivalTimeStack = []
        for i in range(len(positionSpeedArray)):
            currentCar = positionSpeedArray[i]
            arrivalTime = (target - currentCar[0]) / currentCar[1]
            if i == 0:
                fleetArrivalTimeStack.append(arrivalTime)
            else:
                nextFleetAheadTime = fleetArrivalTimeStack[-1]
                if arrivalTime > nextFleetAheadTime:
                    fleetArrivalTimeStack.append(arrivalTime)
        return len(fleetArrivalTimeStack)