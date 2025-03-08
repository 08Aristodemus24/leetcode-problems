#include <iostream>
#include <queue>
#include <vector>
// #include <format>

struct Point{
    int r;
    int c;
};

class Graph{
    private:
        std::vector<std::vector<char>> board;

        int _findShortestPath(std::vector<int>& start, std::vector<int>& end){
            /*
            Given a 15x15 board with cells '0' (open path), '1' (obstacle), 'X’ (starting point), 
            and 'FLAG' (destination), make a python code that will find the shortest path from a 
            start cell (‘X') to 'FLAG. Output should be the coordinates of the 'X' with the 
            shortest path to 'FLAG’.
            */

            // unpack start and end coordinates
            int start_r = start[0], start_c = start[1];
            int end_r = end[0], end_c = end[1];

            // initialize flag to false
            int reached_end = false;
            
            // initialize visited matrix to false values
            // as this we will use to track if a nodes coordinate
            // has been visited indicated as a true value and false
            // otherwise. fill in newly declared matrix with false values
            std::vector<std::vector<bool>> visited;
            visited.resize(m, std::vector<bool>(n, false));

            // row queue and column queue to 
            std::queue<int> rq;
            std::queue<int> cq;
            int curr_r, curr_c;

            // initially push starting row and column indeces
            rq.push(start_r);
            cq.push(start_c);

            while(rq.size() > 0){
                // get front element before popping out of the queue
                curr_r = rq.front();
                curr_c = cq.front();

                // we extract curr_r and curr_c and mark the node as
                // visited
                visited[curr_r][curr_c] = true;

                // pop the current coordinates
                rq.pop();
                cq.pop();

                // check if current coordinates value matches the
                // value of the end coordinate which would be F
                if(board[curr_r][curr_c] == 'F'){
                    reached_end = true;
                    break;
                }

                // explore neighbors
                _enqueueNeighbors(curr_r, curr_c, rq, cq, visited);

                // std::cout << rq.front() << " ";
            }

            // if reached end has been turned to true then
            // the function will return 1
            if(reached_end){
                return 1;
            }
            return -1;
        }

        void _enqueueNeighbors(int curr_r, int curr_c, std::queue<int>& rq, std::queue<int>& cq, std::vector<std::vector<bool>>& visited){
            // these direction vectors represent going up down, right, left
            // respectively
            std::vector<std::vector<int>> drc = {{-1, 0}, {+1, 0}, {0, +1}, {0, -1}};
            int new_r, new_c, dr, dc;

            for(int i = 0; i < drc.size(); i++){
                // std::cout << drc[i][0] << " " << drc[i][1] << "\n";
                dr = drc[i][0];
                dc = drc[i][1];
                
                // calculate new row index and column index of neighbor node
                new_r = curr_r + dr;
                new_c = curr_c + dc;

                if((new_r < 0 || new_r >= m) || (new_c < 0 || new_c >= n)){
                    // check if newly calculated row and column indeces serve as viable
                    // coordinates in that they do not go out of bounds of the grid
                    continue;

                }if((visited[new_r][new_c] == true) || (board[new_r][new_c] == '1')){
                    // likewise if a nodes new coordinate has already been visited 
                    // or if it is an obstacle then don't enqueue it anymore
                    continue;
                }

                // std::cout << new_r << " " << new_c << std::endl;

                // append coordinates of new neighbors of current node
                rq.push(new_r);
                cq.push(new_c);

                // set the popped node as visited
                // visited[new_r][new_c] = true;
            } 
        }

        std::vector<Point> _findXs(){
            std::vector<Point> xs;
            for(int i = 0; i < board.size(); i++){
                for(int j = 0; j < board[0].size(); j++){
                    // check if coordinates of board is an X
                    if(board[i][j] == 'X'){
                        // initialize point structure
                        Point rc;
                        rc.r = i;
                        rc.c = j;
                        
                        // push the point structure to vector
                        xs.push_back(rc);
                    }
                }
            }

            return xs;
        }

        std::vector<int> _findEnd(){
            std::vector<int> end;
            for(int i = 0; i < board.size(); i++){
                for(int j = 0; j < board[0].size(); j++){
                    // check if coordinates of board is an F
                    if(board[i][j] == 'F'){
                        // push the i and j coordinates to vector
                        end.push_back(i);
                        end.push_back(j);
                    }
                }
            }

            return end;
        }

        



    public:
        int m; 
        int n;

        Graph(std::vector<std::vector<char>>& input_board){
            board = input_board;
            // std::cout << board.size() << board[0].size();

            // dimensions of graph
            m = input_board.size();
            n = input_board[0].size();
        }

        std::vector<Point> findShortestPath(){
            // for(int i = 0; i < m; i++){
            //     for(int j = 0; j < n; j++){
            //         std::cout << board[i][j];
            //     }
            // }
            
            // once extracted all the Xs we can figure out which  
            std::vector<Point> xs =  _findXs();
            std::vector<int> end = _findEnd();

            std::vector<Point> coords;
            for(int i = 0; i < xs.size(); i++){
                std::cout << "testing coordinates: (" << xs[i].r << ", " << xs[i].c << ")" << "\n";

                std::vector<int> start = {xs[i].r, xs[i].c};
                // std::vector<int> start = {13, 5};
                
                if(_findShortestPath(start, end) == 1){
                    // std::cout << "coordinates: (13, 5) has a path\n\n";
                    std::cout << "coordinates: (" << xs[i].r << ", " << xs[i].c << ")" << " has a path\n\n";
                }else{
                    std::cout << "coordinates: (" << xs[i].r << ", " << xs[i].c << ")" << " has no path\n\n";
                }
            }

            std::cout << "end coordinates: (" << end[0] << ", " << end[1] << ")" << "\n";
            
            
        }

        
};

int main(int argc, char** argv){
    std::vector<std::vector<char>> board = {
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
    Graph* g = new Graph(board);

    g->findShortestPath();

    return 0;
}