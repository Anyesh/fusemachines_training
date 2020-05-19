parameters = {
    "bert_classifier": {},
    "xgboost": {},
    "randomforest": {},
    "naive_bayes": {"alpha": 0.1},
    "sgd_classifier": {
        "penalty": "l2",
        "alpha": 0.0001,
        "l1_ratio": 0.15,
        "fit_intercept": True,
        "max_iter": 1000,
        "tol": 0.001,
        "shuffle": True,
        "verbose": 0,
        "epsilon": 0.1,
        "n_jobs": None,
        "random_state": 32,
        "learning_rate": "optimal",
        "eta0": 0.0,
        "power_t": 0.5,
        "early_stopping": False,
        "validation_fraction": 0.1,
        "n_iter_no_change": 5,
        "class_weight": None,
        "warm_start": False,
        "average": False,
    },
    "svm_svc": {
        "C": 1.0,
        "kernel": "rbf",
        "degree": 3,
        "gamma": "scale",
        "coef0": 0.0,
        "shrinking": True,
        "probability": True,
        "tol": 0.001,
        "cache_size": 200,
        "class_weight": None,
        "verbose": False,
        "max_iter": -1,
        "decision_function_shape": "ovr",
        "break_ties": False,
        "random_state": None,
    },
}
