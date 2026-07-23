class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        recordSum = 0

        for i in range(0, len(operations)):
            try:
                record.append(int(operations[i]))
            except ValueError:
                pass

            if operations[i] == "+":
                record.append(record[len(record)-1] + record[len(record)-2])
            
            if operations[i] == "D":
                record.append(record[len(record)-1] * 2)
            
            if operations[i] == "C":
                record.pop()
                
        for i in record:
            recordSum += i
        return recordSum
        