%global pypi_name pep517
%bcond_with testing

Name:           python-%{pypi_name}
Version:        0.13.1
Release:        2
Summary:        Wrappers to build Python packages using PEP 517 hooks
Group:          Development/Python
License:        None
URL:            https://github.com/pypa/pep517
Source0:        https://files.pythonhosted.org/packages/source/p/pep517/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildSystem:	python
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pip)
%if %{with testing}
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-flake8)
%endif

%description
Wrappers to build Python packages using PEP 517 hooks

%prep -a
# flit 4 no longer reads [tool.flit.metadata].
cat > pyproject.toml << 'EOF'
[build-system]
requires = ["flit_core >=3.2"]
build-backend = "flit_core.buildapi"

[project]
name = "pep517"
description = "Wrappers to build Python packages using PEP 517 hooks"
readme = "README.rst"
requires-python = ">=3.6"
license = "MIT"
authors = [{name = "Thomas Kluyver", email = "thomas@kluyver.me.uk"}]
dynamic = ["version"]
classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
]

[tool.flit.module]
name = "pep517"
EOF

%if %{with testing}
%check
pytest
%endif

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
