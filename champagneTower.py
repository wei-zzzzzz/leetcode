class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        Glass = []
        for i in range(1,query_row + 2):
                Glass += [[0] * i ]
        Glass[0][0] = poured
        
        for i in range(query_row + 1):
            for j in range(len(Glass[i])):
                if i == query_row:
                    Glass[i][j] = min(1,Glass[i][j])
                
                elif Glass[i][j] > 1:
                    Glass[i+1][j] += (Glass[i][j] -1)/2
                    Glass[i+1][j+1] += (Glass[i][j] -1)/2
                    Glass[i][j] = 1
                    
        
        return Glass[query_row][query_glass]        
        
        '''
        if query_row == 0 :
            if poured > 1:
                return 1
            else:
                return poured
        poured = poured -  ((query_row) * (query_row+1))/2
        if poured > query_row:
            return 1
        ave = 2 + 2*(query_row - 1)
        if query_glass == 0 or query_glass == query_row:
            return poured/ave
        else:
            return (poured*2)/ave
        '''
