import flingHelper
import reverseFling
print("hello")
flings = reverseFling.randomBuilder(4,(5,5))
grid = flingHelper.flingStartup(flings)
flingHelper.printGrid(grid)