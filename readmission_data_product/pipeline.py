from readmission_data_product.readers.read_cms_data import CMSDataReader


def pipeline():
    cms_data_reader = CMSDataReader()

    dict_data = cms_data_reader.get_request()