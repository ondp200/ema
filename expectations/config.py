"""Great Expectations configuration for Clinical Timeline App."""

import os
import pandas as pd
import great_expectations as ge
from great_expectations.core.batch import RuntimeBatchRequest
from great_expectations.data_context import BaseDataContext
from great_expectations.data_context.types.base import DataContextConfig, InMemoryStoreBackendDefaults


class ClinicalTimelineDataContext:
    """Simple Great Expectations setup for clinical timeline data validation."""
    
    def __init__(self, base_path: str = "."):
        self.base_path = base_path
        self.context = self._create_context()
    
    def _create_context(self) -> BaseDataContext:
        """Create a minimal Great Expectations context."""
        data_context_config = DataContextConfig(
            store_backend_defaults=InMemoryStoreBackendDefaults(),
            checkpoint_store_name="checkpoint_store",
        )
        
        context = BaseDataContext(project_config=data_context_config)
        return context
    
    def validate_json_file(self, file_path: str, suite_name: str):
        """Load JSON file as DataFrame and validate with given expectation suite."""
        full_path = os.path.join(self.base_path, file_path)
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Data file not found: {full_path}")
        
        # Load JSON as DataFrame
        if file_path.endswith('.json'):
            df = pd.read_json(full_path, orient='index')  # For users.json structure
        else:
            df = pd.read_csv(full_path)
        
        # Create Great Expectations DataFrame
        ge_df = ge.from_pandas(df)
        
        return ge_df
    
    def run_validation_suite(self, file_path: str, expectations_func):
        """Run a validation suite on a data file."""
        try:
            ge_df = self.validate_json_file(file_path, expectations_func.__name__)
            results = expectations_func(ge_df)
            return results
        except Exception as e:
            print(f"Validation failed for {file_path}: {e}")
            return None


def get_data_context():
    """Get the data context for the current project."""
    return ClinicalTimelineDataContext()