import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):

    qi = [c for c in anon_df.columns if c in aux_df.columns and c != "anon_id"]
    name_col = "matched_name" if "matched_name" in aux_df.columns else "name"
    merged = pd.merge(anon_df, aux_df, on=qi)
    unique = merged.drop_duplicates(subset=["anon_id"], keep=False)
    unique = unique.drop_duplicates(subset=[name_col], keep=False)

    return unique[["anon_id", name_col]].rename(columns={name_col: "matched_name"})

    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """


def deanonymization_rate(matches_df, anon_df):
    return len(matches_df) / len(anon_df)

    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """

