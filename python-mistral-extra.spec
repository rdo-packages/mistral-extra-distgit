%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global service mistral-extra

%global common_desc \
Python library to extend workflow services. \
Mistral Extra is a library which allows contributors to add optional \
functionality to the mistral project, it also contains examples for which \
to base new capabilities.

Name:           python-mistral-extra
Version:        XXX
Release:        XXX
Summary:        Library for optional functionality.
License:        ASL 2.0
URL:            https://pypi.org/project/mistral-extra/
Source0:        https://tarballs.openstack.org/%{service}/%{service}-%{upstream_version}.tar.gz

BuildArch:      noarch

BuildRequires:  git
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-setuptools
BuildRequires:  python2-babel

# test dependencies

BuildRequires: python2-oslotest
BuildRequires: python2-subunit
BuildRequires: python2-stestr
BuildRequires: python2-testrepository


%description
%{common_desc}


Summary:        Mistral Python libraries
Provides:       python-%{name} = %{version}-%{release}
Obsoletes:      python-%{name} < 6.0.0

Requires:       python2-babel >= 2.3.4
Requires:       python2-pbr >= 2.0.0
# OpenStack dependencies
Requires:       python2-oslo-concurrency >= 3.25.0
Requires:       python2-oslo-log >= 3.36.0
Requires:       python2-oslo-config
Requires:       python2-mistral-lib >= 0.3.0


%prep
%autosetup -n mistral-%{service}-{upstream_version} -S git

%py_req_cleanup

%build
%py2_build setup.py build

%install
%py2_install

%files -n python-%{service}
%{python2_sitelib}/%{service}
%{python2_sitelib}/%{service}-*.egg-info
%exclude %{python2_sitelib}/mistral_extra/tests

%license LICENSE

%changelog
