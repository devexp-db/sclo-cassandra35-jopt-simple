%{?scl:%scl_package jopt-simple}
%{!?scl:%global pkg_name %{name}}

Name:		%{?scl_prefix}jopt-simple
Version:	4.6
Release:	4%{?dist}
Summary:	A Java command line parser
License:	MIT
URL:		http://pholser.github.io/%{pkg_name}/
Source0:	https://github.com/pholser/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	%{?scl_prefix_maven}maven-local
BuildRequires:	%{?scl_prefix_maven}joda-time
BuildRequires:	%{?scl_prefix_maven}mvn(org.sonatype.oss:oss-parent:pom:)
%{?scl:Requires: %scl_runtime}

%description
JOpt Simple is a Java library for parsing command line options, such as those
you might pass to an invocation of javac.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_dep org.infinitest:continuous-testing-toolkit
%pom_remove_plugin org.pitest:pitest-maven
%pom_remove_plugin org.codehaus.mojo:cobertura-maven-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-pmd-plugin

# generate artifact
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
# Unit testing is disabled due to a missing dependency in Fedora of continuous-testing-toolkit
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Oct 12 2016 Tomas Repik <trepik@redhat.com> - 4.6-4
- use standard SCL macros

* Mon Aug 01 2016 Tomas Repik <trepik@redhat.com> - 4.6-3
- mvn_file added to generate artifact provides

* Wed Jul 27 2016 Tomas Repik <trepik@redhat.com> - 4.6-2
- added dependency + minor fixes

* Wed Jul 27 2016 Pavel Raiskup <praiskup@redhat.com> - 4.6-1
- sclize
