def asteroidCollision(asteroids: list[int]) -> list[int]:
    result = []
    stack = []
    
    for asteroid in asteroids:
        if asteroid < 0:
            if stack:
                brokenAsteroid = False
                while stack:
                    if stack[-1] == abs(asteroid):
                        brokenAsteroid = True
                        stack.pop()
                        break
                    elif stack[-1] < abs(asteroid):
                        stack.pop()
                    else:
                        brokenAsteroid = True
                        break
                if not brokenAsteroid:
                    result.append(asteroid)
            else:
                result.append(asteroid)
        else:
            stack.append(asteroid)
    
    result.extend(stack)
    
    return result


if __name__ == "__main__":
    print(asteroidCollision([5,10,-5]))
    print(asteroidCollision([8,-8]))
    print(asteroidCollision([10,2,-5]))
    print(asteroidCollision([-2,-1,1,2]))