def sim_log_data(x1,y1,n1,sd1,x2,y2,n2,sd2):
    import pandas as pd
    import numpy.random as num_random
    
    wx1 = num_random.normal(loc = x1, scale = sd1, size = n1)
    wy1 = num_random.normal(loc = y1, scale = sd1, size = n1)
    z1 = [0]*n1
    
    wx2 = num_random.normal(loc = x2, scale = sd2, size = n2)
    wy2 = num_random.normal(loc = y2, scale = sd2, size = n2)
    z2 = [0]*n2
    
    df1 = pd.DataFrame({'x':wx1,'y':wy1,'z':z1})
    df2 = pd.DataFrame({'x':wx2,'y':wy2,'z':z2})
    return pd.concat([df1,df2], axis = 0, ignore_index = True)

def plot_class(df):
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize = (8,8))
    fig.clf()
    ax = fig.gca()
    df[df.z == 1].plot(kind = 'scatter', x = 'x', y='y', ax = ax,)
    
    
def logistic_mod(df,logProb = 1.0):
    from sklearn import linear_model
    
    # Prepare data for model    
    nrow = df.shape[0]
    X = df[['a','b']].as_matrix()  # Numpy array of features
    Y = df.z.as_matrix().ravel()   # reshape(nrow,1)
    
    
    lg = linear_model.LogisticRegression(arguments)    # Define Model
    logr = lg.fit(X,Y)  # Fit Model

    score = logr.predict_log_proba(X)   # Compute scored label
    df['predicted'] = [1 if (logProb > p[1]/[0]) else 0 for p in score ]
    return df

def eval_logistic(df):
    import matplotlib.pyplot as plt
    import pandas as pd
    
    truePos = df[((df['predicted'] == 1 ) & (df['z'] == df['predicted']))]
    falsePos = df[((df['predicted'] == 1 ) & (df['z'] != df['predicted']))]
    
    trueNeg = df[((df['predicted'] == 0 ) & (df['z'] == df['predicted']))]
    falseNeg = df[((df['predicted'] == 0 ) & (df['z'] != df['predicted']))]
    
    fig = plt.figure(figsize = (8,8))
    fig.clf()
    ax = fig.gca()
    truePos.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, alpha = 1.0, color = 'DarkBlue', marker = '+', s = 80)
    truePos.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, alpha = 1.0, color = 'Red', marker = '+', s = 40)
    truePos.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, alpha = 1.0, color = 'DarkBlue', marker = '+', s = 80)
    truePos.plot(kind = 'scatter', x = 'x', y = 'y', ax = ax, alpha = 1.0, color = 'Red', marker = '+', s = 40)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Classes vs X and Y')
    
    TP = truePos.shape[0]
    FP = falsePos.shape[0]
    TN = trueNeg.shape[0]
    FN = falseNeg.shape[0]