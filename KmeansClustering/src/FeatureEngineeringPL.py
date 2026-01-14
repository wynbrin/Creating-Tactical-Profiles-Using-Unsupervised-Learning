#Create Class for Feature Engineering to add to sklearn pipeline
from sklearn.base import BaseEstimator, TransformerMixin
class FeatureEngineeringPL(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        self.feature_names = None

        return self

    def transform(self, X):
        df = X.copy()

        drop = ["Rk", "Comp", "Min", "Subs", "LgRank", "Season", "Team", 'W', 'D', 'L', 'Pts', 'Pts/MP']
        cat_features = ["Rk", "Comp", "Min", "Subs", "LgRank", "Season", "Team"]
        num_features = df.drop(columns=drop).columns
        print(num_features)

        stats = df[num_features]

        selected_features = ["xG", "npxG", "Poss", "Sh", "SoT", "G/Sh", "G/SoT", "npxG/Sh", "CS%", "Dist", "GA", "GF", "GD", "xGD", "npxGD","G-xG", "A-xAG"]
        stats = stats[selected_features]

        stats["xGA"] = stats["xG"] - stats["xGD"]
        stats["xG_xGA_ratio"] = stats["xG"] / stats["xGA"]
        stats["GF_GA_ratio"] = stats["GF"] / stats["GA"]
        stats["finishing_efficiency"] = stats["G-xG"] / stats["xG"]
        stats["assist_efficiency"] = stats["A-xAG"] / (stats["A-xAG"].abs() + 1)
        stats["pressing_intensity"] = stats["Poss"]  / (stats["Sh"] + 1)
        stats["directness"] = stats["Sh"] / (stats["Poss"] + 1)
        stats["verticality"] = stats["Dist"] / (stats["Sh"] + 1)
        stats["shot_quality"] = stats["npxG"] / (stats["Sh"] + 1)
        stats["defensive_efficiency"] = (stats["GA"] - stats["xGA"]) / stats["xGA"]

        stats.replace([np.inf, -np.inf], np.nan, inplace=True)
        stats.fillna(stats.median(), inplace=True)

        self.feature_names = stats.columns.tolist()
        return stats.values
