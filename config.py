#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = []

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []


#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = [
 'DAYS_ID_PUBLISH',
 'DAYS_BIRTH',
'FLAG_DOCUMENT_3',
 'FLAG_WORK_PHONE',
 'FLAG_PHONE',
 'REGION_RATING_CLIENT_W_CITY',
 'REG_CITY_NOT_LIVE_CITY',
 'REG_CITY_NOT_WORK_CITY'
]


#Variables para binarización por sesgo fuerte
BINARIZE_VARS = [
                ]

#Variables categoricas a codificar sin ordinalidad
CATEGORICAL_VARS = [                   
                    'NAME_CONTRACT_TYPE',
                     'CODE_GENDER',
                     'FLAG_OWN_CAR',
                     'NAME_INCOME_TYPE',
                     'NAME_EDUCATION_TYPE',
                     'ORGANIZATION_TYPE'
]

#Variables seleccionadas según análisis de Lasso
FEATURES =  ['DAYS_ID_PUBLISH',
             'DAYS_BIRTH',
             'NAME_CONTRACT_TYPE',
             'CODE_GENDER',
             'FLAG_OWN_CAR',
             'NAME_INCOME_TYPE',
             'NAME_EDUCATION_TYPE',
             'ORGANIZATION_TYPE',
             'FLAG_DOCUMENT_3',
 'FLAG_WORK_PHONE',
 'FLAG_PHONE',
 'REGION_RATING_CLIENT_W_CITY',
 'REG_CITY_NOT_LIVE_CITY',
 'REG_CITY_NOT_WORK_CITY'
            ]