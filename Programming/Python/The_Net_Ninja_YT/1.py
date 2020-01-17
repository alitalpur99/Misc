sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89, 12, 11, 14]
print("Origigal list ", sampleList)
print("length= ", len(sampleList))
length = len(sampleList)    # 12
chunkSize  = int(length/3)   # 4
start = 0
end = chunkSize    # 4
for i in range(1, 4, 1):
  indexes = slice(start, end, 1)
  print(indexes, sampleList[indexes])
  listChunk = sampleList[indexes]
  print("Chunk ", i , listChunk)
  print("After reversing it ", list(reversed(listChunk)))
  start = end
  if(i != 2):
    end +=chunkSize
  else:
    end += length - chunkSize

