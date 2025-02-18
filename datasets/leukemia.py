from benchopt import BaseDataset

from benchopt import safe_import_context


with safe_import_context() as import_ctx:
    from sklearn.datasets import fetch_openml
    from sklearn.preprocessing import LabelBinarizer


class Dataset(BaseDataset):

    name = "leukemia"

    install_cmd = 'conda'
    requirements = ['scikit-learn']
    references = [
        "T. R. Golub, D. K. Slonim, P. Tamayo, C. Huard, M. Gaasenbeek, "
        "J. P. Mesirov, H. Coller, M. L. Loh, J. R. Downing, M. A. Caligiuri, "
        "C. D. Bloomfield, and E. S. Lander. "
        "'Molecular classification of cancer: class discovery and class "
        "prediction by gene expression monitoring. '"
        "Science, (1999)."
    ]

    def get_data(self):
        # Unlike libsvm[leukemia], this dataset corresponds to the whole
        # leukemia  data with train + test data (72 samples) and not just
        # the training set.
        X, y = fetch_openml("leukemia", return_X_y=True)
        X = X.to_numpy()
        y = LabelBinarizer().fit_transform(y)[:, 0].astype(X.dtype)
        data = dict(X=X, y=y)

        return data
