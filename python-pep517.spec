# Created by pyp2rpm-3.3.5
%global pypi_name pep517

Name:           python-%{pypi_name}
Version:        0.9.1
Release:        1
Summary:        Wrappers to build Python packages using PEP 517 hooks
Group:          Development/Python
License:        None
URL:            https://github.com/pypa/pep517
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE tests/samples/pkg1/pkg1-0.5.dist-info/LICENSE tests/samples/pkg2/pkg2-0.5.dist-info/LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
