#include <iostream>
#include <queue>

class Graph{
    private:
        char board[15][15] = {
            {'0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'F'},
            {'0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'},
            {'0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0'},
            {'1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0'},
            {'X', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'},
            {'0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'},
            {'0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'},
            {'0', '0', 'X', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0'},
            {'X', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0'},
            {'X', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'},
            {'0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'},
            {'0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'},
            {'0', '0', 'X', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0'},
            {'X', '1', '0', '0', '0', 'X', '1', '1', '0', '1', '0', '0', '0', '0', '0'},
            {'X', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'}
        };

    public:
        int m; 
        int n;
        bool** visited;
        Graph(){
            // dimensions of graph
            m = sizeof(board) / sizeof(board[0]);
            n = sizeof(board[0]) / sizeof(board[0][0]);

            // initialize visited matrix to false values
            // as this we will use to track if a nodes coordinate
            // has been visited indicated as a true value and false
            // otherwise
            visited = new bool*[m];
            for(int i = 0; i < m; i++){
                visited[i] = new bool[n];
            }

            // fill in newly declared matrix with false values
            for(int i = 0; i < m; i++){
                for(int j = 0; j < n; j++){
                    visited[i][j] = false;
                }
            }
        }

        int findShortestPath(int* start, int* end){
            /*
            Given a 15x15 board with cells '0' (open path), '1' (obstacle), 'X’ (starting point), 
            and 'FLAG' (destination), make a python code that will find the shortest path from a 
            start cell (‘X') to 'FLAG. Output should be the coordinates of the 'X' with the 
            shortest path to 'FLAG’.
            */

            int start_r = start[0], start_c = start[1];
            int end_r = end[0], end_c = end[1];
            int reached_end = false;

            // row queue and column queue to 
            std::queue<int> rq;
            std::queue<int> cq;
            int curr_r, curr_c;

            // for(int i = 0; i < m; i++){
            //     for(int j = 0; j < n; j++){
            //         std::cout << visited[i][j];
            //     }
            // }
            rq.push(start_r);
            cq.push(start_c);

            while(rq.size() > 0){
                // get front element before popping out of the queue
                curr_r = rq.front();
                curr_c = cq.front();

                // pop the current coordinates
                rq.pop();
                cq.pop();
                
                // check if current coordinates value matches the
                // value of the end coordinate which would be F
                if(board[curr_r][curr_r] == 'X'){
                    reached_end = true;
                    break;
                }
            }
            std::cout << curr_r << " " << curr_c;
            // std::cout << m << " " << n;
        }
};


int main(int argc, char** argv){
    Graph g;
    int start[] = {14, 0};
    int end[] = {0, 14};

    g.findShortestPath(start, end);

    return 0;
}

// class Graph:
//     def __init__(self):
        // self.board = [
        //     ['0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', 'FLAG'],
        //     ['0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        //     ['0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0'],
        //     ['1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0'],
        //     ['X', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        //     ['0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        //     ['0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        //     ['0', '0', 'X', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0'],
        //     ['X', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0'],
        //     ['X', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        //     ['0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        //     ['0', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
        //     ['0', '0', 'X', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0'],
        //     ['X', '1', '0', '0', '0', 'X', '1', '1', '0', '1', '0', '0', '0', '0', '0'],
        //     ['X', '1', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0']
        // ]

//     def findShortestPath(self):
//         

//         # X can have multiple starting points
//         xs = self.findXs()
//         m, n = len(self.board), len(self.board[-1])

//         for start_v in xs:
//             self._findShortestPath(start_v)

//     def _findShortestPath(self, v):
//         """
//         v is a coordinate 
//         """
//         x, y = v

//         # base case
//         if "FLAG" in self.board[x][y]:
//             return
        
//         for v in :


//     def findXs(self):
//         xs = []
//         for i in range(self.board):
//             for j in range(i):
//                 if self.board[i][j] == "X":
//                     xs.append([i, j])           
//         return xs