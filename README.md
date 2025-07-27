# Clinical Timeline App - Service Layer Architecture

A secure medical data visualization platform built with Streamlit, featuring role-based access control, clinical timeline visualization, and comprehensive testing and data validation.

## 🏗️ Architecture Overview

This application implements the **Service Layer Pattern** for clean separation of concerns:

- **Models**: Pure data classes with no dependencies
- **Repositories**: Data access layer (JSON file operations)  
- **Services**: Business logic layer (authentication, timeline data)
- **Pages**: UI presentation layer (Streamlit components)
- **Main**: Application orchestration and dependency injection

### Key Benefits
- ✅ **Testable business logic** - Services are pure Python functions
- ✅ **Flexible UI** - Can support web, mobile, CLI, or API interfaces
- ✅ **Clean separation** - Changes to UI don't affect business logic
- ✅ **Team development** - Clear interfaces between layers

## 📁 Directory Structure

```
/home/raghu/cogitation/ema/
├── clinical_timeline.py              # Application entry point
├── service_layer/                    # Core application package
│   ├── __init__.py
│   ├── main.py                       # App orchestration & dependency injection
│   ├── models/                       # Data models
│   │   ├── __init__.py
│   │   ├── user.py                   # User, AuthResult models
│   │   └── timeline.py               # Timeline data models
│   ├── repositories/                 # Data access layer
│   │   ├── __init__.py
│   │   └── file_repository.py        # JSON file operations
│   ├── services/                     # Business logic layer
│   │   ├── __init__.py
│   │   ├── auth_service.py           # Authentication & user management
│   │   ├── captcha_service.py        # CAPTCHA generation
│   │   └── timeline_service.py       # Timeline data & visualization
│   └── pages/                        # UI presentation layer
│       ├── __init__.py
│       ├── login_page.py             # Login & password reset UI
│       ├── timeline_page.py          # Timeline visualization
│       ├── admin_page.py             # Admin panel UI
│       └── viewer_page.py            # Viewer dashboard
├── tests/                            # Test suite
│   ├── unit/                         # Unit tests for services
│   ├── integration/                  # Integration workflow tests
│   ├── ui/                          # UI component tests
│   └── fixtures/                    # Test data & configuration
├── expectations/                     # Data quality validation
│   ├── config.py                    # Great Expectations setup
│   ├── user_data_expectations.py    # User data validation
│   ├── timeline_data_expectations.py # Timeline data validation
│   └── run_all.py                   # Run all validations
├── users.json                       # User credentials & roles
├── audit.log                        # Security & user action audit trail
├── requirements.txt                 # Python dependencies (pip)
├── environment.yml                  # Conda environment specification
└── README.md                        # This document
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Conda or pip package manager

### Installation

#### Option 1: Using Conda (Recommended)
```bash
# Clone or navigate to project directory
cd /home/raghu/cogitation/ema

# Create conda environment
conda env create -f environment.yml

# Activate environment
conda activate ema
```

#### Option 2: Using pip
```bash
# Clone or navigate to project directory  
cd /home/raghu/cogitation/ema

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
# Start the Streamlit application
streamlit run clinical_timeline.py
```

The application will be available at: `http://localhost:8501`

### Default Login Credentials
- **Username**: `admin`
- **Password**: `Admin123!`
- **Role**: Administrator (full access)

## 🔐 Security Features

- **Authentication**: bcrypt password hashing with salt
- **Failed Login Protection**: Account lockout after 3 failed attempts with CAPTCHA
- **Role-Based Access**: Admin vs Viewer permissions
- **Audit Logging**: Comprehensive logging of all user actions
- **Environment Encryption**: Optional Fernet encryption for sensitive environment variables
- **Session Management**: Secure session state handling

## 🎯 Core Functionality

### Admin Features
- User management (create, update, delete users)
- Role assignment (admin/viewer)
- Account unlocking for failed login attempts
- Password reset functionality
- Audit log viewing and download
- Full timeline visualization access

### Viewer Features  
- Timeline visualization with date range selection
- Interactive Plotly charts showing:
  - Patient admission/discharge periods
  - Diagnosis timeline annotations
  - Medication schedules
- Limited read-only access

### Clinical Timeline Visualization
- **Interactive Charts**: Plotly-based timeline with zoom and pan
- **Patient Data**: Admission periods, diagnoses, medications
- **Date Controls**: Range selectors and custom date filtering
- **Responsive Design**: Works on desktop and mobile devices

## 🧪 Testing

The application includes a comprehensive test suite with multiple testing layers:

### Running All Tests
```bash
# Run the complete test suite
pytest tests/

# Run with coverage report
pytest tests/ --cov=service_layer --cov-report=html

# Run tests in parallel
pytest tests/ -n auto

# Generate HTML test report
pytest tests/ --html=reports/test_report.html
```

### Test Categories

#### Unit Tests (`tests/unit/`)
```bash
# Test individual services
pytest tests/unit/test_auth_service.py
pytest tests/unit/test_timeline_service.py
pytest tests/unit/test_repositories.py
pytest tests/unit/test_captcha_service.py
```

#### Integration Tests (`tests/integration/`)
```bash
# Test complete workflows
pytest tests/integration/test_auth_flow.py
pytest tests/integration/test_user_workflow.py
pytest tests/integration/test_data_persistence.py
```

#### UI Tests (`tests/ui/`)
```bash
# Test UI components
pytest tests/ui/test_login_page.py
pytest tests/ui/test_admin_page.py
pytest tests/ui/test_timeline_page.py
```

### Test Reports
- **Coverage**: HTML coverage reports generated in `htmlcov/`
- **HTML Reports**: Detailed test reports with screenshots
- **Performance**: Benchmark tests for critical operations

## 📊 Data Quality Validation

The application includes Great Expectations for data quality monitoring:

### Running Data Validations
```bash
# Run all data quality checks
python -m expectations.run_all

# Run specific validations
python -m expectations.user_data_expectations
python -m expectations.timeline_data_expectations
```

### Validation Coverage

#### User Data Validation
- ✅ Required fields exist (password, role, email)
- ✅ Valid role assignments (admin/viewer only)
- ✅ Email format validation
- ✅ Password strength requirements
- ✅ Data type consistency

#### Timeline Data Validation
- ✅ Patient ID format validation (PAT-123456)
- ✅ Date format and logical consistency
- ✅ Required timeline fields
- ✅ Data relationships and constraints

## 📋 Monitoring & Logs

### Audit Logging
The application maintains comprehensive audit logs in `audit.log`:

```bash
# View recent audit events
tail -f audit.log

# Search for specific user actions
grep "admin" audit.log

# View login attempts
grep "login" audit.log
```

### Log Format
```
[2024-07-26 17:57:53.849497] Successful login: admin
[2024-07-26 17:57:58.839796] User logged out: admin
[2024-07-26 18:15:22.123456] Failed login attempt: invalid_user
[2024-07-26 18:20:15.789012] User created: new_viewer by admin
```

### Monitoring Data Files

#### User Data (`users.json`)
```bash
# View user accounts
cat users.json | python -m json.tool

# Check user count
jq 'length' users.json
```

#### Failed Login Attempts
```bash
# View locked accounts (if failed_attempts.json exists)
cat failed_attempts.json 2>/dev/null || echo "No failed attempts recorded"
```

## 🔧 Configuration

### Environment Variables (Optional)
Create `.env` file for custom configuration:
```bash
# Copy example configuration
cp .env.example .env

# Edit configuration
# APP_ACCESS_PASSWORD=custom_password
# SMTP_USER=email@example.com
# SMTP_PASS=app_password
```

### Encrypted Environment Variables
For production, use Fernet encryption:
```bash
# Generate encryption key
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())" > .env.key

# Encrypt sensitive values (prefix with enc::)
# APP_ACCESS_PASSWORD=enc::gAAAAABh...encrypted_value
```

## 🚀 Deployment

### Streamlit Cloud Deployment
1. **Repository**: Push code to GitHub repository
2. **Dependencies**: Ensure `requirements.txt` is up to date
3. **Data Files**: Commit `users.json` to repository
4. **Environment**: Configure environment variables in Streamlit Cloud dashboard
5. **Deploy**: Connect repository to Streamlit Cloud

### Local Production Deployment
```bash
# Install production dependencies
pip install -r requirements.txt

# Set production environment
export STREAMLIT_SERVER_PORT=8501
export STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run with production settings
streamlit run clinical_timeline.py --server.port 8501 --server.address 0.0.0.0
```

## 📚 Development

### Adding New Features
1. **Models**: Define data structures in `service_layer/models/`
2. **Repositories**: Add data access methods in `service_layer/repositories/`
3. **Services**: Implement business logic in `service_layer/services/`
4. **Pages**: Create UI components in `service_layer/pages/`
5. **Tests**: Add tests in appropriate `tests/` subdirectory
6. **Validation**: Add data expectations in `expectations/`

### Code Style Guidelines
- Follow existing patterns and naming conventions
- Use type hints for all function parameters and returns
- Add docstrings for all public methods
- Keep UI logic separate from business logic
- Write tests for all new functionality

### Testing Guidelines
- Unit tests for individual service methods
- Integration tests for complete workflows
- UI tests for user interaction flows
- Mock external dependencies in unit tests
- Use fixtures for common test data

## 🆘 Troubleshooting

### Common Issues

#### Authentication Problems
```bash
# Check bcrypt version compatibility
python -c "import bcrypt; print(bcrypt.__version__)"

# Verify user data format
cat users.json | python -m json.tool
```

#### Port Already in Use
```bash
# Kill existing Streamlit processes
pkill -f streamlit

# Use different port
streamlit run clinical_timeline.py --server.port 8502
```

#### Module Import Errors
```bash
# Verify Python path
python -c "import sys; print(sys.path)"

# Check installed packages
pip list | grep streamlit
conda list streamlit
```

#### Test Failures
```bash
# Run tests with verbose output
pytest tests/ -v

# Run specific failing test
pytest tests/unit/test_auth_service.py::test_specific_function -v

# Check test dependencies
pip install -r requirements.txt
```

### Support
- Check application logs in `audit.log`
- Review test output for specific error details
- Verify all dependencies are installed correctly
- Ensure data files (`users.json`) are properly formatted

## 📄 License

This project is for educational and demonstration purposes. Ensure compliance with healthcare data regulations (HIPAA, GDPR) when handling real patient data.