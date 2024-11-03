from readmission_data_product.readers.read_cms_data import CMSDataReader


def test_get_request_returns_correct_column_row_counts() -> None:
    """ Test get_request returns correct column and row counts
    """
    reader = CMSDataReader()

    output = reader.get_request()

    assert len(output.get("query").get("properties")) == 12
    assert output.get('count') == 18774


