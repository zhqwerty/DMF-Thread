# Martrix Factorizaion Formulation

$$\min_{X,Y} \ \sum_{(i,j)\in \Omega} loss(A_{ij}, (XY^T)_{ij}) + \lambda \| X\|_F^2 + \lambda \| Y\|_F^2$$

We use the following three loss functions, the algorithm are based on stochastic gradient descent.
Square Loss: $loss(x,y) = (x - y)^2$
Sigmoid Loss: $ loss(x,y) = 1 / ( 1 + exp(x, y)) $
Square-Hinge Loss: $ loss(x,y) = (max(0, 1-xy))^2 $




