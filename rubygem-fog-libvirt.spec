%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from fog-libvirt-0.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fog-libvirt

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.1
Release: 6%{?dist}
Summary: Module for the 'fog' gem to support libvirt
Group: Development/Languages
License: MIT
URL: http://github.com/fog/fog-libvirt
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(fog-core) >= 1.27.4
Requires: %{?scl_prefix}rubygem(fog-core) < 2
Requires: %{?scl_prefix}rubygem(fog-xml) >= 0.1.1
Requires: %{?scl_prefix}rubygem(fog-xml) < 0.2
Requires: %{?scl_prefix}rubygem(fog-json)
Requires: %{?scl_prefix_ruby}rubygem(json)
Requires: %{?scl_prefix}rubygem(ruby-libvirt) => 0.5.0
Requires: %{?scl_prefix}rubygem(ruby-libvirt) < 0.6.0
Requires: libvirt
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
# Test requires, missing shindo in SCL
#BuildRequires: %{?scl_prefix}rubygem(ruby-libvirt)
#BuildRequires: %{?scl_prefix}rubygem(shindo) => 0.3.4
#BuildRequires: %{?scl_prefix}rubygem(shindo) < 0.4
#BuildRequires: %{?scl_prefix}rubygem(fog-core)
#BuildRequires: %{?scl_prefix}rubygem(fog-xml)
#BuildRequires: %{?scl_prefix}rubygem(fog-json)
BuildRequires: libvirt-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This library can be used as a module for 'fog' or as standalone libvirt
provider.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite

%check
pushd .%{gem_instdir}
# Missing shindo in SCL
#FOG_MOCK=true shindont -Ilib tests
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fog-libvirt.gemspec
%{gem_instdir}/tests

%changelog
* Mon Jun 15 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-6
- Adjust dependencies

* Mon Jun 15 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-5
- Add missing ruby-libvirt dependency

* Fri Jun 12 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-4
- Add missing provide

* Tue Jun 09 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-3
- Change license macro back to doc

* Tue Jun 09 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-2
- Add SCL macros

* Fri Jun 05 2015 Josef Stribny <jstribny@redhat.com> - 0.0.1-1
- Initial package
