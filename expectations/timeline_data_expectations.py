"""Timeline data validation expectations for Clinical Timeline App."""

import great_expectations as ge
import pandas as pd
from .config import get_data_context


def validate_timeline_data(ge_df):
    """Validate clinical timeline data structure and content."""
    results = []
    
    # Basic structure validation
    results.append(ge_df.expect_table_row_count_to_be_between(min_value=0, max_value=10000))
    
    # Required columns for patient timeline data
    expected_columns = ["patient_id", "admission_date", "discharge_date", "diagnosis"]
    for col in expected_columns:
        results.append(ge_df.expect_column_to_exist(col))
    
    # Patient ID format validation (example: PAT-123456)
    results.append(ge_df.expect_column_values_to_match_regex(
        "patient_id", 
        r"^PAT-\d{6}$"
    ))
    
    # Date format validation (ISO format)
    results.append(ge_df.expect_column_values_to_match_strftime_format(
        "admission_date", 
        "%Y-%m-%d"
    ))
    
    # Discharge date should be after admission date
    results.append(ge_df.expect_column_pair_values_A_to_be_greater_than_B(
        "discharge_date", 
        "admission_date"
    ))
    
    # No null patient IDs
    results.append(ge_df.expect_column_values_to_not_be_null("patient_id"))
    
    return results


def validate_sample_timeline_data():
    """Create and validate sample timeline data for testing."""
    # Sample data structure for future mock data
    sample_data = {
        "patient_id": ["PAT-123456", "PAT-789012"],
        "admission_date": ["2024-01-15", "2024-02-20"],
        "discharge_date": ["2024-01-20", "2024-02-25"],
        "diagnosis": ["Hypertension", "Diabetes"],
        "medications": ["Lisinopril", "Metformin"]
    }
    
    df = pd.DataFrame(sample_data)
    ge_df = ge.from_pandas(df)
    
    return validate_timeline_data(ge_df)


def run_timeline_validation(file_path: str = None):
    """Run timeline data validation."""
    if file_path:
        # Validate actual file when available
        context = get_data_context()
        return context.run_validation_suite(file_path, validate_timeline_data)
    else:
        # Validate sample data structure
        return validate_sample_timeline_data()


if __name__ == "__main__":
    # Run validation on sample data structure
    print("Validating sample timeline data structure...")
    results = run_timeline_validation()
    
    if results:
        print("Timeline data validation completed!")
        for result in results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            print(f"{status}: {result.expectation_config.expectation_type}")
    else:
        print("❌ Validation failed to run")
    
    print("\n📝 Note: This validates the expected structure for future timeline data files.")