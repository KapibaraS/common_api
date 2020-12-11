import trafaret as t


config_schema = t.Dict(
    mongodb=t.Dict(
        dsn=t.String,
        db_name=t.String,
    ),
    debug=t.Bool,
)

json_create_car_schema = t.Dict(
    manufacturer=t.String,
    model=t.String,
    year_production=t.Int,
    color=t.String,
    vin_code=t.String,
)
