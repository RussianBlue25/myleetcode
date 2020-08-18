class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        turn = 0
        turn_sum_candy = 0
        each_candy = []
        last_turn_each_candy = 0
        
        while True:
            turn_sum_candy = (num_people*((2*(turn+1)-1)*num_people+1))/2
            if candies < turn_sum_candy:
                break
            candies -= turn_sum_candy
            turn += 1
        
        for i in range(num_people):
            each_candy.append(int(turn*(turn-1)*num_people/2 + (i+1)*turn))
            if candies == 0:
                continue
            last_turn_each_candy = turn*num_people+(i+1)
            if candies < last_turn_each_candy:
                each_candy[i] += int(candies)
                candies = 0
            else:
                each_candy[i] += int(last_turn_each_candy)
                candies -= last_turn_each_candy
        return each_candy
