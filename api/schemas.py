import trafaret as t
from marshmallow import Schema, fields
from marshmallow.validate import Length, Range

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


class CarSchema(Schema):
    car_id = fields.Function(lambda obj: str(obj["_id"]), dump_only=True)
    manufacturer = fields.Str(required=True)
    model = fields.Str(required=True)
    year_production = fields.Int(required=True, validate=Range(4, 4))
    color = fields.Str(required=True, validate=Length(min=3))
    vin_code = fields.Str(required=True, validate=[Length(equal=17)])

    class Meta:
        strict = True
