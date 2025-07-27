"""User data validation expectations for Clinical Timeline App."""

import great_expectations as ge
from .config import get_data_context


def validate_users_data(ge_df):
    """Validate users.json data structure and content."""
    results = []
    
    # Basic structure validation
    results.append(ge_df.expect_table_row_count_to_be_between(min_value=1, max_value=100))
    
    # Required columns exist
    results.append(ge_df.expect_column_to_exist("password"))
    results.append(ge_df.expect_column_to_exist("role"))
    results.append(ge_df.expect_column_to_exist("email"))
    
    # Role validation
    results.append(ge_df.expect_column_values_to_be_in_set("role", ["admin", "viewer"]))
    
    # Email format validation (basic)
    results.append(ge_df.expect_column_values_to_match_regex(
        "email", 
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    ))
    
    # Password should not be null/empty
    results.append(ge_df.expect_column_values_to_not_be_null("password"))
    results.append(ge_df.expect_column_value_lengths_to_be_between("password", min_value=1))
    
    return results


def run_user_validation():
    """Run user data validation and return results."""
    context = get_data_context()
    return context.run_validation_suite("users.json", validate_users_data)


if __name__ == "__main__":
    # Run validation when script is executed directly
    results = run_user_validation()
    if results:
        print("User data validation completed!")
        for result in results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            print(f"{status}: {result.expectation_config.expectation_type}")
    else:
        print("❌ Validation failed to run")