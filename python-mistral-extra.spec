%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service mistral-extra

%global common_desc \
Python library to extend workflow services. \
Mistral Extra is a library which allows contributors to add optional \
functionality to the mistral project, it also contains examples for which \
to base new capabilities.

Name:           python-mistral-extra
Version:        7.0.0.0b2
Release:        1
Summary:        Library for optional functionality.
License:        ASL 2.0
URL:            https://pypi.org/project/mistral-extra/
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-pbr
BuildRequires:  openstack-macros
BuildRequires:  python2-babel
BuildRequires:  python-mistral-lib
BuildRequires:  python2-oslo-concurrency
BuildRequires:  python2-oslo-log

%description
%{common_desc}

%prep
%autosetup -n %{service}-%{upstream_version}
%py_req_cleanup

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot}

%check
%{__python} setup.py testr


%files
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst Changelog
%{python2_sitelib}/mistral_extra
%{python2_sitelib}/*.egg-info

%changelog