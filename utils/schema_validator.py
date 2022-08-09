from cerberus import Validator
import allure


@allure.step('Validate Schema')
def validator_schema(schema, response):
    validator = Validator(schema, require_all=False)
    print(validator)
    is_valid = validator.validate(response)
    valid = [is_valid, validator]
    return valid

