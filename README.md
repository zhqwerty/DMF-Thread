# Martrix Factorizaion Formulation

We consider the classical matrix factorization problem which can be formulated as a constrained optimizaition problem:
$$
\min{X,Y} \ \sum_{(i,j)\in \Omega} loss(A{ij}, (XY^T){ij}) + \lambda | X|_F^2 + \lambda | Y|_F^2
$$

We use the following three loss functions, the algorithm are based on stochastic gradient descent with learnint rate $\eta = \eta_0 / (k + 1)^{0.1}$.

Square Loss: $loss(x,y) = (x - y)^2$ with $\lambda = 0.1
Sigmoid Loss: $ loss(x,y) = 1 / ( 1 + exp(x, y)) $ with $\lambda = 0.01$ 
Square-Hinge Loss: $ loss(x,y) = (max(0, 1-xy))^2 $ with $\lambda = 0.1$ 