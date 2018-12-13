arr = [13, 1, 4, 7, 12]

# Print the maximum element on the right of any particular element

max_element = arr[len(arr)-1]

for i in range(len(arr) - 2, - 1, -1):
  if arr[i] <= max_element:
    arr[i] = max_element
  else:
    max_element = arr[i]
    arr[i] = -1

print(arr)