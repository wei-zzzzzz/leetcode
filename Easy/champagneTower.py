'''
10_28
Time: O(r^2)
Space: O(r^2)
r 為排數，若以杯子量考量則為O(n)
思考流程：
1.一開始以為只要上層杯子未滿則無法流往下層
2.所以直接扣除上層杯子數目後所剩的按照權重分配給最下層杯子
但這樣是錯的！！要考量現實物理狀態可能種間的杯子已滿（因為注入量是2倍）而已開始流往下層

重新思考後，決定按照每個杯子去跑
1.先建立好杯子且排好造型（用 list 裝多個 list）
2.接著開始倒入酒：
    若現在杯子其值大於1，代表該杯滿了多的poured 須流向下一排之左右兩杯(平分給予)，並期內容改為1
    修正：到了最後一派時要去確認內容是否大於1
3.小小幅度加快的修正，不跑最後一排（少判斷是否為最後一排），回傳時只修正題目要的杯子其內容

'''
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
        ##修正for迴圈可加快速度
        for i in range(query_row):
            for j in range(len(Glass[i])):
                #if i == query_row:
                 #   Glass[i][j] = min(1,Glass[i][j])
                
                if Glass[i][j] > 1:
                    Glass[i+1][j] += (Glass[i][j] -1)/2
                    Glass[i+1][j+1] += (Glass[i][j] -1)/2
                    Glass[i][j] = 1        
        if Glass[query_row][query_glass] > 1:
            return 1
        else:
            return Glass[query_row][query_glass]
       '''
'''
        #first error
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
