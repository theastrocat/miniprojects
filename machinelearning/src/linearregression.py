import numpy as np

class LinearRegression(object):
    """
    Parameters
    ----------

    Attributes
    ----------
    coef_ : array, shape (n_features, ) or (n_targets, n_features)

    residues_ : array, shape (n_targets)
    """
    def __init__(self):
        self.eta_ = 0.00001
        self.n_iter_ = 10000

    def fit(self, X, y):
        """
        Fit linear model.

        Parameters
        ----------
        X : numpy array or sparse matrix of shape [n_samples,n_features]
            Training data

        y : numpy array of shape [n_samples,]
            Target values

        Returns
        -------
        self : returns an instance of self.
        """

        self.coef_ = np.zeros((X.shape[1]+1,))
        for _ in range(self.n_iter_):
            for xi, target in zip(X,y):
                y_pred = self.predict(xi)
                update = self.eta_ * (target - y_pred)
                self.coef_[1:] += update * xi
                self.coef_[0] += update
        return self


    def predict(self, X):
        return self.coef_[0] + np.sum(self.coef_[1:] * X)
