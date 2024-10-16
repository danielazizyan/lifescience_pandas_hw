import pandas as pd

experiments_data = {
    'experiment_id': [1],
    'experiment_name': ['experiment_1'],
    'property_name': ['channel'],
    'property_value': ['1']
}

plates_data = {
    'plate_id': [1],
    'plate_name': ['plate_1'],
    'experiment_id': [1],
    'property_name': ['concentration_unit'],
    'property_value': ['ul']
}

wells_data = {
    'well_id': [1, 2, 3, 4, 5, 6],
    'well_row': ['1', '1', '1', '1', '2', '2'],
    'well_column': ['1', '2', '3', '4', '1', '2'],
    'plate_id': [1, 1, 1, 1, 1, 1],
    'property_name': ['concentration', 'concentration', 'concentration', 'concentration', 'concentration', 'concentration'],
    'property_value': ['1', '2', '3', 'none', 'none', 'none']
}


experiments_df = pd.DataFrame(experiments_data)
plates_df = pd.DataFrame(plates_data)
wells_df = pd.DataFrame(wells_data)


wells_pivot = wells_df.pivot(
        index=['well_id', 'well_row', 'well_column', 'plate_id'],
        columns='property_name',
        values='property_value'
    ).reset_index()

plates_pivot = plates_df.pivot(
        index='plate_id',
        columns='property_name',
        values='property_value'
    ).reset_index()

experiments_pivot = experiments_df.pivot(
        index='experiment_id',
        columns='property_name',
        values='property_value'
    ).reset_index()


wells_with_plates = wells_pivot.merge(
        plates_pivot,
        on='plate_id', how='left')

wells_with_plates = wells_with_plates.merge(
        plates_df[['plate_id', 'experiment_id']],
        on='plate_id', how='left'
    )

wells_with_all = wells_with_plates.merge(
        experiments_pivot,
        on='experiment_id', how='left')


wells_with_all.to_excel('well_properties.xlsx', index=False)
