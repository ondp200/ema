"""Run all Great Expectations validations for Clinical Timeline App."""

from .user_data_expectations import run_user_validation
from .timeline_data_expectations import run_timeline_validation


def run_all_validations():
    """Run all data validation expectations."""
    print("🔍 Running Clinical Timeline Data Validations...\n")
    
    # User data validation
    print("1. Validating user data...")
    user_results = run_user_validation()
    if user_results:
        user_passed = sum(1 for r in user_results if r.success)
        user_total = len(user_results)
        print(f"   ✅ User validation: {user_passed}/{user_total} expectations passed\n")
    else:
        print("   ❌ User validation failed\n")
    
    # Timeline data validation (sample structure)
    print("2. Validating timeline data structure...")
    timeline_results = run_timeline_validation()
    if timeline_results:
        timeline_passed = sum(1 for r in timeline_results if r.success)
        timeline_total = len(timeline_results)
        print(f"   ✅ Timeline validation: {timeline_passed}/{timeline_total} expectations passed\n")
    else:
        print("   ❌ Timeline validation failed\n")
    
    # Summary
    total_passed = 0
    total_expectations = 0
    
    if user_results:
        total_passed += sum(1 for r in user_results if r.success)
        total_expectations += len(user_results)
    
    if timeline_results:
        total_passed += sum(1 for r in timeline_results if r.success)
        total_expectations += len(timeline_results)
    
    print(f"📊 Overall: {total_passed}/{total_expectations} expectations passed")
    
    if total_passed == total_expectations:
        print("🎉 All data quality checks passed!")
    else:
        print("⚠️  Some data quality issues detected")
    
    return {
        "user_results": user_results,
        "timeline_results": timeline_results,
        "total_passed": total_passed,
        "total_expectations": total_expectations
    }


if __name__ == "__main__":
    run_all_validations()