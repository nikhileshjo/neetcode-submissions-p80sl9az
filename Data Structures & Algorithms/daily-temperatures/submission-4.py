class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        # Run a for loop from the second last index
        # To the first index for the temperatures list
        for i in range(n-2, -1, -1):
            j = i + 1 # Start comparisions from the next element i + 1

            # Run a while loop that checks if we are in bounds of temperatures
            # and checks if the jth element is less than or equal to ith element
            while j < n and temperatures[j] <= temperatures[i]:

                # if the jth result is 0 it means we will never find an
                # element in temperatures after the jth element
                # that's greater that the jth element. Also, we know from
                # the while loop that the jth element is smaller than ith.
                # Therefore, there is no point checking any further if there
                # exists an element in temperatures that's greater than ith element.
                if res[j] == 0:
                    j = n
                    break
                # Skippin the next element that's greater than
                # the current temperatures[j]
                j += res[j]

            # If j < n we never assigned j = n in the while loop above
            # which means  we broke the while loop condition
            # temperatures[j] <= temperatures[i], meaning we found an element
            # that's greater than temperatures[i]
            # so we assign the res[i] with relevent value
            # else we leave it as 0
            if j < n:
                res[i] = j - i
        
        return res