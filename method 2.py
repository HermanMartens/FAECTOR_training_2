#%% tangency portfolio and gmv portfolio rolling window 100 (method 2)
#rolling_mu = excess_return.rolling(100).mean()
#rolling_cov = excess_return.rolling(100).cov()

#weight_tangency=[]
#return_tangency=[]
#std_tangency = []
#weight_gmv=[]
#return_gmv=[]
#std_gmv = []
#one_vector = np.matrix(np.ones(50)).T
#one_transpose = one_vector.T
#for i in range (99,1762):
#    U = np.matrix(rolling_mu.iloc[i,:].to_numpy()).T
#    S = np.matrix(rolling_cov.iloc[50*i:50*(i+1),:].to_numpy()).T
#    S_inv = inv(S)
#    A = S_inv*U
#    B = one_transpose*A
#    C = S_inv*one_vector
#    D = one_transpose*C
#    w_t = A/B
#    w_gmv = C/D
#    weight_tangency.append(w_t)
#    return_tangency.append(float(w_t.T*U))
#    std_tangency.append(float(np.sqrt(w_t.T*S*w_t)))
#    weight_gmv.append(w_gmv)
#    return_gmv.append(float(w_gmv.T*U))
#    std_gmv.append(float(np.sqrt(w_gmv.T*S*w_gmv)))
#
#volatility_tangency = np.mean(std_tangency)
#sharpe_tangency = np.mean(return_tangency) / volatility_tangency
#volatility_gmv = np.mean(std_gmv)
#sharpe_gmv = np.mean(return_gmv) / volatility_gmv
#
#sharpe1_tangency = np.mean(sharpe_tangency_list)
#sharpe1_gmv = np.mean(sharpe_gmv_list)
