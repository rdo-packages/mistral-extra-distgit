%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0x2426b928085a020d8a90d0d879ab7008d0896c8a
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order
%global with_doc 1
%global rhosp 0

%global library mistral-extra
%global module mistral_extra

%global common_desc Python library containting Mistral actions

Name:       python-%{library}
Version:    XXX
Release:    XXX
Summary:    Python library containting Mistral actions
License:    Apache-2.0
URL:        http://launchpad.net/mistral/

Source0:    http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        http://tarballs.openstack.org/%{library}/%{library}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif

BuildArch:  noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core
BuildRequires:  openstack-macros

%package -n python3-%{library}
Summary:    Python library containting Mistral actions

BuildRequires:  python3-devel
%if 0%{rhosp} == 0
BuildRequires:       python3-muranoclient >= 1.3.0
BuildRequires:       python3-senlinclient >= 1.11.0
BuildRequires:       python3-tackerclient >= 0.8.0
BuildRequires:       python3-vitrageclient >= 2.0.0
%endif
BuildRequires:  pyproject-rpm-macros

%if 0%{rhosp} == 0
Requires:       python3-muranoclient >= 1.3.0
Requires:       python3-senlinclient >= 1.11.0
Requires:       python3-tackerclient >= 0.8.0
Requires:       python3-vitrageclient >= 2.0.0
%endif

%description -n python3-%{library}
%{common_desc}


%package -n python3-%{library}-tests
Summary:    Mistral extras library tests
%{?python_provide:%python_provide python3-%{library}-tests}
Requires:   python3-%{library} = %{version}-%{release}

Requires:       python3-oslotest
Requires:       python3-subunit
Requires:       python3-testrepository

%description -n python3-%{library}-tests
Mistral extras library tests.

This package contains the Mistral extras library test files.

%if 0%{?with_doc}
%package -n python-%{library}-doc
Summary:    Mistral extras library documentation

%description -n python-%{library}-doc
Mistral extras library documentation

This package contains the documentation.
%endif

%description
%{common_desc}


%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{library}-%{upstream_version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

# Automatic BR generation
%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
# excluding one test due to upstream bug related to barbicanclient
%tox -e %{default_toxenv}

%files -n python3-%{library}
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-*.dist-info
%exclude %{python3_sitelib}/%{module}/tests

%files -n python3-%{library}-tests
%{python3_sitelib}/%{module}/tests

%if 0%{?with_doc}
%files -n python-%{library}-doc
%license LICENSE
%doc doc/build/html README.rst
%endif

%changelog
