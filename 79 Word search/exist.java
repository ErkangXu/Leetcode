public class Solution {
    public class Coordinate {
        public int r;
        public int c;
        public Coordinate(int row,int column){ // Should use different variables as parameters
            r=row;
            c=column;
        }
        @Override public boolean equals(Object other){
            if (other instanceof Coordinate) {
                Coordinate that = (Coordinate) other;
                if (this.r == that.r && this.c == that.c) return true;
            }
            return false;
        }
        @Override public int hashCode() {
            return (41 * (41 + r) + c);
        }
    }
    public boolean exist(char[][] board, String word) {
        int rowN=board.length;
        int columnN=board[0].length;
        for(int i=0;i<rowN;i++){
            for(int j=0;j<columnN;j++){
                if(board[i][j]==word.charAt(0)){
                    List<List<Coordinate>> pool = new ArrayList<List<Coordinate>>();
                    List<Coordinate> tl = new ArrayList<Coordinate>();
                    tl.add(new Coordinate(i,j));
                    pool.add(tl);
                    int pointer=0;
                    Outer: 
                    while(pointer>-1){
                        List<Coordinate> route = pool.get(pointer--);
                        for(int k=route.size();k<word.length();k++){
                            char z=word.charAt(k);
                            Coordinate c = route.get(k-1);
                            List<Coordinate> tmp = new ArrayList<Coordinate>();
                            if(c.c-1>=0      && !route.contains(new Coordinate(c.r,c.c-1)) && z==board[c.r][c.c-1]) 
                                tmp.add(new Coordinate(c.r,c.c-1));
                            if(c.c+1<columnN && !route.contains(new Coordinate(c.r,c.c+1)) && z==board[c.r][c.c+1]) 
                                tmp.add(new Coordinate(c.r,c.c+1));
                            if(c.r-1>=0      && !route.contains(new Coordinate(c.r-1,c.c)) && z==board[c.r-1][c.c]) 
                                tmp.add(new Coordinate(c.r-1,c.c));
                            if(c.r+1<rowN    && !route.contains(new Coordinate(c.r+1,c.c)) && z==board[c.r+1][c.c]) 
                                tmp.add(new Coordinate(c.r+1,c.c));
                            if(tmp.isEmpty()) continue Outer; // Used break instead of continue;
                            for(int a=1;a<tmp.size();a++) {
                                List<Coordinate> newRoute = new ArrayList<Coordinate>(route);
                                newRoute.add(tmp.get(a));
                                pool.add(++pointer,newRoute);
                            }
                            route.add(tmp.get(0));
                        }
                        return true;
                    }
                }
            }
        }
        return false;
    }
}