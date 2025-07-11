from dagster import Definitions
from .assets.visualize import visualize_credit_score_data

defs = Definitions(
    assets=[visualize_credit_score_data],
) 