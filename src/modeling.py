
import lightgbm as lgb
from sklearn.metrics import f1_score, mean_absolute_error

def train_classifier(X_train, y_train):
    clf = lgb.LGBMClassifier(verbosity=-1)
    clf.fit(X_train.fillna(0).values, y_train)
    return clf

def evaluate_classifier(clf, X_test, y_test):
    preds = clf.predict(X_test.fillna(0).values)
    score = f1_score(y_test, preds, average='macro')
    return preds, score

def train_regressor(X_train, y_train):
    reg = lgb.LGBMRegressor(verbosity=-1)
    reg.fit(X_train.fillna(0).values, y_train)
    return reg

def evaluate_regressor(reg, X_test, y_test):
    preds = reg.predict(X_test.fillna(0).values)
    baseline = abs(y_test - y_test.mean()).mean()
    actual = mean_absolute_error(y_test, preds)
    improvement = baseline - actual
    return preds, baseline, actual, improvement
