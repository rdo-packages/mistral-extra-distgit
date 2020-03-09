# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif
%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc 1
%global rhosp 0

%global library mistral-extra
%global module mistral_extra

%global common_desc Python library containting Mistral actions

Name:       python-%{library}
Version:    XXX
Release:    XXX
Summary:    Python library containting Mistral actions
License:    ASL 2.0
URL:        http://launchpad.net/mistral/

Source0:    http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  git
BuildRequires:  openstack-macros

%package -n python%{pyver}-%{library}
Summary:    Python library containting Mistral actions
%{?python_provide:%python_provide python%{pyver}-%{library}}

BuildRequires:  python%{pyver}-devel
BuildRequires:  python%{pyver}-setuptools

BuildRequires:  python%{pyver}-oslotest

BuildRequires:       python%{pyver}-pbr >= 2.0.0
BuildRequires:       python%{pyver}-babel >= 2.3.4
BuildRequires:       python%{pyver}-oslo-log >= 3.36.0
BuildRequires:       python%{pyver}-mistral-lib >= 1.4.0
BuildRequires:       python%{pyver}-yaql >= 1.1.3
BuildRequires:       python%{pyver}-oauthlib >= 0.6.2

BuildRequires:       python%{pyver}-aodhclient >= 0.9.0
BuildRequires:       python%{pyver}-barbicanclient >= 4.5.2
BuildRequires:       python%{pyver}-cinderclient >= 3.3.0
BuildRequires:       python%{pyver}-designateclient >= 2.7.0
BuildRequires:       python%{pyver}-glanceclient >= 1:2.8.0
BuildRequires:       python%{pyver}-gnocchiclient >= 3.3.1
BuildRequires:       python%{pyver}-heatclient >= 1.10.0
BuildRequires:       python%{pyver}-ironic-inspector-client >= 1.5.0
BuildRequires:       python%{pyver}-ironicclient >= 2.7.0
BuildRequires:       python%{pyver}-keystoneclient >= 1:3.8.0
BuildRequires:       python%{pyver}-magnumclient >= 2.15.0
BuildRequires:       python%{pyver}-manilaclient >= 1.23.0
BuildRequires:       python%{pyver}-mistralclient >= 3.1.0
BuildRequires:       python%{pyver}-neutronclient >= 6.7.0
BuildRequires:       python%{pyver}-novaclient >= 1:9.1.0
BuildRequires:       python%{pyver}-swiftclient >= 3.2.0
BuildRequires:       python%{pyver}-troveclient >= 2.2.0
BuildRequires:       python%{pyver}-zaqarclient >= 1.0.0
%if 0%{rhosp} == 0
BuildRequires:       python%{pyver}-glareclient >= 0.3.0
BuildRequires:       python%{pyver}-muranoclient >= 1.3.0
BuildRequires:       python%{pyver}-senlinclient >= 1.11.0
BuildRequires:       python%{pyver}-tackerclient >= 0.8.0
BuildRequires:       python%{pyver}-vitrageclient >= 2.0.0
%endif

Requires:       python%{pyver}-pbr >= 2.0.0
Requires:       python%{pyver}-babel >= 2.3.4
Requires:       python%{pyver}-oslo-log >= 3.36.0
Requires:       python%{pyver}-mistral-lib >= 1.4.0
Requires:       python%{pyver}-yaql >= 1.1.3
Requires:       python%{pyver}-oauthlib >= 0.6.2
Requires:       python%{pyver}-aodhclient >= 0.9.0
Requires:       python%{pyver}-barbicanclient >= 4.5.2
Requires:       python%{pyver}-cinderclient >= 3.3.0
Requires:       python%{pyver}-designateclient >= 2.7.0
Requires:       python%{pyver}-glanceclient >= 1:2.8.0
Requires:       python%{pyver}-gnocchiclient >= 3.3.1
Requires:       python%{pyver}-heatclient >= 1.10.0
Requires:       python%{pyver}-ironic-inspector-client >= 1.5.0
Requires:       python%{pyver}-ironicclient >= 2.7.0
Requires:       python%{pyver}-keystoneclient >= 1:3.8.0
Requires:       python%{pyver}-magnumclient >= 2.15.0
Requires:       python%{pyver}-manilaclient >= 1.23.0
Requires:       python%{pyver}-mistralclient >= 3.1.0
Requires:       python%{pyver}-neutronclient >= 6.7.0
Requires:       python%{pyver}-novaclient >= 1:9.1.0
Requires:       python%{pyver}-swiftclient >= 3.2.0
Requires:       python%{pyver}-troveclient >= 2.2.0
Requires:       python%{pyver}-zaqarclient >= 1.0.0
%if 0%{rhosp} == 0
Requires:       python%{pyver}-glareclient >= 0.3.0
Requires:       python%{pyver}-muranoclient >= 1.3.0
Requires:       python%{pyver}-senlinclient >= 1.11.0
Requires:       python%{pyver}-tackerclient >= 0.8.0
Requires:       python%{pyver}-vitrageclient >= 2.0.0
%endif

%description -n python%{pyver}-%{library}
%{common_desc}


%package -n python%{pyver}-%{library}-tests
Summary:    Mistral extras library tests
%{?python_provide:%python_provide python%{pyver}-%{library}-tests}
Requires:   python%{pyver}-%{library} = %{version}-%{release}

Requires:       python%{pyver}-oslotest
Requires:       python%{pyver}-subunit
Requires:       python%{pyver}-testrepository

%description -n python%{pyver}-%{library}-tests
Mistral extras library tests.

This package contains the Mistral extras library test files.

%if 0%{?with_doc}
%package -n python-%{library}-doc
Summary:    Mistral extras library documentation

BuildRequires: python%{pyver}-sphinx
BuildRequires: python%{pyver}-openstackdocstheme

%description -n python-%{library}-doc
Mistral extras library documentation

This package contains the documentation.
%endif

%description
%{common_desc}


%prep
%autosetup -n %{library}-%{upstream_version} -S git




# Let's handle dependencies ourseleves
%py_req_cleanup

%build
%{pyver_build}

%if 0%{?with_doc}
# generate html docs
sphinx-build-%{pyver} -b html doc/source doc/build/html
# remove the sphinx-build-%{pyver} leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif
        mock_rm.assert_not_called()

%install
%{pyver_install}

install -p -D -m 644 ./mistral_extra/actions/openstack/mapping.json %{buildroot}%{pyver_sitelib}/%{service}/actions/openstack/mapping.json

%check
stestr-%{pyver} run

%files -n python%{pyver}-%{library}
%license LICENSE
%{pyver_sitelib}/%{module}
%{pyver_sitelib}/%{module}-*.egg-info
%exclude %{pyver_sitelib}/%{module}/tests

%files -n python%{pyver}-%{library}-tests
%{pyver_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
