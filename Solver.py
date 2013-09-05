class Klotski():
    # check to right of empty space

    def prettyprint(self, board):
        output = ''
        i = 0
        for x in board:
            if i > 7 and i < 28:
                if (i + 1) % 4 == 0:
                    output += str(x) + ' ' + '\n'
                else:
                    output += str(x) + ' '
            i += 1
        print output + '\n'

    def check_right(self, board, i):
        moves = []
        moves.append(board)
        if (i + 1) % 4 != 0:
            tempboard = list(board)
            # horizontal rectangle
            if board[i + 1] == 3:
                tempboard[i] = 3
                tempboard[i + 2] = 0
                moves.append(tempboard)
            tempboard = list(board)
            # small square
            if board[i + 1] == 4:
                tempboard[i] = 4
                tempboard[i + 1] = 0
                moves.append(tempboard)
            tempboard = list(board)
            # large square
            if board[i + 4] == 0 and board[i + 1] == 2 and board[i + 5] == 2:
                tempboard[i] = 2
                tempboard[i + 4] = 2
                tempboard[i + 2] = 0
                tempboard[i + 6] = 0
                moves.append(tempboard)
            tempboard = list(board)
            # vertical rectangle
            if board[i + 4] == 0 and board[i + 1] == 1 and board[i + 5] == 1 and ((board[i + 9] != 1) or (board[i - 3] != 1)):
                tempboard[i] = 1
                tempboard[i + 4] = 1
                tempboard[i + 1] = 0
                tempboard[i + 5] = 0
                moves.append(tempboard)
        return moves

    def check_up(self, board, i):
        moves = []
        moves.append(board)
        if i > 11:
            tempboard = list(board)
            # vertical rectangle
            if board[i - 4] == 1:
                tempboard[i] = 1
                tempboard[i - 8] = 0
                moves.append(tempboard)
            tempboard = list(board)
            # small square
            if board[i - 4] == 4:
                tempboard[i] = 4
                tempboard[i - 4] = 0
                moves.append(tempboard)
            tempboard = list(board)
            # large Square
            if board[i + 1] == 0 and board[i - 4] == 2 and board[i - 3] == 2:
                tempboard[i] = 2
                tempboard[i + 1] = 2
                tempboard[i - 8] = 0
                tempboard[i - 7] = 0
                moves.append(tempboard)
            tempboard = list(board)
            # horizontal rectangle
            if board[i + 1] == 0 and board[i - 4] == 3 and board[i - 3] == 3:
                tempboard[i] = 3
                tempboard[i + 1] = 3
                tempboard[i - 4] = 0
                tempboard[i - 3] = 0
                moves.append(tempboard)
        return moves

    def solve(self, board):
        result = None
        queue = []
        queue.append(board)
        n = 0
        past_boards = {str(board): board}
        while result == None:
            i = 0

            candidates = []
            current_board = queue.pop(0)
            upsidedown = list(current_board)
            upsidedown.reverse()
            if current_board[25] == 2 and current_board[26] == 2:
                result = current_board
                print "done"

                while current_board != board:
                    candidates.append(current_board)
                    current_board = past_boards[str(current_board)]
                candidates.reverse()
                for x in candidates:
                    self.prettyprint(x)

                break
            for x in current_board:
                if x == 0:
                    candidates.append(self.check_right(list(current_board), i))
                    candidates.append(self.check_up(list(current_board), i))
                i += 1
            i = 0
            for x in upsidedown:
                if x == 0:
                    rightwayup = []
                    a = self.check_right(list(upsidedown), i)
                    b = self.check_up(list(upsidedown), i)
                    for ls in a:
                        turned = list(ls)
                        turned.reverse()
                        rightwayup.append(turned)
                    for ls in b:
                        turned = list(ls)
                        turned.reverse()
                        rightwayup.append(turned)
                    candidates.append(rightwayup)

                i += 1

            for moves in candidates:
                for boards in moves:
                    if past_boards.has_key(str(boards)):
                        pass
                    else:
                        past_boards[str(boards)] = current_board
                        queue.append(boards)

            n += 1

            if n == 30000:
                for x in queue:
                    print n
                    # print past_boards
                    break
