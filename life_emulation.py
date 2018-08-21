
class LifeEmulation(object):
    def __init__(self, start_state, maximum_value):
        self.maximum_value = maximum_value
        self.start_state = start_state
        self.current_state = list()
        for i in self.start_state:
            self.current_state.append(list(i))

    def __str__(self):
        return '\n'.join(' '.join(str(x) for x in i) for i in self.start_state)

    def get_neighbours_indexes(self, i, j):
        my = list()
        if(i > 0 and j > 0):
            my.append((i - 1, j - 1))
        if(i > 0):
            my.append((i - 1, j))
        if(j > 0):
            my.append((i, j - 1))
        if(i > 0 and len(self.start_state) > 0 and
           j < len(self.start_state[i]) - 1):
            my.append((i - 1, j + 1))
        if(j > 0 and i < len(self.start_state) - 1):
            my.append((i + 1, j - 1))
        if(i < len(self.start_state) - 1):
            my.append((i + 1, j))
        if(len(self.start_state) > 0 and j < len(self.start_state[i]) - 1):
            my.append((i, j + 1))
        if(i < len(self.start_state) - 1 and j < len(self.start_state[i]) - 1):
            my.append((i + 1, j + 1))
        return my

    def get_neighbours_count_with_positive_value(self, i, j):
        my = self.get_neighbours_indexes(i, j)
        positive_count = int()
        for index in my:
            if(int(self.start_state[index[0]][index[1]]) > 0):
                positive_count += 1
        return positive_count

    def get_next_state(self, i, j):
        positive_count = self.get_neighbours_count_with_positive_value(i, j)
        if(self.start_state[i][j] == 0 and int(positive_count) == 3):
            return 1
        elif(self.start_state[i][j] > 0 and (int(positive_count) == 2 or
             int(positive_count) == 3) and
             self.start_state[i][j] != self.maximum_value):
            return self.start_state[i][j] + 1
        elif (self.start_state[i][j] > 0 and (int(positive_count) == 4 or
              int(positive_count) == 5 or int(positive_count) == 1)):
            return 0
        elif (self.start_state[i][j] > 0 and (int(positive_count) == 6 or
              int(positive_count) == 8 or int(positive_count) == 0)):
            return self.start_state[i][j] - 1
        else:
            return self.start_state[i][j]

    def iterate(self):
        for i in range(0, len(self.start_state)):
            for j in range(0, len(self.start_state[i])):
                self.current_state[i][j] = self.get_next_state(i, j)
        for i in range(0, len(self.start_state)):
            for j in range(0, len(self.start_state[i])):
                self.start_state[i][j] = self.current_state[i][j]
        return
