class Solution(object):
    def leastInterval(self, tasks, n):
        """
        Returns the minimum number of intervals required to complete all tasks.
        :param tasks: List[str] - Array of CPU tasks represented by letters A to Z.
        :param n: int - Cooling time, tasks of the same type must be separated by at least n intervals.
        :return: int - Minimum number of intervals required.
        """
        # Count the frequency of each task
        frequencies = [0] * 26
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        
        # Sort the frequencies in descending order
        frequencies.sort(reverse=True)
        
        # Get the maximum frequency
        max_freq = frequencies[0]
        
        # Calculate the number of intervals required
        idle_time = (max_freq - 1) * n
        for freq in frequencies[1:]:
            idle_time -= min(freq, max_freq - 1)
        
        idle_time = max(0, idle_time)
        
        return len(tasks) + idle_time
