def solution_station_3(input): 
   digit_sum = sum(int(digit) for digit in str(n))
   result = digit_sum % 3 == 0 or n == 0
  return result
