class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        if not restaurants:
            return []
        
        result = []
        
        for i, rating, vF, price, distance in restaurants:
            if veganFriendly == 1 and vF != 1:
                continue
                
            if maxPrice < price or maxDistance < distance:
                continue
                
            result.append([-rating, -i])
                
        return [-i for r, i in sorted(result)]