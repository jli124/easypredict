s3_path = "s3a://insightflightpred/flightcsv/"
feature = ["YEAR","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","OP_UNIQUE_CARRIER","FLIGHTS", \
"ORIGIN_AIRPORT_ID","DEST_AIRPORT_ID","WEATHER_DELAY","ARR_DEL15"]
feature_num = ["YEAR","MONTH","DAY_OF_MONTH","DAY_OF_WEEK","WEATHER_DELAY","ARR_DEL15"]
feature_cat = ["OP_UNIQUE_CARRIER","FLIGHTS","ORIGIN_AIRPORT_ID","DEST_AIRPORT_ID"]
feature_response = ["WEATHER_DELAY","ARR_DEL15"]

