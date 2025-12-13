%global pypi_name pep517
%bcond_with testing

Name:           python-%{pypi_name}
Version:        0.13.1
Release:        1
Summary:        Wrappers to build Python packages using PEP 517 hooks
Group:          Development/Python
License:        None
URL:            https://github.com/pypa/pep517
Source0:        https://files.pythonhosted.org/packages/source/p/pep517/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:  python%{pyver}dist(setuptools)
%if %{with testing}
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pytest-flake8)
%endif

%description
Wrappers to build Python packages using PEP 517 hooks

%if %{with testing}
%check
pytest
%endif

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
