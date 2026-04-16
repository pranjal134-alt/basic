import numpy as np
a=np.array([[1,2,3],
            [3,4,5]])
print(np.unique(a)[-2])
d=np.arange(12).reshape(3,4)
print(d([3,4]))