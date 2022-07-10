


# def tryposition(position):
#     row, col = position / 8, position % 8
#     position1 = position
#     position2 = position
#     position3 = position
#     while position1 < 64:
#         queens[position1] = 0
#         position1 += 8
#     while 0 <= position2 <= 63 and col >= 0:
#         queens[position2] = 0
#         position2 += 7
#         col -= 1
#     while 0 <= position3 <= 63 and col <=7:
#         queens[position3] = 0
#         position3 += 9
#         col += 1
#     queens[position] = True
# def try_next():
    
    
# def find_available_place():
#     while True:    
#         queens_new = queens[8:]
#         try:

#             position = queens_new.index()
            
#         except:
            

# def print_queen():
#     p = list()
#     for i in queens:
#         if i is True:
#             p.append('|Q')
#         else:
#             p.append('| ')
#     count = 0
#     for j in p:
#         count += 1
#         print(j, end = '|\n' if count%8 == 0 else "")

# if __name__ == "__main__":
#     print('This is a solution of eight queen problems.')
#     queens = [[False] * 8] * 8
#     tryposition(3)
#     print(queens)
#     print_queen()



# class NQueens:
#     """Generate all valid solutions for the n queens puzzle"""
#     def __init__(self, size):
#        # Store the puzzle (problem) size and the number of valid solutions
#         self.size = size
#         self.solutions = 0
#         self.solve()

#     def solve(self):
#         """Solve the n queens puzzle and print the number of solutions"""
#         positions = [-1] * self.size
#         self.put_queen(positions, 0)
#         print("Found", self.solutions, "solutions.")

#     def put_queen(self, positions, target_row):
#          """
#         Try to place a queen on target_row by checking all N possible cases.
#         If a valid place is found the function calls itself trying to place a queen
#         on the next row until all N queens are placed on the NxN board.
#         """
#         # Base (stop) case - all N rows are occupied
#         if target_row == self.size:
#             self.show_full_board(positions)
#             self.solutions += 1
#         else:
#            # For all N columns positions try to place a queen
#             for column in range(self.size):
#                # Reject all invalid positions
#                 if self.check_place(positions, target_row, column):
#                     positions[target_row] = column
#                     self.put_queen(positions, target_row + 1)

#     def check_place(self, positions, ocuppied_rows, column):
#         """
#        Check if a given position is under attack from any of
#         the previously placed queens (check column and diagonal positions)
#         """
#         for i in range(ocuppied_rows):
#             if positions[i] == column or \
#                positions[i] - i == column - ocuppied_rows or \
#                positions[i] + i == column + ocuppied_rows:

#                 return False
#         return True

#     def show_full_board(self, positions):
#                  """Show the full NxN board"""
#         for row in range(self.size):
#             line = ""
#             for column in range(self.size):
#                 if positions[row] == column:
#                     line += "Q "
#                 else:
#                     line += ". "
#                     print(line)
#             print("\n")

# def main():
#          """Initialize and solve the n queens puzzle"""
#     NQueens(8)

# if __name__ == "__main__":
#     # execute only if run as a script
#     main()




###print({1:2}+{1:2})   #ERROR

### print((3,3)+(3,3))  #####(3,3,3,3)
# num = [1,2,3]
# print(eval(input('Enter:')))
a=[[1,2,3],[4,5,6],[7,8,9]]

m = [[r[-i] for r in a] for i in range(len(a))]
print(m)